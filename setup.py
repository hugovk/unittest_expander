import re

from setuptools import setup


VERSION_REGEX = re.compile(b'''
    ^
    release
    \s*
    =
    \s*
    ['"]
    (?P<version>
        [^'"]+
    )
    ['"]
    \s*
    $
''', re.VERBOSE)


def get_version():
    with open('docs/conf.py', 'rb') as f:
        for line in f:
            match = VERSION_REGEX.search(line)
            if match:
                return match.group('version').decode('utf-8')
    raise AssertionError('version not specified')


def get_long_description():
    with open('README.rst', 'rb') as f:
        return f.read().decode('utf-8')


setup(
    name='unittest_expander',
    version=get_version(),
    py_modules=['unittest_expander'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',

    author='Jan Kaliszewski (zuo)',
    author_email='zuo@kaliszewski.net',
    description='Easy and flexible unittest parameterization.',
    long_description=get_long_description(),
    long_description_content_type='text/x-rst',
    keywords='unittest testing parameterization parametrization',
    url='https://github.com/zuo/unittest_expander',
    project_urls={
        'Documentation': 'https://unittest-expander.readthedocs.io/en/stable/',
        'Source': 'https://github.com/zuo/unittest_expander',
        'Tracker': 'https://github.com/zuo/unittest_expander/issues',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Testing',
    ],
)
