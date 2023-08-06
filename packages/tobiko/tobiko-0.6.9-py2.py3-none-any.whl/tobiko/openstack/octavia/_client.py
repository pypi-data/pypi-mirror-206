# Copyright 2019 Red Hat
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from __future__ import absolute_import

import typing

from octaviaclient.api.v2 import octavia

import tobiko
from tobiko.openstack import _client
from tobiko.openstack import keystone


OCTAVIA_CLIENT_CLASSSES = octavia.OctaviaAPI,


OctaviaClientType = typing.Union[octavia.OctaviaAPI,
                                 'OctaviaClientFixture']


def get_octavia_endpoint(keystone_client=None):
    return keystone.find_service_endpoint(name='octavia',
                                          client=keystone_client)


class OctaviaClientFixture(_client.OpenstackClientFixture):

    def init_client(self, session):
        keystone_client = keystone.get_keystone_client(session=session)
        endpoint = get_octavia_endpoint(keystone_client=keystone_client)
        return octavia.OctaviaAPI(session=session, endpoint=endpoint.url)


class OctaviaClientManager(_client.OpenstackClientManager):

    def create_client(self, session):
        return OctaviaClientFixture(session=session)


CLIENTS = OctaviaClientManager()


@keystone.skip_if_missing_service(name='octavia')
def octavia_client(obj: OctaviaClientType = None) -> octavia.OctaviaAPI:
    if obj is None:
        return get_octavia_client()

    if isinstance(obj, OCTAVIA_CLIENT_CLASSSES):
        return obj

    fixture = tobiko.setup_fixture(obj)
    if isinstance(fixture, OctaviaClientFixture):
        return fixture.client

    message = "Object {!r} is not an OctaviaClientFixture".format(obj)
    raise TypeError(message)


def get_octavia_client(session=None, shared=True, init_client=None,
                       manager=None):
    manager = manager or CLIENTS
    client = manager.get_client(session=session, shared=shared,
                                init_client=init_client)
    tobiko.setup_fixture(client)
    return client.client


def get_member(pool_id: str, member_id: str, client=None):
    return octavia_client(client).member_show(pool_id=pool_id,
                                              member_id=member_id)


def list_members(pool_id: str, client=None):
    return octavia_client(client).member_list(pool_id=pool_id)['members']
