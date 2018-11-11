# Author José Albert Cruz Almaguer <jalbertcruz@gmail.com>
# Copyright 2018 by José Albert Cruz Almaguer.
#
# This program is licensed to you under the terms of version 3 of the
# GNU Affero General Public License. This program is distributed WITHOUT
# ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING THOSE OF NON-INFRINGEMENT,
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Please refer to the
# AGPL (http:www.gnu.org/licenses/agpl-3.0.txt) for more details.

import re
import sys
import json
import os

current_file_content = "".join(open(sys.argv[1]).readlines())

secrets = json.loads("".join(open(os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'values.json')).readlines()))

for k, v in secrets.items():
    current_file_content = re.sub("{}".format(v),
                                  "{{{{ {k} }}}}".format(k=k),
                                  current_file_content)

print(current_file_content, end='')
