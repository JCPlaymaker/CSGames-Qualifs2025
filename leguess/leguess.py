from pwn import *

# Where the magic happens
# So basically the logic is to go with a binary search
def solveGame(min_value, max_value, max_attempts, r):
   
   attempts = 0
   
   while attempts < max_attempts:
      # We get the middle value of the range and send it
      middle_value = (max_value + min_value) // 2
      r.sendline(str(middle_value).encode())
      response = r.recvline().decode().strip()
      print(f"Tentative {attempts}: " + response)

      if "Bleu" in response:
         max_value = middle_value
      elif "Rouge" in response:
         min_value = middle_value
      else:
         break

      attempts += 1      


# ncat leguess.chals.ageei.org 1341
url = "leguess.chals.ageei.org"
port = 1341

r = remote(url, port)

while True:

   # We want to receive lines until we get the ranges and attempts
   line = r.recvline().decode().strip()
   if line.startswith("Défi"):

      # Once we have it we have them we start extracting them
      print("\n" + line + "\n")
      line = line.split(" ")
      values = line [4].lstrip("(").rstrip(")").split("-")

      max_attempts = int(line [6])
      min_value = int(values[0])
      max_value = int(values[1])
      
      # We skip the goddamn extra line
      r.recvline().decode()

      # We start solving
      solveGame(min_value, max_value, max_attempts, r)

   # Once we're done, we'll read everything up until flag then break
   elif "LEGO-" in line:
      print("\n" + line + "\n")
      break
