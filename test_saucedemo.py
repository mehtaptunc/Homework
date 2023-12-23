from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pytest

class Test_saucedemo:
#Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak 
# "Epic sadface: Username is required" gösterilmelidir.
    def test_username_password_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(1)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("")
        sleep(1)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        sleep(1)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(1)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Boş Test Sonuç: {testResult}")

#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak 
#"Epic sadface: Password is required" gösterilmelidir.

    def test_password_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(1)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("Mehtap")
        sleep(1)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        sleep(1)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(1)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Şifre Boş Sonuç: {testResult}")


#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
#"Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
   
    def test_error(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(1)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(1)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(1)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Hatalı Sonuç: {testResult}")

#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde 
#kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_numberOfLists(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")    
        driver.maximize_window()
        sleep(1)
        usernameInput = driver.find_element(By.ID ,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(1)
        passwordInput = driver.find_element(By.ID ,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(1)
        listOfCourses = driver.find_elements(By.CLASS_NAME, "inventory_item")
        testResult = len(listOfCourses) == 6
        print(f"TEST SONUCU: {testResult}")


# testClass = test_saucedemo()
# testClass.test_username_password_empty()
# testClass.test_password_empty()
# testClass.test_error()
# testClass.test_numberOfLists()
