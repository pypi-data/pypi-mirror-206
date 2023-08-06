#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import json

from robin_sd_upload.api_interaction import get_bearer_token
from robin_sd_upload.supportive_scripts import yaml_parser
from robin_sd_upload.supportive_scripts import logger

def push_software(fpath, radarType, version_name):
    config = yaml_parser.parse_config()

    request_url = config['api_url']

    try:
        bearer_token = str(get_bearer_token.get_bearer_token())
    except requests.exceptions.HTTPError as e:
        return "User does not have permission to upload"

    headers = {
        'Authorization': 'Bearer ' + bearer_token,
    }

    # check if can open file path
    if os.path.isfile(fpath):
        logger.log(message="ZIP file exists for push software: " + fpath, log_level="info", to_terminal=True)
    else:
        logger.log(message="ZIP not exist for push software: " + fpath, log_level="error", to_terminal=True)
        return "ZIP not exist (PS): " + fpath
        
    files = {
        'file': (fpath, open(fpath, 'rb'))
    }

    values = {
        'destination': json.dumps(radarType),
        'versionName': json.dumps(version_name)
    }

    logger.log(message="Pushing software to Robin SD...", log_level="info", to_terminal=True)

    response = requests.post(request_url + '/api/softwares/softwarefiles', headers=headers, data=values, files=files)
    if response.status_code == 200:
        logger.log(message="Software pushed successfully!", log_level="info", to_terminal=True)
    else:
        logger.log(message="Software push failed with status code: " + str(response.status_code), log_level="error", to_terminal=True)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error pushing software: " + str(e)

    return response.json()
