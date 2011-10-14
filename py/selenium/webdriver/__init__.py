#!/usr/bin/python
#
# Copyright 2008-2010 Webdriver_name committers
# Copyright 2008-2010 Google Inc.
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

# added Android - Sean Wang
from android.webdriver import WebDriver as Android
from firefox.webdriver import WebDriver as Firefox
from firefox.firefox_profile import FirefoxProfile
from chrome.webdriver import WebDriver as Chrome
from ie.webdriver import WebDriver as Ie
from remote.webdriver import WebDriver as Remote
from common.desired_capabilities import DesiredCapabilities
from common.action_chains import ActionChains

__version__ = '2.8.0'
