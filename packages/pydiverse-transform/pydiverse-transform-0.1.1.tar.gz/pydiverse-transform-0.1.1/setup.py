# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pydiverse',
 'pydiverse.transform',
 'pydiverse.transform.core',
 'pydiverse.transform.core.expressions',
 'pydiverse.transform.core.ops',
 'pydiverse.transform.core.util',
 'pydiverse.transform.eager',
 'pydiverse.transform.lazy',
 'pydiverse.transform.util']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.27', 'numpy>=1.23.1', 'pandas>=1.4.3']

extras_require = \
{'docs': ['Sphinx>=5.1.1,<6.0.0',
          'sphinx-rtd-theme>=1.0.0,<2.0.0',
          'sphinxcontrib-apidoc>=0.3.0,<0.4.0']}

setup_kwargs = {
    'name': 'pydiverse-transform',
    'version': '0.1.1',
    'description': 'Pipe based dataframe manipulation library that can also transform data on SQL databases',
    'long_description': '# pydiverse.transform\n\n[![CI](https://github.com/pydiverse/pydiverse.transform/actions/workflows/ci.yml/badge.svg)](https://github.com/pydiverse/pydiverse.transform/actions/workflows/ci.yml)\n\nPipe based dataframe manipulation library that can also transform data on SQL databases\n\nThis is an early stage version 0.x which lacks documentation. Please contact\nhttps://github.com/orgs/pydiverse/teams/code-owners if you like to become an early adopter\nor to contribute early stage usage examples.\n\n## Usage\n\npydiverse.transform can either be installed via pypi with `pip install pydiverse-transform` or via conda-forge\nwith `conda install pydiverse-transform -c conda-forge`.\n\n## Example\n\nThis code illustrates how to use pydiverse.transform with pandas and SQL:\n\n```python\nfrom pydiverse.transform import Table\nfrom pydiverse.transform.lazy import SQLTableImpl\nfrom pydiverse.transform.eager import PandasTableImpl\nfrom pydiverse.transform.core.verbs import *\nimport pandas as pd\nimport sqlalchemy as sa\n\n\ndef main():\n    dfA = pd.DataFrame(\n        {\n            "x": [1],\n            "y": [2],\n        }\n    )\n    dfB = pd.DataFrame(\n        {\n            "a": [2, 1, 0, 1],\n            "x": [1, 1, 2, 2],\n        }\n    )\n\n    input1 = Table(PandasTableImpl("dfA", dfA))\n    input2 = Table(PandasTableImpl("dfB", dfB))\n\n    transform = (\n        input1\n        >> left_join(input2 >> select(), input1.x == input2.x)\n        >> mutate(x5=input1.x * 5, a=input2.a)\n    )\n    out1 = transform >> collect()\n    print("\\nPandas based result:")\n    print(out1)\n\n    engine = sa.create_engine("sqlite:///:memory:")\n    dfA.to_sql("dfA", engine, index=False, if_exists="replace")\n    dfB.to_sql("dfB", engine, index=False, if_exists="replace")\n    input1 = Table(SQLTableImpl(engine, "dfA"))\n    input2 = Table(SQLTableImpl(engine, "dfB"))\n    transform = (\n        input1\n        >> left_join(input2 >> select(), input1.x == input2.x)\n        >> mutate(x5=input1.x * 5, a=input2.a)\n    )\n    out2 = transform >> collect()\n    print("\\nSQL query:")\n    print(transform >> build_query())\n    print("\\nSQL based result:")\n    print(out2)\n\n    out1 = out1.sort_values("a").reset_index(drop=True)\n    out2 = out2.sort_values("a").reset_index(drop=True)\n    assert len(out1.compare(out2)) == 0\n\n\nif __name__ == "__main__":\n    main()\n```\n',
    'author': 'QuantCo, Inc.',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
