from playwright.sync_api import sync_playwright
from TestBase import TestBase

# Test Case 3
# Login to Demo App.
# Navigate to "Web Application."
# Verify "Design system updates" is in the "In Progress" column.
# Confirm tags: "Design”

url = "https://animated-gingersnap-8cf7f2.netlify.app/"
username = "admin"
password = "password123"
tab = "Web Application"
column = "In Progress"
target_text = "Design system updates"
tags = ["Design"]
test = TestBase(url, username, password, tab, column, target_text, tags)
with sync_playwright() as playwright:
    test.run(playwright)
