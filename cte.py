#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
from lxml import objectify


def formatdate(date):
    date = date.split('T')
    date = date[0].split('-')
    date = date[2]+date[1]+date[0]
    return date


sped = dict()
part_list = []
cte_list = []

arq = open('1.txt', 'r')
texto = arq.readlines()
for line in texto:
    line_split = line.split("|")
    if line_split[1] not in sped:
        sped[line_split[1]] = []
    sped[str(line_split[1])].append(line)
arq.close()

for file in glob.glob('cte/*.xml'):
    arq = open(file, 'r')
    texto = arq.read()
    texto = texto.encode('utf-8')
    arq.close()

    cte = objectify.fromstring(texto)
    participante = "|0150|" + str(cte.cteProc.CTe.infCte.emit.CNPJ) + "|" + \
        str(cte.cteProc.CTe.infCte.emit.xNome) + "|" + "1058|" + \
        str(cte.cteProc.CTe.infCte.emit.CNPJ) + "||" + \
        str(cte.cteProc.CTe.infCte.emit.IE) + "|" + \
        str(cte.cteProc.CTe.infCte.emit.enderEmit.cMun) + "||" + \
        str(cte.cteProc.CTe.infCte.emit.enderEmit.xLgr) + "|" + \
        str(cte.cteProc.CTe.infCte.emit.enderEmit.nro) + "|"

    if hasattr(cte.cteProc.CTe.infCte.emit.enderEmit, 'xCpl'):
        participante = participante + str(cte.cteProc.CTe.infCte.emit.enderEmit.xCpl) + "|"
    else:
        participante = participante + "|"
    participante = participante + str(cte.cteProc.CTe.infCte.emit.enderEmit.xBairro) + "|"
    sped['0150'].append(participante)
