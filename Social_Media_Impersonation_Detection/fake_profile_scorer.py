def fake_profile_score(profile):
    score = 0
    age_days = profile.get("account_age_days", 365)

    if age_days < 30:
        score += 30

    followers = profile.get("followers", 1)
    following = profile.get("following", 1)
    ratio = following / max(followers, 1)

    if ratio > 10:
        score += 25
    if profile.get("no_profile_pic"):
        score += 20
    if profile.get("posts", 100) < 5:
        score += 15
    if profile.get("default_bio"):
        score += 10

    return min(score, 100)


profiles = [
    {
        "account_age_days": 7,
        "followers": 2,
        "following": 900,
        "no_profile_pic": True,
        "posts": 1,
        "default_bio": True,
    },
    {
        "account_age_days": 1200,
        "followers": 4500,
        "following": 320,
        "no_profile_pic": False,
        "posts": 870,
        "default_bio": False,
    },
    {
        "account_age_days": 15,
        "followers": 30,
        "following": 1800,
        "no_profile_pic": True,
        "posts": 3,
        "default_bio": True,
    },
    {
        "account_age_days": 600,
        "followers": 220,
        "following": 410,
        "no_profile_pic": False,
        "posts": 150,
        "default_bio": False,
    },
    {
        "account_age_days": 45,
        "followers": 80,
        "following": 950,
        "no_profile_pic": False,
        "posts": 12,
        "default_bio": True,
    },
]

for i, p in enumerate(profiles):
    print(f"Profile {i+1} -> Fake Score: {fake_profile_score(p)}%")
