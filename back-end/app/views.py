#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import json
import os
import logging
from flask import Flask
from typing import List, Dict
from process import petition, count_answers, less_views, older_newer_answer, higer_reputation
from queries import config, test, diasMayVuelo, mayorAeropu, mayorAeroli, mayorDia
from db_connect import query_mysql

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

source = f"https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"


@app.route("/")
def index():
    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Reto Tecnico!"


@app.route('/dbtest')
def test_db() -> str:
    return json.dumps({'Case test: ': query_mysql(test)})


@app.route('/apitest')
def test_request() -> str:
    return json.dumps(petition(source))


@app.route('/case1')
def request_case1() -> str:
    return json.dumps({'Case 1: ': count_answers(petition(source))})


@app.route('/case2')
def request_case2() -> str:
    return json.dumps({'Case 1: ': less_views(petition(source))})


@app.route('/case3')
def request_case3() -> str:
    return json.dumps({'Case 1: ': older_newer_answer(petition(source))})


@app.route('/case4')
def request_case4() -> str:
    return json.dumps({'Case 1: ': higer_reputation(petition(source))})


@app.route('/case5')
def db_case5() -> str:
    return json.dumps({'Case test: ': query_mysql(mayorAeropu)})


@app.route('/case 6')
def db_case6() -> str:
    return json.dumps({'Case test: ': query_mysql(mayorAeroli)})


@app.route('/case 7')
def db_case7() -> str:
    return json.dumps({'Case test: ': query_mysql(mayorDia)})


@app.route('/case 8')
def db_case8() -> str:
    return json.dumps({'Case test: ': query_mysql(diasMayVuelo)})
