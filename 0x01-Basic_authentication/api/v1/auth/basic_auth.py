#!/usr/bin/env python3
"""a module that implements a Basic auth"""
from api.v1.auth.auth import Auth


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
        if not re.search("^Basic ", authorization_header):
            return None
        return authorization_header[6:]
