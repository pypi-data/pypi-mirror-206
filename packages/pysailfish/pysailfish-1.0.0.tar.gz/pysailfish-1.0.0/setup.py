# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysailfish', 'pysailfish.app', 'pysailfish.internal']

package_data = \
{'': ['*']}

install_requires = \
['sfdevtools>=1.74.0,<2.0.0']

setup_kwargs = {
    'name': 'pysailfish',
    'version': '1.0.0',
    'description': '',
    'long_description': '\n## pysailfish\n\n### How to publish to pypi\n```bash\n# set up pypi token\n$ poetry config pypi-token.pypi my-token\n\n# build the project\n$ poetry build\n\n# publish the project\n$ poetry publish\n\n# DONE\n```\n\n### How to use QC CLI\n[reference](https://www.quantconnect.com/docs/v2/lean-cli)\n```bash\n# Install lean\n$ poetry add lean\n$ poetry install\n\n# Login\n$ poetry run lean login --user-id xxx --api-token xxx\n\n# Initial workspace\n$ poetry run lean init\n\n# Pull projects\n$ poetry run lean cloud pull\n\n# Push projects\n$ poetry run lean cloud push\n```\n\n### kubernetes helm related\n```bash\n# check helm template\n$ helm template pysailfish ./chart --values=./chart/values.dev.yaml\n\n# install helm chart\n$ helm upgrade --wait --timeout=1200s --install --values ./chart/values.dev.yaml pysailfish ./chart\n\n# uninstall helm chart\n$ helm uninstall pysailfish\n```\n\n### GRPC related\n[reference](https://github.com/chelseafarley/PythonGrpc)\n```bash\n# generate python script from proto file\n$ cd pysailfish/app/grpc_api\n$ poetry run python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/pysailfish.proto\n\n$ poetry add grpcio-tools',
    'author': 'SulfredLee',
    'author_email': 'sflee1112@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
