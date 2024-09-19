from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# path to chromedriver
driver_path = 'path/to/your/chromedriver.exe'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Create a Service object for ChromeDriver
service = Service(driver_path)

# Initialize the Chrome WebDriver using the Service object
driver = webdriver.Chrome(service=service,options=chrome_options)

# Open a webpage
driver.get('https://www.freelancer.in/dashboard')
try:
    email=driver.find_element(by=By.CSS_SELECTOR,value='#emailOrUsernameInput')
    email.send_keys('youremail@email.com')#Enter your email or user name

    password=driver.find_element(by=By.CSS_SELECTOR,value='#passwordInput')
    password.send_keys('Your Password')#Enter your account password

    login=driver.find_element(by=By.CSS_SELECTOR,value='body > app-root > app-logged-out-shell > div > app-login-page > div > div.LoginPageContainer > app-login > app-credentials-form > form > app-login-signup-button > fl-button > button')
    login.click()
except:
    print('WRONG CREDENTIALS')
    driver.quit()
time.sleep(5)

try:
    # Wait for the element to be present
    wait = WebDriverWait(driver, 10)
    unread = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//fl-unread-indicator/div/span[contains(@class, 'UnreadIndicator-counter')]"))
    )
    # Print the unread messages of the element
    print('unread messages-',unread.text)
except TimeoutError:
    print('NO UNREAD MESSAGES')
finally:

    driver.quit()