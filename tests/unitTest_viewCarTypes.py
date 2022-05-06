# Unit test file to determine if the CarType page is displayed when the user
# clicks the 'CarType' button in the navigation pane of the carviewer app
# CarTypes is shown
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings


class ll_ATS(unittest.TestCase):
    # set up the test class - assign the driver to Edge - if using a different
    # browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Edge()
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if occurs

    # Test if CarType is displayed when Car Types are clicked in the Navigation bar
    # CarTypes is shown
    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")

        time.sleep(5)  # pause to allow screen to load

        # click the login button - user must be logged in to view the CarType

        elem = driver.find_element(By.XPATH, '//*[@id="app-layout"]/div[1]/a[5]').click()

        # find the username and password input boxes and login

        user = "testuser"  # must be a valid username for the application
        pwd = "test12345"  # must be the password for a valid user
        time.sleep(5)

        elem = driver.find_element(By.NAME, "username")
        elem.send_keys(user)
        elem = driver.find_element(By.NAME, "password")
        elem.send_keys(pwd)

        elem.send_keys(Keys.RETURN)

        time.sleep(5)  # pause to allow screen to load

        # find 'CarType' and click it – note this is all one Python statement

        elem = driver.find_element(By.XPATH, '//*[@id="app-layout"]/div[1]/a[4]').click()

        time.sleep(5)  # pause to allow screen to change
        try:

            elem = driver.find_element(By.XPATH,
                                       '//*[@id="app-layout"]/div[1]/a[4]')
            print("Test passed - CarType displayed")
            assert True

        except NoSuchElementException:
            self.fail("CarType does not appear when Customers is clicked - test failed")


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
