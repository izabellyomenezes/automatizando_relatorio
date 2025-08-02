import yagmail

def send_email(arquivo_gerado, dicionario_email, email, senha, assinatura):
    yag = yagmail.SMTP(email, senha)

    for gerente, arquivo in arquivo_gerado.items():
        if gerente in dicionario_email:
            destinatario = dicionario_email[gerente]
            assunto = f'Relatório da sua loja - {gerente}'
            corpo = f'Olá {gerente}, \n\nSegue em anexo o seu relatório. \n\nAtenciosamente,\n{assinatura}'
            yag.send(
                to=destinatario,
                subject=assunto,
                contents=corpo,
                attachments=arquivo
            )
            print(f'Email enviado para {gerente}')
        else:
            print(f'[AVISO] E-mail não encontrado para {gerente}, e-mail não enviado')