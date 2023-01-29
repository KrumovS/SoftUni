username = input()
password = input()
sign_in_password = input()

while sign_in_password != password:
    sign_in_password = input()


print (f'Welcome {username}!')