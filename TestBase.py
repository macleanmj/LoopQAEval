import json
from playwright.sync_api import Playwright, expect, sync_playwright


class TestBase:
    def __init__(self, url: str, username: str, password: str, tab: str, column: str, target_text: str, tags: list):
        self.url = url
        self.username = username
        self.password = password
        self.tab = tab
        self.column = column
        self.target_text = target_text
        self.tags = tags

    # Function to enter the Username and Password that the test was created with
    def login(self):
        self.page.get_by_label("Username").fill(self.username)
        self.page.get_by_label("Password").fill(self.password)
        self.page.get_by_role("button", name="Sign in").click()

    # Function to confirm the Title of the specified task is present. Returns the Locator for the title to be used later
    def confirm_task_title(self):
        # Find the heading for the specified column
        column_title = self.page.get_by_role("heading", name=self.column, level=2)

        # Get all level 3 headings under the specified column. One of these should be the target_text
        task_titles = column_title.locator("..//h3")

        # Select only the target text, and assert that it is there
        target_task_name = task_titles.get_by_text(self.target_text)
        expect(target_task_name, f"{self.target_text} not found in column {self.column}").to_contain_text(
            self.target_text)
        print(f"'{self.target_text}' found under 'To Do' heading")

        return target_task_name

    # Function to determine the presence of tags given the Locator for the title of the task
    def confirm_tags(self, task_title):
        # Select all span objects in the same parent as the target_text. The Tags will be among these
        feature_details = task_title.locator("..//span")

        # For each tag that we are searching for, confirm that they are in the details of the feature
        for tag in self.tags:
            temp_loc = feature_details.get_by_text(tag)
            expect(temp_loc, f"{tag} not found under {self.target_text}").to_contain_text(tag)

        print(f"All tags found under {self.target_text}")

    # Initial steps for all tests. Any other functions to be overridden in the test
    def run(self, playwright: Playwright):
        self.browser = playwright.chromium.launch()
        self.page = self.browser.new_page()
        self.page.goto(self.url)
        self.login()

        # Navigate to the correct tab for the test
        self.page.get_by_role("button", name=self.tab).click()

        target_task_name = self.confirm_task_title()

        self.confirm_tags(target_task_name)

        self.browser.close()


if __name__ == "__main__":
    with open('TestCases.json') as f:
        cases = json.load(f)["TestCases"]

    for case in cases:
        print(f"*** Running {case['name']} ***")
        test = TestBase(case["url"], case["username"], case["password"], case["tab"], case["column"],
                        case["target_text"], case["tags"])
        with sync_playwright() as playwright:
            test.run(playwright)
        print(f"*** Finished {case['name']} ***")
