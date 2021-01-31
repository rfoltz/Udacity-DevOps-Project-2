import pytest
from app import predict


def test_predict():
    assert predict() == """{"prediction":[20.35373177134412]}"""

