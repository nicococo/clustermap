try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

description = "A tool to handle distributed computing on our group cluster. Based on GridMap."

config = {
    'name': 'clustermap',
    'description': description,
    'url': 'https://github.com/nicococo/clustermap',
    'author': 'Nico Goernitz',
    'author_email': 'nico.goernitz@tu-berlin.de',
    'version': '2017.3',
    'install_requires': ['drmaa'],
    'packages': ['clustermap'],
    'package_dir' : {'clustermap': 'clustermap'},
    'classifiers':['Intended Audience :: Science/Research',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python :: 2.7']
}

setup(**config)
