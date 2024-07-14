import tkinter as tk
from tkinter import ttk
import os

def formatar_moeda(valor):
    valor_formatado = '{:,.2f}'.format(valor)
    return valor_formatado.replace('.', '_').replace(',', '.').replace('_', ',')

def formatar_milhar(valor):
    valor_formatado = '{:,.0f}'.format(valor)
    return valor_formatado.replace(',', '.')

def formatar_hora(hora):
    try:
        hora_str = str(hora)
        hora_formatada = f"{hora_str[:2]}:{hora_str[2:4]}:{hora_str[4:6]}.{hora_str[6:]}"
        return hora_formatada
    except:
        return hora

def formatar_data(data):
    try:
        ano, mes, dia = data.split('-')
        return f"{dia}-{mes}-{ano}"
    except:
        return data

mapeamento = {
    '39': 'Agora',
    '4': 'Alfa',
    '226': 'Amaril Franklin',
    '147': 'Ativa',
    '6451': 'Alfa',
    '497': 'Bradesco',
    '1026': 'BTG',
    '1116': 'Citibank',
    '833': 'Credit Suisse',
    '1123': 'Banco do Brasil',
    '252': 'Itau',
    '206': 'JP Morgan',
    '683': 'Modal',
    '2800': 'Morgan Stanley',
    '1230': 'Rabobank',
    '304': 'Safra',
    '622': 'Santander',
    '50935': 'XP',
    '1817': 'Bank of America Merrill Lynch',
    '172': 'Banrisul',
    '122': 'BGC Liquidez',
    '72': 'Bradesco',
    '85': 'BTG',
    '6003': 'C6',
    '298': 'Citibank',
    '77': 'Citigroup',
    '308': 'Clear',
    '88': 'CM Capital',
    '45': 'Credit Suisse',
    '1290': 'Deutsche Bank',
    '90': 'Easynvest',
    '174': 'Elite',
    '131': 'Fator',
    '120': 'Genial',
    '1320': 'Goldman',
    '238': 'Goldman',
    '15': 'Guide',
    '115': 'H. Commcor',
    '735': 'Icap',
    '1618': 'Ideal',
    '1099': 'Inter',
    '2446': 'Itaú',
    '2028': 'Itaú Unibanco',
    '16': 'JP Morgan',
    '106': 'Mercantil',
    '13': 'Merrill',
    '262': 'Mirae',
    '1982': 'Modal',
    '40': 'Morgan',
    '23': 'Necton',
    '93': 'Nova Futura',
    '63': 'Novinvest',
    '3701': 'Orama',
    '3142': 'Pi',
    '129': 'Planner',
    '1089': 'RB Capital',
    '92': 'Renascenca',
    '386': 'Rico',
    '59': 'Safra',
    '27': 'Santander',
    '1240': 'Scotiabank',
    '7078': 'Scotiabank',
    '1130': 'Stonex',
    '107': 'Terra',
    '4090': 'Toro',
    '127': 'Tullett',
    '8': 'UBS',
    '1855': 'Vitreo',
    '190': 'Warren',
    '3': 'XP',
    '114': 'Itaú',
    '746': 'Modal',
}

def show_table(file_path):
    def filtrar_dados():
        filtro = entry_filtro.get().upper()
        for item in tree.get_children():
            tree.delete(item)
        
        for line in lines:
            data = line.strip().split(';')
            data_original = data.copy()
            if len(data) > 5:
                data[5] = mapeamento.get(data[5], data[5])
            if len(data) > 6:
                data[6] = mapeamento.get(data[6], data[6])
            
            if any(filtro in str(col).upper() for col in data) and data[0] not in ["FNAM11", "FNOR11"]:
                inserir_linha(data_original)
    
    def inserir_linha(data):
        if len(data) > 2:
            col2 = data[1].replace(',', '.')
            col3 = data[2].replace(',', '.')
            if col2.strip().replace('.', '').isdigit() and col3.strip().replace('.', '').isdigit():
                valor_total = float(col2.strip()) * float(col3.strip())
                data.append(formatar_moeda(valor_total))
            else:
                data.append("")
        else:
            data.append("")

        if len(data) > 1:
            try:
                data[1] = '{:.2f}'.format(float(data[1].replace(',', '.'))).replace('.', ',')
            except ValueError:
                pass

        if len(data) > 2:
            try:
                data[2] = formatar_milhar(float(data[2].replace(',', '.')))
            except ValueError:
                pass

        if len(data) > 3:
            data[3] = formatar_hora(data[3])

        if len(data) > 4:
            data[4] = formatar_data(data[4])

        if len(data) > 5:
            data[5] = mapeamento.get(data[5], data[5])
        if len(data) > 6:
            data[6] = mapeamento.get(data[6], data[6])

        if len(data) > 2:
            try:
                col3_value = float(data[2].replace('.', '').replace(',', '.'))
                if col3_value >= 1000000:
                    tag = 'red'
                elif col3_value >= 750000:
                    tag = 'orange'
                elif col3_value >= 500000:
                    tag = 'yellow'
                else:
                    tag = ''
            except ValueError:
                tag = ''
        else:
            tag = ''

        tree.insert("", tk.END, values=data[:8], tags=(tag,))

    root = tk.Tk()
    root.title("Dados Filtrados")

    frame_filtro = tk.Frame(root)
    frame_filtro.pack(pady=10)

    entry_filtro = tk.Entry(frame_filtro)
    entry_filtro.pack(side=tk.LEFT, padx=5)

    btn_filtro = tk.Button(frame_filtro, text="Filtrar", command=filtrar_dados)
    btn_filtro.pack(side=tk.LEFT, padx=5)

    tree = ttk.Treeview(root)
    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    tree.heading("1", text="Ativo")
    tree.heading("2", text="Valor")
    tree.heading("3", text="Quantidade")
    tree.heading("4", text="Hora")
    tree.heading("5", text="Data")
    tree.heading("6", text="Comprador")
    tree.heading("7", text="Vendedor")
    tree.heading("8", text="Valor Total da Transação")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("1", anchor=tk.CENTER, width=100)
    tree.column("2", anchor=tk.CENTER, width=100)
    tree.column("3", anchor=tk.CENTER, width=100)
    tree.column("4", anchor=tk.CENTER, width=100)
    tree.column("5", anchor=tk.CENTER, width=100)
    tree.column("6", anchor=tk.CENTER, width=150)
    tree.column("7", anchor=tk.CENTER, width=150)
    tree.column("8", anchor=tk.CENTER, width=150)

    scroll_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_x = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

    tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    tree.tag_configure('yellow', background='yellow')
    tree.tag_configure('orange', background='orange')
    tree.tag_configure('red', background='red')

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        data = line.strip().split(';')
        if data[0] not in ["FNAM11", "FNOR11"]:
            inserir_linha(data)

    tree.pack(expand=True, fill=tk.BOTH)

    root.mainloop()

# Exemplo de uso
# Substitua 'caminho_para_seu_arquivo.txt' pelo caminho correto do seu arquivo
# show_table('caminho_para_seu_arquivo.txt')
