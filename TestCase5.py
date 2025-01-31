from playwright.sync_api import sync_playwright
from TestBase import TestBase

# Test Case 5
# Login to Demo App.
# Navigate to "Mobile Application."
# Verify "Offline mode" is in the "In Progress" column.
# Confirm tags: "Feature" & "High Priority”

url = "https://animated-gingersnap-8cf7f2.netlify.app/"
username = "admin"
password = "password123"
tab = "Mobile Application"
column = "In Progress"
target_text = "Offline mode"
tags = ["Feature", "High Priority"]
test = TestBase(url, username, password, tab, column, target_text, tags)
with sync_playwright() as playwright:
    test.run(playwright)
