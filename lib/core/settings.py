#!/usr/bin/env python

import os
import sys

# The name of the operating system dependent module imported.
# The following names have currently been registered: 'posix', 'nt', 'mac', 'os2', 'ce', 'java', 'riscos'
PLATFORM = os.name
PYVERSION = sys.version.split()[0]
IS_WIN = PLATFORM == "nt"
