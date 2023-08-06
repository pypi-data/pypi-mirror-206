import codecs

from setuptools import setup, find_packages


# -*- Long Description -*-


def long_description():
    try:
        return codecs.open('README.md', 'r', 'utf-8').read()
    except OSError:
        return 'Long description error: Missing README.rst file'


setup(
    name='py-strongly-typed',
    description='Python type enforcer',
    long_description=long_description(),
    packages=find_packages(exclude=["*tests*"]),
    author='Christian Silva',
    author_email='chrislcontrol@hotmail.com',
    long_description_content_type='text/markdown',
    license='MIT License',
    python_requires=">=3.5",
    version='1.1.2',
    project_urls={
        "GitHub": "https://github.com/chrislcontrol/py-strongly-typed"
    },
    install_requires=[
        'wheel'
    ],
    extras_require={
        'dev': [
            'pycodestyle',
            'flake8',
            'twine>=4.0.2',
        ],
    }
)
