from datetime import datetime,timedelta
status={}
def uploadstatus():
    name=input("username:")
    text=input("Enter status:")
    status[name]={
        "text":text,
        "time":datetime.now(),
        "view":0
    }
    print("Status uploaded successfully")
    print("-------------------------------------------------------")
def showstatus():
    if len(status) == 0:
        print("No Status Available")
    else:
        print("Available Statuses:")
        for name in status:
            print(name)
    print("-------------------------------------------------------")
def viewstatus():
    name = input("Enter username to View: ")
    if name in status:
        if datetime.now()-status[name]["time"]>=timedelta(hours=24):
            del status[name]
            print("status is expired")
        else:
            print("Status:", status[name]["text"])
            status[name]["view"]+=1
            print("Views:", status[name]["view"])
            print("Uploading time:",status[name]["time"])
            print("status viewed successfully")
        print()  
    else:
        print("status is not available")

while True:
    print("-----------------WHATSAPP STATUS-----------------------")
    print("1.upload staus\n2.show available status\n3.view status\n4.exit")
    print("-------------------------------------------------------")
    ch=int(input("Enter your choice:"))
    print("-------------------------------------------------------")
    if ch==1:
       uploadstatus()
    elif ch==2:
        showstatus()
    elif ch==3:
        viewstatus()
    elif ch==4:
         break
    else:
        print("Invalid input:")