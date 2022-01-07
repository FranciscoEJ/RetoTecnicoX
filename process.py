#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Espinoza Jimenez Francisco Javier
# Created Date: 06/01/2022
# version ='1.0'
# ---------------------------------------------------------------------------
import requests
import json
import logging

source = f"https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
logging.basicConfig(level=logging.INFO)


def petition(link):
    """
    Funtion to request data from API
    Args:
        link (str) -> URL from the soruce
    Returns:
        r (json) -> Data in json format
    """
    try:
        r = requests.get(link)
        return r.json()
    except Exception as e:
        logging.error(e)
        return "No data source found... check the exception"


def count_answers(data):
    """
    Process json object to find the question answered and the no ones
    Args:
        data (json): Data in json format
    Returns:
        answer (dict): Num of answered and Num of no-answered items
    """
    try:
        no_answered = len([d for d in data.get('items')
                           if d.get('is_answered') == False and d.get('is_answered') is not None])
        return {"No-answered": no_answered, "Answered": len(data['items'])-no_answered}
    except Exception as E:
        logging.error(E)
        return "Not able to process info in the source"


def less_views(data):
    """
    Process json object to find the less viewed answer
    Args:
        data (json): Data in json format
    Returns:
        answer (dict): less viewed answer value
    """
    try:
        min_answer = min(d.get('view_count') for d in data.get(
            'items') if d.get('view_count') is not None)
        return {"Minimun": min_answer}
    except Exception as e:
        logging.error(E)
        return "Not able to process info in the source"


def older_newer_answer(data):
    """
    Process json object to find the oldest and newest answer
    Args:
        data (json): Data in json format
    Returns:
        answer (dict): Newest and oldest answers
    """
    try:
        # TO-DO: Verifiy the format of dates in the data to work with actually dates
        min_answer = min(d.get('creation_date') for d in data.get(
            'items') if d.get('creation_date') is not None)
        max_answer = min(d.get('creation_date') for d in data.get(
            'items') if d.get('creation_date') is not None)
        return {"Oldest": min_answer, "Newest": max_answer}
    except Exception as e:
        logging.error(E)
        return "Not able to process info in the source"


def higer_reputation(data):
    """
    Process json object to find the owner who has thee higest reputation
    Args:
        data (json): Data in json format
    Returns:
         answer (dict): Newest and oldest answers
    """
    try:
        high_answer = max(d.get('owner').get('reputation') for d in data.get(
            'items') if d.get('owner').get('reputation') is not None)
        return {"Highest": high_answer}
    except Exception as E:
        logging.error(E)
        return "Not able to access info in the source"


def __main__():
    """
    The main functiion
    """
    r = petition(source)
    logging.info("Answer to case 2:")
    logging.info(count_answers(r))
    logging.info("Answer to case 3:")
    logging.info(less_views(r))
    logging.info("Answer to case 4:")
    logging.info(older_newer_answer(r))
    logging.info("Answer to question 5:")
    logging.info(higer_reputation(r))


__main__()
