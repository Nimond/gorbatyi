from bs4 import BeautifulSoup
import requests
import os
import json
import time


proxies = { # tor proxies yaya
	   'http': 'socks5://localhost:9050',
    	   'https': 'socks5://localhost:9050'
 	  }

def pidaras():
	os.system("clear")
	print("your ip is: {}, used {} times.".format(ip, emails_from_ip))
	print("total emails: {}".format(total_emails))
	print("""


.d8888b.                   888               888             d8b 
d88P  Y88b                  888               888             Y8P 
888    888                  888               888                 
888         .d88b.  888d888 88888b.   8888b.  888888 888  888 888 
888  88888 d88""88b 888P"   888 "88b     "88b 888    888  888 888 
888    888 888  888 888     888  888 .d888888 888    888  888 888 
Y88b  d88P Y88..88P 888     888 d88P 888  888 Y88b.  Y88b 888 888 
 "Y8888P88  "Y88P"  888     88888P"  "Y888888  "Y888  "Y88888 888 
                                                          888     
                                                     Y8b d88P     
                                                      "Y88P"      

		  """)


def restart_tor():
	os.system('sudo service tor restart')
	time.sleep(0.5)
	r = requests.get('http://httpbin.org/ip', proxies=proxies) 

	return json.loads(r.text)['origin']


def sent_poo(message, fio, email):
	session = requests.session()
	r = session.get('http://www.gorbatyi.ru/feedback.aspx', proxies=proxies)
	soup = BeautifulSoup(r.text)
	hidden = soup.findAll('input')

	data = {
		'__VIEWSTATEGENERATOR': hidden[1]['value'],
		'__VIEWSTATE': hidden[0]['value'],
		'mail': email,
		'fio': fio,
		'mes': message
	}

	r = session.post('http://www.gorbatyi.ru/feedback.aspx', proxies=proxies, data=data)

	return 'Спасибо!' in r.text


emails_from_ip = 5
total_emails = 0
ip = None
if __name__ == '__main__':
	while True:
		if emails_from_ip == 5:
			emails_from_ip = 0
			ip = restart_tor()

		emails_from_ip += 1
		total_emails += 1

		pidaras()
		time.sleep(0.5)












		'''
		ip = json.loads(requests.get('http://httpbin.org/ip', proxies=proxies).text)['origin']
		os.system("clear")
		print(ip)
		os.system('sudo service tor restart')
		time.sleep(5)
		'''



