import sys
from io import StringIO

import pytest

from sqrt_calc import sqrt_calc


def test_sqrt_calc(monkeypatch: pytest.MonkeyPatch):

   monkeypatch.setattr('sys.stdin', StringIO("4\n4\ntrun"))
   sqrt_calc()

   # captured = capsys.readouterr()
   # captured_stdout = captured.out

   # print(captured_stdout)
   pass
