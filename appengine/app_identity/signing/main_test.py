# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tests import AppEngineTestbedCase
import webtest

from . import main


class TestAppIdentityHandler(AppEngineTestbedCase):
    def setUp(self):
        super(TestAppIdentityHandler, self).setUp()

        self.app = webtest.TestApp(main.app)

    def test_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_int, 200)
        self.assertTrue('Verified: True' in response.text)
