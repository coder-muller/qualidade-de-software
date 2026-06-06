"""Captura screenshot da pagina de pedidos para evidencias BDD."""

from playwright.sync_api import sync_playwright

URL_LOGIN = "https://local-eats-unisenac.vercel.app/static/login.html"
URL_PEDIDOS = "https://local-eats-unisenac.vercel.app/static/orders.html"
EVIDENCIA = "artefatos/evidencias/pbl8-pagina-pedidos.png"


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(URL_LOGIN)
        page.locator("#loginEmail").fill("teste@teste.com")
        page.locator("#loginPassword").fill("123")
        page.locator("#loginForm button[type='submit']").click()
        page.wait_for_url("**/index.html")
        page.goto(URL_PEDIDOS)
        page.wait_for_load_state("networkidle")
        page.screenshot(path=EVIDENCIA, full_page=True)
        browser.close()


if __name__ == "__main__":
    main()
