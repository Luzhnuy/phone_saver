from tkinter import *
import json

phone_list = {"items" : {}, }

file = open("phones.json", "r")
file_text = file.read()
file.close()

if file_text == "":
    file = open("phones.json", "w")
    file.write(json.dumps(phone_list))
    file.close()


def save_func(event):
    file = open("phones.json", "r")
    items = file.read()
    items = json.loads(items)
    file.close()
    username = name.get()
    phone = phone_number.get()
    items['items'][username] = phone
    file = open("phones.json", "w")
    file.write(json.dumps(items))
    file.close()
    label['text'] = "Saved"

def watch_func(event):
    file = open("phones.json", "r")
    all_phones = file.read()
    file.close()
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