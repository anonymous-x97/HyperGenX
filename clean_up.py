import os

path_ = "tools/in_memory=True.session"

if os.path.exists(str(path_)):
    os.remove(path_)
