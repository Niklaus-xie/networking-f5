"""Setup install script for F5 Networks ML2 plugin driver."""
# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from setuptools import setup, find_packages

setup(
          name="NETWORKING-F5",
          version="2018.10",
          packages=find_packages(),
          zip_safe=False,
          description="ML2 Driver for F5",
          author = "F5",
          author_email = "",
          keywords=("plugin", "network", "F5"),
          platforms="Linux",
          url="www.f5.com <http://www.f5.com/> ",
          package_data={'networking_f5': ['*']},
          entry_points={
              'neutron.ml2.mechanism_drivers': [
                  'f5networks= networking_f5.plugins.ml2.drivers.f5.mech_f5networks_bigip:F5NetworksMechanismDriver']
           },
)
