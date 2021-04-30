# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import HTTPCommand

from .exceptions import CallLogdError
from .exceptions import CallLogdServiceUnavailable
from .exceptions import InvalidCallLogdError


class CallLogdCommand(HTTPCommand):

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise CallLogdServiceUnavailable(response)

        try:
            raise CallLogdError(response)
        except InvalidCallLogdError:
            HTTPCommand.raise_from_response(response)
