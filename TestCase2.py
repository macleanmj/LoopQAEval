from playwright.sync_api import sync_playwright
from TestBase import TestBase

# Test Case 2
# Login to Demo App.
# Navigate to "Web Application."
# Verify "Fix navigation bug" is in the "To Do" column.
# Confirm tags: "Bug"

url = "https://animated-gingersnap-8cf7f2.netlify.app/"
username = "admin"
password = "password123"
tab = "Web Application"
column = "To Do"
target_text = "Fix navigation bug"
tags = ["Bug"]
test = TestBase(url, username, password, tab, column, target_text, tags)
with sync_playwright() as playwright:
    test.run(playwright)
