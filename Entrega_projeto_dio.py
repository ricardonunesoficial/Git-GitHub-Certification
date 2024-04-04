# Recebe a URL do repositório como entrada
repository_url = input()

# Escreve o comando Git para clonar o repositório
git_command = f"git clone {repository_url}"

# Imprime o comando Git seguido da URL do repositório recebida como entrada
print(git_command)

# Exemplos de URLs
urls = [
    "https://github.com/digitalinnovationone/js-developer-pokedex",
    "https://github.com/alinealien/desafio-github-markdown",
    "https://github.com/digitalinnovationone/dio-lab-open-source",
    "https://github.com/elidianaandrade/dio-curso-git-github"
]

# Imprime o comando Git para cada URL com uma mensagem personalizada
for url in urls:
    git_command = f"git clone {url}"
    if "alinealien" in url:
        print(f"{git_command} - Desafio de Markdown por Aline Alien")
    elif "digitalinnovationone" in url:
        print(f"{git_command} - Projeto da Digital Innovation One")
    elif "elidianaandrade" in url:
        print(f"{git_command} - Curso de Git e GitHub por Elidiana Andrade")
    else:
        print(git_command)