#!/usr/bin/env python3
"""
Return a log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    """Return the log message obfuscated"""
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}', f'{i}={redaction}{separator}',
                          message)
    return message
