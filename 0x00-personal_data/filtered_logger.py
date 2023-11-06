#!/usr/bin/env python3
"""
Return a log message obfuscated
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message obfuscated"""
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}', f'{i}={redaction}{separator}',
                         message)
    return message
