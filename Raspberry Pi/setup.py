from distutils.core import setup

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name	= 'Nunchuck_pi',
version	= '0.1',
author	= 'Jason Barnett',
author_email	= 'jase@boeeerb.co.uk',
description	= 'A module to read a wii nunchuck for Raspberry Pi',
long_description= 'A module to read a wii nunchuck for Raspberry Pi',
license	= 'CC BY-SA 3.0',
keywords	= 'Raspberry Pi Nunchuck',
url	= 'http://www.boeeerb.co.uk',
classifiers = classifiers,
py_modules	= ['nunchuck'],
install_requires= ['rpi.gpio >= 0.5.4']
)