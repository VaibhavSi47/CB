from win10toast import ToastNotifier
from cowin_api import CoWinAPI
import sched , time
import requests
import json
from datetime import datetime, timedelta
import time

s = sched.scheduler(time.time, time.sleep)
toaster = ToastNotifier()


def filter_centers_by_vaccine(available_centers: dict):
    original_centers = available_centers.get('centers')
    filtered_centers = {'centers': []}
    for index, center in enumerate(original_centers):
        filtered_sessions = []
        for session in center.get('sessions'):
            if session.get('vaccine') == "COVAXIN":
                filtered_sessions.append(session)
        if len(filtered_sessions) > 0:

            center['sessions'] = filtered_sessions
            filtered_centers['centers'].append(center)
            for capacity in center.get('sessions'):
                 if capacity.get('available_capacity') > 0:
                     toaster.show_toast("Cowin", "Available", icon_path=None, duration=60, threaded=True)


    return filtered_centers

def centers_name(filtered_centers):
    org_centers = filtered_centers.get('centers')
    for ind, cent in enumerate(org_centers):
        print(cent.get('name'))



def do_something(sc):
    print("\nWelcome to Vaccination Slot Finder")
    min_age_limit = input("\nEnter Age \n=>")
    min_age_limit = int(min_age_limit)
    num_days = input("\nFor how many day you want to search (max=7):\n=>")
    num_days = int(num_days)

    actual = datetime.today()
    list_format = [actual + timedelta(days=i) for i in range(num_days)]
    date = [i.strftime("%d-%m-%Y") for i in list_format]
    district_ids = []
    district_name = []
    n = input("\nEnter number of Districts you want to search for:")
    n = int(n)
    for i in range(0, n):
        district_name.append(input("\nEnter District Name:\n => "))
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    for state_code in range(1, 40):
        response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code),
                                headers=header)
        json_data = json.loads(response.text)
        for i in json_data["districts"]:
            for j in district_name:
                if j == i["district_name"]:
                    district_ids.append(i["district_id"])
    for i in district_ids:
#        date = '22-05-2021'  # Optional. Default value is today's date
#        min_age_limit = 45  # Optional. By default returns centers without filtering by min_age_limit
        cowin = CoWinAPI()
        available_centers = cowin.get_availability_by_district(i, date, min_age_limit)
        # print(available_centers)
        filtered_centers = filter_centers_by_vaccine(available_centers)
        # print(filtered_centers)
        centers_name(filtered_centers)
        print('\n')

    print('\n')
    s.enter(20, 1, do_something, (sc,))


s.enter(20, 1, do_something, (s,))
s.run()










# from cowin_api import CoWinAPI
#
# cowin = CoWinAPI()
# states = cowin.get_states()
# print(states)


# from cowin_api import CoWinAPI
#
# state_id = '15'
# cowin = CoWinAPI()
# districts = cowin.get_districts(state_id)
# print(districts)

from win10toast import ToastNotifier
# from cowin_api import CoWinAPI
# import sched, time
#
# s = sched.scheduler(time.time, time.sleep)
# toaster = ToastNotifier()
# pin_code = "410210"
# date = '08-05-2021'  # Optional. Default value is today's date
# min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit
#
# cowin = CoWinAPI()
# available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
# for i in available_centers:
#     print(i)


# toaster.show_toast("Cowin", "Available", icon_path= "C:\\Users\\Vikrant\\Desktop\\GOI.ico", duration=3600, threaded=True)

# date = '03-05-2021'  # Optional. Takes today's date by default
# min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit

# cowin = CoWinAPI()
# available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
# print(available_centers)

# "400074","400071","400001","400051"

# def do_something(sc):
#     pin_code = ["370001"]
#     for i in pin_code:
#         date = '13-05-2021'  # Optional. Default value is today's date
#         min_age_limit = 45  # Optional. By default returns centers without filtering by min_age_limit
#
#         cowin = CoWinAPI()
#         available_centers = cowin.get_availability_by_pincode(i, date, min_age_limit)
#         # print(available_centers)
#         # print(type(available_centers["centers"]))
#         # for j in available_centers["centers"] :
#         # if (available_centers["centers"][:] )!= 0 :
#         #         print(available_centers)
#         #         toaster.show_toast("Cowin", "Available", icon_path=None, duration=60, threaded=True)
#         original_centers = available_centers.get('centers')
#         filtered_centers = {'centers': []}
#         for index, center in enumerate(original_centers):
#             filtered_sessions = []
#             for session in center.get('sessions'):
#                 if session.get('vaccine') == "COVAXIN":
#                    filtered_sessions.append(session)
#             if len(filtered_sessions) > 0:
#                center['sessions'] = filtered_sessions
#                filtered_centers['centers'].append(center)
#
#         print(filtered_centers)
#
#     s.enter(20, 1, do_something, (sc,))
#
#
# s.enter(20, 1, do_something, (s,))
# s.run()