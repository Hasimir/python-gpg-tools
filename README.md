# Python GPG Tools

Central point of collation for multiple projects, primarily related to [GPGME](https://www.gnupg.org/).

## License Notes

Some of this work may subsequently be added to other projects and so the Apache license has been selected on the grounds that it is permissive enough for most projects, while still being free enough to permit a re-release under the GPL or LGPL if necessary (e.g. as example code for GPGME's Python bindings).

## Python 2 vs. Python 3

For the most part the focus here is Python 3.  Python 2 is nearly EOL and should not be encouraged, however there will be some things which will need to run on both and thus will contain certain Python 2 specific things.

## GPGME Official bindings vs. other Python GPG wrappers

The focus of my works is, obviously, the official GPGME Python bindings and not the wrappers.  However, some of this code is geared towards explicitly detecting what a system can support or has available and using what is there (or recommending an update in some cases).  Mostly this will be checking for the python-gnupg module, not the gnupg fork, since the python-gnupg module is *far* more widespread.
