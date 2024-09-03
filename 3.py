import json
import xml.etree.ElementTree as ET

def info_faturamento(faturamentos):
    min, max = float('inf'), float('-inf')
    dias_do_mes = 0
    faturamento_total = 0
    for faturamento in faturamentos:
        if (faturamento['valor'] != 0):
            dias_do_mes += 1
            faturamento_total += faturamento['valor']
            if (faturamento['valor'] < min):
                min = faturamento['valor']
            elif (faturamento['valor'] > max):
                max = faturamento['valor']

    faturamento_medio = faturamento_total / dias_do_mes
    dias_maior_faturamento_medio = 0
    for faturamento in faturamentos:
        if faturamento['valor'] > faturamento_medio:
            dias_maior_faturamento_medio += 1

    print(f'Menor faturamento {min}')
    print(f'Maior faturamento {max}')
    print(f'Numero de dias com faturamento maior do que a media mensal {dias_maior_faturamento_medio}')

def main():
    with open('dados.json') as data:
        dados_json = json.load(data)

    tree = ET.parse('dados.xml')
    root = tree.getroot()
    dados_xml = []
    for row in root:
        full_data = {}
        for data in row:
            full_data[data.tag] = float(data.text)
        dados_xml.append(full_data)

    print('Para o arquivo dados.json')
    info_faturamento(dados_json)

    print('Para o arquivo dados.xml')
    info_faturamento(dados_xml)

main()