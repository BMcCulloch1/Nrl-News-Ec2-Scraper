from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True = no UI
        page = browser.new_page()
        page.goto("https://www.zerotackle.com/news/")
        page.wait_for_timeout(5000)  # wait 5 seconds
        print(page.title())
        browser.close()

if __name__ == "__main__":
    run_test()
