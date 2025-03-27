from PIL import Image
from tkinter import Tk, filedialog
import threading

def processar_faixa(imagem, imagem_pb, inicio, fim):
    
    largura, _ = imagem.size
    for y in range(inicio, fim):
        for x in range(largura):
            r, g, b = imagem.getpixel((x, y))
            luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_pb.putpixel((x, y), luminancia)

def converter_para_preto_e_branco():
    try:
        root = Tk()
        root.withdraw()
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )
        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem).convert("RGB")
        largura, altura = imagem.size
        imagem_pb = Image.new("L", (largura, altura))
        
        num_threads = 4  # Numero de threads
        faixas = [(altura * i // num_threads, altura * (i + 1) // num_threads) for i in range(num_threads)]
        
        threads = [threading.Thread(target=processar_faixa, args=(imagem, imagem_pb, inicio, fim)) for inicio, fim in faixas]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )
        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return
        
        imagem_pb.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")
    
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Exemplo de uso

if __name__ == "__main__":
    converter_para_preto_e_branco()
