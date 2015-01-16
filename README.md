[![Build Status](https://travis-ci.org/WellDone/pymomo.svg?branch=dev)](https://travis-ci.org/WellDone/pymomo)
[![PyPI version](https://badge.fury.io/py/pymomo.svg)](http://badge.fury.io/py/pymomo)

# pymomo
A python library for interacting with MoMo devices.

## Installation

```
pip install --allow-external intelhex --allow-unverified intelhex --allow-external dirspec --allow-unverified dirspec pymomo
```

Pymomo currently relies on two non-PyPI packages, `intelhex` and `dirspec`.  This should change soon.

To build MoMo firmware you must also install [SCons](http://www.scons.org/)* and [two Microchip compilers](http://www.microchip.com/pagehandler/en_us/devtools/mplabxc/) - XC8 and XC16

* On Mac OSX you may need to add the environment variable `export PYTHONPATH=/usr/local/lib/scons-2.3.4` (or similar if you installed a different version or in a different location) to your shell initialization script (i.e. ~/.bashrc)

## Copyright and license
Code and documentation copyright 2012-2015 WellDone International. Code released under the [GPLv3](http://www.gnu.org/licenses/gpl.html) Open Source license.  See the LICENSE file for more details.