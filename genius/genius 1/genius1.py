from pwn import *

url = "genius.chals.ageei.org"
port = 1338

r = remote(url, port)

def solve(question):
   operand_one = int(question[0])
   operator = question[1]
   operand_two = int(question[2])

   if operator == "+":
      solution = operand_one + operand_two
   elif operator == "-":
      solution = operand_one - operand_two
   elif operator == "*":
      solution = operand_one * operand_two

   return solution
   


while True:

   line = r.recvline().decode().strip()
   print(line)
   if line.startswith("3"):

      print("\n" + line + "\n")
      r.sendline(str(2).encode())
      r.recvline()
      r.sendline(str(1).encode())
      break

while True:
   line = r.recvline().decode().strip()
   if line.startswith("Question"):
      print(line)
      question = r.recvline().decode().strip().split(" ")
      #print(question)
      r.sendline(str(solve(question)).encode())      

   elif "LEGO-" in line:
      print("\n" + line + "\n")
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      break

      
