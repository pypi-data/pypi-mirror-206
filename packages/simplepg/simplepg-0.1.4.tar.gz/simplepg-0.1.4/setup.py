# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simplepg']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.0,<0.6.0', 'psycopg2>=2.9.5,<3.0.0']

setup_kwargs = {
    'name': 'simplepg',
    'version': '0.1.4',
    'description': 'Simple PostgreSQL connections',
    'long_description': '# SimplePG\n\nSimple PostgreSQL connections: a wrapper around psycopg2.\n\nFeatures:\n- Thread-safe connection pooling\n- Auto-reconnect on connection loss\n- Unified interface for execute, executemany, and execute_values\n\n## Installation\n\n```bash\npip install simplepg\n```\n\n## Example\n\n```python\nfrom simplepg import DbConnection\n\ndb = DbConnection(\n    user="postgres",\n    password="postgres",\n    host="localhost",\n    port=5432,\n    database="postgres",\n    connect_kwargs={},\n    pool_min_connections=1,\n    pool_max_connections=1,\n)\n\ndb.execute("CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR)")\ndb.execute_values("INSERT INTO test_table (name) VALUES %s", [("test1",), ("test2",)])\nrecords, columns = db.execute("SELECT * FROM test_table")\ndb.execute("DROP TABLE test_table")\n```\n',
    'author': 'Mysterious Ben',
    'author_email': 'datascience@tuta.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
