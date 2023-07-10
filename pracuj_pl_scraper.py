import math
from selenium import webdriver
from selenium.webdriver.common.by import By

technology = "TypeScript"
driver = webdriver.Chrome()
driver.implicitly_wait(60)
url = f"https://it.pracuj.pl/?et=17&tt={technology}&jobBoardVersion=2"
driver.get(url)


def get_url(page_number):
    return f"https://it.pracuj.pl/?et=17&tt={technology}&jobBoardVersion=2&pn={page_number}"


def get_job_offers_count():
    job_offers_count_xpath = '//span[@data-title="offers-count"]'
    element = driver.find_element(By.XPATH, job_offers_count_xpath)
    job_offers_count = element.text.replace("(", "").replace(")", "")
    return int(job_offers_count)


def get_job_offers():
    job_title_xpath = '//h3[@data-test="offer-title"]'
    company_name_xpath = '//span[@data-test="company-name"]'
    page_count = math.ceil(get_job_offers_count() / 20)
    current_page_number = 1
    job_titles = []
    company_names = []

    while current_page_number <= page_count:
        driver.get(get_url(current_page_number))
        job_title_elements = driver.find_elements(By.XPATH, job_title_xpath)
        company_name_elements = driver.find_elements(By.XPATH, company_name_xpath)
        job_titles.extend([job_title_page_element.text for job_title_page_element in job_title_elements])
        company_names.extend([company_name_element.text for company_name_element in company_name_elements])
        current_page_number += 1

    return create_job_offer_dictionaries(job_titles, company_names)


def create_job_offer_dictionaries(job_titles, company_names):
    count = 0
    job_offers = []

    while count < len(job_titles):
        job_offer = {
            "company_name": company_names[count],
            "job_title": job_titles[count]
        }
        job_offers.append(job_offer)
        count += 1

    return job_offers


job_offers = get_job_offers()
print(job_offers)
print(len(job_offers))

driver.close()
