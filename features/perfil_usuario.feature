# language: pt
Funcionalidade: Perfil do usuario
  Como usuario autenticado do Local Eats
  Quero acessar meu perfil
  Para visualizar meus dados e favoritos

  Cenario: Acessar pagina de perfil
    Dado que o usuario esta autenticado no sistema
    Quando acessa a pagina de perfil
    Entao o sistema deve exibir o nome do usuario

  Cenario: Visualizar secao de favoritos
    Dado que o usuario esta autenticado no sistema
    Quando acessa a pagina de perfil
    Entao o sistema deve exibir a secao de restaurantes favoritos
