from selenium import webdriver


def get_rendered_html(url):
    driver = webdriver.Chrome()

    driver.get(url)

    html = driver.page_source

    driver.quit()

    return html