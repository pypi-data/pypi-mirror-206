# -*- coding: utf-8 -*-
# author: 长风
import os
import sys

os.system("pip install -r requirements.text -i https://pypi.tuna.tsinghua.edu.cn/simple")
os.system(f"{sys.executable} sql_manage.py")
os.system(f"start /B {sys.executable} app.py>app.log 2>&1")
os.system(f"start /B {sys.executable} fontview.py>fontview.log 2>&1")
