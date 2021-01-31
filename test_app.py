import os
import tempfile
import pytest
from flask import request, jsonify
from app import app

def test_predict():
    with app.test_client() as c
        resp = c.post('/predict')
        json_data = resp.get_json()
        assert json_data['prediction'] == [20.35373177134412]

