# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycudahll']

package_data = \
{'': ['*']}

install_requires = \
['cupy-cuda12x>=12.0.0,<13.0.0',
 'hyperloglog>=0.0.14,<0.0.15',
 'numpy>=1.24.2,<2.0.0',
 'scipy>=1.10.1,<2.0.0']

setup_kwargs = {
    'name': 'pycudahll',
    'version': '0.1.0',
    'description': 'A GPU implementation of HyperLogLog',
    'long_description': '# PyCudaHLL\n\nThis is a GPU accelerated implementation of HyperLogLog using the CuPy library. It was created for the class "Algorithmic Techniques for Taming Big Data" at the department of Computing and Data Science at Boston University.\n\n## Using the Code\n\nTo use this code, you can either get the library from PyPI or build it from source.\n\n### Get from PyPI (Recommended)\n\n- Install using pip: `pip install pycudahll`\n- In your code, import the library: `from pycudahll.CudaHLL import CudaHLL`\n\n### Building from Source\n\n- Clone the repository\n- Install dependencies: `poetry install`\n- In your code, import the library: `from pycudahll.CudaHLL import CudaHLL`\n- See `test.py` for examples. (Note: `test.py` is most likely in a broken state, but should give you an idea of how to use the library.)\n\n## API\n\nThe main class of the library is CudaHLL. It can be imported in your code with:\n```python\nfrom pycudahll.CudaHLL import CudaHLL\n```\n\nCudaHLL also includes a helper function to hash data to use with the main class:\n```python\nfrom pycudahll.CudaHLL import hashDataGPUHLL\n```\n\nA short example of how to use the library is as follows:\n```python\nfrom pycudahll.CudaHLL import CudaHLL, hashDataGPUHLL\n\nwith open(\'data.csv\', \'r\') as file:\n    data = file.read().split(\',\')\n    hashedData = hashDataGPUHLL(data)\n\n    threads = 64\n    p = 14\n    cudaDevice = 0 # optional\n    roundThreads = True # optional\n    hll = CudaHLL(p, threads, cudaDevice, roundThreads)\n\n    hll.add(hashedData)\n    print(hll.card()) # print unrounded cardinality estimate\n    print(len(hll)) # print rounded cardinality estimate\n```\n\n\n## Test Data\n\nText of Shakespeare plays obtained from https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt. Original text can be found in t8.shakespeare.txt and the modified text can be found in shakespeare.csv.\n\nTotal number of items = 899300\nExact cardinality = 34065',
    'author': 'Gabe Maayan',
    'author_email': 'gabemgem@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gabemgem/PyCudaHLL',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.10,<3.12',
}


setup(**setup_kwargs)
