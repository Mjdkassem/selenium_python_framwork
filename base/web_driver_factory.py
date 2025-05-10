"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.letskodeit.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
             # Set properties for chromedriver (if needed, Selenium Manager might handle this)
            # chromedriver_path = "/path/to/your/chromedriver"
            # service = Service(chromedriver_path)

            # Configure Chrome Options for CI/Headless execution
            options = ChromeOptions()
            options.add_argument("--headless") # Run in headless mode
            options.add_argument("--no-sandbox") # Bypass OS security model (necessary in some CI)
            options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
            options.add_argument("--disable-gpu") # Disable GPU hardware acceleration (often good for headless)
            options.add_argument("--window-size=1920,1080") # Set a default window size

            # If the 'user data directory' error persists, you might need to be more specific:
            # options.add_argument("--user-data-dir=/tmp/chrome-user-data") # Use a temporary, unique directory
            # options.add_argument("--remote-debugging-port=9222") # Often included, though not directly for this error

            # Initialize the Chrome driver with options
            # driver = webdriver.Chrome(service=service, options=options) # If using Service
            driver = webdriver.Chrome(options=options) # If letting Selenium Manager find the driver
        # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(3)
        # Maximize the window
            driver.maximize_window()

        return driver