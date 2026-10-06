def ler_pessoais():
    print("\n--- INFORMACOES PESSOAIS ---")
    nome = input("Nome: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")
    email = input("Email: ")

    arq = open("pessoais.txt", "w")
    arq.write(nome + "\n")
    arq.write(idade + "\n")
    arq.write(cidade + "\n")
    arq.write(email + "\n")
    arq.close()


def ler_profissionais():
    print("\n--- INFORMACOES PROFISSIONAIS ---")
    objetivo = input("Objetivo profissional: ")
    curso = input("Curso: ")
    faculdade = input("Faculdade: ")

    arq = open("profissionais.txt", "w")
    arq.write(objetivo + "\n")
    arq.write(curso + "\n")
    arq.write(faculdade + "\n")

    print("Digite suas habilidades (digite 'fim' para parar)")
    habilidade = input("Habilidade: ")

    while habilidade != "fim":
        arq.write(habilidade + "\n")
        habilidade = input("Habilidade: ")

    arq.close()


def ler_idiomas():
    print("\n--- IDIOMAS ---")
    nativo = input("Idioma nativo: ")
    ingles = input("Nivel de ingles: ")
    espanhol = input("Nivel de espanhol: ")

    arq = open("idiomas.txt", "w")
    arq.write(nativo + "\n")
    arq.write(ingles + "\n")
    arq.write(espanhol + "\n")

    print("Digite outros idiomas (digite 'fim' para parar)")
    idioma = input("Outro idioma: ")

    while idioma != "fim":
        arq.write(idioma + "\n")
        idioma = input("Outro idioma: ")

    arq.close()


def gerar_html():
    pessoais = open("pessoais.txt", "r")
    profissionais = open("profissionais.txt", "r")
    idiomas = open("idiomas.txt", "r")
    html = open("curriculo.html", "w")

    nome = pessoais.readline().strip()
    idade = pessoais.readline().strip()
    cidade = pessoais.readline().strip()
    email = pessoais.readline().strip()

    objetivo = profissionais.readline().strip()
    curso = profissionais.readline().strip()
    faculdade = profissionais.readline().strip()

    idioma_nativo = idiomas.readline().strip()
    ingles = idiomas.readline().strip()
    espanhol = idiomas.readline().strip()

    html.write("""
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Currículo</title>

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #eef2f7;
        margin: 0;
        padding: 30px;
        color: #333;
    }

    .curriculo {
        max-width: 850px;
        margin: auto;
        background-color: white;
        padding: 35px;
        border-radius: 12px;
        box-shadow: 0 4px 15px #999;
    }

    .cabecalho {
        text-align: center;
        border-bottom: 3px solid #6e0606;
        padding-bottom: 20px;
    }

    .cabecalho img {
        width: 140px;
        height: 140px;
        object-fit: cover;
        border-radius: 50%;
        border: 4px solid #6e0606;
    }

    h1 {
        color: #6e0606;
        margin-bottom: 5px;
    }

    h2 {
        color: white;
        background-color: #6e0606;
        padding: 10px;
        border-radius: 6px;
        margin-top: 30px;
    }

    .informacoes {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }

    .informacao {
        background-color: #f4f6fb;
        padding: 10px;
        border-radius: 5px;
    }

    ul {
        background-color: #f4f6fb;
        padding: 15px 35px;
        border-radius: 5px;
    }

    li {
        margin: 7px;
    }

    strong {
        color: #6e0606M;
    }
</style>

</head>

<body>

<div class="curriculo">

    <div class="cabecalho">
        <img src="miles.jpg">
        <h1>""" + nome + """</h1>
        <p>Currículo Profissional</p>
    </div>

    <h2>Informações Pessoais</h2>

    <div class="informacoes">
        <div class="informacao">
            <strong>Nome:</strong> """ + nome + """
        </div>

        <div class="informacao">
            <strong>Idade:</strong> """ + idade + """
        </div>

        <div class="informacao">
            <strong>Cidade:</strong> """ + cidade + """
        </div>

        <div class="informacao">
            <strong>Email:</strong> """ + email + """
        </div>
    </div>

    <h2>Informações Profissionais</h2>

    <p><strong>Objetivo:</strong> """ + objetivo + """</p>
    <p><strong>Curso:</strong> """ + curso + """</p>
    <p><strong>Faculdade:</strong> """ + faculdade + """</p>

    <p><strong>Habilidades:</strong></p>
    <ul>
""")

    linha = profissionais.readline()

    while linha != "":
        html.write("<li>" + linha.strip() + "</li>\n")
        linha = profissionais.readline()

    html.write("""
    </ul>

    <h2>Idiomas</h2>

    <p><strong>Idioma nativo:</strong> """ + idioma_nativo + """</p>
    <p><strong>Inglês:</strong> """ + ingles + """</p>
    <p><strong>Espanhol:</strong> """ + espanhol + """</p>

    <p><strong>Outros idiomas:</strong></p>
    <ul>
""")

    linha = idiomas.readline()

    while linha != "":
        html.write("<li>" + linha.strip() + "</li>\n")
        linha = idiomas.readline()

    html.write("""
    </ul>

</div>

</body>
</html>
""")

    pessoais.close()
    profissionais.close()
    idiomas.close()
    html.close()


ler_pessoais()
ler_profissionais()
ler_idiomas()
gerar_html()
print("\nCurriculo.html criado com sucesso!")