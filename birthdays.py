birthdays={'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar4'}

while True:
    print('Enter a name: (blank to quit)')
    name=input()
    #quit program if no name is given
    if name== '':
        break

    if name in birthdays:
        print(birthdays[name]+ ' is ' + name + "'s" + ' birthday')
    else:
        print('There is no available birthday information for ' +name)
        #ask for a birthday input if none is given
        print('What is their birthday?')
        #ask for birthday input
        birthday=input()
        birthdays[name]=birthday
        print('Birthday database updated')
    
