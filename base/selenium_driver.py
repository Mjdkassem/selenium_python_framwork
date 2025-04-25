from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():
    
    my_log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
    def get_title(self):
        return self.driver.title
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.my_log.info("Locator type " + locatorType + 
                          " not correct/supported")
        return False

    def get_element(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.my_log.info("Found element with locator: " + locator + "Locator Type:" + locatorType)
        except:
            self.my_log.info("Not found element with locator: " + locator + "Locator Type:" + locatorType)
        return element
    
    def click_element(self, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            element.click()
            self.my_log.info("Clicked on the element with locator: " + locator + "Locator Type:" + locatorType)
        except:
            self.my_log.info("Can not click on the element with locator: " + locator + "Locator Type:" + locatorType)
            print_stack()
    
    def send_values(self, data, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            element.clear()
            element.send_keys(data)
            self.my_log.info("Send data on the element with locator: " + locator + "Locator Type:" + locatorType)
        except:
            self.my_log.info("Can send data on the element with locator: " + locator + "Locator Type:" + locatorType)
            print_stack()


    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False
    
    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        self.driver.implicitly_wait(2)
        return element
    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()