import tkinter as tk

class Cronometro:
    def _init_(self, root):
        self.root = root
        self.root.title("Cronômetro")
        
        self.tempo = 0
        self.rodando = False
        
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()
        
        self.iniciar_btn = tk.Button(root, text="Iniciar", command=self.iniciar)
        self.iniciar_btn.pack(side="left")
        
        self.pausar_btn = tk.Button(root, text="Pausar", command=self.pausar)
        self.pausar_btn.pack(side="left")
        
        self.retomar_btn = tk.Button(root, text="Retomar", command=self.retomar)
        self.retomar_btn.pack(side="left")
        
        self.reiniciar_btn = tk.Button(root, text="Reiniciar", command=self.reiniciar)
        self.reiniciar_btn.pack(side="left")
        
        self.atualizar_tempo()
    
    def iniciar(self):
        if not self.rodando:
            self.rodando = True
            self.atualizar_tempo()
    
    def pausar(self):
        if self.rodando:
            self.rodando = False
    
    def retomar(self):
        if not self.rodando:
            self.rodando = True
            self.atualizar_tempo()
    
    def reiniciar(self):
        self.rodando = False
        self.tempo = 0
        self.label.config(text="00:00:00")
    
    def atualizar_tempo(self):
        if self.rodando:
            self.tempo += 1
            minutos, segundos = divmod(self.tempo, 60)
            horas, minutos = divmod(minutos, 60)
            tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"
            self.label.config(text=tempo_formatado)
            self.root.after(1000, self.atualizar_tempo)

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()