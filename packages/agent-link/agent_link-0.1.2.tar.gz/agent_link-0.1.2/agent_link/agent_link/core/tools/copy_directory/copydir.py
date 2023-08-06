import os
import shutil

def copy_directory(src, dest):
    os.makedirs(dest, exist_ok=True)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_directory(s, d)
        else:
            shutil.copy2(s, d)
