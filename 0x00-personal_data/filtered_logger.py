#!/usr/bin/env python3
'''Read and filter logs.
'''
import os
import re
import logging
import mysql.connector
from typing import List

def filter_datum(fields, redaction, message, separator):
    return re.sub(r'({0})(?={1})'.format('|'.join(map(re.escape, fields)), re.escape(separator)), redaction, message)

