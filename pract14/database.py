import dbm
import pickle
import sys


def perform(database, command, arguments):
    if command == 'set':
        if len(arguments) < 2:
            pass
        else:
            db = dbm.open(database, 'c')
            db[arguments[0]] = pickle.dumps(arguments[1:])
            db.close()
    elif command == 'get':
        key = arguments[0]
        db = dbm.open(database, 'r')
        data = db[key]
        data = pickle.loads(data)
        print(data[0])
        db.close()
    elif command == 'del':
        key = arguments[0]
        db = dbm.open(database, 'c')
        del db[key]
        db.close()
    elif command == 'keys':
        db = dbm.open(database, 'r')
        print(' '.join([key.decode('utf-8') for key in db.keys()]))
        db.close()
    elif command == 'values':
        db = dbm.open(database, 'r')
        for k, v in db.items():
            print(f'{k.decode("utf-8")} {pickle.loads(v)[0]}')
        db.close()
    elif command == 'info':
        print('''usage:
            database-name set key value
            database-name get key
            database-name del key
            database-name keys
            database-name values''')
    else:
        pass


run = True
while run:
    prompt = ' '.join(sys.argv[1:])
    # prompt = input('')
    run = False
    if prompt == 'q':
        run = False
    else:
        prompt = prompt.split(' ')
        # print(prompt)
        if len(prompt) > 2:
            name, action, args = prompt[0], prompt[1], prompt[2:]
        elif len(prompt) == 2:
            name, action = prompt[0], prompt[1]
            args = []
        elif len(prompt) == 1:
            name = prompt[0]
            action = 'info'
            args = []
        else:
            pass
        perform(name, action, args)
