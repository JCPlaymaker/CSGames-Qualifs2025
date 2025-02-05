from pwn import *
from sympy import symbols, Eq, solve

url = "genius.chals.ageei.org"
port = 1338
key = "dF83jAcMKZLSUrrVGvAX"  # Unlock key for Genius 3

r = remote(url, port)

def solve_q(question):
    x = symbols('x')  # Define x as a symbolic variable otherwise it crashes
    question = question.replace("x", "*x")  # Ensure multiplication

    left, right = question.split("=")  # Split at '='
    eq = Eq(eval(left), eval(right))  # Evaluate both sides
    solution = solve(eq, x)  # Solve for x

    return str(solution[0]) if solution else "No solution"

while True:

   line = r.recvline().decode().strip()
   print(line)
   if line.startswith("3"):

      print("\n" + line + "\n")
      r.sendline(str(2).encode())
      r.recvline()
      r.sendline(str(3).encode())
      r.recvline()
      r.sendline(str(key).encode())
      break

while True:
   line = r.recvline().decode().strip()
   if line.startswith("Question"):
      print(line)
      question = r.recvline().decode().strip()
      print(question)
      line = r.recvuntil(b"x =")
      if b"x =" in line:
         solution = eval(solve_q(question))
         print(solution)
      print(r.sendline(str(solution).encode()))

   elif "LEGO-" in line:
      print("\n" + line + "\n")
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      break
#print(eval(solve_equation(equation)))    
