from django.shortcuts import render
from lxml import objectify
from participantes.models import Participantes
from notas.models import Notas
def cadastro(request):
    arq = open('1.txt', 'r')
    texto = arq.readlines()
    arq.close()
    for line in texto:
        line_split = line.split("|")
        if line_split[1] == '0150':
            try:
                Participantes.objects.create(
                    COD_PART=line_split[2],
                    NOME=line_split[3],
                    COD_PAIS=line_split[4],
                    CNPJ=line_split[5],
                    CPF=line_split[6],
                    IE=line_split[7],
                    COD_MUN=line_split[8],
                    SUFRAMA=line_split[9],
                    END=line_split[10],
                    NUM=line_split[11],
                    COMPL=line_split[12],
                    BAIRRO=line_split[13],
                )
            except:
                print(line_split)

        if line_split[1] == 'C100':
            try:
                Notas.objects.create(
                    IND_OPER=line_split[2],
                    IND_EMIT=line_split[3],
                    COD_PART=line_split[4],
                    COD_MOD=line_split[5],
                    COD_SIT=line_split[6],
                    SER=line_split[7],
                    NUM_DOC=line_split[8],
                    CHV_NFE=line_split[9],
                    DT_DOC=line_split[10],
                    DT_E_S=line_split[11],
                    VL_DOC=line_split[12],
                    IND_PGTO=line_split[13],
                    VL_DESC=line_split[14],
                    VL_ABAT_NT=line_split[15],
                    VL_MERC=line_split[16],
                    IND_FRT=line_split[17],
                    VL_FRT=line_split[18],
                    VL_SEG=line_split[19],
                    VL_OUT_DA=line_split[20],
                    VL_BC_ICMS=line_split[21],
                    VL_ICMS=line_split[22],
                    VL_BC_ICMS_ST=line_split[23],
                    VL_ICMS_ST=line_split[24],
                    VL_IPI=line_split[25],
                    VL_PIS=line_split[26],
                    VL_COFINS=line_split[27],
                    VL_PIS_ST=line_split[28],
                    VL_COFINS_ST=line_split[29],
                )
            except ValueError as Error:
                print(line_split)
                print(Error)
    return render(request, 'cadastro/index.html', {})
