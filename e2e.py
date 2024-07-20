import main_score
from selenium import webdriver
from selenium.webdriver.common.by import By


def main_function():
    if test_scores_service():
        return 0
    else:
        return -1


def test_scores_service():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")
    score = driver.find_element(By.ID, "score").text
    if 0 < int(score) < 1000:
        return True
    else:
        return False


if __name__ == "__main__":
    exit_code = main_function()
    exit(exit_code)

