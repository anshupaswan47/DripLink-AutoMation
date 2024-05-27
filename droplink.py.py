from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium_stealth import stealth
from random import randint, choice
import sys

import json
# urls = ['https://linkpays.in/Z7N6Vz25','https://linkpays.in/ALnKpCv','https://linkpays.in/AWptRg']

G = "\033[32m"    # Green
W = "\033[0m"     # White
RR = "\033[31;1m" # Red light 
YY = "\033[33;1m" # Yellow light
C = "\033[36m"    # Cyan
B = "\033[34m"    # Blue

def save_used_user_agent(used_user_agent):
        with open('used_user_agents.txt', 'a') as file:
            file.write(used_user_agent+'\n')
            
def choose_random_user_agent():
    with open('user-agents.txt', 'r') as file:
        user_agents = file.readlines()

    try:
        with open('used_user_agents.txt', 'r') as file:
            used_user_agents = file.readlines()
    except FileNotFoundError:
        used_user_agents = []

    user_agents = [user_agent for user_agent in user_agents if user_agent not in used_user_agents]

    if len(user_agents) == 0:
        return "All user agents have been used."
    else:
        random_user_agent = choice(user_agents)
        # save_used_user_agent(random_user_agent)
        return random_user_agent.strip()


options = Options()
options.add_extension('adgaurd.crx')
options.add_extension('urban.crx')
options.add_experimental_option("detach", True)
agent = choose_random_user_agent()
options.add_argument(f"user-agent={agent}")
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    '''
})

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/welcome-consent")
driver.maximize_window()

def waitforid(id):
    t=0
    while True:
        if t==8:
            driver.quit()
        try:
            driver.find_element(By.ID,value=id)
            print(G+"ID Found ")
            break
        except:
            print('waiting......')
            sleep(2)
            t=t+1
def waitfor(path):
    t=0
    while True:
        if t==8:
            break
        try:
            driver.find_element(By.XPATH,value=path)
            break
        except:
            print('waiting......')
            sleep(2)
            t=t+1
        

def vpn(driver):
    sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    waitfor("/html/body/div/div/div[2]/div/div/div/button[2]")
    clickby_xpath(driver,"/html/body/div/div/div[2]/div/div/div/button[2]")
    clickby_xpath(driver,"/html/body/div/div/div[3]/div[2]/div/div[1]/input")
    driver.find_element(By.XPATH,value="/html/body/div/div/div[3]/div[2]/div/div[1]/input").send_keys("United States (USA)")
    driver.implicitly_wait(5)
    i=1
    clickby_xpath(driver,"/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li["+str(i)+"]")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    print(B+"VPN ACTIVATED"+YY)
    sleep(1)
    # /html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[81]
    
    start(driver)

def new_tab():
    driver.execute_script("window.open('');")
    sleep(2)
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://droplink.co/bwXe")
    
def start(driver):
    sleep(2)
    driver.get("https://droplink.co/bwXe")
    while True:
        try:
            if driver.find_element(By.XPATH,value="/html/body/a/img"):
                break
        except:
            new_tab()
    if driver.find_element(By.XPATH,value="/html/body/a/img"):
        print(G+"Started Not")
    print(B+'LINK SEARCHED'+YY)
    sleep(1)
    process(driver)

def clickby_id(id):
    while True:
        try:
            driver.find_element(By.ID,value= id).click()
            print(G+"ID Success"+C)
            break
        except:
            print(RR+"ID error"+C)
            sleep(1)


            
def clickby_xpath(driver, path, attempts=5):
    if attempts == 0:
        driver.quit()
        sys.exit() 
        # driver.quit()
    try:
        driver.find_element(By.XPATH, path).click()
        print(G+"XPath Success"+C)
    except :
        print(RR+"XPath error:",C)
        sleep(1)
        clickby_xpath(driver, path, attempts-1)

id="go_d"
id_2="go_d2"
id_x="t_modal_close_x"
get='/html/body/div[1]/div/div/div/div[3]/a'
def process(driver):
    print(B+"PROCCESS STARTED "+YY)
    print("5")
    
    waitforid(id)##
    clickby_id(id)##
    print("4")
    # waitfor(id_x)##
    clickby_id(id_x)##
    
    clickby_id(id_2)##
    print("3")
    
    waitforid(id)##
    clickby_id(id)##
    
    # waitfor(id_x)##
    clickby_id(id_x)##
    print("2")
    clickby_id(id_2)##
    clickby_xpath(driver,get)
    print("1")
    sleep(3)

    save_used_user_agent(agent)
    print("USER AGENT SAVED")
    driver.quit()
    
vpn(driver)
