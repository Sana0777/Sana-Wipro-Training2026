# E-Commerce UI Automation – Capstone Project

**URL:** https://demowebshop.tricentis.com  
**Frameworks:** Selenium + Pytest | Selenium + Robot Framework
 

---

## How It Works

Each row in the CSV = **one user** = **one browser session**.

```
Browser opens
  ↓ Register
  ↓ Login
  ↓ Search product
  ↓ Open product detail page
  ↓ Add to cart (with quantity from CSV)
  ↓ Navigate to cart – verify product & quantity
  ↓ Update quantity (updated_quantity from CSV)
  ↓ Remove item from cart
  ↓ Logout
  ↓ Verify session terminated
Browser closes

→ Repeat for next user row
```

---

## Directory Structure

```
Capstone_Project/
├── requirements.txt
│
├── Selenium_Pytest/
│   ├── config/
│   │   └── config.ini                 ← browser, URL, waits
│   ├── data/
│   │   └── e2e_test_data.csv          ← one row = one user's full E2E data
│   ├── pages/                         ← Page Object Model
│   │   ├── base_page.py
│   │   ├── registration_page.py
│   │   ├── login_page.py
│   │   ├── home_page.py
│   │   ├── product_page.py
│   │   └── cart_page.py
│   ├── tests/
│   │   └── test_e2e_full_flow.py      ← single parametrized E2E test
│   ├── utilities/
│   │   ├── browser.py
│   │   └── helper.py                  ← CSV loader
│   ├── reports/                       ← HTML report + log
│   ├── screenshots/                   ← auto-saved on failure
│   ├── conftest.py                    ← driver fixture + screenshot hook
│   └── pytest.ini
│
└── Selenium_Robot/
    ├── keywords/
    │   ├── common_keywords.robot
    │   ├── register_keywords.robot
    │   ├── login_keywords.robot
    │   ├── product_keywords.robot
    │   └── cart_keywords.robot
    ├── resources/
    │   ├── config.robot
    │   └── locators.robot
    ├── tests/
    │   └── test_All.robot             ← TC_E2E_User1, User2, User3
    ├── variables/
    │   └── test_data.csv              ← same structure as Pytest CSV
    └── reports/
```

---

## CSV Format

### test_data.csv (Pytest) / test_data.csv (Robot)

```
first_name, last_name, email, password, gender,
product_search, product_name, add_quantity, updated_quantity
```

Add more rows to test more users — no code changes needed.

---

## Setup

```bash
pip install -r requirements.txt
```

---

## Run

### Pytest
```bash
cd Selenium_Pytest
pytest -v --html=reports/report.html
```

### Robot Framework
```bash
cd Selenium_Robot
robot -d reports tests/
```

---

## Assertions at Every Step

Every page method asserts:
- Field values after typing (input.value == expected)
- Page title after navigation
- URL fragment after page change
- Element visibility before interaction
- Notification text content after actions
- Cart count before and after update/remove
- Quantity value in cart after update
- Session state after logout
