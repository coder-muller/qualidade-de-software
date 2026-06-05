class HomePage:
    URL = "https://local-eats-unisenac.vercel.app/static/index.html"

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(self.URL)

    def buscar(self, termo: str):
        self.page.locator("#searchInput").fill(termo)
        self.page.locator("#searchBtn").click()

    def filtrar_por_culinaria(self, culinaria: str):
        self.page.locator(f".filter-btn[data-cuisine='{culinaria}']").click()

    def aguardar_restaurantes(self):
        self.page.locator("#restaurantGrid .rest-card").first.wait_for(
            state="visible",
            timeout=15000,
        )

    def quantidade_restaurantes_visiveis(self) -> int:
        return self.page.locator("#restaurantGrid .rest-card").count()

    def restaurantes_contem_texto(self, texto: str) -> bool:
        cards = self.page.locator("#restaurantGrid .rest-card")
        total = cards.count()
        for indice in range(total):
            if texto.lower() in cards.nth(indice).inner_text().lower():
                return True
        return False
