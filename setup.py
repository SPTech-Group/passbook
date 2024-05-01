from setuptools import setup

version = __import__('passbook').__version__

setup(
    name='Passbook',
    version=version,
    author='RIZZO',
    author_email='',
    packages=['passbook', 'passbook.test'],
    url='http://github.com/SPTech-Group/passbook',
    license=open('LICENSE.txt').read(),
    description='Passbook file generator',
    long_description=open('README.md').read(),

    download_url='git+https://github.com/SPTech-Group/passbook.git',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    install_requires=[
        'cryptography==38.0.4',
    ],

)
