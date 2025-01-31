from playwright.sync_api import sync_playwright
from TestBase import TestBase

# Test Case 4
# Login to Demo App.
# Navigate to "Mobile Application."
# Verify "Push notification system" is in the "To Do" column.
# Confirm tags: "Feature”

url = "https://animated-gingersnap-8cf7f2.netlify.app/"
username = "admin"
password = "password123"
tab = "Mobile Application"
column = "To Do"
target_text = "Push notification system"
tags = ["Feature"]
test = TestBase(url, username, password, tab, column, target_text, tags)
with sync_playwright() as playwright:
    test.run(playwright)
