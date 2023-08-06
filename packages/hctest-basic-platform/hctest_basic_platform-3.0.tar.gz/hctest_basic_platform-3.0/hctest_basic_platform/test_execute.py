# -*- coding: utf-8 -*-
# author: 华测-长风老师

from requests import request
from run import RunData
import pytest

data = RunData.data


@pytest.mark.parametrize(argnames="d", argvalues=data)
def test(d):
    da = d

    keys = list(da.keys())
    values = list(da.values())
    for v in values:
        if not d:
            d.pop(keys[values.index(v)])

    req = request(**d)
    print(req.text)
