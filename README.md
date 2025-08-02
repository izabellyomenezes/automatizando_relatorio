# Automatizador de Relatórios por Gerente
Este projeto automatiza a divisão de um relatório Excel por gerente e envia os arquivos resultantes para seus respectivos e-mails. Ele utiliza `pandas` para manipulação de dados, `yagmail` para envio de e-mails e `tkinter` para interface gráfica de seleção do arquivo.

## Funcionalidades
- Divide automaticamente um arquivo Excel por gerente (coluna `Gerente`).
- Lê e-mails de uma aba chamada `email_gerente` no mesmo arquivo.
- Envia cada relatório individual por e-mail.
- Interface gráfica para seleção do arquivo.
- Preparado para ser transformado em um executável com `PyInstaller`.

## Estrutura do Projeto
```
📦automatizador_relatorios
 ┣ 📄 app.py              # Arquivo principal que executa a interface
 ┣ 📄 processamento.py    # Funções de processamento (dividir arquivo, envio de e-mails)
 ┣ 📄 README.md           # Este arquivo
```

## Requisitos
- Python 3.x
- Bibliotecas:
  - pandas
  - yagmail
  - openpyxl
  - tkinter (já vem com o Python)
  - smtplib (biblioteca padrão)

Instale os pacotes com:

```bash
pip install pandas yagmail openpyxl
```

## Estrutura esperada do Excel
- **Planilha principal**: deve conter uma coluna chamada `Gerente`.
- **Planilha `email_gerente`**:
  - Coluna A: Nome do Gerente (igual ao da planilha principal)
  - Coluna B: E-mail do gerente

## Como usar
1. Execute o app com:
```bash
python app.py
```
2. Selecione o arquivo Excel com os dados.
3. O sistema solicitará seu Login e Senha do Email
  - Gere uma nova senha (apenas para essa situação), acessando 'https://myaccount.google.com/apppasswords'.
  - Em caso de não ter ativado a verificação de duas etapas, o passo anterior não funcionará, confirme a verificação em 'https://myaccount.google.com/security'.
4. O sistema irá gerar arquivos separados e enviar para os e-mails encontrados.

## Gerando um executável (.exe)
Para criar um executável com o PyInstaller:
1. Instale o PyInstaller:
```bash
pip install pyinstaller
```
2. Gere o executável:
```bash
pyinstaller --onefile app.py
```
O executável estará disponível na pasta `dist`.

> **Dica:** Se usar interface gráfica (Tkinter), adicione o argumento `--noconsole` para esconder o terminal:
```bash
pyinstaller --onefile --noconsole app.py
``