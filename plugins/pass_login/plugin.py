import time

f = open('pass_login\pass.txt')
for line in f:
    line
pass_auth = input("Password: ")
if pass_auth == line:
    print("Succes")
else:
    print("ERROR")
    time.sleep(5)
    exit(0)
