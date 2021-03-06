[![Travis Build Status](https://travis-ci.org/WellDone/pymomo.svg)](https://travis-ci.org/WellDone/pymomo)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/7t80jgu9efkmale5?svg=true)](https://ci.appveyor.com/project/amcgee/pymomo)
[![PyPI version](https://badge.fury.io/py/pymomo.svg)](http://badge.fury.io/py/pymomo)

# pymomo
A python library for interacting with MoMo devices.

## Installation

```
pip install pymomo
```

To build MoMo firmware you must also install [SCons](http://www.scons.org/)* and [two Microchip compilers](http://www.microchip.com/pagehandler/en_us/devtools/mplabxc/) - XC8 and XC16

* On Mac OSX you may need to add the environment variable `export PYTHONPATH=/usr/local/lib/scons-2.3.4` (or similar if you installed a different version or in a different location) to your shell initialization script (i.e. ~/.bashrc)

## Copyright and license
Code and documentation copyright 2015 WellDone International. The pymomo library is released under the [LGPLv3](https://www.gnu.org/licenses/lgpl.html) Open Source license.  See the LICENSE file.

Pymomo embeds version 1.5 of the [intelhex](http://pythonhosted.org/IntelHex/) package.  The `intelhex` code retains its original BSD license, which [allows for embedded redistribution](http://pythonhosted.org/IntelHex/part4.html#embedding-into-other-projects).
