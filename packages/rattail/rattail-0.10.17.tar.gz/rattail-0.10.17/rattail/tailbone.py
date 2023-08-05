# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2023 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Tailbone API Client
"""

import json
import logging

import requests


log = logging.getLogger(__name__)


class TailboneAPIClient(object):
    """
    Simple client for Tailbone web API.
    """
    session = None
    logged_in = False

    def __init__(self, config, base_url=None, **kwargs):
        self.config = config
        self.base_url = base_url or self.config.require(
            'tailbone.api', 'base_url')

    def _init(self):
        if self.session:
            return

        self.session = requests.Session()
        response = self.get('/session')
        self.session.headers.update({
            'X-XSRF-TOKEN': response.cookies['XSRF-TOKEN']})

    def _request(self, request_method, api_method, params=None, data=None):
        """
        Perform a request for the given API method, and return the response.
        """
        api_method = api_method.lstrip('/')
        url = '{}/{}'.format(self.base_url, api_method)
        if request_method == 'GET':
            response = self.session.get(url, params=params)
        elif request_method == 'POST':
            response = self.session.post(url, params=params,
                                         data=json.dumps(data))
        else:
            raise NotImplementedError("unknown request method: {}".format(
                request_method))
        response.raise_for_status()
        return response

    def get(self, api_method, params=None):
        """
        Perform a GET request for the given API method, and return the response.
        """
        return self._request('GET', api_method, params=params)

    def post(self, api_method, **kwargs):
        """
        Perform a POST request for the given API method, and return the response.
        """
        self._init()
        return self._request('POST', api_method, **kwargs)

    def login(self, username=None, password=None):
        if self.logged_in:
            return True

        if not username:
            username = self.config.require('tailbone.api', 'login.username')
        if not password:
            password = self.config.require('tailbone.api', 'login.password')

        response = self.post('/login', data={'username': username,
                                             'password': password})

        # ok means success
        data = response.json()
        if data.get('ok'):
            self.logged_in = True
            return True

        # log what we can if failure
        if data.get('error'):
            log.error("login failed: %s", data['error'])
        else:
            log.error("login failed somehow, please investigate")
        return False
