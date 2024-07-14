import requests
import os
import zipfile
from datetime import datetime
from tkinter import messagebox
from filter_and_process_data import filter_and_process_data
import show_table_gui

def download_and_extract_file(cal):
    selected_date_str = cal.get_date()
    messagebox.showinfo("Shark Hunter", "Aguarde, processando....")

    try:
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d')
        
        if selected_date.weekday() in (5, 6):
            raise ValueError("Não é possível selecionar fins de semana.")

        if selected_date > datetime.now():
            raise ValueError("Não é possível selecionar datas futuras.")
        
        url_date_format = selected_date.strftime("%Y-%m-%d")
        formatted_date = selected_date.strftime('%d-%m-%Y')
    except ValueError as e:
        messagebox.showerror("Erro", f"Selecione uma data válida. {str(e)}")
        return

    current_directory = os.getcwd()
    zip_file_path = os.path.join(current_directory, f"{url_date_format}_NEGOCIOSAVISTA.zip")
    expected_txt_filename = f'{formatted_date}'
    extracted_file_path = os.path.join(current_directory, expected_txt_filename + "_NEGOCIOSAVISTA.txt")

    if os.path.exists(extracted_file_path):
        messagebox.showinfo("Arquivos Já Existentes", "Os arquivos já existem no diretório. Nenhum download necessário.")
        process_and_show_table(extracted_file_path)
        return

    url = f"https://arquivos.b3.com.br/apinegocios/tickercsv/{url_date_format}"

    response = requests.get(url)
    if response.status_code == 200:
        with open(zip_file_path, 'wb') as f:
            f.write(response.content)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(current_directory)

        os.remove(zip_file_path)

        # Aplicar filtro e remover colunas
        filter_and_process_data(extracted_file_path)
        messagebox.showinfo("Shark Hunter", "Download concluído com sucesso.")
        process_and_show_table(extracted_file_path)
    else:
        messagebox.showerror("Erro de Download", "Falha ao baixar o arquivo. Verifique a data selecionada e tente novamente.")

def process_and_show_table(extracted_file_path):
    show_table_gui.show_table(extracted_file_path)
