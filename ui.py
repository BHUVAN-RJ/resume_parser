from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import ttk
import nlp_parser
import threading
import os


win = Tk()
win.geometry("700x350")

style=ttk.Style(win)
list_of_shortlisted_candidates = {}
folder_path = ""
file_select = Frame(win)
text_input = Frame(win)
final_output = Frame(win)
skills_needed = []

shortlisted_candidates = {}

def open_win_diag():
    global folder_path
    folder_path = askdirectory(initialdir="")


def change_to_input_text():
    text_input.pack(fill='both', expand=1)
    file_select.pack_forget()


def change_to_final_output():
    final_output.pack(fill='both', expand=1)
    text_input.pack_forget()


def skills_extract_from_text():
    global skills_needed
    entered_skills = entry.get()
    skills_needed = entered_skills.split(",")


def nlp_extractor():
    global list_of_shortlisted_candidates
    resumes_folder_open = os.listdir(folder_path)
    for item in resumes_folder_open:
        current_doc = f"{folder_path}/{item}"
        number_and_skills = nlp_parser.extract_text_and_parse(skills_needed, current_doc)
        extracted_skills = number_and_skills[1]
        phone_number = number_and_skills[0]
        if len(extracted_skills) <= 0:
            continue
        list_of_shortlisted_candidates[item] = extracted_skills, phone_number
    scroll_x = Scrollbar(final_output)
    scroll_x.pack(side=RIGHT, fill=Y)

    scroll_y = Scrollbar(final_output, orient='horizontal')
    scroll_y.pack(side=BOTTOM, fill=X)
    content = ttk.Treeview(final_output, yscrollcommand=scroll_x.set, xscrollcommand=scroll_y.set)

    # content = ttk.Treeview(final_output,yscrollcommand=scroll_x.set, xscrollcommand =scroll_y.set)
    # content.pack()
    content["columns"] = ('PDF_NAME', 'PHONE', 'EXTRACTED_SKILLS')

    content.column("#0", width=0, stretch=NO)
    content.column("PDF_NAME", anchor=CENTER, width=80)
    content.column("PHONE", anchor=CENTER, width=80)
    content.column("EXTRACTED_SKILLS", anchor=CENTER, width=80)

    content.heading("#0", text="No.", anchor=CENTER)
    content.heading("PDF_NAME", text="PDF_NAME", anchor=CENTER)
    content.heading("PHONE", text="PHONE", anchor=CENTER)
    content.heading("EXTRACTED_SKILLS", text="EXTRACTED_SKILLS", anchor=CENTER)
    i = 0
    for key, value in list_of_shortlisted_candidates.items():
        i += 1
        content.insert("", "end", text=key, values=(i, key, list_of_shortlisted_candidates[key][0], list_of_shortlisted_candidates[key][1]))
    content.pack()
def get_result():
    global shortlisted_candidates
    shortlisted_candidates = nlp_extractor()


def label_update():
    file_path_show_label.config(text=folder_path)


label = Label(file_select, text= "Click the button to browse the file", font='Arial 15 bold')
label.pack(pady=20)
file_path_show_label = Label(file_select, text= "File path", font='Arial 15 bold')
file_path_show_label.pack(pady=20)

button1 = ttk.Button(file_select, text="Select folder", command=lambda:[open_win_diag(), label_update()])
button1.pack(pady=5)
button2 = ttk.Button(file_select, text="Next", command=change_to_input_text)
button2.pack(pady=5)

label=Label(text_input, text="Enter the keywords you need for shortlisting\n(NOTE:separate each skill with a comma "
                             "\",\"):", font="Courier 22 bold")
label.pack()
entry = Entry(text_input, width=40)
entry.focus_set()
entry.pack()

button3 = ttk.Button(text_input, text="Parse", command=lambda: [change_to_final_output(), skills_extract_from_text(), get_result()])
button3.pack(pady=5)

label=Label(final_output, text="Shortlisted Resumes", font="Courier 22 bold")
label.pack()

# label=Label(final_output, text="Shortlisted Resumes", font="Courier 22 bold")
# label.pack()

file_select.pack(fill='both', expand=1)
win.mainloop()