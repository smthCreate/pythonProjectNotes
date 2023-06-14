import os
import glob, os
import EnDecoder
import datetime
from Note import Note
from time import sleep
import Inputs

cur_dir_path = os.path.abspath(os.curdir)
dir_path = os.path.join(cur_dir_path,"NotesDir")
if os.path.exists("NotesDir")!=True:
    os.mkdir(dir_path)

def note_search():
    message = "What you know about this note? Input one parametr (id/name):"
    answer = Inputs.inputing_str(message)
    founded_file = searching_idname(answer, message)
    check_que = Inputs.inputing_str("Is there only file what you need? (Yes/No) \n")
    while str(check_que).lower()!="yes":
        dop_answer = Inputs.inputing_str("Please, input additional parameter")

    additional_operations=[[1, "Edit note", lambda: edit_note(founded_file)],
    [2, "Remove note", lambda: remove_note(founded_file)]]


def searching_idname(answer, message):
    search_files = None
    os.chdir(dir_path)
    search = glob.glob(f"*{answer}*.txt")
    if len(search) != 0:
        for file in search:
            print(file)
            search_files = file
    else:
        print("No file with this parameter!")
        answer = Inputs.inputing_str(message)
        searching_idname(answer, message)
    return search_files


def notes_by_date():
    pass


def print_note_list():
    pass


def add_note():
    name = Inputs.inputing_str("What name of note?")
    body = Inputs.inputing_str("What text of note? (input in 1 string")
    ident = len(os.listdir(dir_path))
    cur_note = Note(ident+1,name,body)
    with open(dir_path+f"\\{cur_note.ident}_{cur_note.name}_{cur_note.time}_{cur_note.data}.txt",'w') as f:
        f.write(body)
        print("File is done!")
        sleep(0.6)


def edit_note(cur_note):
    pass


def remove_note(cur_note):
    pass


def menu():
    operations = [[1, "Note search", lambda: note_search()],
                  [2, "Print notes by date", lambda: notes_by_date()],
                  [3, "Print whole note list", lambda: print_note_list()],
                  [4, "Add note", lambda: add_note()],
                  [5, "End work", lambda: exit()]]  #if you want to change or remove note, you schould search it first.
    choice = front_menu(operations)
    while choice != (operations[-1][0] + 1):  # cicle for not end
        operations[choice - 1][2]()  #
        choice = front_menu(operations)

def front_menu(operations):
    leng = max([len(i[1]) for i in operations])
    for i in operations:
        print("|{}".format(i[0]) + "|{}".format(i[1]) + " " * (leng - len(i[1])))
    return Inputs.inputing_int("Select one of the following menu items")

menu()