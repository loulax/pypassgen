import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "&~#{}[]()-_^@$*%!:;"
length = int(input("Password length : "))
all = lower + upper + numbers + symbols

password = "".join(random.sample(all, length))

print(password)