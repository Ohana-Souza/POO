from tkinter import Tk
from telas import Tela_Inicial

def main():
    root = Tk()
    root.title("Contagem de Carboidratos")
    root.geometry("400x400")
    Tela_Inicial(root)
    root.mainloop()

if __name__ == "__main__":
    main()
