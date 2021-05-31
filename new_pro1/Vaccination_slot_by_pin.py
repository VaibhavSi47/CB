
import requests
import json
from pygame import mixer
from datetime import datetime, timedelta
import time


print("\n****************************************************************************************************")
print("\nWelcome to Vaccination Slot Finder")
age = input("\nEnter Age \n=>")
age = int(age)
num_days = input("\nFor how many day you want to search (max=7):\n=>")
num_days = int(num_days)

print_flag = 'Y'
actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]
print("\nYou Want to Find Available Slots: (Choose any one)")
choice = input("\n1.Using Pincode\n2.Using District Name\n3.Using District Id\n=>")
choice = int(choice)

if choice == 1:
    pincodes = []
    n = input("\nEnter number of pincode you want to search for:")
    n = int(n)
    for i in range(0, n):
        pin = input("\nEnter Pincode:")
        pincodes.append(pin)
    print("Starting search for Covid vaccine slots!")
    while True:
        counter = 0

        for pincode in pincodes:
            for given_date in actual_dates:
                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
                    pincode, given_date)
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
                                        print('\nPincode: ' + pincode)
                                        print("Available on: {}".format(given_date))
                                        print("\t center ID:", center["center_id"])
                                        print("\t State Name:", center["state_name"])
                                        print("\t District Name:", center["district_name"])
                                        print("\t", center["name"])
                                        print("\t", center["block_name"])
                                        print("\t Pincode: ", center["pincode"])
                                        print("\t Price: ", center["fee_type"])
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
            mixer.init()
            mixer.music.load('C:\\Users\\Singh\\Downloads\\sound_dingdong.wav')
            mixer.music.play()
            print("Search Completed!")

        dt = datetime.now() + timedelta(seconds=20)

        while datetime.now() < dt:
            time.sleep(1)

if choice == 2:
    district_ids = []
    district_name = []
    n = input("\nEnter number of Districts you want to search for:")
    n = int(n)
    for i in range(0, n):
#        district_name = input("\nEnter District Name:\n => ")
        district_name.append(input("\nEnter District Name:\n => "))
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    for state_code in range(1, 40):
        #    print("State code: ", state_code)
        response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code),
                                headers=header)
        json_data = json.loads(response.text)
        for i in json_data["districts"]:
            for j in district_name:
                if j == i["district_name"]:
#                    print(i["district_id"], '\t', i["district_name"])
                    district_ids.append(i["district_id"])
#    print(district_ids)
    print("Starting search for Covid vaccine slots!")
    while True:
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
                                        print("\t", center["name"])
                                        print("\t", center["block_name"])
                                        print("\t Pincode: ", center["pincode"])
                                        print("\t Price: ", center["fee_type"])
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
            mixer.init()
            mixer.music.load('C:\\Users\\Singh\\Downloads\\sound_dingdong.wav')
            mixer.music.play()
            print("Search Completed!")

        dt = datetime.now() + timedelta(seconds=20)

        while datetime.now() < dt:
            time.sleep(1)

if choice == 3:
    district_ids = []
    n = input("\nEnter number of district ID you want to search for:")
    n = int(n)
    for i in range(0, n):
        pin = input("\nEnter District ID:")
        district_ids.append(pin)
    print("Starting search for Covid vaccine slots!")
    while True:
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
                                        print('District ID: ' + district_id)
                                        print("Available on: {}".format(given_date))
                                        print("\t center ID:", center["center_id"])
                                        print("\t State Name:", center["state_name"])
                                        print("\t District Name:", center["district_name"])
                                        print("\t", center["name"])
                                        print("\t", center["block_name"])
                                        print("\t Pincode: ", center["pincode"])
                                        print("\t Price: ", center["fee_type"])
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
            mixer.init()
            mixer.music.load('C:\\Users\\Singh\\Downloads\\sound_dingdong.wav')
            mixer.music.play()
            print("Search Completed!")

        dt = datetime.now() + timedelta(seconds=20)

        while datetime.now() < dt:
            time.sleep(1)
