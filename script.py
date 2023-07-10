from selenium import webdriver
from selenium.webdriver.common.by import By

technology = "JavaScript"
driver = webdriver.Chrome()
driver.implicitly_wait(60)
url = f"https://it.pracuj.pl/?tt={technology}&jobBoardVersion=2"
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


jobTitles = get_job_titles()
companyNames = get_company_names()
print(jobTitles)
print(companyNames)
driver.close()
