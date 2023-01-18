from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


with open('ccn.json') as f:
  CCN = json.load(f)

with open('exp.json') as f:
  EXP = json.load(f)

with open('cvv.json') as f:
  CVV = json.load(f)
  
  
web = webdriver.Chrome()
web.maximize_window()

web.get('https://www.spotify.com/us/purchase/offer/reusable-unique-hero-trial-3m/?marketing-campaign-id=holiday-2021&country=CA')

time.sleep(2)

mail = "ttanj95@gmail.com"
password = "Tanjiro  123"

web.find_element(By.ID, "login-username").send_keys(mail)
web.find_element(By.ID, "login-password").send_keys(password)
web.find_element(By.XPATH, '//*[@id="login-button"]/div[1]/span').click()

time.sleep(2)

#go to account overview if loging in from the main link basha kaka!
# web.find_element(By.ID, "account-settings-link").click()

time.sleep(2)

#scrollup
# WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="spoti-root"]/div/main/section[1]/article/header/div/div[3]/div[1]/a')))
web.execute_script("window.scrollTo(0, 0);")

time.sleep(2)

#go premium
web.find_element(By.XPATH, '//*[@id="spoti-root"]/div/main/section[1]/article/header/div/div[3]/div[1]/a').click()

time.sleep(2)

#bo select krdny credit card
web.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/section[2]/div/div/ul/li[1]').click()

time.sleep(2)

#agree to the terms
web.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/section[2]/div/form/div[2]/div[1]/div').click()

time.sleep(2)

if(web.current_url == "https://www.spotify.com/ca-en/purchase/offer/default-trial-1m/?country=CA"):
    for i in range(len(CCN)):
        #witch to the i frame
        iframe = web.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/section[2]/div/form/div[1]/div[2]/iframe')
        web.switch_to.frame(iframe)
        
        card = (CCN[i])
        web.find_element(By.ID, "cardnumber").send_keys(card)
        
        expire = (EXP[i])
        web.find_element(By.ID, "expiry-date").send_keys(expire)
        
        cvvnum = (CVV[i])
        web.find_element(By.ID, "security-code").send_keys(CVV)
        
        #select the reigon
        reg = Select(web.find_element(By.ID, "zip-code-choices"))
        reg.select_by_value("CA-NB")
        
        web.switch_to.default_content()
        
        time.sleep(3)
        
        #submit
        web.find_element(By.ID, "checkout_submit").click()
        
        time.sleep(3)
        
        if(web.current_url == "https://www.spotify.com/ca-en/purchase/offer/default-trial-1m/?country=CA"):

            #witch to the i frame
            iframe = web.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/section[2]/div/form/div[1]/div[2]/iframe')
            web.switch_to.frame(iframe)

            web.find_element(By.ID, "cardnumber").clear()
            web.find_element(By.ID, "expiry-date").clear()
            web.find_element(By.ID, "security-code").clear()

            web.switch_to.default_content()
        else:
            pass
        
    else:
        print(i['credit_card'] + i['expiration_date'] + i['cvv'])
        web.close()
        
        
        
time.sleep(360)