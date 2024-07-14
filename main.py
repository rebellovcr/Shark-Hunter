import tkinter as tk
from tkcalendar import Calendar
from download_and_extract_file import download_and_extract_file
from show_table_gui import show_table

def create_gui():
    global cal

    root = tk.Tk()
    root.title("Shark Hunter")

    cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(padx=10, pady=10)

    btn_download = tk.Button(root, text="Obter dados", command=lambda: download_and_extract_file(cal))
    btn_download.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
