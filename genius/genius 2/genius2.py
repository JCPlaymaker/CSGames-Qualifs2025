from pwn import *

url = "genius.chals.ageei.org"
port = 1338
key = "NaQnXVGdSRhVCjobmw1W"

r = remote(url, port)

def solve (question):
   i = 1
   solution = 0
   operand = int(question[0])

   # For the 1st operation we just add the 1st operand to solution
   solution += operand
   
   # We just add the next operand to the solution depending on operator
   while i < len(question) - 2:
      operator = question[i]
      operand = int(question[i + 1])

      if operator == "+":
         solution += operand
      elif operator == "-":
         solution -= operand
      elif operator == "*":
         solution *= operand

      # To skip to next operator
      i += 2 

   return solution


while True:

   line = r.recvline().decode().strip()
   print(line)
   if line.startswith("3"):

      print("\n" + line + "\n")
      r.sendline(str(2).encode())
      r.recvline()
      r.sendline(str(2).encode())
      r.recvline()
      r.sendline(str(key).encode())
      break

while True:
   line = r.recvline().decode().strip()
   if line.startswith("Question"):
      print(line)
      question = r.recvline().decode().strip().split(" ")
      print(question)
      r.sendline(str(solve(question)).encode())

   elif "LEGO-" in line:
      print("\n" + line + "\n")
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      break
      
     
