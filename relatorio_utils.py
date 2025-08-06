import win32com.client as win32
import os

def send_email(arquivo_gerado, dicionario_email, assinatura):
    outlook = win32.Dispatch('outlook.application')

    for gerente, arquivo in arquivo_gerado.items():
        if gerente in dicionario_email:
            try:
                destinatario = dicionario_email[gerente]
                mail = outlook.CreateItem(0)
                mail.To = destinatario
                mail.Subject = f'Relatório da sua loja {gerente}'
                mail.Body = f'Olá {gerente}, \n\nSegue em anexo o seu relatório. \n\nAtenciosamente, \n{assinatura}'
                mail.Attachments.Add(os.path.abspath(arquivo))
                mail.Send()
                print(f'Email enviado para {gerente}')
            except Exception as e:
                print(f'[ERRO] Falha ao enviar e-mail para {gerente}: {e}')
        else:
            print(f'[AVISO] E-mail não encontrado para {gerente}, e-mail não enviado')