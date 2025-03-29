import re
import os
def replace_comma_with_dot_in_numbers(file_path):
    """
    Substitui vírgulas entre números por pontos em um arquivo (modificação in-place).
    Equivalente a: sed -i 's/\([0-9]\),\([0-9]\)/\1.\2/g' file_path
    
    Args:
        file_path (str): Caminho para o arquivo a ser modificado
    """
    # Expressão regular para encontrar vírgulas entre dígitos
    pattern = re.compile(r'(\d),(\d)')
    
    # Criar um arquivo temporário para as modificações
    temp_file_path = file_path + '.tmp'
    
    with open(file_path, 'r', encoding='utf-8') as input_file, \
         open(temp_file_path, 'w', encoding='utf-8') as output_file:
        
        for line in input_file:
            # Substituir todas as ocorrências do padrão
            modified_line = pattern.sub(r'\1.\2', line)
            output_file.write(modified_line)
    
    # Substituir o arquivo original pelo temporário
    os.replace(temp_file_path, file_path)

years = ['2023', '2024']
ts = ['1T', '2T', '3T', '4T']
for year in years:
    for t in ts:
        replace_comma_with_dot_in_numbers(f'files/{t}{year}.csv')