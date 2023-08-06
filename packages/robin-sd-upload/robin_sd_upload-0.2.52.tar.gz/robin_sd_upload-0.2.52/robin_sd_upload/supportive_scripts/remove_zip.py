#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from robin_sd_upload.supportive_scripts import logger

#remove zip file if exists
def remove_zip(zip_name):
    if os.path.isfile(zip_name):
        os.remove(zip_name)
        logger.log(message="ZIP file removed: " + zip_name, log_level="info", to_terminal=True)
    else:
        logger.log(message="ZIP file not exist: " + zip_name, log_level="info", to_terminal=True)
        