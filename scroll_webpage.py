import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com/search?sca_esv=371673003b9a266f&sxsrf=ADLYWIKtxxwk6hXQ41XmK91J1dRItPZXZA:1726253824979&q=pandas&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2joQcoZ-0Q2Udkt2zEybT7HdNV1kobqvEwEVRYBCltlBtQd5-pPeakpVgpgEn2RgmgzeZo15rltNMrDtoZe63sl46hHJXZmfPBeZdqdwrtlSxkvce3I&sa=X&ved=2ahUKEwiPvp7QzMCIAxVXEEQIHfA3AUQQtKgLegQIEBAB")
height=driver.execute_script("return document.body.scrollHeight")
print(height)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight) ")
