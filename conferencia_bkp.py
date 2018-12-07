#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
from lxml import objectify

arq = open('1.txt', 'r')
emitente = {}
participantes = {}
texto = arq.readlines()
notas = {}
arq.close()
for line in texto:
    line_split = line.split("|")
    if line_split[1] == '0005':
        emitente['FANTASIA'] = line_split[2]
        emitente['CEP'] = line_split[3]
        emitente['END'] = line_split[4]
        emitente['NUM'] = line_split[5]
        emitente['COMPL'] = line_split[6]
        emitente['BAIRRO'] = line_split[7]
        emitente['FONE'] = line_split[8]
        emitente['FAX'] = line_split[9]
        emitente['EMAIL'] = line_split[10]

    if line_split[1] == '0150':
        if line_split[5] not in participantes:
            participantes[line_split[5]] = {}
        else:
            print("O Participante {0} com cnpj {1} esta duplicado no "
                  "arquivo txt, corrija para dar continuidade".format(line_split[3], line_split[5]))

        participantes[line_split[5]]['COD_PART'] = line_split[2]
        participantes[line_split[5]]['NOME'] = line_split[3]
        participantes[line_split[5]]['COD_PAIS'] = line_split[4]
        participantes[line_split[5]]['CNPJ'] = line_split[5]
        participantes[line_split[5]]['CPF'] = line_split[6]
        participantes[line_split[5]]['IE'] = line_split[7]
        participantes[line_split[5]]['COD_MUN'] = line_split[8]
        participantes[line_split[5]]['SUFRAMA'] = line_split[9]
        participantes[line_split[5]]['END'] = line_split[10]
        participantes[line_split[5]]['NUM'] = line_split[11]
        participantes[line_split[5]]['COMPL'] = line_split[12]
        participantes[line_split[5]]['BAIRRO'] = line_split[13]

    if line_split[1] == 'C100':
        notas['IND_OPER'] = line_split[1]
        notas['IND_EMIT'] = line_split[1]
        notas['COD_PART'] = line_split[1]
        notas['COD_PART'] = line_split[1]
        notas['COD_MOD'] = line_split[1]
