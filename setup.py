"""
Flipkart Products API
=====================

Flipkart products API enables you to use the current products listed, and the
current offers available on flipkart.com to provide high-quality and reliable
information to your users.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='fkapi',
    version='0.1.0-alpha',
    url='http://www.flipkart.com/affiliate/',
    license='Apache',
    author='Dipanjan Mukherjee',
    author_email='dipanjan.mu@gmail.com',
    description='APIs for programmatic access to products and offers on flipkart.com',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    packages=[],
    include_package_data=True,
    test_suite='',
    zip_safe=False,
    platforms='any'
)
