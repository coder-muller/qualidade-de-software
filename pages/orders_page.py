class OrdersPage:
    URL = "https://local-eats-unisenac.vercel.app/static/orders.html"

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(self.URL)

    def titulo_historico_visivel(self) -> bool:
        return self.page.locator("text=Histórico de Transações").is_visible()

    def possui_pedidos(self) -> bool:
        return self.page.locator(".order-card").count() > 0

    def primeiro_pedido_visivel(self) -> bool:
        return self.page.locator(".order-card").first.is_visible()

    def total_do_primeiro_pedido_visivel(self) -> bool:
        return self.page.locator(".order-card").first.locator(
            "text=Total Estimado:"
        ).is_visible()
