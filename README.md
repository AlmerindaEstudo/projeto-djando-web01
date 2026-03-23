

O projeto Controle de Estoque foi desenvolvido na disciplina de Desenvolvimento Web, com o objetivo de aplicar na prática os conceitos aprendidos tanto no frontend quanto no backend.
No início, aprendemos conceitos de design utilizando HTML e CSS. Depois, avançamos para o backend com Python, utilizando o framework Django, onde desenvolvemos a lógica do sistema. Durante o desenvolvimento, utilizamos conceitos importantes como views, models e também APIs, que foram fundamentais para o funcionamento do sistema.
O sistema foi pensado para que o usuário tenha controle total sobre fornecedores, produtos, estoque e clientes, e ele é dividido em algumas partes principais:
Página de Fornecedores e Cadastro de Produtos:
Nessa parte, o usuário cadastra os fornecedores e também os produtos que cada fornecedor disponibiliza. Ou seja, é aqui que começa todo o fluxo do sistema, pois os produtos só existem a partir dos fornecedores.

Aba "Comprar Produtos":
Essa aba é responsável por registrar a compra de produtos dos fornecedores. Ou seja, o controlador do estoque escolhe, entre os produtos que o fornecedor cadastrou, quais deseja comprar. Esses produtos comprados são então adicionados ao estoque do sistema.

Aba "Vender":
Essa parte do sistema é utilizada para vender produtos para os clientes. Porém, existe uma regra importante: só é possível vender produtos que já estão no estoque, ou seja, que foram previamente comprados dos fornecedores.
   
Aba "Vendidos":
Essa aba é voltada para o controle de vendas realizadas. Nela, é possível acompanhar todas as vendas feitas para os clientes, garantindo um melhor controle do negócio.

Um ponto importante do projeto é que todo o sistema foi desenvolvido utilizando APIs. O uso de API foi essencial para organizar a comunicação entre o frontend e o backend, além de deixar o sistema mais escalável e bem estruturado.
Aprofundando um pouco nos conceitos utilizados:
Models:
Os models representam a estrutura dos dados do sistema. Foi através deles que definimos entidades como fornecedores, produtos, clientes e vendas. Cada model corresponde a uma tabela no banco de dados.
Views:
As views são responsáveis pela lógica do sistema. Elas recebem as requisições do usuário, processam as informações (como cadastrar um produto, realizar uma compra ou uma venda) e retornam uma resposta, geralmente em formato JSON no caso das APIs.
APIs:
As APIs foram utilizadas para permitir a comunicação entre diferentes partes do sistema. Por exemplo, quando um produto é comprado ou vendido, essa informação é enviada e processada através de uma API. Isso torna o sistema mais organizado, reutilizável e preparado para futuras expansões, como integração com outros sistemas ou aplicativos.
O projeto está disponível no repositório:
https://github.com/AlmerindaEstudo/projeto-djando-web01/tree/projetoprincipal
Para executar o projeto localmente:

1)git clone -b projetoprincipal --single-branch https://github.com/AlmerindaEstudo/projeto-djando-web01.git

2)cd projeto-djando-web01

3)python -m venv venv

4)venv\Scripts\Activate

5)pip install -r requirements.txt

6)cd backend

7)python manage.py makemigrations

8)python manage.py migrate

9)python manage.py runserver

