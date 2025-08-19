import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Adjust this path if your HTML file is in a subfolder
        html_path = 'file://' + os.path.abspath('wk1exercise4.html')  # or your HTML filename
        driver.get(html_path)

        # Wait for the page and API to load
        time.sleep(5)

        # Check map container exists and is visible
        map_element = driver.find_element(By.ID, 'map')
        assert map_element.is_displayed(), "Map container is not visible"

        # Check if Google Maps API loaded
        maps_loaded = driver.execute_script(
            "return typeof google !== 'undefined' && typeof google.maps !== 'undefined';"
        )
        assert maps_loaded, "Google Maps API not loaded"

        # Check if the global map variable is initialized (adjust if your variable has a different name)
        map_initialized = driver.execute_script("return typeof map !== 'undefined';")
        assert map_initialized, "Map object not initialized"

        print("PASS: Google Maps API loaded and map is initialized.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
