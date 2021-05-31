"""import requests
import json
from cowin_api import CoWinAPI

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
district_nm = input("\nenter district name:\n=>")
for state_code in range(1,40):
#    print("State code: ", state_code)
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code), headers=header)
    json_data = json.loads(response.text)
    if response_json["districts"]:
        for i in json_data["districts"]:
            if district_nm.lower() == json_data["districts"]:
#or district_nnm == i["district_name"]:
                print(i["district_id"],'\t', i["district_name"])
#"""
"""
state_name = "Andaman and Nicobar Islands"
cowin = CoWinAPI()
states = cowin.get_states()
print(states)
for state in states.get("state_name"):
    if states.get("state_name") == state_name:
        print(state.get('state_id'))
#districts = cowin.get_districts(state_name)
#print(districts)

district_name = ["Mumbai","Thane"]
district_ids = []
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
for state_code in range(1,40):
#    print("State code: ", state_code)
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code), headers=header)
    json_data = json.loads(response.text)
    for i in json_data["districts"]:
        for j in district_name:
            if j == i["district_name"]:
                print(i["district_id"],'\t', i["district_name"])
                district_ids.append(i["district_id"])
print(district_ids)

       # print("\n")
 #   if district_name == i["district_name"]:
#        print(i["district_id"])
"""
import requests
import json
from pygame import mixer
from datetime import datetime, timedelta
import time
import email
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("\n****************************************************************************************************")
print("\nWelcome to Vaccination Slot Finder")
username = input("\nEnter your complete Email ID (ex:-abc@gmail.com)\n=> ")
age = input("\nEnter Age \n=>")
age = int(age)
num_days = input("\nFor how many day you want to search (max=7):\n=>")
num_days = int(num_days)

print_flag = 'Y'
actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]
name = ""
pincd = ""
Fee = ""
district_ids = []
district_name = []
n = input("\nEnter number of Districts you want to search for:")
n = int(n)
for i in range(0, n):
    district_name.append(input("\nEnter District Name:\n => "))
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
                    district_ids.append(i["district_id"])

    print("Starting search for Covid vaccine slots!")
    cnd = 0
    while cnd == 0:
        cnd = 1
        counter = 0

        for district_id in district_ids:
            for given_date in actual_dates:
                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(
                    district_id, given_date)
                header = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

                result = requests.get(URL, headers=header)

                if result.ok:
                    response_json = result.json()
                    if response_json["centers"]:
                        if print_flag.lower() == 'y':
                            for center in response_json["centers"]:
                                for session in center["sessions"]:
                                    if session["min_age_limit"] <= age and session["available_capacity"] > 0:
                                        #  print('District ID: ' , center["district_id"])
                                        print("Available on: {}".format(given_date))
                                        print("\t center ID:", center["center_id"])
                                        print("\t State Name:", center["state_name"])
                                        print("\t District Name:", center["district_name"])
                                        name = "\t Hospital: " + center["name"]
                                        print(name)
                                        print("\t", center["block_name"])
                                        pincd = center["pincode"]
                                        print(str(pincd))
                                        Fee = "\t Price: " + center["fee_type"]
                                        print(Fee)
                                        print("\t Availablity : ", session["available_capacity"])
                                        print("\t Availablity Dose 1 : ", session["available_capacity_dose1"])
                                        print("\t Availablity Dose 2 : ", session["available_capacity_dose2"])

                                        if session["vaccine"] != '':
                                            print("\t Vaccine type: ", session["vaccine"])
                                        print("\n")
                                        counter = counter + 1

                else:
                    print("No Response!")
        if counter:
            print("No Vaccination slot available!")
        else:
            content = "\nSlot Available :\n" + "Name: " + name + "\n" + "Pincode: " + pincd + "\n" + "Fees: " + Fee + "\n"
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
                    server.login(owner, password)
                    server.send_message(email_msg, owner, username)
