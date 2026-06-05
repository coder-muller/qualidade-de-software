"""Captura screenshot da pagina principal apos login para evidencias."""

from playwright.sync_api import sync_playwright

URL_LOGIN = "https://local-eats-unisenac.vercel.app/static/login.html"
EVIDENCIA = "artefatos/evidencias/pbl7-pagina-logada.png"


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(URL_LOGIN)
        page.locator("#loginEmail").fill("teste@teste.com")
        page.locator("#loginPassword").fill("123")
        page.locator("#loginForm button[type='submit']").click()
        page.wait_for_url("**/index.html")
        page.locator("#restaurantGrid .rest-card").first.wait_for(timeout=15000)
        page.screenshot(path=EVIDENCIA, full_page=True)
        browser.close()


if __name__ == "__main__":
    main()
