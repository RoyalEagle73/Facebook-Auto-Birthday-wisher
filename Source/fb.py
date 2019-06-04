from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
import time

size = 0
ids = []
names = []
class wish:
	def __init__(self, username, password, message):
		self.username= username
		self.password= password
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('--headless')
		self.driver = webdriver.Chrome(options=self.options)
		self.inita = 0
		self.user_list = []
		self.id_list = []
		self.name_list = []
		self.message = message


	def collect_data(self):
		global size
		global ids
		global names
		##INTERNET CHECK
		try:
			self.driver.get("https://facebook.com")
			email = self.driver.find_element_by_id("email")
		except Exception as e:
			self.driver.close()
			return 0

		password_box = self.driver.find_element_by_id("pass")
		login_button = self.driver.find_element_by_id("loginbutton")

		email.send_keys(self.username)
		password_box.send_keys(self.password)
		try:
			login_button.click()
		except Exception as e:
			return 0
			

		## LOGIN CHECK
		try:
			temp = self.driver.find_element_by_name("q")
			print("Logged in")
		except Exception as e:
			self.driver.close()
			return 1

		##NEW TAB OPENING FOR BIRTHDAYS
		try:
			print("Opening new tab")
			self.driver.execute_script("window.open('');")
			print("Switching to new tab")
			self.driver.switch_to.window(self.driver.window_handles[1])
		except Exception as e:
			return 2

		print("Opening Birthday Window")
		try:
			self.driver.get("https://www.facebook.com/events/birthdays/")
		except Exception as e:
			print(e)
		
		print("Link opened")

		## GETTING HTML CONTENT IN A STRING
		print("Getting html_content")
		html = self.driver.execute_script("return document.documentElement.innerHTML")

		script = html[ html.find("birthdays_today_card") : html.find("birthdays_recent_card") ]


		while script.find('class="_tzm"', self.inita, len(script)) != -1:
			self.user_list.append(script.find('class="_tzm"', self.inita, len(script)))
			self.inita = script.find('class="_tzm"', self.inita, len(script)) + 1

		self.user_list.append(len(script))


		for i in range(len(self.user_list)-1):
			data = script[self.user_list[i]: self.user_list[i+1]] 
			soup = BeautifulSoup(data, 'html.parser')
			try:
				id_temp = soup.find_all('textarea', class_="enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput")
				self.id_list.append(id_temp[0]['id'])
			except Exception as e:
				self.id_list.append("No_id")
			name_temp = soup.find_all('div', class_="_tzn lfloat _ohe")
			self.name_list.append(name_temp[0].a['title'])

		size = len(self.id_list)
		ids = self.id_list.copy()
		names = self.name_list.copy()
		return 3


	def wishing(self, index):
		if self.id_list[index] == "No_id":
			return 0
		else:
			wish_box = self.driver.find_element_by_id(self.id_list[index])
			wish_box.send_keys(self.message)
			wish_box.send_keys(Keys.ENTER)
			print("Wished %s"%(self.name_list[index]))
			return 1
				
	def kill(self):
		try:
			##Closing birthday window
			self.driver.close()
			##Closing facebook window
			self.driver.close()
		except Exception as e:
			pass
		

# new_wish = wish("username here", "password here")
# collect_result = new_wish.collect_data()
# wishing_result = 0

# if collect_result == 0:
#  	print("Please Check your Internet Connection")
# elif collect_result == 1:
# 	print("Please Check Login Credentials")
# elif collect_result == 2:
# 	print("Error opening wishing page")
# elif collect_result == 3:
# 	print("Data Collected")
# 	for i in range(size):
# 		wishing_result = new_wish.wishing(i)
# 		if wishing_result == 0:
# 			print("You've already wished %s."%(names[i]))
# 		else:
# 			print("Wished %s"%(names[i]))

# print(ids)
# print(names)
# new_wish.kill()
