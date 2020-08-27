import requests
import sys
from datetime import datetime
def subdomain_finder(domain):
    with open("top5.txt","r") as f:
        for i in f:
            sub_domain = i.strip()
            new_url = sub_domain + "." + domain
            try:
                res = requests.get("http://"+new_url)
                print("Discovered Subdomain :",new_url)
            except:
                pass
if len(sys.argv) < 2:
    print("*"*50)
    print("Invalid Agruments")
    print("-"*50)
    print("Syntax")
    print("python Subdomain_finder.py Domain_Name")
    print("Please just enter domain like: google.com not www.google.com")
    print("-"*50)
    print("Example")
    print("python Subdomain_finder.py google.com")
    print("*"*50)
else:
    domain = sys.argv[1]
    
    s = datetime.now()
    print("Script start at :",s)
    print("*"*50)
    subdomain_finder(domain)
    print("*"*50)
    print("Total Time taken :",datetime.now()-s)
