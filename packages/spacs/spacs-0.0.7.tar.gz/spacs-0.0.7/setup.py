# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spacs']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.4,<4.0.0', 'pydantic>=1.10.7,<2.0.0']

setup_kwargs = {
    'name': 'spacs',
    'version': '0.0.7',
    'description': 'Simple Pydantic AIOHTTP Client Sessions',
    'long_description': '# SPACS: Simple Pydantic AIOHTTP Client Sessions\n\nA package to assist in managing and using long-lived AIOHTTP client sessions with simplicity. Built to handle Pydantic objects.\n\n## Features\n\n- Handles request params and bodies as either Pydantic objects or native Python dictionaries, converting items to JSON-safe format.\n- Abstracts away internals of managing the request/response objects, instead either returning parsed response content on success, or raising a specialized error object.\n- Automatically manages persistent connections to be shared over extended lifespan across application, cleaning up all open connections on teardown.\n- Utilizes modern Python type hinting.\n\n## Installation\n\nUsing poetry (preferred):\n\n```bash\npoetry add spacs\n```\n\nUsing pip:\n\n```bash\npip install spacs\n```\n\n## Usage\n\n```python\nfrom spacs import SpacsClient, SpacsRequest, SpacsRequestError\nfrom pydantic import BaseModel\n\n...\n\nexample_client = SpacsClient(base_url="http://example.com")\n\n# Basic request with error handling\ntry:\n    request = SpacsRequest(path="/fruit/apple", params={"cultivar": "honeycrisp"})\n    apples = await example_client.get(request)\nexcept SpacsRequestError as error:\n    print({"code": error.status_code, "reason": error.reason})\n\n# Sending Pydantic objects via HTTP POST\nclass MyModel(BaseModel):\n    name: str\n    age: int\n\nexample_object = MyModel(name="James", age=25)\nrequest = SpacsRequest(path="/person", body=example_object, response_model=MyModel)\ncreated_person = await example_client.post(request)\n\n# Manually closing a session\nawait example_client.close()\n# Alternatively, to close all open sessions:\nawait SpacsClient.close_all()\n```\n\n## Building\n\n```\npoetry build\n```\n',
    'author': 'rlebel12',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rlebel12/spacs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
