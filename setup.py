from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name='unittest_expander',
    version='0.1.0',
    packages = find_packages(),

    author='Jan Kaliszewski',
    author_email='zuo@kaliszewski.net',
    description='Easy and flexible unittest parameterization.',
    long_description=(
        'A library that provides flexible and easy-to-use tools to '
        'parameterize (i.e. multiply applying the specified parameters) '
        'your unit tests, especially those based on `unittest.TestCase`.'),
    license='MIT',
    keywords='unittest testing parameterization parametrization',
    url='https://github.com/zuo/unittest_expander',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
    ],
)