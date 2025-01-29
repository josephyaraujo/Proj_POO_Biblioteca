# Documento de Visão

## Sistema de Biblioteca

### Histórico da Revisão 

|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 26/01/2025 |  **`1.00`** | Versão Inicial  | Emanuelly Karine |


### 1. Objetivo do Projeto 

O projeto __Sistema de Biblioteca__ tem como objetivo prover um sistema simples e eficiente para o conjunto de atividades presentes em uma biblioteca, gereciando o acervo de livros, usuários e o processo de empréstimo e devolução. Facilitando, assim, o controle e a organização.

### 2. Descrição do Problema 

|         __        | __   |
|:------------------|:-----|
| **_O problema_**    | Dificuldade em gerenciar os livros presentes na biblioteca e os usuários que pegam empréstimos dos mesmos e estrapolam o prazo pré-definido.  |
| **_afetando_**      | Bibliotecários e os demais funcionários que não conseguem manter uma organização e controle dos livros. |
| **_cujo impacto é_**| Desorganização, dificuldade para localizar livros na biblioteca, perda de livros ou esquecimento da devolução. |
| **_uma boa solução seria_** | Um sistema que os funcionários consigam separar os livros por categoria para auxiliar no encontro de livros específicos, disponibilizando ferramentas de busca tanto para os funcionários quanto para os clientes. Além de permitir o acompanhamento do empréstimo dos livros, contendo o prazo de devolução e uma forma do cliente permitir aumentar esse prazo. |

### 3. Descrição dos Usuários

| Nome | Descrição | Responsabilidades |
|:---  |:--- |:--- |
| Administrador  | Realiza as atividades básicas para o início da operação do sistema | Mantém o cadastro dos funcionários responsáveis pela operação do empréstimo e devolução de livros e cadastro dos mesmos |
| Funcionário  | Realiza as atividades relacionadas ao controle do empréstimo de livros e cadastro de novos | Mantém o cadastro de livros; consulta a situação dos empréstimos e prazos de devolução |
| Cliente | Realiza as atividades relacionadas ao empréstimo de livros | Realiza o próprio cadastro no sistema; consulta o acervo de livros disponíveis; pega um livro e realiza o empréstimo; consulta seus empréstimo e realiza a devolução |

### 4. Descrição do Ambiente dos Usuários

Normalmente quando o cliente vai a uma biblioteca, ele necessita procurar os livros disponíveis sozinho ou com o auxílio do bibliotecário que precisa se deslocar para ir encontrar. Muitas vezes o controle de livros disponíveis é feito de forma manual por meio de uma planilha ou caderno, o que acarreta em confusões tanto para o funcionário, quanto para o cliente.

Desta forma, a ideia central do sistema é permitir que funcionários consigam cadastrar e remover livros de forma rápida e eficiente, facilitando a procura dos mesmos, garantindo um melhor controle sobre os empréstimos e devoluções.

### 5. Principais Necessidades dos Usuários

Para o administrador e os funcionários, a necessidade é garantir um melhor controle sobre os cadastro e atualização do estado dos livros, garantindo um melhor atendimento para os clientes.

Para os clientes, as necessidades são a procura mais rápida e eficiente de livros disponíveis e o auxílio nas datas de devolução dos mesmos ou aumento de prazo.


### 6. Lista de operações

| Nome | Descrição |
|:--- |:--- |
| Entrar no sistema | Usuários devem logar no sistema para acessar as funcionalidades relacionadas aos livros|
| Cadastro de Funcionários | Administrador do sistema mantém o cadastro dos funcionários responsáveis pelo gerenciamento dos livros |
| Gerenciamento de livros |  Funcionário mantém a relação de livros e gêneros |
| Gerenciamento da disponibilidade | Funcionário registra os livros disponíveis, modificando o status do mesmo |
| Cadastro de Clientes | Cliente deve realizar o auto cadastramento |
| Consulta de livros | Cliente consulta disponibilidade de livros, podendo fazer o empréstimo |
| Consulta de empréstimo de livros | Cliente consulta livros que pediu empréstimo, podendo marcar a devolução ou pedir aumento de prazo |
| Gerenciamento de prazos | Funcionário consulta prazos estipulados para a devolução do livro, podendo permitir o aumento de prazo por no máximo 3 vezes |

