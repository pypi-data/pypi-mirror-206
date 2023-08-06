# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyspmp']

package_data = \
{'': ['*'], 'pyspmp': ['dataset/*', 'parametros/*']}

install_requires = \
['pandas>=1.4.3,<2.0.0']

extras_require = \
{'buscapi': ['pythonnet>=3.0.1,<4.0.0']}

setup_kwargs = {
    'name': 'pyspmp',
    'version': '0.1.12',
    'description': 'Busca e pré seleção de períodos para modelos de monitoramento e predição de máquinas e equipamentos',
    'long_description': '# PySPMP GitLab\n\n## Descrição\n\nEste projeto tem como objetivo realizar buscas e pré seleção de períodos dentro dos parâmentros definidos pelo usuário para modelos de monitoramento e predição de máquinas e equipamentos, visando mitigar e reduzir o esforço de trabalho do usuário na busca de períodos adequados para um bom modelo de monitoramento e predição.\n\n## Fonte\n\nA fonte do PySPMP é [hospedado em\nGitLab.com](https://codigo-externo.petrobras.com.br/leandro.castro.prestserv/pyspmp).\n\n## Requisitos\n\npython = "^3.8.1"\npandas = "^1.4.3"\npythonnet(opcional) = "^3.0.1"\n\n',
    'author': 'Leandro Ribeiro de Castro',
    'author_email': 'lr.castro@yahoo.com.br',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
