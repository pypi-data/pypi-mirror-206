# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['langsrc']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'langsrc',
    'version': '0.0.8',
    'description': 'A language package manager',
    'long_description': '<h1 style="text-align: center"> langSrc </h1>\n\n## Install\n\n```shell\npip3 install langSrc\n```\n\n## Demo\n\n```python\nfrom langSrc import LanguageDetector\n\nlang = LanguageDetector("zh", "lang.json")\nlang.register(\n    "language",\n    {\n        "zh": "语言",\n        "en": "Language",\n        "jp": "言語",\n        "kor": "언어",\n        "fra": "Langue",\n        "spa": "Idioma",\n        "th": "ภาษา",\n    },\n)\n\nprint(lang.language) # or print(lang["language"])\n\n# 语言\n```\n\nThis will generate a file named [`lang.json`](./lang.json):\n\n```json title="lang.json"\n{\n  "language": {\n    "zh": "语言",\n    "en": "Language",\n    "jp": "言語",\n    "kor": "언어",\n    "fra": "Langue",\n    "spa": "Idioma",\n    "th": "ภาษา"\n  }\n}\n```\n',
    'author': 'Rhythmicc',
    'author_email': 'rhythmlian.cn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
