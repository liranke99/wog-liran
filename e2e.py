from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_scores_service(app_url):
    print(f"Opening browser and navigating to {app_url}")
    driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
    driver.get(app_url)
    time.sleep(5)  # Wait for the page to load
    try:
        print("Attempting to find the score element on the page")
        score_element = driver.find_element(By.ID, "score")  # Ensure this matches the ID in your HTML
        score = int(score_element.text)
        print(f"Score found: {score}")
        if 1 <= score <= 1000:
            print("Score is within the expected range (1 to 1000)")
            return True
        else:
            print("Score is out of the expected range (1 to 1000)")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()
        print("Browser closed")

def main_function():
    app_url = "http://127.0.0.1:5000"  # Ensure this URL is correct
    print(f"Starting test for URL: {app_url}")
    if test_scores_service(app_url):
        print("Test passed")
        return 0
    else:
        print("Test failed")
        return -1

if __name__ == "__main__":
    exit(main_function())
