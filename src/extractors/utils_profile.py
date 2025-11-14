thonpython
import hashlib
import random

def generate_mock_profile_data(url: str) -> dict:
    """Generate deterministic mock data for demonstration."""
    seed = int(hashlib.md5(url.encode()).hexdigest(), 16)
    random.seed(seed)

    names = ["Alice Doe", "John Smith", "Maria Gomez", "David Lee"]
    locations = ["USA", "Canada", "UK", "Germany"]

    profile = {
        "name": random.choice(names),
        "profileImgURL": f"https://images.example.com/{seed % 1000}.jpg",
        "coverURL": f"https://covers.example.com/{seed % 500}.jpg",
        "distance": "2nd",
        "title": "Software Engineer",
        "location": random.choice(locations),
        "followers": random.randint(100, 2000),
        "connections": f"{random.randint(100, 500)}+",
        "about": "This is a generated mock profile.",
        "profileContacts": {
            "linkedinProfile": url,
            "website": "https://example.com",
            "phone": "+123456789",
            "email": "user@example.com",
            "twitter": "",
            "birthday": "January 1",
            "ims": "mock@example.com",
        },
        "experience": [
            {
                "expTitle": "Developer",
                "expCompName": "TechCorp",
                "expCompLogo": "https://logo.example.com/company.png",
                "expCompURL": "https://linkedin.com/company/techcorp",
                "expDuration": "2020 - Present",
                "expLocation": "Remote",
            }
        ],
        "education": [
            {
                "eduFrom": "University of Example",
                "eduDegree": "B.Sc. Computer Science",
                "eduLogo": "https://logo.example.com/university.png",
                "eduURL": "https://linkedin.com/school/university",
                "eduDate": "2016 - 2020",
            }
        ],
        "license": [
            {
                "licenseName": "Certified Tester",
                "compName": "Testing Org",
                "licenseURL": "https://certs.example.com",
                "credentialID": "ID-12345",
            }
        ],
        "skills": ["Python", "Data Analysis", "Automation"],
    }

    return profile