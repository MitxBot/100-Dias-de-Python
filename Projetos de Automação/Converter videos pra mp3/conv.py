import subprocess
from pathlib import Path

#Função qu recebe o caminho de um arquivo de vídeo e o converte em um arquivo de áudio no formato .mp3
def conversor_video(video_path):
    video = Path(video_path)

    if not video.exists():
        print("Arquivo não encontrado.")
        return
    
    mp3= video.with_suffix(".mp3")

    comando = [
        "ffmpeg",
        "-i", str(video),
        "-vn",
        "acodec", "libmp3lame",
        "-q:a", "2",
        str(mp3)
    ]

    try:
        subprocess.run(comando, check=True)
        print(f"Conversão concluída: {mp3}")

    except subprocess.CalledProcessError:
        print("Erro durante a conversão.")

#Solicita o caminho do arquivo para o usuário e remove as aspas que o sistema operacional adiciona ao arrastar e soltar arquivos no terminal
if __name__ == "__main__":
    arquivo = input("Digite o caminho do vídeo: ").strip('"')
    conversor_video(arquivo)