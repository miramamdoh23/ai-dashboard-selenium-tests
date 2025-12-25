# AI Dashboard Selenium Tests

Automated UI testing suite for AI/ML dashboards using Selenium WebDriver. This project provides comprehensive test coverage for user interactions, data visualizations, and AI model result displays.

---

## Project Overview

This testing framework is designed to ensure the reliability and functionality of AI-powered dashboards through automated browser testing. It follows industry best practices including the Page Object Model (POM) pattern for maintainable and scalable test code.

---

## Features

- **Automated Login Flow Testing**: Validates authentication mechanisms
- **Dashboard Navigation Tests**: Ensures smooth user experience across dashboard sections
- **Model Results Display Tests**: Verifies AI/ML model outputs are correctly rendered
- **Data Visualization Tests**: Validates charts, graphs, and interactive elements
- **Page Object Model (POM)**: Clean separation of test logic and page elements
- **Detailed HTML Reports**: Comprehensive test execution reports

---

## Project Structure
```
ai-dashboard-selenium-tests/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
│
├── tests/                             # Test suites
│   ├── test_login_flow.py            # Login/authentication tests
│   ├── test_dashboard_navigation.py  # Navigation and routing tests
│   ├── test_model_results_display.py # AI model output tests
│   └── test_data_visualization.py    # Chart and graph tests
│
├── pages/                             # Page Object Model
│   ├── login_page.py                 # Login page elements and actions
│   ├── dashboard_page.py             # Dashboard page elements and actions
│   └── results_page.py               # Results page elements and actions
│
├── utils/                             # Utility functions
│   ├── driver_setup.py               # WebDriver configuration
│   └── test_helpers.py               # Helper functions for tests
│
├── config/                            # Configuration files
│   └── config.yaml                   # Test configuration settings
│
└── reports/                           # Test execution reports
    └── test_results.html             # HTML test report
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Chrome/Firefox/Edge browser installed
- Internet connection for WebDriver downloads

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/miramamdoh23/ai-dashboard-selenium-tests.git
cd ai-dashboard-selenium-tests
```

**2. Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Configure test settings:**
Edit `config/config.yaml` with your dashboard URL and credentials:
```yaml
base_url: "https://your-dashboard-url.com"
browser: "chrome"  # chrome, firefox, or edge
headless: false
timeout: 10

test_user:
  username: "test@example.com"
  password: "your_password"
```

---

## Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test Suite
```bash
pytest tests/test_login_flow.py -v
pytest tests/test_dashboard_navigation.py -v
pytest tests/test_model_results_display.py -v
pytest tests/test_data_visualization.py -v
```

### Run Tests in Headless Mode
```bash
pytest tests/ -v --headless
```

### Generate HTML Report
```bash
pytest tests/ -v --html=reports/test_results.html --self-contained-html
```

### Run Tests in Parallel
```bash
pytest tests/ -v -n 4  # Run with 4 parallel workers
```

---

## Test Coverage

### Login Flow Tests (test_login_flow.py)
- Valid login credentials
- Invalid login attempts
- Password visibility toggle
- Remember me functionality
- Logout functionality
- Session timeout handling

### Dashboard Navigation Tests (test_dashboard_navigation.py)
- Main menu navigation
- Sidebar menu functionality
- Breadcrumb navigation
- Page load performance
- Responsive design elements
- Search functionality

### Model Results Display Tests (test_model_results_display.py)
- Model prediction display
- Confidence scores rendering
- Result data accuracy
- Export functionality
- Pagination of results
- Filter and sort operations

### Data Visualization Tests (test_data_visualization.py)
- Chart rendering (line, bar, pie)
- Interactive tooltips
- Legend display
- Zoom and pan functionality
- Data point accuracy
- Responsive chart sizing

---

## Configuration Options

### Browser Configuration
Supported browsers:
- Chrome (default)
- Firefox
- Edge

### Test Data Management
Test data can be configured in `config/config.yaml` or passed as environment variables:
```bash
export DASHBOARD_URL="https://your-dashboard.com"
export TEST_USERNAME="test@example.com"
export TEST_PASSWORD="password123"
```

### Custom Wait Times
Adjust timeout settings in `config/config.yaml`:
```yaml
timeout:
  implicit: 10  # seconds
  explicit: 20  # seconds
  page_load: 30 # seconds
```

---

## Writing New Tests

