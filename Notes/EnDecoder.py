import json
def encoder(cur_note):
    return (json.dumps({'id': cur_note.ident,
                        'name': str(cur_note.name),
                        'body': str(cur_note.body),
                        'data': str(cur_note.data),
                        'time': str(cur_note.time)}))

def decoder(cur_note):
    note=None
    parameters = []
    with open(cur_note,'r') as f:
        note = (json.loads(f.read()))
    return note
