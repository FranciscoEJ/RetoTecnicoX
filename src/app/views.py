#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import json
import os
import logging
from flask import Flask
from typing import List, Dict
from process import petition, count_answers, less_views, older_newer_answer, higer_reputation
from queries import config, diasMayVuelo, test
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

    return "Hello from Flask"


@app.route('/db')
def index_db() -> str:
    return json.dumps({'Case 4: ': query_mysql(diasMayVuelo)})
