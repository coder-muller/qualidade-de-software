"""
Script gerado com Playwright Codegen para o fluxo de login do Local Eats.

Comando:
    playwright codegen https://local-eats-unisenac.vercel.app/static/login.html
"""

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.locator("#loginEmail").click()
    page.locator("#loginEmail").fill("teste@teste.com")
    page.locator("#loginPassword").click()
    page.locator("#loginPassword").fill("123")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.wait_for_url("**/index.html")

    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
