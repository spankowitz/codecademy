
import requests 
import sys 

sub_list = open("subdomains.txt").read() 
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" 

    try:
        r = requests.get(sub_domains)
        if r.status_code==404:
            pass
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains) 
