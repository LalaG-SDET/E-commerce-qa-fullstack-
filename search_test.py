from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_ecommerce_search():
    # Chrome brauzerini QA rejmində açırıq
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # Test mağazasına giriş
    driver.get("https://automationexercise.com/products")
    
    # Axtarış xanasına "Dress" yazırıq
    search_input = driver.find_element(By.ID, "search_product")
    search_input.send_keys("Dress")
    
    # Axtarış düyməsini klikləyirik
    driver.find_element(By.ID, "submit_search").click()
    
    # Nəticələrin gəldiyini 2 saniyə gözləyib yoxlayırıq
    time.sleep(2)
    assert "SEARCHED PRODUCTS" in driver.page_source
    
    print("UI Automation Test: SUCCESS")
    driver.quit()

if __name__ == "__main__":
    test_ecommerce_search()
