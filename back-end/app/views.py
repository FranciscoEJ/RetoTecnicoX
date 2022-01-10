#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import json
import os
import logging
from flask import Flask
from typing import List, Dict
from .process import petition, count_answers, less_views, older_newer_answer, higer_reputation
from .queries import config, test, diasMayVuelo, mayorAeropu, mayorAeroli, mayorDia
from .db_connect import query_mysql

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

source = f"https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
cases = [{"number_case": 'case1',
          "description": 'Obtener el número de respuestas contestadas y no contestadas'},
         {"number_case": 'case2',
          "description": 'Obtener la respuesta con menor número de vistas'},
         {"number_case": 'case3',
          "description": 'Obtener la respuesta más vieja y más actual'},
         {"number_case": 'case4',
          "description": 'Obtener la respuesta del owner que tenga una mayor reputación'},
         {"number_case": 'case5',
          "description": '¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?'},
         {"number_case": 'case6',
          "description": '¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año'},
         {"number_case": 'case7',
          "description": '¿En qué día se han tenido mayor número de vuelos?'},
         {"number_case": ' case8',
          "description": '¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?'}]


@ app.route("/")
def index():
    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Reto Tecnico!"


@ app.route('/dbtest')
def test_db() -> str:
    return json.dumps({'Case test: ': query_mysql(test)})


@ app.route('/apitest')
def test_request() -> dict:
    return json.dumps(petition(source))


@ app.route('/index')
def test_cases() -> list:
    return json.dumps(cases)


@ app.route('/case1')
def request_case1() -> dict:
    return json.dumps({'case1': count_answers(petition(source))})


@ app.route('/case2')
def request_case2() -> dict:
    return json.dumps({'case2': less_views(petition(source))})


@ app.route('/case3')
def request_case3() -> dict:
    return json.dumps({'case3': older_newer_answer(petition(source))})


@ app.route('/case4')
def request_case4() -> dict:
    return json.dumps({'case4': higer_reputation(petition(source))})


@ app.route('/case5')
def db_case5() -> dict:
    return json.dumps({'case5': query_mysql(mayorAeropu)})


@ app.route('/case6')
def db_case6() -> str:
    return json.dumps({'case6': query_mysql(mayorAeroli)})


@ app.route('/case7')
def db_case7() -> dict:
    return json.dumps({'case7': query_mysql(mayorDia)})


@ app.route('/case8')
def db_case8() -> dict:
    return json.dumps({'case8': query_mysql(diasMayVuelo)})
