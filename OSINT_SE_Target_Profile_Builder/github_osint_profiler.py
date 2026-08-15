import requests, json

def github_profile(username):
    base = "https://api.github.com"
    u = requests.get(f"{base}/users/{username}").json()
    repos = requests.get(f"{base}/users/{username}/repos").json()
    
    langs = {}
    for r in repos[:10]:
        if r.get('language'):
            langs[r['language']] = langs.get(r['language'],0)+1
            
    profile = {
        "name" : u.get("name"),
        "company" : u.get("company"),
        "location" : u.get("location"),
        "public_repos": u.get("public_repos"),
        "top_langs" : langs,
        "bio" : u.get("bio"),
    }
    print(json.dumps(profile, indent=2))

github_profile("CyberBros435")
