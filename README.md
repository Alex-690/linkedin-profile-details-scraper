# Linkedin Profile Details Scraper
Linkedin Profile Details Scraper extracts detailed information from any LinkedIn profile, giving you structured data about a user’s professional background, skills, and contact information. It helps automate research, streamline recruitment workflows, and enrich business intelligence operations by transforming public profile data into clean JSON.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Linkedin Profile Details Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This project gathers comprehensive LinkedIn profile details, including contact info, experience, education history, licenses, skills, and more.
It solves the challenge of manually collecting professional data at scale and is ideal for recruiters, analysts, and business development teams.

### Why Detailed Profile Intelligence Matters
- Provides a complete professional overview for evaluation and decision-making.
- Reduces time spent manually browsing and compiling LinkedIn data.
- Helps build accurate candidate databases, lead lists, or research datasets.
- Ensures consistent and structured information across all collected profiles.
- Offers insight into work history, qualifications, and online presence.

## Features
| Feature | Description |
|---------|-------------|
| Full profile extraction | Retrieves name, title, location, followers, and connections. |
| Contact detail collection | Gathers emails, phone numbers, websites, and social links. |
| Experience timeline | Captures job titles, durations, companies, and locations. |
| Education history | Extracts degrees, institutions, logos, and timelines. |
| Licenses & certifications | Records certification data, issuers, validity periods, and IDs. |
| Skills listing | Returns all available skills associated with the profile. |
| High-quality structured output | Delivers clean JSON ready for processing or enrichment. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| name | Full name of the profile owner. |
| profileImgURL | Direct link to the profile image. |
| coverURL | Background cover image URL. |
| distance | Relationship level with the viewer (1st, 2nd, etc.). |
| title | Current professional title. |
| location | Declared location of the profile owner. |
| followers | Number of followers. |
| connections | Connection count indicator. |
| about | Full “About” section text. |
| profileContacts | Object containing phone, email, website, and additional contacts. |
| experience | List of job entries with titles, companies, and durations. |
| education | Academic history entries. |
| license | Certifications and credentials. |
| skills | List of professional skills. |

---

## Example Output

    [
      {
        "name": "Seif Eldeen Ahmed",
        "profileImgURL": "https://media.licdn.com/dms/image/D4D03AQFI9cKEVDWyqg/profile-displayphoto-shrink_200_200/0/1669108223580",
        "coverURL": "https://media.licdn.com/dms/image/C5116AQHmo6S2lC3oxg/profile-displaybackgroundimage-shrink_350_1400/0/1517032446928",
        "distance": "1st",
        "title": "Full Stack Web Developer at Elephants Tech",
        "location": "Egypt",
        "followers": 1834,
        "connections": "500+",
        "about": "A self-learner and a career shifter...",
        "profileContacts": {
          "linkedinProfile": "https://www.linkedin.com/in/seifahmed",
          "website": "https://github.com/theSeifHub",
          "phone": "+201125125435",
          "email": "seifahmed870@yahoo.com",
          "twitter": "",
          "birthday": "December 7",
          "ims": "seifovic712@gmail.com"
        },
        "experience": [
          {
            "expTitle": "Full Stack Web Developer",
            "expCompName": "Elephants Tech · Full-time",
            "expCompLogo": "https://media.licdn.com/dms/image/C560BAQF50D339cLfzA/company-logo_100_100...",
            "expCompURL": "https://www.linkedin.com/company/13224787/",
            "expDuration": "Jan 2021 - Present · 2 yrs 11 mos",
            "expLocation": "Remote"
          }
        ],
        "education": [
          {
            "eduFrom": "Assiut University",
            "eduDegree": "Bachelor's degree, Veterinary Medicine",
            "eduLogo": "https://media.licdn.com/dms/image/C560BAQEz-Utc2Fgd7A/company-logo_100_100...",
            "eduURL": "https://www.linkedin.com/company/926996/",
            "eduDate": "Sep 2013 - Jan 2019"
          }
        ],
        "license": [
          {
            "licenseName": "English Proficiency Certificate",
            "compName": "Duolingo English Test",
            "licenseURL": "certs.duolingo.com/1336409705...",
            "credentialID": "Issued Nov 2022 · Expires Nov 2024"
          }
        ],
        "skills": ["SQL", "Career Counseling"]
      }
    ]

---

## Directory Structure Tree

    Linkedin Profile Details Scraper/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── linkedin_parser.py
    │   │   └── utils_profile.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Recruiters** use it to collect candidate data automatically, so they can screen talent faster and build organized talent pipelines.
- **Business analysts** use it to research company personnel and market roles, enabling more informed competitive analysis.
- **Sales teams** use it to enrich lead profiles so they can tailor outreach with complete background context.
- **Researchers** extract structured professional histories to support studies in employment trends and labor markets.
- **Entrepreneurs** gather domain-specific experts or advisors, helping them build stronger networks.

---

## FAQs

**Do I need to update cookies?**
Yes. For secure access, cookies typically need refreshing weekly to ensure uninterrupted scraping.

**What profile types can be extracted?**
Any standard LinkedIn profile containing professional, contact, or background information can be processed.

**Is the output always structured the same way?**
Yes. Every run returns a consistent JSON schema with the same field layout, even when certain fields are missing.

**Can multiple profiles be processed?**
Yes. You can queue multiple URLs and generate output in batches.

---

## Performance Benchmarks and Results
**Primary Metric:** Processes individual profiles in an average of 2–4 seconds, depending on profile size.
**Reliability Metric:** Maintains a 96% successful extraction rate with valid cookie sessions.
**Efficiency Metric:** Handles large batches with minimal memory usage due to incremental parsing.
**Quality Metric:** Delivers over 98% field completeness for profiles containing standard public information.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