### Example Test Structure
```python
import pytest
from pages.dashboard_page import DashboardPage
from utils.driver_setup import get_driver

class TestNewFeature:
    
    @pytest.fixture
    def setup(self):
        self.driver = get_driver()
        self.dashboard = DashboardPage(self.driver)
        yield
        self.driver.quit()
    
    def test_new_functionality(self, setup):
        # Arrange
        self.dashboard.navigate_to_feature()
        
        # Act
        result = self.dashboard.perform_action()
        
        # Assert
        assert result == expected_value
```

---

## Debugging Tests

### Screenshots on Failure
Screenshots are automatically captured on test failures and saved to `reports/screenshots/`

### Enable Debug Logging
```bash
pytest tests/ -v --log-cli-level=DEBUG
```

### Run Single Test
```bash
pytest tests/test_login_flow.py::TestLoginFlow::test_valid_login -v
```

---

## Best Practices

1. **Use Page Object Model**: Keep page elements and actions in page classes
2. **Wait Explicitly**: Use explicit waits instead of sleep()
3. **Independent Tests**: Each test should be able to run independently
4. **Clear Test Names**: Use descriptive test function names
5. **Clean Up Resources**: Always close drivers in teardown
6. **Parameterize Tests**: Use pytest.mark.parametrize for multiple test cases
7. **Regular Updates**: Keep Selenium and WebDriver versions updated

---

## Dependencies

Main dependencies (see `requirements.txt` for full list):
- `selenium>=4.15.0`: WebDriver automation
- `pytest>=7.4.0`: Testing framework
- `pytest-html>=4.1.0`: HTML report generation
- `pytest-xdist>=3.5.0`: Parallel test execution
- `webdriver-manager>=4.0.0`: Automatic driver management
- `PyYAML>=6.0`: Configuration file parsing
- `Pillow>=10.0.0`: Screenshot handling

---

## Troubleshooting

### Common Issues

**Issue: WebDriver not found**
```bash
# Solution: Install webdriver-manager
pip install webdriver-manager
```

**Issue: Element not found**
```python
# Solution: Use explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)
```

**Issue: Tests fail in headless mode**
```yaml
# Solution: Increase viewport size in config.yaml
window_size:
  width: 1920
  height: 1080
```

---

## Continuous Integration

### GitHub Actions Example
```yaml
name: Selenium Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest tests/ -v --html=reports/test_results.html
      - name: Upload test reports
        uses: actions/upload-artifact@v2
        with:
          name: test-reports
          path: reports/
```

---

## Skills Demonstrated

- **UI Test Automation**: Comprehensive Selenium WebDriver implementation
- **Page Object Model**: Clean architecture for maintainable tests
- **Test Framework Design**: Pytest-based testing suite
- **CI/CD Integration**: Automated testing pipeline
- **Best Practices**: Industry-standard testing methodologies
- **Configuration Management**: YAML-based test configuration
- **Parallel Execution**: Efficient test running strategies
- **Report Generation**: Detailed HTML test reports

---

## Use Cases

This framework is ideal for:

- **AI/ML Dashboards**: Testing machine learning model interfaces
- **Data Visualization Platforms**: Validating charts and graphs
- **Analytics Applications**: Testing data-driven applications
- **Enterprise Dashboards**: Quality assurance for business intelligence tools
- **SaaS Platforms**: Automated testing for web applications

---

## Additional Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [WebDriver Best Practices](https://www.selenium.dev/documentation/webdriver/best_practices/)

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Author

**Mira Mamdoh Yousef Mossad**  
AI QA Engineer | Test Automation Specialist

**Specializing in**:
- UI Test Automation
- Selenium WebDriver
- AI/ML Dashboard Testing
- Test Framework Design

**Connect**:
- Email: miramamdoh10@gmail.com
- LinkedIn: [linkedin.com/in/mira-mamdoh-a9aa78224](https://www.linkedin.com/in/mira-mamdoh-a9aa78224)
- GitHub: [github.com/miramamdoh23](https://github.com/miramamdoh23)

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments

Built to demonstrate professional UI test automation methodologies for AI/ML dashboard applications using Selenium WebDriver and pytest framework.

---

**Note:** This testing suite is designed for AI/ML dashboard applications. Customize the tests according to your specific dashboard requirements and features.

For questions or issues, please open an issue on GitHub or contact the maintainers.

