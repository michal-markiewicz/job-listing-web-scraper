from selenium import webdriver
from selenium.webdriver.common.by import By

technology = "JavaScript"
driver = webdriver.Chrome()
driver.implicitly_wait(60)
url = f"https://it.pracuj.pl/?et=17&tt={technology}&jobBoardVersion=2"
driver.get(url)


def get_job_titles():
    job_title_xpath = '//h3[@data-test="offer-title"]'
    elements = driver.find_elements(By.XPATH, job_title_xpath)
    job_titles = [element.text for element in elements]
    return job_titles


def get_company_names():
    company_names_xpath = '//span[@data-test="company-name"]'
    elements = driver.find_elements(By.XPATH, company_names_xpath)
    company_names = [element.text for element in elements]
    return company_names


def get_job_offers():
    company_names = get_company_names()
    job_titles = get_job_titles()
    job_offers = []
    count = 0
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

driver.close()
