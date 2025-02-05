from pwn import *
from sympy import *

url = "genius.chals.ageei.org"
port = 1338
key = "Jyi9r1XYtDetTP8zG1Xg"  # Unlock key for Genius 5

r = remote(url, port)

def solve_q(question):
    x = symbols('x')  # Define x as a symbolic variable otherwise it crashes
    question = question.replace("x", "*x")  # Ensure multiplication
    question = question.replace("^", "**")

    left, right = question.split("=")  # Split at '='
    equation = Eq(sympify(left.strip()), sympify(right.strip()))
    solutions = solve(equation, x)
    solutions = [float(sol.evalf()) for sol in solutions]
    print(solutions)
    return solutions[0]

while True:

   line = r.recvline().decode().strip()
   print(line)
   if line.startswith("3"):

      print("\n" + line + "\n")
      r.sendline(str(2).encode())
      r.recvline()
      r.sendline(str(5).encode())
      r.recvline()
      r.sendline(str(key).encode())
      break

while True:
   line = r.recvline().decode().strip()
   print(line)
   if line.startswith("Question"):
      print(line)
      question = r.recvline().decode().strip()
      print(question)
      line = r.recvuntil(b"x =")
      if b"x =" in line:
         
         solution = solve_q(question)
      print(r.sendline(str(solution).encode()))

   elif "LEGO-" in line:
      print("\n" + line + "\n")
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      break
#print(eval(solve_equation(equation)))    
