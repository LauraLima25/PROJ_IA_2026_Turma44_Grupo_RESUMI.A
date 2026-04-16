import streamlit as st

st.set_page_config(page_title="RESUM.IA", layout="wide")

st.title("🤖 IA que resume QUALQUER video do YouTube")

import os
import yt_dlp
import subprocess
from openai import OpenAI

client = OpenAI(api_key="sua chave")

FFMPEG_PATH = r"C:colque seu caminho"

---------------- FUNÇÕES ----------------

def baixar_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        arquivo = ydl.prepare_filename(info)  
        print(f"Áudio baixado: {arquivo}")    
        return arquivo


def cortar_trecho(input_file, inicio, duracao, output):
    comando = [
        FFMPEG_PATH,
        "-ss", str(inicio),
        "-i", input_file,
        "-t", str(duracao),
        "-y",
        output
    ]
    subprocess.run(comando, capture_output=True)
    return output

def transcrever(caminho):
    with open(caminho, "rb") as f:
        resp = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=f
        )
    return resp.text

def resumir(texto):
    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Resuma de forma clara e completa, capturando os principais pontos do vídeo."},
            {"role": "user", "content": texto}
        ],
        max_tokens=800
    )
    return resp.choices[0].message.content

# ---------------- INTERFACE ----------------

url = st.text_input("🎥 Cole o link do YouTube")

if st.button("🚀 Processar vídeo") and url:
    with st.spinner("Baixando áudio..."):
        arquivo = baixar_audio(url)

    if arquivo:
        trechos = [
            (0, 300),       # início
            (600, 300),     # 10 min
            (1800, 300),    # 30 min
            (3600, 300),    # 1h
        ]

        textos = []

        for i, (inicio, duracao) in enumerate(trechos):
            nome = f"parte_{i}.mp3"

            with st.spinner(f"Processando trecho {i+1}..."):
                cortar_trecho(arquivo, inicio, duracao, nome)
                texto = transcrever(nome)
                textos.append(texto)

            os.remove(nome)

        with st.spinner("Gerando resumo final..."):
            resumo = resumir(" ".join(textos))

        st.subheader("📄 Resumo:")
        st.write(resumo)

        os.remove(arquivo)
