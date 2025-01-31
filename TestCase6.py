from playwright.sync_api import sync_playwright
from TestBase import TestBase

# Test Case 6
# Login to Demo App.
# Navigate to "Mobile Application."
# Verify "App icon design" is in the "Done" column.
# Confirm tags: "Design”

url = "https://animated-gingersnap-8cf7f2.netlify.app/"
username = "admin"
password = "password123"
tab = "Mobile Application"
column = "Done"
target_text = "App icon design"
tags = ["Design"]
test = TestBase(url, username, password, tab, column, target_text, tags)
with sync_playwright() as playwright:
    test.run(playwright)
