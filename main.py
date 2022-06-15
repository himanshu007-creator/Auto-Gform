"""
Selenium script to automate G-form filling.
Modify accordingly and have fun :)

@author :- https://gituhb.com/himanshu007-creator
@source :- https://github.com/himanshu007-creator/Gform-automation
@lincence :- Apache License Version 2.0

"""
import random
import pyfiglet
import getindianname as rand_naam
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium import webdriver
from time import time
import warnings
import sys
from termcolor import colored
warnings.filterwarnings("ignore", category=DeprecationWarning)


option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_argument("--window-position=450,100")
driver = webdriver.Chrome(options=option)
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=option)

# ENTER YOUR FORM LINK BELOW.
link = input("Enter form URL: ")
browser.get(link)

# function to change the browser dimensions


def set_browser_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)


set_browser_size(browser, 350, 350)


# def link(uri, label=None):
#     if label is None:
#         label = uri
#     parameters = ''

#     # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST
#     escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

#     return escape_mask.format(parameters, uri, label)


ascii_banner = pyfiglet.figlet_format("AUTO-GFORM")
# # text = "made with 💖🟩 by Himanshu"
# # target = "http://github.com/himanshu007-creator"
# sys.stdout.write(
#     colored(link('https://github.com/himanshu007-creator', 'made with 💖🟩 by Himanshu'), 'cyan'))
sys.stdout.write(colored(ascii_banner, 'cyan'))
i = int(input(colored(f'Enter number of inject ops: ', 'green')))
sys.stdout.write('\n')
count = 1
while(count <= i):
    try:
        # gender
        GENDER = ['male', 'female']
        ans = random.choice(GENDER)

        # name
        name_input = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        if(ans == 'male'):
            name = rand_naam.male()
            name_input.send_keys(name)
        else:
            name = rand_naam.female()
            name_input.send_keys(name)

        # email
        email_input = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        if(ans == 'male'):
            email_input.send_keys(
                name.replace(" ", "")+str(random.randint(2000, 9000))+"@gmail.com")
        else:
            email_input.send_keys(
                name.replace(" ", "")+str(random.randint(2000, 9000))+"@gmail.com")

        # age
        age_choice = [13, 16, 19]
        age_choice = random.choice(age_choice)
        age = browser.find_element_by_xpath(
            '//*[@id="i'+str(age_choice)+'"]/div[3]/div')
        age.click()
        # textboxes[0].send_keys("Hello World")

        # gender

        # 38
        gender_choice = [35, 32]
        gender_choice = random.choice(gender_choice)
        gender = browser.find_element_by_xpath(
            '//*[@id="i'+str(gender_choice)+'"]/div[3]/div')
        gender.click()

        # agli screen pe jane ki ninja technique
        next = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        next.click()

        # often
        often_choice = ['1', '2', '3', '4', '5']
        often_choice = random.choice(often_choice)
        often = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label['+often_choice+']/div[2]/div/div/div[3]/div')
        often.click()

        # handwriting
        handwriting_choice = ['1', '2', '3', '4', '5']
        handwriting_choice = random.choice(handwriting_choice)
        handwriting = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label['+str(handwriting_choice)+']/div[2]/div/div/div[3]/div')
        handwriting.click()

        # bored
        bored_choice = ['1', '2', '3', '4', '5']
        bored_choice = random.choice(bored_choice)
        bored = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label['+str(bored_choice)+']/div[2]/div/div/div[3]/div')
        bored.click()

        # appointment
        appointment_choice = ['1', '2', '3', '4', '5']
        appointment_choice = random.choice(appointment_choice)
        appointment = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label['+str(appointment_choice)+']/div[2]/div/div/div[3]/div')
        appointment.click()

        # forgetSlip
        forget_choice = ['1', '2', '3', '4', '5']
        forget_choice = random.choice(forget_choice)
        forgetSlip = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label['+str(forget_choice)+']/div[2]/div/div/div[3]/div')
        forgetSlip.click()

        # Damage
        damage_choice = ['1', '2', '3', '4', '5']
        damage_choice = random.choice(damage_choice)
        Damage = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label['+str(damage_choice)+']/div[2]/div/div/div[3]/div')
        Damage.click()

        # Convenient
        convenient_choice = ['1', '2', '3', '4', '5']
        convenient_choice = random.choice(convenient_choice)
        Convenient = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label['+str(convenient_choice)+']/div[2]/div/div/div[3]/div')
        Convenient.click()

        next = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next.click()

        # Technical_sound
        technical_choice = ['1', '2', '3', '4', '5']
        technical_choice = random.choice(technical_choice)
        Technical_sound = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[' + str(technical_choice) + ']/div[2]/div/div/div[3]/div')
        Technical_sound.click()

        # Digital_aletrnatives
        digital_choice = ['1', '2', '3', '4', '5']
        digital_choice = random.choice(digital_choice)
        Digital_aletrnatives = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label['+str(digital_choice)+']/div[2]/div/div/div[3]/div')
        Digital_aletrnatives.click()

        # E_identity
        id_choice = ['1', '2', '3', '4', '5']
        id_choice = random.choice(id_choice)
        E_identity = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label['+str(id_choice)+']/div[2]/div/div/div[3]/div')
        E_identity.click()

        # Sensitive_info
        info_choice = ['1', '2', '3', '4', '5']
        info_choice = random.choice(info_choice)
        Sensitive_info = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label['+str(info_choice)+']/div[2]/div/div/div[3]/div')
        Sensitive_info.click()

        # Solution
        sol_choice = ['3', '4', '5']
        sol_choice = random.choice(sol_choice)
        Solution = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label['+str(sol_choice)+']/div[2]/div/div/div[3]/div')
        Solution.click()

        Submit = browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div[2]/span/span')

        Submit.click()
        browser.implicitly_wait(2)
        submitAgain = browser.find_element_by_link_text(
            "Submit another response")
        submitAgain = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submitAgain.click()
        sys.stdout.write(colored(f'💉{count} records injected', 'red'))
        sys.stdout.write('\n')
        sys.stdout.flush()
        count += 1
    except NoSuchElementException:
        browser.execute_script(
            "alert('CAPTCHA's MESSING, run the script after a while')")
        time.sleep(3)
        # browser.close()
    except WebDriverException:
        pass
        browser.switch_to.alert.text
        time.sleep(3)
        browser.switch_to.alert.accept()
        # browser.close()
    except ValueError:
        sys.stdout.write("oops")


# browser.close()
