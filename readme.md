# 🐍 Python Hangman Game (Jogo da Forca)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

Este é um projeto de **Jogo da Forca** desenvolvido em Python, focado em lógica estruturada e tratamento de dados via terminal (CLI). O projeto demonstra práticas de validação de entrada, manipulação de strings e controle de fluxo.

## 🚀 Funcionalidades

* **Validação de Input:** O sistema rejeita números ou caracteres especiais, permitindo apenas letras (A-Z) através do método `.isalpha()`.
* **Chute Direto:** O jogador pode tentar adivinhar a palavra completa.
* **Mecânica de Derrota Instantânea:** Caso o jogador tente chutar a palavra completa e erre, o jogo é encerrado imediatamente (Game Over).
* **Interface Visual:** Evolução da forca em arte ASCII conforme o número de erros.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Biblioteca:** `random` (para o sorteio das palavras)
* **Editor:** Visual Studio Code

## 📋 Como Executar

1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `forca.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python forca.py
