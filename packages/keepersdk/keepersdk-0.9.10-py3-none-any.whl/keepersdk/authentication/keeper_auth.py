#  _  __
# | |/ /___ ___ _ __  ___ _ _ ®
# | ' </ -_) -_) '_ \/ -_) '_|
# |_|\_\___\___| .__/\___|_|
#              |_|
#
# Keeper Commander
# Copyright 2023 Keeper Security Inc.
# Contact: ops@keepersecurity.com
#

import concurrent.futures
import enum
import time
from typing import Optional, Dict, Any, List, Type

from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

from . import endpoint, notifications
from .. import errors


class SessionTokenRestriction(enum.IntFlag):
    Unrestricted = 1 << 0
    AccountRecovery = 1 << 1
    ShareAccount = 1 << 2
    AcceptInvite = 1 << 3
    AccountExpired = 1 << 4


class AuthContext:
    def __init__(self) -> None:
        self.username = ''
        self.account_uid = b''
        self.session_token = b''
        self.session_token_restriction: SessionTokenRestriction = SessionTokenRestriction.Unrestricted
        self.data_key = b''
        self.client_key = b''
        self.rsa_private_key: Optional[RSAPrivateKey] = None
        self.ec_private_key: Optional[EllipticCurvePrivateKey] = None
        self.ec_public_key: Optional[EllipticCurvePublicKey] = None
        self.enterprise_rsa_public_key: Optional[RSAPublicKey] = None
        self.enterprise_ec_public_key: Optional[EllipticCurvePublicKey] = None
        self.is_enterprise_admin = False
        self.enforcements: Dict[str, Any] = {}
        self.settings: Dict[str, Any] = {}
        self.license: Dict[str, Any] = {}


class _AsyncExecutor:
    def __init__(self) -> None:
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    def execute_async(self, fn, *args, **kwargs):
        return self._executor.submit(fn, *args, **kwargs)

    def close(self):
        if self._executor:
            self._executor.shutdown(wait=False)
            self._executor = None


class KeeperAuth(_AsyncExecutor):
    def __init__(self, keeper_endpoint: endpoint.KeeperEndpoint, auth_context: AuthContext) -> None:
        _AsyncExecutor.__init__(self)
        self.keeper_endpoint = keeper_endpoint
        self.auth_context = auth_context
        self.push_notifications: Optional[notifications.FanOut[Dict[str, Any]]] = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self) -> None:
        if self.push_notifications and not self.push_notifications.is_completed:
            self.push_notifications.shutdown()

        _AsyncExecutor.close(self)

    def execute_auth_rest(self, rest_endpoint: str, request: Optional[endpoint.TRQ],
                          response_type: Optional[Type[endpoint.TRS]]=None) -> Optional[endpoint.TRS]:
        return self.keeper_endpoint.execute_rest(
            rest_endpoint, request, response_type=response_type, session_token=self.auth_context.session_token)

    def execute_auth_command(self, request: Dict[str, Any], throw_on_error=True) -> Dict[str, Any]:
        request['username'] = self.auth_context.username
        response = self.keeper_endpoint.v2_execute(request, session_token=self.auth_context.session_token)
        if response is None:
            raise errors.KeeperApiError('server_error', 'JSON response is empty')
        if throw_on_error and response.get('result') != 'success':
            raise errors.KeeperApiError(response.get('result_code') or '', response.get('message') or '')
        return response

    def execute_batch(self, requests: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        responses: List[Dict[str, Any]] = []
        if not requests:
            return responses

        chunk_size = 98
        queue = requests.copy()
        while len(queue) > 0:
            chunk = queue[:chunk_size]
            queue = queue[chunk_size:]

            rq = {
                'command': 'execute',
                'requests': chunk
            }
            rs = self.execute_auth_command(rq)
            results = rs['results']
            if isinstance(results, list) and len(results) > 0:
                responses.extend(results)
                if len(results) < len(chunk):
                    queue = chunk[len(results):] + queue

                if len(results) > 50:
                    time.sleep(5)

        return responses
