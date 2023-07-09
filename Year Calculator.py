import os
whatyearpower = 'start'
while whatyearpower == 'start':
    usersquestion = input('Enter the year you want to query here:')
    uq = usersquestion
    uq = int(uq)
    if uq % 4 == 0:
        year = 'yes'
    else:
        year = 'no'
    if year == 'yes':
        os.system('msg * The year you are querying is a leap year')
    if year == 'no':
        os.system('msg * The year you are querying is a common year')
    if uq == 'exit':
        os.system('msg * Exited the Year Calculator')
        whatyearpower = 'poweroff'