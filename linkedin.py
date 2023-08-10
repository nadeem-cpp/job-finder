from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t
from os import environ

linkedin_url = "https://www.linkedin.com/feed/"


class Selenium:
    def __init__(self):
        self.driver = webdriver.Firefox()


class Linkedin(Selenium):
    def __init__(self):
        super().__init__()
        self.driver.get(url=linkedin_url)
        self.wait(2)
        self.signin()

    def signin(self):
        signin = self.driver.find_element(By.CLASS_NAME, "main__sign-in-link")
        signin.click()
        email = self.driver.find_element(By.NAME, "session_key")
        password = self.driver.find_element(By.NAME, "session_password")
        email.send_keys(environ.get("EMAIL"))
        password.send_keys(environ.get("PASSWORD"))
        submit = self.driver.find_element(By.CLASS_NAME, "from__button--floating")
        submit.click()

    def search_job(self, title: str):
        # wait until page load
        self.wait(10)
        job_search = self.driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        job_search.send_keys("python developer")
        job_search.send_keys(Keys.ENTER)
        self.wait(7)
        # click on first job and save its details in dict
        job_filter = self.driver.find_element(By.CLASS_NAME, "search-reusables__filter-pill-button")
        job_filter.click()
        self.wait(5)

    def jobs_processing(self):
        jobs = self.driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
        jobs_details = {}
        count: int = 0
        for job in jobs:
            job.click()
            t.sleep(2)
            title = self.driver.find_element(By.CLASS_NAME, "jobs-unified-top-card__job-title")
            details = self.driver.find_element(By.CSS_SELECTOR, ".jobs-unified-top-card__company-name a")
            jobs_details[str(count)] = {"Title": title.get_attribute("textContent"),
                                        "Company": details.get_attribute("textContent"),
                                        "Link": details.get_attribute("href")}
            count += 1

        print(jobs_details)

    def wait(self, timer: int):
        t.sleep(timer)


