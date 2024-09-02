# Nao encontrei o json ou xml que era para ser usado

import random

def create_faturamentos():
    out = []

    for dia in range(1, 31):
        if dia in (6, 7, 13, 14, 20, 21, 27, 28): # finais de semana
            out.append(0)
        else:
            out.append(random.random() * random.randint(1e3, 1e6))

    out[11] = 0 # simular feriado

    return out

def main():
    faturamentos = create_faturamentos()
    min, max = faturamentos[0], faturamentos[0]
    dias_do_mes = 0
    for faturamento in faturamentos:
        if (faturamento != 0):
            dias_do_mes += 1
            if (faturamento < min):
                min = faturamento
            elif (faturamento > max):
                max = faturamento

    faturamento_medio = sum(faturamentos) / dias_do_mes
    dias_maior_faturamento_medio = 0
    for faturamento in faturamentos:
        if faturamento != 0 and faturamento > faturamento_medio:
            dias_maior_faturamento_medio += 1

    print(f'Menor faturamento {min}')
    print(f'Maior faturamento {max}')
    print(f'Numero de dias com faturamento maior do que a media mensal {dias_maior_faturamento_medio}')

main()