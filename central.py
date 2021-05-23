import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import random

sg.change_look_and_feel('Topanga')

class TelaPython:
	def __init__(self):
		layout = [
			[sg.Text('URL da pesquisa :',size=(15,0)), sg.Input(key='urlpesquisa', size=(30,0))],
			[sg.Text('Tag FOR :',size=(15,0)), sg.Input(key='tagfor',size=(20, 1))],
			[sg.Text('Quantidade de votos:',size=(15,0)), sg.Input(key='nvotos',size=(11, 1))],
			[sg.HorizontalSeparator()],
			[sg.Text('Definições de privacidade:')],
			[sg.Checkbox('Usar Proxy',key='proxy')],
			[sg.Slider(range=(0,255), default_value=0, orientation='h',size=(15,20),key='sliderVelocidade')],
			[sg.Button('Iniciar',key='iniciar')],
			[sg.Output(size=(50,10))]
		]
		# Janela
		self.janela = sg.Window("Dados do Usuário").layout(layout)

	def Iniciar(self):
		while True:
			# Extraindo os dados da tela
			self.button, self.values = self.janela.Read()

			url = self.values['urlpesquisa']
			tagfor = self.values['tagfor']
			nvotos = self.values['nvotos']
			proxy = self.values['proxy']
			velocidade_script = self.values['sliderVelocidade']

			print(f'goto:	{url}')
			print(f' tag: 	{tagfor}')
			print(f'qtde: 	{nvotos}')
			print(f'prxy:	{proxy}')
			print(f'velo:   {velocidade_script}')

			


tela = TelaPython()
tela.Iniciar()

#abrir pesquisa

PATH = "C:/Users/diego/Desktop/Programação/Account Creator/chromedriver.exe"
driver = webdriver.Chrome(PATH)
ndevotos = {nvotos}
fator = 1
natual = 1

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

	if natual == ndevotos:
		break


	


	driver.quit()


		