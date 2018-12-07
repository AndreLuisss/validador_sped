#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
from typing import List
from lxml import objectify

arq = open('1.txt', 'r')
texto = arq.readlines()
arq.close()
notas = {}
notas1 = {}
for line in texto:
    line_split = line.split("|")
    if line_split[1] == 'C100' and line_split[2] == '0' and line_split[8] not in notas:
        notas[line_split[8]] = {
            'mod':line_split[5]
        }
    elif line_split[1] == 'C100' and line_split[2] == '0' and line_split[8] in notas and notas[line_split[8]] != line_split[5]:
        notas[line_split[8]] = {
            'mod':line_split[5],
            #'chNFe': line_split[9]
        }

for file in glob.glob('nfe_entrada/*.xml'):
    arq = open(file, 'r', encoding='utf-8')
    texto = arq.read()
    texto = texto.encode('utf-8')
    arq.close()

    nfe = objectify.fromstring(texto)
    if hasattr(nfe, 'NFe'):
        if str(nfe.NFe.infNFe.ide.nNF) not in notas1:
            notas1[str(nfe.NFe.infNFe.ide.nNF)] = {
                'mod': str(nfe.NFe.infNFe.ide.mod),
                'chNFe': nfe.protNFe.infProt.chNFe
            }
        elif str(nfe.NFe.infNFe.ide.nNF) in notas1 and notas1[str(nfe.NFe.infNFe.ide.nNF)] != str(nfe.NFe.infNFe.ide.mod):
            notas1[str(nfe.NFe.infNFe.ide.nNF)] = {
                'mod': str(nfe.NFe.infNFe.ide.mod),
                'chNFe': nfe.protNFe.infProt.chNFe
            }

if len(list(set(notas) - set(notas1))) > 0:
    print("Ta no SPED, mas não deveria esta:\n")
    for oi in list(set(notas) - set(notas1)):
        print(str(notas[oi]['chNFe']))

if len(list(set(notas1) - set(notas))) > 0:
    print("\nNão ta no SPED, mas deveria esta:")
    for oi in list(set(notas1) - set(notas)):
        print(str(notas1[oi]['chNFe']))
