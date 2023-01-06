import time

import pandas as pd

from dataclasses import dataclass
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup




@dataclass
class SeleniumAdapter:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="browser/chromedriver", chrome_options=options)

    def load_page(self, url):
        self.driver.get(url)

    def get_source_page(self):
        self.load_100_item()
        return self.driver.page_source

    def load_100_item(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/div/div[2]/div/div/div/section/div/div[2]/div/div[3]/select/option[4]')
            )
        )
        selector = Select(self.driver.find_element(
            By.XPATH, '/html/body/main/div/div[2]/div/div/div/section/div/div[2]/div/div[3]/select'
        ))
        selector.select_by_index(3)
        time.sleep(20)


@dataclass
class SiteScraper(SeleniumAdapter):

    @staticmethod
    def get_project(selector) -> Optional[str]:
        project = selector.find('h3', class_='row-title')
        if project:
            return project.get_text()

    @staticmethod
    def get_country(selector) -> Optional[str]:
        country = selector.find('div', class_='row-tags')
        if country:
            return country.find('span').find('a').get_text()

    @staticmethod
    def get_sector(selector) -> Optional[str]:
        divs = selector.findAll('div', class_='row-tags')
        for div in divs:
            a = div.find('a')
            if not a:
                return div.get_text()

    @staticmethod
    def get_amounts(selector) -> Optional[str]:
        amounts = selector.findAll('div', class_='col-md-2 col-xs-12')
        for a in amounts:
            a_span = a.find('div')
            if a_span:
                return a.get_text()

    def extract_loans(self):
        page_source = self.get_source_page()
        soup = BeautifulSoup(page_source, 'lxml')
        loans = []
        loan_selectors = soup.findAll('article', class_='col-xs-12')
        for selector in loan_selectors[1:]:
            loan = selector.find('div', class_='row-list')
            output = {
                'title': self.get_project(loan),
                'country': self.get_country(loan),
                'sector': self.get_sector(loan),
                'amount': self.get_amounts(loan)
            }
            loans.append(output)
        return loans

    def save_to_csv(self):
        data = self.extract_loans()
        df = pd.DataFrame.from_dict(data)
        df.to_csv('browser/result.csv', sep=';', encoding='utf-8', index=False)
