# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

# Run with: python checkgpg.py or python3 checkgpg.py

import os.path
import sys

if sys.version_info[0] == 2:
    try:
        import gpg
        found_gpg = True
    except ImportError:
        found_gpg = False
        pass
    try:
        import pyme
        found_pyme = True
    except ImportError:
        found_pyme = False
        pass
    except AttributeError:
        found_pyme = False
        pass
    try:
        import gnupg
        found_gnupg = True
    except ImportError:
        found_gnupg = False
        pass
    pass
elif sys.version_info[0] >= 3:
    try:
        import gpg
        found_gpg = True
    except ModuleNotFoundError:
        found_gpg = False
        pass
    try:
        import pyme
        found_pyme = True
    except ModuleNotFoundError:
        found_pyme = False
        pass
    except AttributeError:
        found_pyme = False
        pass
    try:
        import gnupg
        found_gnupg = True
    except ModuleNotFoundError:
        found_gnupg = False
        pass
    pass
else:
    pass

if found_gpg is True:
    print("A gpg module has been found, check to see if it is the official module.")
    if os.path.exists(gpg.core.get_engine_info()[0].file_name) is True:
        found_gpgme = True
        print("The gpg module appears to be the official GPGME Python module.")
    else:
        found_gpgme = False
        print("There is a module called gpg, but it is not the correct one; please check your installed modules.")
else:
    found_gpgme = False
    print("There is no gpg module, please install it with the GPGME API available from https://gnupg.org/")

if found_pyme is True:
    print("The pyme module is an earlier version of the GPGME official module, please upgrade to the current version of the GPGME API available from https://gnupg.org/")
else:
    pass

if found_gnupg is True:
    try:
        gnupg.GPG(gnupghome=None)
        found_gnupg_lib = True
        found_gnupg_bin = True
        print("The python-gnupg module is available.")
    except TypeError:
        gnupg = None
        found_gnupg_lib = False
        found_gnupg_bin = True
        print("There is a module called gnupg available, but it is not the python-gnupg module.")
    except OSError:
        gnupg = None
        found_gnupg_lib = True
        found_gnupg_bin = False
        print("The python-gnupg module is installed, but the GPG executable cannot be found.")
elif found_gnupg is False:
    print("The python-gnupg module is not installed.")
else:
    pass
