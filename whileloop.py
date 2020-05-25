num_of_tries =0
while num_of_tries != 3:
    username = input('please enter username: ')
    password = input('please enter password: ')
    if username == 'kamel' and password == '123':
        print('login')
        num_of_tries=0
        exit()
    else:
        print('error')
        num_of_tries +=1
        print('you have ' + str( 3 - num_of_tries) + ' tries left')