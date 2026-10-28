import re
from pathlib import Path

from setuptools import setup, find_packages

here = Path(__file__).parent

# Single source of truth: Products/ZSQLiteDA/__init__.py.__version__
# (read as text -- importing the package would pull in Zope).
version = re.search(
    r"^__version__ = '([^']+)'",
    here.joinpath('Products', 'ZSQLiteDA', '__init__.py').read_text(
        encoding='utf-8'),
    re.M,
).group(1)

setup(name='Products.ZSQLiteDA',
      version=version,
      description="SQLite database adapter for Zope4",
      long_description=open("README.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Zope :: 4",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: Zope Public License",
        ],
      keywords='SQLite',
      author='Hajime Nakagami',
      author_email='nakagami@gmail.com',
      url='https://github.com/nakagami/Products.ZSQLiteDA',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'Products.ZSQLMethods',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
