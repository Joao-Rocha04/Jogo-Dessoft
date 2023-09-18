# Jogo-Dessoft
Barbara's Adventure

-João Vitor Rocha
-Roberta Barros Teixeira Pereira
-Marcos Paulo

Primeiramente, para rodar nosso jogo se deve baixar o pygame. Para isso, você deve procurar em sua barra de busca no windows o Anaconda Prompt, nele, você deve digitar pip install pygame, após seu dowload ser confirmado, você pode abrir nosso jogo em sua IDE de preferência e se preparar para o desafio!!

Nosso jogo consiste de uma personagem que deve eliminar os inimigos que irão aparecer, os inimigos vão aparecer nas duas extremidades da tela e irão em direção a ela, porém existe um inimigo que vai permanecer na extremidade esquerda da tela, e vai tentar te acertar um uma bola de MAGIA!! Os personagens possuem vidas diferentes e a personagem principal posui 3 vidas, sempre perdendo uma a ser atacada pela inimigo.
Para atacar, você deve apertar a tecla espaço, que irá lançar uma adaga que em contato com os inimigos tira uma vida deles.
A cada inimigo abatido, vcê carregada 5% de seu especial, que após ser carregado totalmente irá lançar uma SUPER ADAGA que elimina todos os inimigos que entrarem em seu caminho. Para o especial fique atento ao canto superior esquerdo da tela, que irá avisar quando seu especial estiver pronto, ai é somente apertar a tecla Q e ver a mágica acontecer.
Você tambem possui um DASH, que ao apertar E irá se "teletransportar" para a esquerda ou diretita, dependendo de sua direção.
A movimentação ocorre com as setinhas do teclado, para esquerda, direita, e para cima você consegue pular.
Aqui está o link de um vídeo demonstração sobre o jogo: https://youtu.be/eX61NidBtwU
Vale lembrar que para o desenvolvimento do jogo a maioria dos commits foram feitos de um perfil, tudo foi feito em grupo, sendo em aula ou em chamadas de voz.

Explicação da refatoração de abstração:
Durante o processo de revisão do código das diversas telas do jogo, notamos uma recorrência significativa em padrões de comportamento e implementação, o que gerou um código repetido entre os arquivos telainicial.py, telaconfig.py, e telagame_over.py. Essa repetição não apenas tornou o código mais difícil de ler, mas também aumentou a chance de inconsistências e erros no futuro. Para abordar esse desafio, implementamos uma refatoração de abstração, onde isolamos a lógica padrão de exibição e interação das telas em uma função genérica, localizada no arquivo utilidade_tela.py. Esta mudança nos permitiu reduzir o código repetido e melhorar o que cada tela realmente faz, garantindo que cada uma delas se concentrasse apenas em seus comportamentos e representações específicas. Como resultado, o código agora apresenta uma estrutura mais limpa, facilitando futuras alterações e manutenções, bem como uma melhor compreensão de suas funções e responsabilidades individuais.

Explicação da refatoração de coesão:
A refatoração de coesão no arquivo assets.py foi realizada com o objetivo de melhorar a organização de recursos sonoros do jogo. Ao criar a classe SOM, centralizamos todas as operações relacionadas ao som. Isso não apenas torna o código mais limpo e coeso, mas também facilita a manutenção e futuras expansões do jogo, uma vez que todas as operações de som estão encapsuladas em uma única classe. Além disso, a refatoração permitiu uma maior flexibilidade na configuração de volume dos sons e na definição de loops, tornando o gerenciamento de recursos sonoros mais versátil e adaptável às necessidades do jogo. Dessa forma, a refatoração de coesão contribuiu para uma estrutura de código mais organizada e sustentável.