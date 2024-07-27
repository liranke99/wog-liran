# e2e.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_scores_service(app_url):
    driver = webdriver.Chrome()
    driver.get(app_url)
    time.sleep(5)  # Wait for the page to load
    try:
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()

def main_function():
    app_url = "http://localhost:5000"
    if test_scores_service(app_url):
        return 0
    else:
        return -1

if __name__ == "__main__":
    exit(main_function())
