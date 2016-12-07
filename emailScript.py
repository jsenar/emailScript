from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from getpass import getpass

def main():
	num_emails = 15
	start_email = 1
	#url = "https://acs-webmail.ucsd.edu/squirrelmail/src/right_main.php?use_mailbox_cache=0&startMessage={0}&mailbox=INBOX".format(start_email)
	driver = webdriver.Firefox()
	driver.get("https://acs-webmail.ucsd.edu")

	username = raw_input("Please enter your UCSD username: ")
	pw = getpass("Please enter your password: ")	

	elem = driver.find_element_by_name("login_username")
	elem.clear()
	elem.send_keys(username)
	elem = driver.find_element_by_name("secretkey")
	elem.clear()
	elem.send_keys(pw)
	elem = driver.find_element_by_name("requested_other_imap_server")
	elem.clear()
	elem.send_keys("sdcc15.ucsd.edu")
	elem.send_keys(Keys.RETURN)	

	time.sleep(1)	
	
	#initial call
	driver.get("https://acs-webmail.ucsd.edu/squirrelmail/src/right_main.php?use_mailbox_cache=0&startMessage={0}&mailbox=INBOX".format(start_email))
	
	while "ERROR" not in driver.page_source:
		driver.find_element_by_link_text("Toggle All").click()
		driver.find_element_by_name("markRead").click()
		start_email = start_email + num_emails
		driver.get("https://acs-webmail.ucsd.edu/squirrelmail/src/right_main.php?use_mailbox_cache=0&startMessage={0}&mailbox=INBOX".format(start_email))
	'''list = driver.find_elements_by_tag_name('a')
	print list
	for link in list:
		print link.get_attribute("href")'''
	driver.close()

if __name__ == "__main__":
    main()

