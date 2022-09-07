

data = {}


def loaddata(data):
    lib = open('D:\\do\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_hackpasswords\\lib.txt', 'r')
    for acc in lib:
        data[acc.split(' ')[0]] = acc.split(' ')[1].split('\n')[0]
    lib.close()

def createacc():
    accname = input('Your are creating new account.\nEnter your account name: ')
    while ' ' in accname:
        accname = input('No space, please enter your account name: ')
    accpass = input('Enter your password: ')
    while ' ' in accpass:
        accpass = input('No space, please enter your password: ')
    lib = open('D:\\do\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_hackpasswords\\lib.txt', 'a')
    lib.write('\n')
    lib.write(accname)
    lib.write(' ')
    lib.write(accpass)
    lib.close()

def login():
    loaddata(data)
    accname = input('Enter account name: ')
    if accname in data:
        accpass = input('Enter your password: ')
        while accpass != data[accname]:
            print('Wrong password!')
            accpass = input('Enter your password: ')
        else:
            print('Login successfully.')
    else:
        print('There is no account like this.')
login()
