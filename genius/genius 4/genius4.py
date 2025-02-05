from pwn import *
from sympy import *

url = "genius.chals.ageei.org"
port = 1338
key = "syibBOl88cm545dcER5R"  # Unlock key for Genius 4

r = remote(url, port)

def solve_q(a,b):
   #Define x and y as symbolic var so it doesnt crash
   x,y = symbols('x,y')
   
   left1,right1 = a.split("= ")
   eq1 = Eq(sympify(left1), int(right1))

   left2,right2 = b.split("=")
   eq2 = Eq(sympify(left2), int(right2))

   solution = solve((eq1, eq2), (x, y))
   solution = {var: float(value.evalf()) for var, value in solution.items()}
   print(f"SymPy Solution: {solution}")

   return [solution[x], solution[y]]


while True:

   line = r.recvline().decode().strip()
   print(line)
   if line.startswith("3"):

      print("\n" + line + "\n")
      r.sendline(str(2).encode())
      r.recvline()
      r.sendline(str(4).encode())
      r.recvline()
      r.sendline(str(key).encode())
      break

while True:
   line = r.recvline().decode().strip()
   print(line)
   if line.startswith("Question"):
      eq_1 = r.recvline().decode().strip()
      eq_1 = eq_1.replace("x ", "*x").replace("y ", "*y").replace("+ ", "+")
      eq_2 = r.recvline().decode().strip()
      eq_2 = eq_2.replace("x ", "*x").replace("y ", "*y").replace("+ ", "+")
      matrix = solve_q(eq_1,eq_2)
      # For the goddamn answer without crashing
      line = r.recvuntil(b"x =")
      if b"x =" in line:
         print(r.sendline(str(matrix[0]).encode()))
      line = r.recvuntil(b"y =")
      if b"y =" in line:
         print(r.sendline(str(matrix[1]).encode()))

   elif "LEGO-" in line:
      print("\n" + line + "\n")
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      print(r.recvline().decode().strip())
      break   
