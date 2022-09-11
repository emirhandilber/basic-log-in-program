
username=input('Type your user name : ')
i = 0
password='password'
while True:
    inputpass=input('Type your password : ')
    i+=1
    if inputpass == password:
        print('Log in succesfull!')
        break
    elif i == 3:
        break