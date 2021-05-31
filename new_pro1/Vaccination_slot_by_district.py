import requests
from pygame import mixer
from datetime import datetime, timedelta
import time

age = 19
district_ids = ["151"]
num_days = 2

print_flag = 'Y'

print("Starting search for Covid vaccine slots!")

actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

while True:
    counter = 0

    for district_id in district_ids:
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={" \
                  "}&date={}".format(
                district_id, given_date)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

            result = requests.get(URL, headers=header)

            if result.ok:
                response_json = result.json()
                if response_json["centers"]:
                    if (print_flag.lower() == 'y'):
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= age and session["available_capacity"] > 0):
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

                                if (session["vaccine"] != ''):
                                    print("\t Vaccine type: ", session["vaccine"])
                                print("\n")
                                counter = counter + 1
            else:
                print("No Response!")

    if counter:
        print("No Vaccination slot available!")
    else:
        mixer.init()
        mixer.music.load('C:\\Users\\Singh\\Downloads\\sound\\dingdong.wav')
        mixer.music.play()
        print("Search Completed!")

    dt = datetime.now() + timedelta(seconds=10)

    while datetime.now() < dt:
        time.sleep(1)
