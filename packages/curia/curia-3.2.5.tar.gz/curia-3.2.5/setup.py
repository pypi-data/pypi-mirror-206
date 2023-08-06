import codecs
import os.path
from glob import glob

from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]

    raise RuntimeError("Unable to find version string.")

setup_packages = [
    'Cython',
    'pytest-runner'
]

required_packages = [
    'importlib-metadata',
    'ipykernel',
    'numpy',
    'scipy',
    'pandas',
    'requests',
    'dynaconf',
    'validation_decorators',
    'scikit-learn',
    'logzero',
    'docutils',
    'packaging',
    'pymaybe',
    'boto3',
    'pyarrow',
    'requests',
    'moto',
    'moto[server]'
]

test_packages = [
    'click',
    'freezegun',
]

extras = {
    'testing': {
        'pytest-cov',
        'pytest-pylint',
        'pytest-mock',
        'flake8',
    },
    'docs': {
        'sphinx',
        'sphinx_rtd_theme',
        'sphinxcontrib-apidoc',
        'sphinx_markdown_builder',
        'sphinx-jekyll-builder',
        'python-frontmatter'
    }
}

name = "curia"
version = get_version("src/curia/__init__.py")

setup(
    name=name,
    version=version,
    description="A library for training and using risk & impactability models on Curia",
    packages=find_packages("src"),
    package_dir={
        "": "src",
        # 'curia': 'src/curia',
        'curia.api': 'src/curia/api',
        'swagger_client': 'src/curia/api/swagger_client'
    },
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type='text/markdown',
    author="Curia.ai",
    url="https://github.com/Curia-ai/curia-python-sdk",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent"
    ],
    setup_requires=setup_packages,
    install_requires=required_packages,
    tests_require=test_packages,
    extras_require=extras,
)
