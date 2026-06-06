# language: pt
Funcionalidade: Historico de pedidos
  Como usuario autenticado do Local Eats
  Quero visualizar meus pedidos anteriores
  Para acompanhar o historico de transacoes

  Cenario: Visualizar pedidos realizados
    Dado que o usuario esta autenticado no sistema
    Quando acessa a pagina de pedidos
    Entao o sistema deve exibir o historico de transacoes

  Cenario: Validar valor total do pedido
    Dado que o usuario esta autenticado no sistema
    Quando visualiza um pedido realizado
    Entao o sistema deve exibir o valor total do pedido
