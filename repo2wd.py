from jinja2 import Environment, DictLoader

import sys
import json
import os

env = Environment(
    loader=DictLoader({'index.html': "".join(sys.stdin.readlines())}),
    trim_blocks=True, lstrip_blocks=True
)

template = env.get_template('index.html')
secrets = json.loads(open(os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'values.json')).read())

res = template.render(
    **secrets
)
print(res)
