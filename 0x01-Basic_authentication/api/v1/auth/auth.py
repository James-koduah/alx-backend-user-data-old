#!/usr/bin/env python3
"""An authentication module"""
from flask import request
from typing import List, TypeVar


class Auth():
    """An authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth return false"""
        if path[-1] != '/':
            path = path + '/'
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False

        return False

    def authorization_header(self, request=None) -> str:
        """The flask authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user"""
        return None
