from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import random

PATH = "C:/Users/diego/Desktop/Programação/Account Creator/chromedriver.exe"
driver = webdriver.Chrome(PATH)
print(nvotos)
ndevotos = nvotos
fator = 1
natual = 1

def update(num):

	print("Voto número [ " + num + " ] enviado com sucesso.")
#abrir pesquisa

try:

	while True:

		driver.get("https://s.surveyplanet.com/irdv1LwwV")
		time.sleep(1)
		#clica no begin
		element = driver.find_element_by_xpath("//*[@id='begin-button']").click()
		time.sleep(1)
	#<label class="radio" for="60a6e99ae73e7cfce83b7268[NUMERO DA OPÇÃO CORRESPONDENTE À OPÇÃO]">
		voto = driver.find_element_by_xpath("//*[@for='60a6e99ae73e7cfce83b7268[0]']").click()

		element = driver.find_element_by_class_name('submit-button')
		element.click()

		time.sleep(1)
		driver.get("https://google.com.br")
		update(str(natual))

		natual += 1

		if natual == 200:
			break


finally:
	


	driver.quit()