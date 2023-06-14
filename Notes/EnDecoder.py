import json
def encoder(cur_note):
    print(json.dumps({'id':cur_note.ident,
                'name':str(cur_note.name),
                'body':str(cur_note.body),
                'data_time':str(cur_note.data_time)}))

def decoder(cur_note):
    print(json.loads(cur_note))