import tkinter as tk
from tkinter import ttk, messagebox

# Inicialização das variáveis globais de votos
totalA = 0
totalB = 0

def contabilizar_votos():
    global totalA, totalB

    try:
        votosA = int(entry_votosA.get()) if entry_votosA.get() else 0
        votosB = int(entry_votosB.get()) if entry_votosB.get() else 0
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor numérico válido.")
        return

    totalA += votosA
    totalB += votosB

    totalGeral = totalA + totalB
    percentualA = (totalA / totalGeral * 100) if totalGeral > 0 else 0
    percentualB = (totalB / totalGeral * 100) if totalGeral > 0 else 0

    # Atualização dos labels de resultados
    label_totalA.config(text=f"Total de Votos do Candidato A: {totalA}")
    label_totalB.config(text=f"Total de Votos do Candidato B: {totalB}")
    label_totalGeral.config(text=f"Total de Votos Geral: {totalGeral}")
    label_percentualA.config(text=f"Percentual de Votos do Candidato A: {percentualA:.2f}%")
    label_percentualB.config(text=f"Percentual de Votos do Candidato B: {percentualB:.2f}%")

    # Atualização das barras de progresso e labels de porcentagem
    barraA['value'] = percentualA
    barraB['value'] = percentualB
    barraA_label.config(text=f"{percentualA:.2f}%")
    barraB_label.config(text=f"{percentualB:.2f}%")

    # Limpar entradas
    entry_votosA.delete(0, tk.END)
    entry_votosB.delete(0, tk.END)

# Configuração da janela principal
window = tk.Tk()
window.title("Sistema de Votação")
window.geometry("450x550")
window.configure(bg="#C0FF02")

# Título
title = tk.Label(window, text="Sistema de Votação", font=("Arial", 20, "bold"), bg="#C0FF02", fg="#333")
title.pack(pady=15)

# Input Votos A
frame_votosA = tk.Frame(window, bg="#C0FF02")
frame_votosA.pack(pady=8)
label_votosA = tk.Label(frame_votosA, text="Votos para o Candidato A:", font=("Arial", 12), bg="#C0FF02")
label_votosA.pack(side=tk.LEFT)
entry_votosA = tk.Entry(frame_votosA, font=("Arial", 12), width=8)
entry_votosA.pack(side=tk.LEFT)

# Input Votos B
frame_votosB = tk.Frame(window, bg="#C0FF02")
frame_votosB.pack(pady=8)
label_votosB = tk.Label(frame_votosB, text="Votos para o Candidato B:", font=("Arial", 12), bg="#C0FF02")
label_votosB.pack(side=tk.LEFT)
entry_votosB = tk.Entry(frame_votosB, font=("Arial", 12), width=8)
entry_votosB.pack(side=tk.LEFT)

# Botão Contabilizar
button = tk.Button(window, text="Contabilizar Votos", font=("Arial", 12, "bold"), bg="#007bff", fg="white", command=contabilizar_votos)
button.pack(pady=15)

# Resultados
label_resultados = tk.Label(window, text="Resultados:", font=("Arial", 18, "bold"), bg="#C0FF02", fg="#333")
label_resultados.pack()

label_totalA = tk.Label(window, text="Total de Votos do Candidato A: 0", font=("Arial", 12, "bold"), bg="#C0FF02", fg="#00A53e")
label_totalA.pack()

label_totalB = tk.Label(window, text="Total de Votos do Candidato B: 0", font=("Arial", 12, "bold"), bg="#C0FF02", fg="#006Abf")
label_totalB.pack()

label_totalGeral = tk.Label(window, text="Total de Votos Geral: 0", font=("Arial", 12, "bold"), bg="#C0FF02", fg="#828200")
label_totalGeral.pack()

label_percentualA = tk.Label(window, text="Percentual de Votos do Candidato A: 0%", font=("Arial", 12, "bold"), bg="#C0FF02", fg="#00A53e")
label_percentualA.pack()

label_percentualB = tk.Label(window, text="Percentual de Votos do Candidato B: 0%", font=("Arial", 12, "bold"), bg="#C0FF02", fg="#006Abf")
label_percentualB.pack()

# Gráfico de Barras
frame_grafico = tk.Frame(window, bg="#e0e0e0")
frame_grafico.pack(pady=20)

# Barra Candidato A
barraA = ttk.Progressbar(frame_grafico, orient='horizontal', length=150, mode='determinate', style="A.Horizontal.TProgressbar")
barraA.pack(side=tk.LEFT, padx=5)
barraA_label = tk.Label(frame_grafico, text="0%", font=("Arial", 10), bg="#4CAF50", fg="white")
barraA_label.pack(side=tk.LEFT, padx=5)

# Barra Candidato B
barraB = ttk.Progressbar(frame_grafico, orient='horizontal', length=150, mode='determinate', style="B.Horizontal.TProgressbar")
barraB.pack(side=tk.LEFT, padx=5)
barraB_label = tk.Label(frame_grafico, text="0%", font=("Arial", 10), bg="#2196F3", fg="white")
barraB_label.pack(side=tk.LEFT, padx=5)

# Estilos das barras de progresso
style = ttk.Style()
style.configure("A.Horizontal.TProgressbar", troughcolor="#d0d0d0", background="#4CAF50")
style.configure("B.Horizontal.TProgressbar", troughcolor="#d0d0d0", background="#2196F3")

# Loop principal da interface
window.mainloop()
