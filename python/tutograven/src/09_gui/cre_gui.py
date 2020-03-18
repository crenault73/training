from tkinter import *
import webbrowser


def open_graven_channel():
    webbrowser.open("http://youtube.com/gravenilvectuto")


# Créer une première fenêtre
window = Tk()

# Personnaliser cette fenêtre
window.title("My application")
window.geometry("480x360")
window.minsize(480, 360)
window.maxsize(800, 600)
window.iconbitmap("logo.ico")
window.config(background='#2CDF85')

# Créer la Frame
# frame = Frame(window, bg='#2CDF85', bd=1, relief=SUNKEN)
frame = Frame(window, bg='#2CDF85')

# Ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur l'application", font=("Courrier", 20), bg='#2CDF85', fg='white')
label_title.pack()

# Ajouter un second texte
label_subtitle = Label(frame, text="Hey c'est Graven", font=("Courrier", 15), bg='#2CDF85', fg='white')
label_subtitle.pack()

# Ajouter un premier bouton
yt_button = Button(frame, text="Ouvrir Youtube", font=("Courrier", 15), bg='white', fg='#2CDF85',
                   command=open_graven_channel)
yt_button.pack(pady=25, fill=X)

# Ajouter la Frame
frame.pack(expand=YES)

# Afficher la fenêtre
window.mainloop()
