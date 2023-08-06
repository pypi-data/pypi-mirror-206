# Copyright (c) 2019 Red Hat, Inc.
#
# All Rights Reserved.
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

import tobiko
from tobiko.shell import sh
from tobiko.openstack import keystone
from tobiko.openstack import nova
from tobiko.openstack import stacks
from tobiko.tests.functional.openstack.stacks import test_cirros


@keystone.skip_unless_has_keystone_credentials()
class CentosServerStackTest(test_cirros.CirrosServerStackTest):
    """Test CentOS server instance"""

    #: Stack of resources with a server attached to a floating IP
    stack = tobiko.required_fixture(stacks.CentosServerStackFixture)

    def test_user_data(self):
        user_data = self.stack.user_data
        self.assertEqual('', user_data)

    def test_python(self):
        python_version = sh.execute(['/usr/libexec/platform-python',
                                     '--version'],
                                    ssh_client=self.stack.ssh_client).stdout
        self.assertTrue(python_version.startswith('Python 3.'),
                        python_version)

    def test_cloud_init_done(self):
        nova.wait_for_cloud_init_done(ssh_client=self.stack.ssh_client)


@tobiko.skip("Can't SSH to CentOS 7 server")
@keystone.skip_unless_has_keystone_credentials()
class Centos7ServerStackTest(CentosServerStackTest):

    #: Stack of resources with a server attached to a floating IP
    stack = tobiko.required_fixture(stacks.Centos7ServerStackFixture)

    def test_python(self):
        python_version = sh.execute(['python', '--version'],
                                    ssh_client=self.stack.ssh_client).stderr
        self.assertTrue(python_version.startswith('Python 2.'),
                        python_version)
