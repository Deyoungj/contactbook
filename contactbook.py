import sqlite3

password = '12345'
print('please enter your password.')
pd_input1 = input()
tries = 5
while pd_input1!= password:
    tries -= 1
    print('wrong password, try again.')
    pd_input = input()
    if tries == 1:
        print('this is not your safe')
        break
if pd_input1 == password:
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    try:       
        c.execute('''CREATE TABLE contacts (
            Names text,
            phone int,
            email text
            )''')

    except:
        print('safe exist.')
           

    
    while True:
        print('*'*40)
        print('a  = add a contact')
        print('d  = delete a contact')
        print('q  = quit')
        print('v  = view a contact')
        print('vc  = view contact with the same name')
        print('v-update = update contact')
        print('*'*40)
        add = 'a'
        delete = 'd'
        quit = 'q'
        view = 'v'
        viewa = 'v-update'
        viewc = 'vc'

        option = input()
        if option == quit:
            break
        if option == add:
            namen = input('name: ')
            phonen = int(input('phone: '))
            emailn = input('email: ')
            c.execute("INSERT INTO contacts VALUES (:names, :phone, :email)",{'names':namen, 'phone':phonen, 'email': emailn})
            conn.commit()
            print('your contact as been added')
        if option == view:
            print('enter a name.')
            namev = input()
            c.execute("SELECT * FROM contacts WHERE names=:names",{'names': namev})
            print(c.fetchone())
            conn.commit()
        if option == viewc:
            print('contacts with the same name.')
            namec = input()
            c.execute("SELECT * FROM contacts WHERE names=:names",{'names': namec})
            print(c.fetchall())
            conn.commit()
        if option == 'v-update':
            print('-'*8,'update','-'*8)
            print('v-number = to update a contact')
            print('v-email = to update an email')
            print('-'*24)
            updateopt = input()
            if updateopt == 'v-number':
                print('name of the contact you want to update')
                nameupdn = input()
                print('new number')
                newnum = input()
                c.execute("""UPDATE contacts SET phone=:phone WHERE names=:names""",{'names': nameupdn, 'phone':newnum})
                conn.commit()
                print('your contact has been updated')
            if updateopt == 'v-email':
                print('name of the contact you want to update')
                nameem = input()
                print('new email')
                newemail = input()
                c.execute("""UPDATE contacts SET email=:email WHERE names=:names""",{'names': nameem, 'email':newemail})
                conn.commit()
                print('your email has been updated')
        if option == 'd':
            print('enter name of contact to be deleted')
            namedel = input()
            c.execute("DELETE from contacts WHERE names=:names",{'names': namedel})
            conn.commit()
            print('contact has been deleted')
    conn.close