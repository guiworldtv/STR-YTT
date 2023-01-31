import glob
import os

# Obter o caminho do arquivo atual
file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_path)

# Verificar se o arquivo LISTASAGRUPADAS.m3u8 já existe
file_to_merge = "LISTASAGRUPADAS.m3u8"
if os.path.exists(file_to_merge):
    try:
        os.remove(file_to_merge)
    except OSError as e:
        print("Erro ao excluir o arquivo: ", e)
else:
    print("O arquivo {} não existe".format(file_to_merge))

# Obter todos os arquivos .m3u na pasta
source_files = glob.glob("*.m3u")

# Imprimir a lista de arquivos encontrados
print("Arquivos encontrados:", source_files)

# Abrir o arquivo de saída para escrita
with open(file_to_merge, "wb") as merged_file:
    for file in source_files:
        try:
            # Adicionar uma linha em branco entre cada arquivo
            merged_file.write(b"\n")
            
            # Abrir o arquivo de entrada para leitura
            with open(file, "rb") as source_file:
                # Copiar o conteúdo do arquivo de entrada para o arquivo de saída
                merged_file.write(source_file.read())
        except IOError as e:
            print("Erro ao processar o arquivo: ", file, e)
