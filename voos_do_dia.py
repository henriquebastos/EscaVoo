#Falta terminar de padronizar se deixa as outras anvs da formação com "" ou repete horário, código de chamada e área.

import re

isolado1 = ['10:00Z', 'ISOLADO 01', '01:00', 'BAR', '01FT001', 'Texto livre', 'STA']
isolado2 = ['10:30Z', 'ISOLADO 02', '01:00', 'BAR', '01FT002', 'Texto livre', 'AAA', 'BBB']
elemento1 = ['11:00Z', 'ELEMENTO 01', '01:00', 'BAR', '02FT001', 'Texto livre', 'CCC', '01:00', '02FT001', 'Texto livre', 'DDD']
elemento2 = ['11:30Z', 'ELEMENTO 02', '01:00', 'BAR', '02FT002', 'Texto livre', 'EEE', 'FFF', '01:00', '02FT002', 'Texto livre', 'GGG']
elemento3 = ['12:00Z', 'ELEMENTO 03', '01:00', 'BAR', '02FT003', 'Texto livre', 'HHH', '01:00', '02FT003', 'Texto livre', 'III', 'JJJ']
elemento4 = ['12:30Z', 'ELEMENTO 04', '01:00', 'BAR', '02FT004', 'Texto livre', 'KKK', 'MMM', '01:00', '02FT004', 'Texto livre', 'LLL', 'NNN']
trilento1 = ['13:00Z', 'TRILENTO 01', '00:40', 'OCE', '03FT001', 'Texto livre', 'AAA', '00:40', '03FT001', 'Texto livre', 'BBB', '01:00', '03FT001', 'Texto livre', 'CCC']
trilento2 = ['13:30Z', 'TRILENTO 02', '00:40', 'OCE', '03FT002', 'Texto livre', 'AAA', 'DDD', '00:40', '03FT002', 'Texto livre', 'BBB', '00:40', '03FT002', 'Texto livre', 'CCC']
trilento3 = ['14:00Z', 'TRILENTO 03', '00:40', 'OCE', '03FT003', 'Texto livre', 'AAA', '00:40', '03FT003', 'Texto livre', 'BBB', 'DDD', '00:40', '03FT003', 'Texto livre', 'CCC']
trilento4 = ['14:30Z', 'TRILENTO 04', '00:40', 'OCE', '03FT004', 'Texto livre', 'AAA', 'DDD', '00:40', '03FT004', 'Texto livre', 'BBB', 'EEE', '00:40', '03FT004', 'Texto livre', 'CCC']
esquadrilha1 = ['15:00Z', 'ESQUADRILHA 01', '01:10', 'SAICA', '04FT001/16FT001', 'Texto livre', 'AAA', '01:10', '04FT001/16FT001', 'Texto livre', 'BBB', '01:10', '04FT001/16FT001', 'Texto livre', 'CCC', '01:10', '04FT001/16FT001', 'Texto livre', 'DDD']
esquadrilha2 = ['15:30Z', 'ESQUADRILHA 02', '01:10', 'SAICA', '04FT002/16FT002', 'Texto livre', 'AAA', 'EEE', '01:10', '04FT002/16FT002', 'Texto livre', 'BBB', '01:10', '04FT002/16FT002', 'Texto livre', 'CCC', '01:10', '04FT002/16FT002', 'Texto livre', 'DDD']
esquadrilha3 = ['16:00Z', 'ESQUADRILHA 03', '01:10', 'SAICA', '04FT003/16FT003', 'Texto livre', 'AAA', 'EEE', '01:10', '04FT003/16FT003', 'Texto livre', 'BBB', 'FFF', '01:10', '04FT003/16FT003', 'Texto livre', 'CCC', '01:10', '04FT003/16FT003', 'Texto livre', 'DDD']
cinco1 = ['16:30Z', 'CINCO 01', '02:00', 'AB-CD', '05FT001', 'Texto livre', 'AAA', '02:00', '05FT001', 'Texto livre', 'BBB', '02:00', '05FT001', 'Texto livre', 'CCC', '02:00', '05FT001', 'Texto livre', 'DDD', '02:00', '05FT001', 'Texto livre', 'EEE']
cinco2 = ['17:30Z', 'CINCO 02', '02:00', 'AB-CD', '05FT002', 'Texto livre', 'AAA', '02:00', '05FT002', 'Texto livre', 'BBB', '02:00', '05FT002', 'Texto livre', 'CCC', '02:00', '05FT002', 'Texto livre', 'DDD', '02:00', '05FT002', 'Texto livre', 'EEE', 'FFF']
seis1 = ['18:30Z', 'SEIS 01', '01:30', 'ABCDE', '06FT001', 'Texto livre', 'AAA', '01:30', '06FT001', 'Texto livre', 'BBB', '01:30', '06FT001', 'Texto livre', 'CCC', '01:30', '06FT001', 'Texto livre', 'DDD', '01:30', '06FT001', 'Texto livre', 'EEE', '01:30', '06FT001', 'Texto livre', 'FFF']
seis2 = ['18:30Z', 'SEIS 01', '01:30', 'ABCDE', '06FT002', 'Texto livre', 'AAA', '01:30', '06FT002', 'Texto livre', 'BBB', '01:30', '06FT002', 'Texto livre', 'CCC', '01:30', '06FT002', 'Texto livre', 'DDD', '01:30', '06FT002', 'Texto livre', 'EEE', '01:30', '06FT002', 'Texto livre', 'FFF', 'GGG']
sete1 = ['19:00Z', 'SETE 01', '01:30', 'ABCDE', '07FT001', 'Texto livre', 'AAA', '01:30', '07FT001', 'Texto livre', 'BBB', '01:30', '07FT001', 'Texto livre', 'CCC', '01:30', '07FT001', 'Texto livre', 'DDD', '01:30', '07FT001', 'Texto livre', 'EEE', '01:30', '07FT001', 'Texto livre', 'FFF', '01:30', '07FT001', 'Texto livre', 'GGG']
oito1 = ['19:30Z', 'OITO 01', '01:30', 'ABCDE', '08FT001', 'Texto livre', 'AAA', '01:30', '08FT001', 'Texto livre', 'BBB', '01:30', '08FT001', 'Texto livre', 'CCC', '01:30', '08FT001', 'Texto livre', 'DDD', '01:30', '08FT001', 'Texto livre', 'EEE', '01:30', '08FT001', 'Texto livre', 'FFF', '01:30', '08FT001', 'Texto livre', 'GGG', '01:30', '08FT001', 'Texto livre', 'HHH']


