from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
from time import time, sleep


class googleFormFiller():

    def __init__(self, link_list, price_list, addr_list):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.url = "https://docs.google.com/forms/d/e/1FAIpQLSduxqSXJJCaXUiFGqINiwlj8zjbREWQX6ccZuEcS0Z58d4Ocg/viewform?usp=sf_link"
        self.link_list = link_list
        self.price_list = price_list
        self.addr_list = addr_list
        self.sheet_url ="https://docs.google.com/spreadsheets/d/1aftCoM0lKEyp56AxS8F_xmWifbksvmBZ8ZmZfq9wn9w/edit?usp=sharing"


    def fillForm(self):
        self.driver.get(self.url)
        sleep(1)

        # Fill out the form
        for i in range(len(self.link_list)):
            address = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(self.addr_list[i])
            price = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(self.price_list[i])
            link = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(self.link_list[i])
            send_btn = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            send_btn.click()
            sleep(0.5)
            next_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            next_btn.click()
            sleep(1)

    def show_sheet(self):
        self.driver.get(self.sheet_url)

        print("Sheet is shown")
