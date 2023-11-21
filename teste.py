import pathlib

# Defina o diretório que você deseja verificar
a = pathlib.Path("./dataset brasileiro/TREINO/output")

# Use o método glob() para listar todos os arquivos no diretório
arquivos_na_pasta = list(a.glob("*/*.png"))
arquivos_na_pasta2 = list(a.glob("*/*.jpg"))
arquivos_na_pasta3 = list(a.glob("*/*.jpeg"))

# Use a função len() para contar o número de arquivos
numero_de_arquivos = len(arquivos_na_pasta) + len(arquivos_na_pasta2) + len(arquivos_na_pasta3)

# Exiba o número de arquivos
print(f"Número de arquivos na pasta: {numero_de_arquivos}")