#!/usr/bin/env python3
"""a module that implements a Basic auth"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """A subclass of the Auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Base64 part of the Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is False:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decode a base64 string"""
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            return base64.b64decode(
                    base64_authorization_header.encode('utf-8')
                    ).decode('utf-8')
        except Exception:
            return None
