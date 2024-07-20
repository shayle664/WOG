from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def test_scores_service():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Run without sandbox (required for Docker)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=chrome_options)

    try:
        driver.get("http://localhost:8777")
        score_element = driver.find_element(By.ID, 'score')  # Adjust selector as needed
        score = int(score_element.text)
        if 1 <= score <= 1000:
            return True
        else:
            print(f"Score {score} is out of range.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()


def main_function():
    if test_scores_service():
        print("Test passed.")
        return 0
    else:
        print("Test failed.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main_function())
