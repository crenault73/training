from tkinter import *
import webbrowser

def open_yt():
    webbrowser.open_new("https://www.youtube.com/channel/UCIHVyohXw6j2T-83-uLngEg")
#Créer une premiere fenetre

window = Tk()

#Personaliser la fenetre
window.title("My Application")
window.geometry("480x360")
window.minsize(480, 360)
window.maxsize(800, 600)
#window.iconbitmap("A.ico")
window.config(background='#f3bdf3')
#Creer la frame
frame = Frame(window, bg='#f3bdf3')

#Ajouter un premier text
label_title = Label(frame, text="Bienvenue sur l'application", font=("Courrier", 20), bg='#f3bdf3', fg='white')
label_title.pack()

label_subtitle = Label(frame, text="Hello à tous !", font=("Courrier", 15), bg='#f3bdf3', fg='white')
label_subtitle.pack()

#Ajouter un premier bouton

yt_button = Button(frame, text="Ouvrir youtube", font=("Courrier", 15), bg='white', fg='#f3bdf3', command=open_yt)
yt_button.pack(pady=10, fill=X)
#Ajouter une FRame
frame.pack(expand=YES)

# Afficher

window.mainloop()
