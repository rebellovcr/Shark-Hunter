def filter_and_process_data(file_path):
    # Abrir arquivo para leitura
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filtered_lines = []

    # Processar cada linha do arquivo
    for line in lines:
        # Dividir a linha em colunas usando ponto e vírgula como delimitador
        columns = line.strip().split(';')

        # Verificar se a quinta coluna contém um número válido e é >= 100000
        if len(columns) > 4 and columns[4].strip().isdigit():
            if int(columns[4].strip()) >= 100000:
                # Remover a 1ª, 3ª, 7ª e 8ª coluna
                filtered_columns = [columns[i] for i in range(len(columns)) if i not in [0, 2, 6, 7]]
                filtered_line = ';'.join(filtered_columns)
                filtered_lines.append(filtered_line + '\n')

    # Escrever as linhas filtradas de volta no arquivo, substituindo o original
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)
