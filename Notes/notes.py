import os

import Operations

cur_dir_path = os.path.abspath(os.curdir)
dir_path = os.path.join(cur_dir_path, "NotesDir")
if not os.path.exists("NotesDir"):
    os.mkdir(dir_path)

operations = [[1, "Note search", lambda: Operations.note_search()],
              [2, "Print notes by date", lambda: Operations.notes_by_date()],
              [3, "Print whole note list", lambda: Operations.print_note_list()],
              [4, "Add note", lambda: Operations.add_note()],
              [5, "End work", lambda: exit()]]


# Programm start
Operations.menu(operations,dir_path)
