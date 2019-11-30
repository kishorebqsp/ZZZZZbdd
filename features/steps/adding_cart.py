from behave import *
from selenium import webdriver
import time



@when(u'user search the product and click on serach button')
def seraching(context):
    driver.find_element_by_id("twotabsearchtextbox").send_keys("phone")
    driver.find_element_by_xpath("//input[@value='Go']").click()
    
     
@then(u'it should select the phone and add to cart')
def phone(context):
    driver.find_element_by_xpath("(//span[contains(.,'Samsung Galaxy')])[3]").click()

@then(u'user should be able to add the product to cart')
def adding_cartt(context):
    time.sleep(5)
    driver.find_element_by_id("add-to-cart-button").click()
    print("scuccessfully added to cart")
    driver.close()
    
    
    