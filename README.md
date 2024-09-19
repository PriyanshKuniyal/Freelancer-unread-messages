README
## Selenium Headless Login Script
This Python script uses Selenium WebDriver to log into a website in headless mode and retrieve unread message counts. It performs the following tasks:

Initialize Chrome in Headless Mode: Configures Chrome to run in headless mode for automation.
Navigate to Login Page: Opens the specified webpage.
Login Automation: Inputs email and password, then clicks the login button.
Check Unread Messages: Waits for the unread messages indicator to appear and prints the count.
Graceful Shutdown: Ensures the browser is closed properly even if an error occurs.

Requirements:
Selenium (pip install selenium)
ChromeDriver (download from ChromeDriver)

Usage:

Replace path/to/your/chromedriver.exe with the path to your chromedriver.exe.
Update the email and password fields with your credentials.
Run the script.
