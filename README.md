# 🌾 TheFarmerWasReplaced - Automação e Evolução Lógica 🧑‍🌾

![hq720](https://github.com/user-attachments/assets/bd92aabf-658f-4267-9392-b1beb1a60f6c)

> "Transformando o tempo de tela em código didático."

Este repositório documenta minha jornada de aprendizado em programação através da criação de scripts e automações para o jogo de simulação e gerenciamento de fazendas **TheFarmerWasReplaced**. Aqui, o jogo se torna um *sandbox* (caixa de areia) para testar lógica de programação, controle de fluxo e, acima de tudo, a arte da automação.



https://github.com/user-attachments/assets/68c927a2-dc28-4558-ab48-32d8843a25a4



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

## 📁 Estrutura dos Arquivos

A organização visa a modularidade, separando a lógica de automação da lógica de apoio (configurações e visão).

## 📚 Aprendizados e Dificuldades (O Tópico Mais Importante!)

Esta seção reflete o verdadeiro aprendizado do projeto.

### 🧠 Lógica e Soluções
* **O Desafio do *Timing*:** A maior dificuldade foi o tempo de resposta do jogo (*latency*). Solução: Introduzimos um sistema de *delays* dinâmicos no `config.py`, baseados em testes empíricos, para garantir que o script sempre esperasse o *frame* correto para a próxima ação. Isso ensinou a importância do **tratamento assíncrono** em automação.
* **Bugs de Colisão:** O personagem travava em árvores. Solução: Mapeamos rotas fixas e usamos funções de 'ajuste de rota' que adicionam um pequeno desvio lateral (`pyautogui.move(10, 0)`) antes de continuar o movimento, simulando a correção humana.

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

