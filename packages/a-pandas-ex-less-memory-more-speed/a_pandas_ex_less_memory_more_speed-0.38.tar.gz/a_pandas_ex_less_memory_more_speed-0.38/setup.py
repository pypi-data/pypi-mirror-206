from setuptools import setup, find_packages
# import codecs
# import os
# 
# here = os.path.abspath(os.path.dirname(__file__))
# 
# with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()\

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '''0.38'''
DESCRIPTION = '''A Python package to reduce the memory usage of pandas DataFrames. It speeds up your workflow and reduces the risk of running out of memory.'''

# Setting up
setup(
    name="a_pandas_ex_less_memory_more_speed",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_less_memory_more_speed',
    author="Johannes Fischer",
    author_email="aulasparticularesdealemaosp@gmail.com",
    description=DESCRIPTION,
long_description = long_description,
long_description_content_type="text/markdown",
    #packages=['check_if_nan', 'deepcopyall', 'isiter', 'numpy', 'pandas', 'tolerant_isinstance'],
    keywords=['flatten', 'pandas', 'dict', 'list', 'numpy', 'tuple', 'Tagsiter', 'nested', 'iterable', 'listsoflists', 'flattenjson', 'iter', 'explode', 'squeeze', 'nan', 'pd.NA', 'np.nan'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.10', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Utilities'],
    install_requires=['check_if_nan', 'deepcopyall', 'isiter', 'numpy', 'pandas', 'tolerant_isinstance'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*