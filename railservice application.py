#THIS IS A SMALL PROJECT WHICH USES RAILWAY API IN ORDER TO GIVE THE TRAIN ROUTE
#PNR STATUS ,SEAT AVAILABILITY AND TRAIN RUNNING STATUS
# ITS valid till 27.09.2019
# ITS CREATED BY PRIYANSHU RANI



import requests#in order to use railway api in json format
def menu():
    user_input=input("""welcome to our rail service. press.....
    1. To find train route
    2. To check PNR status
    3. To check seat availability
    4. To find train running status
    5. To exit""")

    if user_input=="1":
        print("RAIL ROUTE ")
        print("---------------------------------")
        train_route()
    elif user_input == "2":
        print("Find PNR status")
        print("---------------------------------")
        pnr_status()
    elif user_input == "3":
        print("Check seat availability")
        print("---------------------------------")
        availability()
    elif user_input == "4":
        print("Train Status")
        print("---------------------------------")
        live_status()
    else:
        print("Bye")
def train_route():
    train_num=int(input("ENTER THE TRAIN NUMBER"))
    url="https://api.railwayapi.com/v2/route/train/{}/apikey/q83hyb6hce/".format(train_num)
    response=requests.get(url)
    response=response.json()
    for i in response['route']:
        print(i['station']['name'],"    |",i['scharr'],"    |",i['schdep'])

def pnr_status():
    pnr = input("Enter the PNR number: ")
    print("---------------------------------")
    url = "https://api.railwayapi.com/v2/pnr-status/pnr/{}/apikey/q83hyb6hce/".format(pnr)
    response = requests.get(url)
    response = response.json()
    # print(response)
    for i in response['passengers']:
        print("current status:", (response.get("passengers"))[i].get('current_status'))
    print("---------------------------------")
    print("Train Details:", (response.get("train")).get("name"), "|", (response.get("train")).get("number"))
    print("---------------------------------")
    print("From:", (response.get("from_station")).get("name"), "To:",
            (response.get("reservation_upto")).get("name"), "On:", response.get("doj"))

def availability():
    train_num=input("ENTER THE TRAIN NUMBER");
    print("------------------------------------")
    source=input("ENTER THE SOURCE STATION CODE")
    print("------------------------------------")
    dest=input("ENTER THE DESTINATION STATION CODE")
    print("------------------------------------")
    doj=input("ENTER THE DATE OF JOURNEY IN DD-MM-YYYY FORMAT ")
    print("------------------------------------")
    cls=input("ENTER THE COACH CLASS TYPE i.e. 1A,2A,3A,SL")
    print("------------------------------------")
    quota=input("ENTER THE QUOTA TYPE~GEN BY DEFAULT...")
    print("------------------------------------")
    url="""https://api.railwayapi.com/v2/check-seat/train/{}/source/{}/dest/{}/date/{}/pref/{}
        /quota/{}/apikey/q83hyb6hce/""",format(train_num,source,dest,doj,cls,quota)
    response = requests.get(url)
    response = response.json()
    #response
    print("Seat Availability on {}".format(doj), "in train no:{}".format(train_num), "is: ",
          (response.get("availability")[0]).get("status"))
    print("---------------------------------")

def live_status():
    train = input("Enter the train number:")
    print("---------------------------------")
    stn_code = input("Enter the station code to get the status:")
    print("---------------------------------")
    date = input("Enter the date in dd-mm-yyy format:")
    print("---------------------------------")
    url = "https://api.railwayapi.com/v2/live/train/{}/station/{}/date/{}/apikey/q83hyb6hce/".format(train,stn_code, date)
    response = requests.get(url)
    response = response.json()
    # print(response)
    # print(response.get("start_date"))
    print("Schedule_Arrival_Date | Actual_Arrival_Date :", (response.get("status")).get("scharr_date"), "|",
        (response.get("status")).get("actarr_date"))
    print("---------------------------------")
    print(response.get("position"))
    print("---------------------------------")
    print("Schedule_Arrival | Schedule_Departure :", (response.get("status")).get("scharr"), "|",
              (response.get("status")).get("schdep"))
    print("---------------------------------")
    print("Actual_Arrival | Actual_Departure :", (response.get("status")).get("actarr"), "|",
              (response.get("status")).get("actdep"))
    print("---------------------------------")
    print("Late In Minutes: ", (response.get("status")).get("latemin"))
    print("---------------------------------")


menu()
