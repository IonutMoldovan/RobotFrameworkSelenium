import os
import time
from selenium import webdriver
from robot.api import logger


class ScreenshotListener:
    def __init__(self):
        self.driver = None
        self.report_dir = None
        self.screenshot_dir = None

    def start_suite(self, suite):
        # Initialize WebDriver and create directories
        self.driver = webdriver.Chrome()

        # Define the report and screenshot directories inside the report folder
        self.report_dir = os.path.join(os.getcwd(), 'report')
        if not os.path.exists(self.report_dir):
            logger.info(f"Creating report directory: {self.report_dir}")
            os.makedirs(self.report_dir)

        self.screenshot_dir = os.path.join(self.report_dir, 'screenshots')
        if not os.path.exists(self.screenshot_dir):
            logger.info(f"Creating screenshots directory: {self.screenshot_dir}")
            os.makedirs(self.screenshot_dir)

    def end_suite(self, suite):
        if self.driver:
            self.driver.quit()

    def end_test(self, test):
        if self.driver:
            timestamp = int(time.time())
            screenshot_path = os.path.join(self.screenshot_dir, f'{test.name}_{timestamp}.png')
            self.driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot saved for test '{test.name}' at {screenshot_path}")
