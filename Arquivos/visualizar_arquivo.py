import os
pasta_padrao = r'C:/Users/felip/Downloads'

def visualizar_arquivo(filename):
    # Concatena a pasta padrão com o nome do arquivo
    filepath = os.path.join(pasta_padrao, filename)
    
    if os.path.exists(filepath):
        if filepath.endswith('.txt'):
            with open(filepath, 'r') as f:
                conteudo = f.read()
                print(conteudo)
        elif filepath.endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4')):
            os.startfile(filepath)  # No Windows
        else:
            print("Tipo de arquivo não suportado.")
    else:
        print("Arquivo não encontrado.")

nome_arquivo = input("Insira o nome do seu arquivo: ")
visualizar_arquivo(nome_arquivo)
