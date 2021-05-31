import json
import email
import smtplib
from datetime import datetime

import requests

print("\n****************************************************************************************************")
print("\nWelcome to Vaccination Slot Finder")
username = input("\nEnter your complete Email ID (ex:-abc@gmail.com)\n=> ")
age = input("\nEnter Age \n=>")
age = int(age)
district_ids = ""
#district_name = []
#n = input("\nEnter number of Districts you want to search for:")
#n = int(n)
#for i in range(0, n):
district_name = input("\nEnter District Name:\n => ")
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
for state_code in range(1, 40):
        #    print("State code: ", state_code)
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code),
                                headers=header)
    json_data = json.loads(response.text)
    for i in json_data["districts"]:
        for j in district_name:
            if j == i["district_name"]:
                district_ids = (i["district_id"])
#                district_ids = int(district_ids)
                print(district_ids)

print("Starting search for Covid vaccine slots!")


def create_session_info(center, session):
    return {"name": center["name"],
            "date": session["date"],
            "capacity": session["available_capacity"],
            "age_limit": session["min_age_limit"]}


def get_sessions(data):
    for center in data["centers"]:
        for session in center["sessions"]:
            yield create_session_info(center, session)


def is_available(session):
    return session["capacity"] > 0


def is_eighteen_plus(session):
    Age = age
    return session["age_limit"] == Age


def get_for_seven_days(start_date):
    district_id = district_ids
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    params = {"district_id": district_id, "date": start_date.strftime("%d-%m-%Y")}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    resp = requests.get(url, params=params, headers=headers)
    data = resp.json()
    return [session for session in get_sessions(data) if is_eighteen_plus(session) and is_available(session)]


def create_output(session_info):
    return f"{session_info['date']} - {session_info['name']} ({session_info['capacity']})"


print(get_for_seven_days(datetime.today()))
content = "\n".join([create_output(session_info) for session_info in get_for_seven_days(datetime.today())])
print(content)
owner = "vaibhav.singh18@siesgst.ac.in"
password = "vaibhav.singh18"

if not content:
    print("No availability")
else:
    email_msg = email.message.EmailMessage()
    email_msg["Subject"] = "Vaccination Slot Open"
    email_msg["From"] = owner
    email_msg["To"] = username
    email_msg.set_content(content)

    with smtplib.SMTP(host='smtp.gmail.com', port='587') as server:
        server.starttls()
        server.login(username, password)
        server.send_message(email_msg, owner, username)
