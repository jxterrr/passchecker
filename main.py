import requests
import hashlib

def check(password):
    password_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = password_sha1[:5], password_sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}" 
    response = requests.get(url)

    password = [i for i in response.text.split()]

    for i in password:
        if i.split(':')[0] == suffix:
            return f"The password was found in the leak database. It occurs {i.split(':')[1]} times."
    return f"The password was not found in the leak database. Great password :) "

print(check(input('Enter your password: ')))