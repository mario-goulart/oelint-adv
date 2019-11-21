import ast

from oelint_adv.cls_item import Function
from oelint_adv.cls_rule import Rule


class TaskPythonPrefix(Rule):
    def __init__(self):
        super().__init__(id="oelint.task.pythonprefix",
                         severity="warning",
                         message="Tasks containing python code, should be prefixed with python in function header")

    def check(self, _file, stash):
        res = []
        for item in stash.GetItemsFor(filename=_file, classifier=Function.CLASSIFIER):
            try:
                print(item.FuncBodyRaw)
                ast.parse(item.FuncBodyRaw, "tempfile")
                if not item.IsPython:
                    res += self.finding(item.Origin, item.InFileLine)
            except Exception:
                pass
        return res