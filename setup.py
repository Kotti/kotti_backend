import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

version = '0.1.1.dev0'

install_requires = [
    'Kotti>=1.0.0',
]


setup(
    name='kotti_backend',
    version=version,
    description="Turns Kotti CMS into a private content administration area",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
    ],
    author='Kotti developers',
    author_email='kotti@googlegroups.com',
    url='https://github.com/Kotti/kotti_backend',
    keywords='kotti web cms wcms pylons pyramid sqlalchemy bootstrap',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[],
    entry_points={
    },
    extras_require={},
)
