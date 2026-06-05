class LoginPage:
    URL = "https://local-eats-unisenac.vercel.app/static/login.html"

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(self.URL)

    def realizar_login(self, email: str, senha: str):
        self.page.locator("#loginEmail").fill(email)
        self.page.locator("#loginPassword").fill(senha)
        self.page.locator("#loginForm button[type='submit']").click()

    def usuario_logado(self):
        self.page.wait_for_url("**/index.html", timeout=10000)
        return "index.html" in self.page.url