print('isolado = ', len(isolado1), len(isolado2))
print('elemento = ', len(elemento1), len(elemento2), len(elemento3), len(elemento4))
print('trilento = ', len(trilento1), len(trilento2), len(trilento3), len(trilento4))
print('esquadrilha = ', len(esquadrilha1), len(esquadrilha2), len(esquadrilha3))
print('cinco = ', len(cinco1), len(cinco2))
print('seis = ', len(seis1), len(seis2))
print('sete = ', len(sete1))
print('oito = ', len(oito1))

total_dia = [isolado1, isolado2, elemento1, elemento2, elemento3, elemento4, trilento1, trilento2, trilento3, trilento4, esquadrilha1,
             esquadrilha2, esquadrilha3, cinco1, cinco2, seis1, seis2, sete1, oito1]

total_anvs = []

for i in total_dia:
    if len(i) < 11:
        # define o voo de apenas 1 aeronave
        if re.match(r'[A-Z]{3}', i[-2]): # checa se a aeronave tem 2 pilotos
            total_anvs.append(i)
        else:
            i.append('') # insere campo em branco para nacele traseira
            total_anvs.append(i)

    elif len(i) < 15:
        # define o voo de 2 aeronaves
        if re.match(r'[A-Z]{3}', i[7]): # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            anv2 = i[8:]

        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            anv2 = i[7:]

        anv2.insert(0, "")
        anv2.insert(0, "")
        anv2.insert(3, "")
        if re.match(r'[A-Z]{3}', anv2[-2]): # checa se a segunda aeronave tem 2 pilotos
            total_anvs.append(anv2)
        else:
            anv2.append('')
            total_anvs.append(anv2)

    elif len(i) < 19:
        # define o voo de 3 aeronaves
        if re.match(r'[A-Z]{3}', i[7]): # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            resto = i[8:]
        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            resto = i[7:]

        resto.insert(0, "")
        resto.insert(0, "")
        resto.insert(3, "")
        if re.match(r'[A-Z]{3}', resto[7]): # checa se a segunda aeronave tem 2 pilotos
            anv2 = resto[:8]
            total_anvs.append(anv2)
            anv3 = resto[8:]
        else:
            anv2 = resto[:7]
            anv2.append('')
            total_anvs.append(anv2)
            anv3 = resto[7:]

        anv3.insert(0, "")
        anv3.insert(0, "")
        anv3.insert(3, "")
        if re.match(r'[A-Z]{3}', anv3[-2]):  # checa se a terceira aeronave tem 2 pilotos
            total_anvs.append(anv3)
        else:
            anv3.append('')
            total_anvs.append(anv3)

    elif len(i) < 23:
        # define o voo de 4 aeronaves
        if re.match(r'[A-Z]{3}', i[7]): # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            resto = i[8:]
        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            resto = i[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]): # checa se a segunda aeronave tem 2 pilotos
            anv2 = resto[:8]
            total_anvs.append(anv2)
            resto = resto[8:]
        else:
            anv2 = resto[:7]
            anv2.append('')
            total_anvs.append(anv2)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]): # checa se a terceira aeronave tem 2 pilotos
            anv3 = resto[:8]
            total_anvs.append(anv3)
            anv4 = resto[8:]
        else:
            anv3 = resto[:7]
            anv3.append('')
            total_anvs.append(anv3)
            anv4 = resto[7:]

        anv4.insert(0, anv1[1])
        anv4.insert(0, anv1[0])
        anv4.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', anv4[-2]):  # checa se a quarta aeronave tem 2 pilotos
            total_anvs.append(anv4)
        else:
            anv4.append('')
            total_anvs.append(anv4)

    elif len(i) < 27:
        # define o voo de 5 aeronaves
        if re.match(r'[A-Z]{3}', i[7]):  # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            resto = i[8:]
        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            resto = i[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]):  # checa se a segunda aeronave tem 2 pilotos
            anv2 = resto[:8]
            total_anvs.append(anv2)
            resto = resto[8:]
        else:
            anv2 = resto[:7]
            anv2.append('')
            total_anvs.append(anv2)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]):  # checa se a terceira aeronave tem 2 pilotos
            anv3 = resto[:8]
            total_anvs.append(anv3)
            resto = resto[8:]
        else:
            anv3 = resto[:7]
            anv3.append('')
            total_anvs.append(anv3)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]):  # checa se a quarta aeronave tem 2 pilotos
            anv4 = resto[:8]
            total_anvs.append(anv4)
            anv5 = resto[8:]
        else:
            anv4 = resto[:7]
            anv4.append('')
            total_anvs.append(anv4)
            anv5 = resto[7:]

        anv5.insert(0, anv1[1])
        anv5.insert(0, anv1[0])
        anv5.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', anv5[-2]):  # checa se a quinta aeronave tem 2 pilotos
            total_anvs.append(anv5)
        else:
            anv5.append('')
            total_anvs.append(anv5)

    elif len(i) < 31:
        # define o voo de 6 aeronaves
        if re.match(r'[A-Z]{3}', i[7]):  # checa se a primeira aeronave tem 2 pilotos
            anv1 = i[:8]
            total_anvs.append(anv1)
            resto = i[8:]
        else:
            anv1 = i[:7]
            anv1.append('')
            total_anvs.append(anv1)
            resto = i[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]):  # checa se a segunda aeronave tem 2 pilotos
            anv2 = resto[:8]
            total_anvs.append(anv2)
            resto = resto[8:]
        else:
            anv2 = resto[:7]
            anv2.append('')
            total_anvs.append(anv2)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]):  # checa se a terceira aeronave tem 2 pilotos
            anv3 = resto[:8]
            total_anvs.append(anv3)
            resto = resto[8:]
        else:
            anv3 = resto[:7]
            anv3.append('')
            total_anvs.append(anv3)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]):  # checa se a quarta aeronave tem 2 pilotos
            anv4 = resto[:8]
            total_anvs.append(anv4)
            resto = resto[8:]
        else:
            anv4 = resto[:7]
            anv4.append('')
            total_anvs.append(anv4)
            resto = resto[7:]

        resto.insert(0, anv1[1])
        resto.insert(0, anv1[0])
        resto.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', resto[7]):  # checa se a quinta aeronave tem 2 pilotos
            anv5 = resto[:8]
            total_anvs.append(anv5)
            anv6 = resto[8:]
        else:
            anv5 = resto[:7]
            anv5.append('')
            total_anvs.append(anv5)
            anv6 = resto[7:]

        anv6.insert(0, anv1[1])
        anv6.insert(0, anv1[0])
        anv6.insert(3, anv1[3])
        if re.match(r'[A-Z]{3}', anv6[-2]):  # checa se a sexta aeronave tem 2 pilotos
            total_anvs.append(anv6)
        else:
            anv6.append('')
            total_anvs.append(anv6)



for i in total_anvs:
    print(i)

for i in total_anvs:
    print(len(i))

print(len(total_anvs))