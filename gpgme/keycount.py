#!/usr/bin/env python3

import gpg

c = gpg.Context()
skeys = c.keylist(pattern=None, secret=True)
pkeys = c.keylist(pattern=None, secret=False)

skeys_list = list(skeys)
secret_keys = len(skeys_list)

pkeys_list = list(pkeys)
public_keys = len(pkeys_list)

print("""
Number of secret keys:  {0}
Number of public keys:  {1}
""".format(secret_keys, public_keys))
