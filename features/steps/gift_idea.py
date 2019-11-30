from behave import *
from selenium import webdriver
import time

driver=""
@given(u'user should enter the vaslid url of the application')
def step_impl(context):
    global driver
    driver=webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    

@when(u'user click on giftidea')
def gift_idea(context):
    time.sleep(10)
    driver.find_element_by_xpath("//a[.='Best Sellers']").click()

@then(u'user click on books link and user should be able to select the book')
def books(context):
    try:
        driver.find_element_by_xpath("//a[.='Boo']").click()
        time.sleep(10)
        driver.find_element_by_xpath("//div[.='Think and Grow Rich']").click()
        driver.close()
          
    except:
        driver.save_screenshot("failed_photo.png")
        print("not able to find element")
            
        
         
    
    
    
    
    
    
    