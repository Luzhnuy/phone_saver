from tkinter import *
import json

def read():
    file = open("phones.json", "r")
    file_text = file.read()
    file.close()
    return file_text

def write(data):
    file = open("phones.json", "w")
    file.write(json.dumps(data))
    file.close()

phone_list = {"items" : {}, }

file_text = read()

if file_text == "":
    write(phone_list)


def save_func(event):
    items = read()
    items = json.loads(items)
    username = name.get()
    phone = phone_number.get()
    items['items'][username] = phone
    write(items)
    label['text'] = "Saved"

def watch_func(event):
    all_phones = read()
    all_phones = json.loads(all_phones)['items']
    str = ""
    for name in all_phones:
        str+= "\n" + name + " : " + all_phones[name]
    label['text'] = str


root = Tk()
phone_number = Entry(width=30)
name = Entry(width=30)
save = Button(width=40, bg="grey", text="Save")
watch = Button(width=40, bg="grey", text="watching all phones")
label = Label(width=40, bg="white", fg="black")

save.bind("<Button-1>", save_func)
watch.bind("<Button-1>", watch_func)

phone_number.pack()
name.pack()
save.pack()
watch.pack()
label.pack()
root.mainloop()