# -*- coding: utf-8 -*-
# author: 长风
import os
import sys

import site

print()


os.chdir(f'{site.getsitepackages()[-1]}/hctest_basic_platform')
os.system(f"{sys.executable} sql_manage.py")
os.system(f"start /B {sys.executable} app.py>app.log 2>&1")
os.system(f"start /B {sys.executable} fontview.py>fontview.log 2>&1")
