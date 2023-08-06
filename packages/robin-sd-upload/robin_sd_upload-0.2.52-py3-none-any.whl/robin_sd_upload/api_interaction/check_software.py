#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
import json

from robin_sd_upload.api_interaction import get_bearer_token
from robin_sd_upload.supportive_scripts import yaml_parser
from robin_sd_upload.supportive_scripts import logger


def check_software(radar_type, version_name):
    config = yaml_parser.parse_config()
    request_url = config['api_url']

    try:
        bearer_token = str(get_bearer_token.get_bearer_token())
    except requests.exceptions.HTTPError as e:
        return "User does not have permission to upload"

    headers = {
        'Authorization': 'Bearer ' + bearer_token,
    }

    response = requests.get(
        request_url + '/api/softwares/versions', headers=headers)
    if response.status_code == 200:
        logger.log(message="Successfully fetched all uploaded software versions.",
                   log_level="info", to_terminal=True)
    else:
        logger.log(message="Uploaded software versions fetching failed with status code: " +
                   str(response.status_code), log_level="error", to_terminal=True)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error pushing software: " + str(e)

    uploaded_versions = response.json()["softwares"]

    version_exists = False

    for version in uploaded_versions:
        if version['version'] == version_name and version['rtype'] == radar_type:
            version_exists = True
            break

    if version_exists:
        logger.log(message=f"Version {version_name} for {radar_type} already exists. ",
                   log_level="warning", to_terminal=True)
    else:
        logger.log(message=f"Version {version_name} for {radar_type} does not exist. ",
                   log_level="info", to_terminal=True)

    return version_exists
