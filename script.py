from selenium import webdriver
from selenium.webdriver.common.by import By

technology = "JavaScript"
driver = webdriver.Chrome()
driver.implicitly_wait(60)
url = f"https://it.pracuj.pl/?tt={technology}&jobBoardVersion=2"
driver.get(url)


def extract_text_from_elements(elements):
    text_list = []
    for element in elements:
        text_list.append(element.text)
    return text_list


def get_job_titles():
    job_title_xpath = '//h3[@data-test="offer-title"]'
    elements = driver.find_elements(By.XPATH, job_title_xpath)
    job_titles = extract_text_from_elements(elements)
    return job_titles


jobTitles = get_job_titles()
print(jobTitles)
driver.close()
