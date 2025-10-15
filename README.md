# 🌾 TheFarmerWasReplaced - Automação e Evolução Lógica 🧑‍🌾

> "Transformando o tempo de tela em código didático."

Este repositório documenta minha jornada de aprendizado em programação através da criação de scripts e automações para o jogo de simulação e gerenciamento de fazendas **TheFarmerWasReplaced**. Aqui, o jogo se torna um *sandbox* (caixa de areia) para testar lógica de programação, controle de fluxo e, acima de tudo, a arte da automação.

## 🚀 Objetivos e O Que Este Repositório Oferece

O principal objetivo é utilizar a repetição e a lógica do jogo para solidificar conceitos de programação, provando que o aprendizado pode ser divertido e prático.

### O Que Você Encontra Aqui:
* **Scripts Modulares:** Funções limpas para automatizar tarefas repetitivas (plantio, rega, movimentação).
* **Estudos de Lógica:** Como resolvemos os desafios de *timing* e *pathfinding* (caminhamento) do jogo.
* **Documentação Didática:** Explicações claras de como e por que cada automação funciona.
* **Evidência de Evolução:** Um registro de como a complexidade dos scripts evoluiu à medida que novos desafios surgiram.

## 🧩 O Jogo: TheFarmerWasReplaced

TheFarmerWasReplaced é um jogo de simulação de fazenda onde o jogador deve gerenciar recursos, tempo e tarefas para restaurar uma fazenda em declínio.

| Aspecto | Detalhe |
| :--- | :--- |
| **Contexto** | Você substituiu o fazendeiro original e deve provar seu valor. |
| **Objetivo** | Otimizar a produção da fazenda, gerenciar recursos e progredir. |
| **Desafio Central** | **Gestão de Tempo.** Cada ação deve ser calculada para maximizar o rendimento em um ciclo de tempo limitado. |

---

## 💻 Tecnologias Utilizadas

A escolha da tecnologia dependeu da necessidade de interagir com o sistema operacional e simular ações de usuário.

| Tecnologia | Finalidade |
| :--- | :--- |
| **Python** | Linguagem principal para o desenvolvimento dos scripts de automação. |
| **`pyautogui` / `pynput`** | Para simular inputs de teclado e mouse, interagindo diretamente com o jogo. |
| **`OpenCV` (Opcional)** | Para visão computacional simples, ajudando o script a "ver" a tela e tomar decisões (ex: reconhecer o ícone de 'inventário cheio'). |
| **Markdown** | Para a documentação clara e rica deste `README`. |

## 📁 Estrutura dos Arquivos

A organização visa a modularidade, separando a lógica de automação da lógica de apoio (configurações e visão).

## ⚙️ Como Executar os Códigos

Para replicar os testes de automação, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o Python instalado e as bibliotecas necessárias.
    ```bash
    pip install pyautogui pynput opencv-python  # Se for usar todas
    ```
2.  **Configuração do Jogo:**
    * O jogo deve estar em modo janela ou em uma resolução fixa para que as coordenadas de automação não sejam perdidas.
    * As teclas de atalho (*keybindings*) configuradas no jogo devem coincidir com as definidas no arquivo `config.py`.
3.  **Execução:**
    ```bash
    # A partir da pasta raiz
    python scripts/rotina_diaria.py
    ```
    ⚠️ **ATENÇÃO:** Mantenha o mouse e teclado livres enquanto o script estiver rodando, pois ele irá controlar o cursor e os inputs.

## 📸 Automação em Ação: Prova de Conceito

*Aqui você inserirá screenshots e gifs. As legendas a seguir são sugestões.*

### Exemplo 1: Otimizando o Plantio

**< insira um GIF aqui mostrando o personagem plantando em linha reta e voltando para pegar mais sementes >**

**Legenda Sugerida:** A função `automatizacao_colheita` em ação. O script utiliza loops para garantir que cada quadrado de solo arado receba uma semente, minimizando os passos desnecessários. Isso demonstra o poder dos **loops sequenciais** na prática.

### Exemplo 2: Diagrama de Fluxo de Decisão

**< insira um diagrama de blocos simples aqui >**

**Legenda Sugerida:** Nosso diagrama de fluxo para a função `checar_e_regar()`. O script primeiro verifica (IF/ELSE) se o item atual na mão é o regador e se o solo está seco (através de coordenadas de pixel). Uma demonstração clara do **controle de fluxo**.

---

## 📚 Aprendizados e Dificuldades (O Tópico Mais Importante!)

Esta seção reflete o verdadeiro aprendizado do projeto.

### 🧠 Lógica e Soluções
* **O Desafio do *Timing*:** A maior dificuldade foi o tempo de resposta do jogo (*latency*). Solução: Introduzimos um sistema de *delays* dinâmicos no `config.py`, baseados em testes empíricos, para garantir que o script sempre esperasse o *frame* correto para a próxima ação. Isso ensinou a importância do **tratamento assíncrono** em automação.
* **Bugs de Colisão:** O personagem travava em árvores. Solução: Mapeamos rotas fixas e usamos funções de 'ajuste de rota' que adicionam um pequeno desvio lateral (`pyautogui.move(10, 0)`) antes de continuar o movimento, simulando a correção humana.

### 🛠️ Exemplo de Debug

**< insira um print de tela do console com um erro comum (ex: `KeyError` ou `IndexError`) >**

**Legenda Sugerida:** Erro de `KeyError`: o script tentou interagir com uma tecla não mapeada. **A correção:** Adicionamos um bloco `try/except` ao redor de todos os comandos de *input* para garantir que o *script* não falhe completamente, mas sim tente a próxima ação.

---

## ⭐ Contribua com o Projeto

Gostou do que viu? O aprendizado é colaborativo!

Se você encontrou uma maneira mais eficiente de realizar alguma rotina, melhorou o *pathfinding* ou tem uma ideia de nova automação, fique à vontade para contribuir!

1.  **Fork** o repositório.
2.  Crie uma *branch* para sua funcionalidade (`git checkout -b feature/minha-nova-automacao`).
3.  Faça o *commit* das suas alterações (`git commit -m 'feat: Adiciona automação de pesca'`).
4.  Faça o *push* para a *branch* (`git push origin feature/minha-nova-automacao`).
5.  Abra um **Pull Request**!

---

### Ícones e Cores
* Use a cor verde ($`\color{green}{\text{green}}$) e tons de marrom/terra (dourado/laranja) para remeter à temática da fazenda.
* **Emojis Sugeridos:**
    * `⚙️` - Configurações, Execução
    * `🌾` - Fazenda, Colheita
    * `💻` - Tecnologia
    * `🧠` - Lógica, Aprendizado
    * `🐛` - Bugs, Dificuldades

---

