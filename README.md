# PROJ_IA_2026_Turma44_Grupo_RESUMI.A
O RESUM.IA é uma aplicação que utiliza Inteligência Artificial para resumir vídeos do YouTube. O sistema extrai o áudio, realiza a transcrição e gera um resumo com os pontos principais, ajudando usuários a consumirem conteúdos longos de forma rápida, prática e eficiente.

PROJ_IA_2026_Turma44_Grupo_RESUMI.A

Equipe
Ingrid Ramos de Oliveira – RA 2222200879
Kauan Rodrigo Seles Nogueira – RA 2222203931
Mateus Machado Freire – RA 2222109498
Laura Pereira de Lima – RA 2224200199

Turma: 44
Curso: Ciência da Computação
Período: Noturno
Ano: 2026


Problema

Alunos e professores têm rotinas muito corridas, o que dificulta assistir conteúdos longos, como aulas e palestras. Mesmo com muito material disponível, a falta de tempo faz com que informações importantes sejam ignoradas ou não aproveitadas. Esse problema impacta principalmente quem precisa aprender ou ensinar de forma mais rápida e eficiente no dia a dia.

Abordagem de IA

A técnica utilizada é o Processamento de Linguagem Natural (NLP), que permite analisar e entender o conteúdo falado nos vídeos, identificando as partes mais relevantes para gerar resumos claros e objetivos. Essa abordagem é adequada porque transforma conteúdos longos em informações rápidas e fáceis de consumir.

Métrica principal:
Qualidade do resumo, avaliada pela precisão das informações e pelo tempo economizado pelo usuário.

Dados

Os dados são obtidos a partir de vídeos do YouTube. O sistema extrai o áudio, realiza a transcrição automática e, em seguida, gera o resumo utilizando Inteligência Artificial.

Como reproduzir:
python -m venv .venv
# Ative o ambiente virtual (Windows: .venv\Scripts\activate | Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
python src/main.py --seed 42
python -m streamlit run app.py

Estrutura do Projeto:
src/ → Código principal da aplicação
data/ → Arquivos gerados (áudios, textos)
models/ → Configurações e recursos de IA
reports/ → Resultados gerados (resumos)
notebooks/ → Testes e experimentos
app.py → Interface em Streamlit

Descrição do projeto:

RESUMI.A
Hoje em dia, tanto alunos quanto professores lidam com uma rotina muito corrida, o que dificulta assistir vídeos longos, como aulas, palestras ou conteúdos educativos. Apesar de existir muito material disponível na internet, nem sempre as pessoas têm tempo/paciência para consumir tudo. Isso acaba fazendo com que muita informação importante seja perdida ou deixada de lado. 

Pensando nisso, foi criada RESUM.IA que faz resumos de vídeos automaticamente. Ela funciona analisando o conteúdo falado no vídeo e identificando as partes mais importantes, gerando um resumo claro e direto. Para isso, utilizamos uma técnica de IA voltada para entender textos e linguagem, chamada Processamento de Linguagem Natural (NLP). Essa escolha faz sentido porque permite transformar conteúdos longos em algo mais simples e fácil de consumir, ajudando principalmente quem tem pouco tempo no dia a dia.


requirements.txt → Dependências
