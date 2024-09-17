import os

def visualizar_arquivo(filepath):
    if os.path.exists(filepath):
        if filepath.endswith('.txt'):
            with open(filepath, 'r') as f:
                conteudo = f.read()
                print(conteudo)
        elif filepath.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            os.system(f'xdg-open {filepath}')  # No Linux
        elif filepath.endswith('.mp4'):
            os.system(f'xdg-open {filepath}')  # No Linux
        else:
            print("Tipo de arquivo não suportado.")
    else:
        print("Arquivo não encontrado.")

nome_arquivo = input("Insira o nome do seu arquivo: ")
visualizar_arquivo(nome_arquivo)
