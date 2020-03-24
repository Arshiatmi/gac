import sys
import requests
from functions import *
from win10toast import ToastNotifier

if len(sys.argv) < 2:
    print("Error !")
    exit(0)

if " ".join(sys.argv[1:]).startswith("win10://"):
    if not win10():
        print("This Option Not Available Here")
        exit(0)
    other = " ".join(sys.argv[1:]).replace("win10://","")
    parts = other.split("/")
    if parts[0].strip() == "toaster":
        toaster = ToastNotifier()
        full = "/".join(parts[1:])
        title = full.split(":")[0]
        text = full.split(":")[1]
        toaster.show_toast(title,text)
    elif parts[0].strip() == "clipboard":
        full = "/".join(parts[1:])
        cmd = full.split(":")[0]
        if cmd == "set":
            text = full.split(":")[1]
            setClipboard(text)
        elif cmd == "get":
            print(getClipboard())
elif " ".join(sys.argv[1:]).startswith("http://"):
    other = " ".join(sys.argv[1:]).replace("http://","")
    parts = other.split("/")
    if parts[0].strip() == "get":
        all = "/".join(parts[1:])
        data = {}
        try:
            datas = all.split("?")[1]
            data_parts = datas.split("&")
            for i in data_parts:
                data[i.split("=")[0].strip()] = i.split("=")[1].strip()
        except:
            pass
        all = "http://" + all
        r = requests.post(all,data)
        print(r.text)
    elif parts[0].strip() == "post":
        all = "/".join(parts[1:])
        data = {}
        try:
            datas = all.split("?")[1]
            data_parts = datas.split("&")
            for i in data_parts:
                data[i.split("=")[0].strip()] = i.split("=")[1].strip()
        except:
            pass
        all = "http://" + all
        r = requests.post(all,data)
        print(r.text)
elif " ".join(sys.argv[1:]).startswith("https://"):
    other = " ".join(sys.argv[1:]).replace("https://","")
    parts = other.split("/")
    if parts[0].strip() == "get":
        all = "/".join(parts[1:])
        data = {}
        try:
            datas = all.split("?")[1]
            data_parts = datas.split("&")
            for i in data_parts:
                data[i.split("=")[0].strip()] = i.split("=")[1].strip()
        except:
            pass
        all = "https://" + all
        r = requests.post(all,data)
        print(r.text)
    elif parts[0].strip() == "post":
        all = "/".join(parts[1:])
        data = {}
        try:
            datas = all.split("?")[1]
            data_parts = datas.split("&")
            for i in data_parts:
                data[i.split("=")[0].strip()] = i.split("=")[1].strip()
        except:
            pass
        all = "https://" + all
        r = requests.post(all,data)
        print(r.text)
elif " ".join(sys.argv[1:]).startswith("ftp://"):
    other = " ".join(sys.argv[1:]).replace("ftp://","")
    parts = other.split("/")
    if parts[0].strip() == "get":
        all = "/".join(parts[1:])
        data = {}
        try:
            datas = all.split("?")[1]
            data_parts = datas.split("&")
            for i in data_parts:
                data[i.split("=")[0].strip()] = i.split("=")[1].strip()
        except:
            pass
        all = "ftp://" + all
        r = requests.post(all,data)
        print(r.text)
    elif parts[0].strip() == "post":
        all = "/".join(parts[1:])
        data = {}
        try:
            datas = all.split("?")[1]
            data_parts = datas.split("&")
            for i in data_parts:
                data[i.split("=")[0].strip()] = i.split("=")[1].strip()
        except:
            pass
        all = "ftp://" + all
        r = requests.post(all,data)
        print(r.text)
elif " ".join(sys.argv[1:]).startswith("win8://"):
    if not win8():
        print("This Option Not Available Here")
        exit(0)
    pass
elif " ".join(sys.argv[1:]).startswith("win7://"):
    if not win7():
        print("This Option Not Available Here")
        exit(0)
    pass
elif " ".join(sys.argv[1:]).startswith("win://"):
    if not win():
        print("This Option Not Available Here")
        exit(0)
    pass
elif " ".join(sys.argv[1:]).startswith("lin://"):
    if not lin():
        print("This Option Not Available Here")
        exit(0)
    pass
