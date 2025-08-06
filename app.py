from tkinter import Tk, filedialog, messagebox, simpledialog
from excel_utils import div_gerente, load_email
from relatorio_utils import send_email

def interface():
    root = Tk()
    root.withdraw()
    messagebox.showinfo('Automatizador de relatórios', 'Selecione o arquivo excel tratado')
    arquivo = filedialog.askopenfilename(filetypes=[('Arquivos Excel', '*.xlsx')])

    if not arquivo:
        messagebox.showwarning('Atenção', 'nenhum arquivo selecionado')
        return
    
    endereco_email = load_email(arquivo)
    assinatura = simpledialog.askstring('Assinatura', 'Digite seu nome para assinar o e-mail')

    try:
        arquivo_gerado = div_gerente(arquivo)
        send_email(arquivo_gerado, endereco_email, assinatura)
        messagebox.showinfo('Sucesso', 'Arquivos gerados e e-mails enviados com sucesso')
    except Exception as e:
        messagebox.showerror('Erro', str(e))

if __name__ == '__main__':
    interface()