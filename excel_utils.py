import pandas as pd

def div_gerente(arquivo):
    df = pd.read_excel(arquivo)
    if 'Gerente' not in df.columns:
        raise ValueError('A coluna "Gerente" não está presente na planilha')
    
    gerentes = df['Gerente'].unique()
    arquivo_gerado = {}

    for gerente in gerentes:
        grupo = df[df['Gerente'] == gerente]
        nome_arquivo = f'{gerente.replace(' ', '_')}.xlsx'
        grupo.to_excel(nome_arquivo, index=False)
        arquivo_gerado[gerente] = nome_arquivo
    return arquivo_gerado

def load_email(arquivo):
    df_email = pd.read_excel(arquivo, sheet_name='email_gerente')
    if 'Gerente' not in df_email.columns or 'Email' not in df_email.columns:
        raise ValueError('A planilha "email_gerente" deve conter as colunas "Gerente" e "Email"')
    return dict(zip(df_email['Gerente'], df_email['Email']))