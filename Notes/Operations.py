import glob, os
import EnDecoder
from Note import Note
from time import sleep
import Inputs
import Identification
operations = [[1, "Note search", "note_search"],
              [2, "Print notes by date","notes_by_date"],
              [3, "Print whole note list", "print_note_list"],
              [4, "Add note", "add_note"],
              [5, "End work", lambda: exit()]]

def menu(operations,dir_path, message="Menu",cur_note=None):
    choice = front_menu(operations,message)

    while choice != (operations[-1][0]):  # cicle for not end
        try:
            globals()[operations[choice - 1][2]](cur_note,dir_path)
        except TypeError:
            globals()[operations[choice - 1][2]](dir_path)
        choice = front_menu(operations,message)


def front_menu(operations,message):
    leng = max([len(i[1]) for i in operations])
    print(message)
    for i in operations:
        print("|{}".format(i[0]) + "|{}".format(i[1]) + " " * (leng - len(i[1])))
    return Inputs.inputing_int("Select one of the following menu items")

def note_search(dir_path):
    if len(os.listdir(dir_path)) == 0:
        print("Catalog is empty. Add a note first")
        sleep(0.7)
    else:
        message = "What you know about this note? Input one parameter (id/name):"
        answer = Inputs.inputing_str(message)
        founded_file = searching_idname(answer, message,dir_path)
        check_que = Inputs.inputing_str("Is there file what you need? (Yes/No) \n")
        if str(check_que).lower() == "yes":
            if len(founded_file) > 1:
                cur_note = dir_path+f'\\{searching_idname(Inputs.inputing_str("Input full id of the file"), "Input here: ",dir_path)[0]}'
            else:
                cur_note = dir_path+f'\\{founded_file[0]}'
            additional_operations = [[1, "Edit note", lambda: edit_note(cur_note,dir_path)],
                                     [2, "Remove note", lambda: remove_note(cur_note)],
                                     [3, "Go to head menu", lambda: quit()]]
            menu(additional_operations,
                 "If you want to do something with note you can choose here",
                 cur_note)
        else:
            print("Sorry, but we cannot find your note. Try something another!")
            exit(note_search(dir_path))


def searching_idname(answer, message,dir_path):
    search_files = []
    os.chdir(dir_path)
    search = glob.glob(f"*{answer}*.json")
    if len(search) != 0:
        for file in search:
            search_files.append(file)
            print(str(len(search_files))+"| "+search_files[-1])
    else:
        print("No file with this parameter!")
        answer = Inputs.inputing_str(message)
        searching_idname(answer, message,dir_path)
    return search_files

def notes_by_date(dir_path):
    if len(os.listdir(dir_path)) == 0:
        print("Catalog is empty. Add a note first")
        sleep(0.7)
    else:
        dirLs ={}
        for i in os.listdir(dir_path):
            dirLs[i]=os.path.getmtime(dir_path+f"\\{i}")
        sortedDir = dict(sorted(dirLs.items(),key=lambda item: item[1]))
        for i in sortedDir.items():
            print(f"{i[0]}:{i[1]}")



def print_note_list(dir_path):
    if len(os.listdir(dir_path)) == 0:
        print("Catalog is empty. Add a note first")
        sleep(0.7)
    else:
        print("LIST OF NOTES")
        print(os.listdir(dir_path))
        sleep(1)


def add_note(dir_path):
    name = Inputs.inputing_str("What is name of note? ")
    body = Inputs.inputing_str("What is text of note? (input in 1 string): ")
    cur_note = Note(Identification.identificator(), name, body)
    with open(dir_path + f"\\{cur_note.ident}_{cur_note.name}.json", 'w') as f:
        f.write(EnDecoder.encoder(cur_note))
        f.flush()
        os.fsync(f.fileno())



def edit_note(cur_note,dir_path):
    body = Inputs.inputing_str("What is new text of note? (input in 1 string): ")
    note = EnDecoder.decoder((cur_note))
    parameters = [i[1] for i in dict(note).items()]
    new_note = Note(parameters[0],parameters[1],body)
    os.remove(cur_note)
    with open(dir_path + f"\\{new_note.ident}_{new_note.name}.json", 'w') as f:
        print(dir_path + f"\\{new_note.ident}_{new_note.name}.json")
        f.write(EnDecoder.encoder(new_note))
        f.flush()
        os.fsync(f.fileno())
    print('You new note was saved like this:')
    printing =[print(f"{i[0]} : {i[1]}") for i in dict(EnDecoder.decoder(dir_path + f"\\{new_note.ident}_{new_note.name}.json")).items()]


def remove_note(cur_note):
    os.remove(cur_note)
