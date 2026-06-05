class ProfilePage:
    URL = "https://local-eats-unisenac.vercel.app/static/profile.html"

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(self.URL)

    def nome_usuario_visivel(self) -> bool:
        return self.page.locator("#userNameProfile").is_visible()

    def secao_favoritos_visivel(self) -> bool:
        return self.page.locator("text=Restaurantes Favoritos").is_visible()
