import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard_page import DashboardPage
import time

class TestDashboardNavigation:
    '''Test suite for AI Dashboard navigation and interactions'''
    
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    
    @pytest.fixture
    def dashboard(self, driver):
        driver.get('https://example-ai-dashboard.com')
        return DashboardPage(driver)
    
    def test_dashboard_loads_successfully(self, dashboard):
        assert dashboard.is_loaded(), 'Dashboard failed to load'
        assert dashboard.header_is_visible(), 'Header not visible'
        assert dashboard.sidebar_is_visible(), 'Sidebar not visible'
