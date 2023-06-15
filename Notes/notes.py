import os

import Operations

cur_dir_path = os.path.abspath(os.curdir)
dir_path = os.path.join(cur_dir_path, "NotesDir")
if not os.path.exists("NotesDir"):
    os.mkdir(dir_path)


# Programm start
Operations.menu(Operations.operations,dir_path)
