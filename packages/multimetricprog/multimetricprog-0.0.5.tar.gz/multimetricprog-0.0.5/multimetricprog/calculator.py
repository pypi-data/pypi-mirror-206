import argparse
import json
import os
import textwrap
import multiprocessing as mp


from multimetricprog.cls.importer.pick import importer_pick
from multimetricprog.cls.modules import get_additional_parser_args
from multimetricprog.cls.modules import get_modules_calculated
from multimetricprog.cls.modules import get_modules_metrics
from multimetricprog.cls.modules import get_modules_stats
import sys
import chardet
from pygments import lexers

from multimetricprog.cls.modules import get_modules_calculated
from multimetricprog.cls.modules import get_modules_metrics
from multimetricprog.cls.importer.filtered import FilteredImporter


def calculate(code):
    _result = {"files": {}, "overall": {}}

    _args = {
        "ignore_lexer_errors": None,
        "warn_compiler": None,
        "warn_duplication": None,
        "warn_functional": None,
        "warn_standard": None,
        "warn_security": None,
        "coverage": None,
        "dump": False,
        "jobs": 1
    }

    # Get importer
    _importer = {}
    _importer["import_compiler"] = None
    _importer["import_coverage"] = None
    _importer["import_duplication"] = None
    _importer["import_functional"] = None
    _importer["import_security"] = None
    _importer["import_standard"] = None
    # sanity check
    _importer = {k: v for k, v in _importer.items() if v}

    # instance metric modules
    _overallMetrics = get_modules_metrics(_args, **_importer)
    _overallCalc = get_modules_calculated(_args, **_importer)
    _file = "fp.py"
    res = {}
    store = {}
    try:
        _lexer = lexers.get_lexer_for_filename(_file)
    except Exception as e:
        if _args.ignore_lexer_errors:
            # Printing to stderr since we write results to STDOUT
            print("Processing unknown file type: " + _file, file=sys.stderr)
            return (res, _file, "unknown", [], store)
        else:
            raise
    try:
        _cnt = bytes(code, "utf-8")
        _enc = chardet.detect(_cnt)
        _cnt = _cnt.decode(_enc["encoding"]).encode("utf-8")
        _localImporter = {k: FilteredImporter(
            v, _file) for k, v in _importer.items()}
        tokens = list(_lexer.get_tokens(_cnt))

        _localMetrics = get_modules_metrics(_args, **_localImporter)
        _localCalc = get_modules_calculated(_args, **_localImporter)
        for x in _localMetrics:
            x.parse_tokens(_lexer.name, tokens)
            res.update(x.get_results())
            store.update(x.get_internal_store())
        for x in _localCalc:
            res.update(x.get_results(res))
            store.update(x.get_internal_store())
    except Exception:
        tokens = []

    results = [(res, _file, _lexer.name, tokens, store)]

    for x in results:
        _result["files"][x[1]] = x[0]

    for y in _overallMetrics:
        _result["overall"].update(
            y.get_results_global([x[4] for x in results]))
    for y in _overallCalc:
        _result["overall"].update(y.get_results(_result["overall"]))
    for m in get_modules_stats(_args, **_importer):
        _result = m.get_results(_result, "files", "overall")

    return _result
