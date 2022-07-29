import speech_recognition as sr
from tkinter import *
from tkinter import ttk

import tkinter.messagebox
from tkinter.messagebox import showinfo

root = Tk()
img=PhotoImage(file= r'C:\Users\ww\Desktop\Speech to text for Debates\logo.png')
root.iconphoto(False, img)
root.title('Debate speech recognition')

root.geometry("625x600")

# Создание основного фрейма // Create A Main Frame
main_frame = Frame(root,width=625,height=600)
main_frame.place(x=0,y=0)

# Создание канваса // Create A Canvas
my_canvas = Canvas(main_frame, width=625, height=200)
my_canvas.place(x=0,y=0)

# Добавление скроллинга в канвас // Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.place(x=605,y=0,height=600)

# Настройка канваса // Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# Создание ДРУГОГО фрейма в канвасе // Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas,width=625,height=500)
second_frame.place(x=0,y=0)

# Добавление нового фрейма в окно канваса // Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")


# Основная программа // Main Program

r = sr.Recognizer()

language="languagecode"


def converting():
   
    with sr.Microphone() as source:
        print("Скажите что-нибудь (Speak something): ")
        audio = r.listen(source, phrase_time_limit=450)

        response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        text = r.recognize_google(audio,language="ru-RU")
        response["transcription"] = text
        print("Вы сказали (You said): {}".format(text))

        
        for i in range(len(text)):
            outcome[i].configure(text=text)
            outcome[i].pack()

    except sr.RequestError:
        response["success"] = False
        response["error"] = print(tkinter.messagebox.showerror("Ошибка", "Извините, что-то пошло не так, запустите программу снова. Напоминание: начинайте говорить только после того, как программа включила микрофон."))
    except sr.UnknownValueError:
        response["error"] = print(tkinter.messagebox.showerror("Ошибка", "Извините, что-то пошло не так, запустите программу снова. Напоминание: начинайте говорить только после того, как программа включила микрофон."))

    return response



button = Button(root,text="Запустить",command=converting, 
bg='gray11', fg='white', height=2, width=10, font=('Time 13 bold'), activebackground='gray51',
    activeforeground='white')
button.pack(pady=20)

outcome = []
outcome.append(Label(second_frame, text=str,  font=('Comic Sans', 16), justify='center',  wraplength=450))


root.mainloop()




