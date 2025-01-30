import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('exemplo.xml')
root = tree.getroot()

print(ET.tostring(root))

# ‹projetos empresa="Pytax" Canal="Pytax">
# ‹projeto›Sistema de cadastro</projeto>
# • ‹projeto›Sistema de Gerenciamento </projeto>
# -• ‹ projeto>Curos de Pyside2</projeto>
# ‹projeto>Automatiza&#231;&#227;o do sap</projeto>
# ‹projeto›Sistema Gerador de DCTF</projeto>
# </projetos>

for desc in tree.findall("projeto"):
   print(desc.text)
   
# Sistema de cadastro
# Sistema de Gerenciamento
# Curos de Pyside2
# Automatização do sap
# Sistema Gerador de DCTF

# incluindo id
for id, projeto in enumerate(tree.findall("projeto")):
   projeto.set('id', str(id))

tree.write ("exemplo.xm1")

# ‹projetos empresa="Pytax" Canal="Pytax"›
# ‹projeto id="0"›Sistema de cadastro‹/projeto >
# ‹projeto id="1"›Sistema de Gerenciamento </projeto>
# ‹projeto id="2"›Curos de Pyside2</projeto>
# ‹projeto id="3">Automatiza&#231;&#227;0 do sap</projeto>
# ‹projeto id="4"›Sistema Gerador de DCTF</projeto >
# </projetos>

# alterando a descrição do id = 2
descricao = tree.find('projeto[@id="2"]').text
print(descricao)
# Curos de Pyside2

# deletando o id
for proj in tree.findall("projeto"):
   del(proj.attrib['id'])
   
# escrevendo uma tag
proj = ET.Element("projeto")
proj.text = "Jogo super senha"
root.append(proj)
tree.write("exemplo.xml")

# ‹projetos empresa="Pytax" Canal="Pytax"›

# ‹projeto›Sistema de cadastro‹/projeto>
# ‹projeto›Sistema de Gerenciamento </projeto>
# ‹projeto>Curos de Pyside2</projeto>
# ‹projeto>Automatiza&#231;&#227;o do sap</projeto>
# ‹projeto›Sistema Gerador de DCTF</projeto>

# ‹projeto>Jogo super senha‹/projeto/projetos>

# Alterando a Tag
projeto = ET.fromstring("<projeto> Jogo de perguntas e respostas </projeto>")
root.append(projeto)
tree.write("exemplo.xml")

# ‹projetos empresa="Pytax" Canal="Pytax">

# ‹projeto›Sistema de cadastro‹/projeto>
# ‹projeto›Sistema de Gerenciamento </projeto>
# ‹projeto>Curos de Pyside2</projeto>
# ‹projeto>Automatiza&#231;&#227;o do sap</projeto>
# ‹projeto›Sistema Gerador de DCTF</projeto>

# ‹projeto›Jogo super senha‹/projeto><projeto› Jogo de perguntas e respostas

# ===================================================================================

root = ET.parse("Nfe mod 55.xm]").getroot()
nsNFE = {'ns': "http://www.portalfiscal.inf.br/nfe" }

numero_nfe = root.find('ns:NFe/ns: infNFe/ns: ide/ns:nNF', nSNFE)
print(numero_nfe.text)

print(chave.attrib['Id'][3:])

# <nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">
# v<NFe xmlns="http://www.portalfiscal.inf.br/nfe">
# v<infNFe versao="4.00" Id="NFe31200870940994008277550200000398481382207964">
# 7<ide>
# <cUF>31</cUF›
# <CNF>38220796</cNF>
# ‹natOp>Vnd mer.adq.rec.ter.op.mer.sj.rg.sub.trb.cnd.sub.t</natOp>
# <mod>55</mod>
# <serie>20</serie›
# <nNF>39848</nNF>
# <dhEmi >2020-08-23T13:46:16-03:00</dhEmi>
# <tpNF>1</tpNF>

numero_do_item = root.find('ns:NFe/ns: infNFe/ns: det', nSNFE)
print(numero _do_item.attrib)
print(numero_do_item.attrib['nItem'])
# {'nItem': '1'}

# outra forma de fazer
xm1 = open("Nfe mod 55. xml")
nfe = minidom.parse(xml)

num_nfe = nfe-getElementsByTagName('nNF')
print(num_nfe[0].firstChild.data)
# 39848

# </dest>
# 7 <det nItem="1"›
# • <prod>
# ...
# </prod>
# v< imposto>
# 7 <ICMS>
# 7 <ICMS10>
# <orig>5</orig>
# <CST>10</CST>
# <modBC>3</modBC>
# <vBC>3795.24</vBC>
# <pICMS>12.0000</pICMS>
# <vICMS>455.43</vICMS>
# <modBCST>4</modBCST>
# <pMVAST>40.4600</pMVAST>
# <vBCST>5330.79</vBCST>
# <pICMSST>12.0000</pICMSST>
# <VICMSST>184.27</vICMSST>
# </ICMS10>
# </ICMS>

num_nfe = nfe.getElementsByTagName('nNF')
print(num_nfe[0].firstChild.data)

itens = nfe.getElementsByTagName('det')
cod_produto = nfe.getElementsByTagName('cProd')

for i in itens:
   print(i.attributes['nItem'].value)

for p in cod_produto:
   print(p.firstchild.data)

# 000000000040002062
# 000000000040002383
# 0000000 040002064
# 000000000040001932
# 000000000040001933
# 000000000040000068
# 000000000040002063
# 000000000040000082
# 000000000040000397
# 000000000040000499

# ===================================================================================

import xmltodict Mesa - Local

with open("moedas.xml", "rb") as arquivo_moedas:
   dic_moedas = xmltodict.parse(arquivo_moedas)

moedas = dic_moedas["xml"]
print (moedas)

# ===================================================================================

from xml.dom import minidom

with open("original.xml", 'r', encoding='utf-8') as f:
   xml = minidom-parse(f)
   nome = xml.getElementsByTagName("primeiro")

   for tag in nome:
      print(tag.firstchild.data)
      
# {'empresa': 'Pytax', 'Canal': 'Pytax'}

tree.write("exemplo.xml")

# <‹ projetos empresa="Pytax"- Canal="Pytax"›

# ‹projeto›Sistema de cadastro‹/projeto>
# ‹projeto>Sistema de Gerenciamento </projeto>
# ‹projeto>Curos de Pyside2</projeto>
# ‹projeto>Automatiza&#231;&#227;0 do sap</projeto >
# ‹projeto›Sistema Gerador de DCTF</projeto>
# </projetos>

inf = root-get ("Canal")
print(f"o nome do canal é: {inf]")

# o nome do canal é: Pytax

# ===================================================================================

import xml.etree.ElementTree as ET
tree = ET.parse('exemplo.xml')
root = tree-getroot()

print(ET.tostring(root))

# b'‹projetos empresa="Pytax"> \n\n ‹projeto›Sistema de cadastro</projeto>\n
# ‹ projeto›Sistema de Gerenciamento </projeto>\n ‹projeto>Curos de
# Pyside2</projeto>\n <projeto>Automatiza&#231;&#227;o do sap</projeto>\n
# ‹projeto›Sistema Gerador de DCTF</projeto> In\n</projetos>*

for desc in tree.findall("projeto"):
   print(desc.text)

# Sistema de cadastro
# Sistema de Gerenciamento

# Curos de Pyside2
# Automatização do sap
# Sistema Gerador de DCTF

# ===================================================================================

tree = ET.parse("exemplo_1.xml")
root = tree.getroot()

for desc in tree.findall(".//descricao"):
   print(desc.text)
   
# ‹! --Todos os dados são meramente ilustrativos--›

# ‹BPQL>
# ‹header specialResourceUse="0" resourceUse="®"›
# < date-time>17/10/2021 05:16:59</date-time>
# ‹ description>TJSE - Consulta Procesual por Número Único‹/descriptio
# </header>

# < body>
# ‹processo>
# ‹ classe>Acompanhamento de Cumprimento de Decisão‹/classe>
# ‹ situacao>ANDAMENTO</ situacao>
# ‹distribuicao format="d/m/Y" raw-format="d/m/Y" raw-value="31/01/20
# ‹juizo>3ª Vara Criminal de Socorro</juizo>
# < fase>EM CUMPRIMENTO</fase>
# ‹assunto>DIREITO PENAL - Crimes Previstos na Legislação Extravagant

# ‹partes>
# ‹parte tipo="Réu" polo="Passivo"›Carlos Luiz Ferreira Lobato‹/parte
# </partes>
# ‹andamentos>
# ‹andamento categoria-"Outros">
# ****************************************‹ descricao›Um documento ou petição protocolizado anteriormente na
# ‹data hash="308f2d6b271e944e961eba4b5ced92c0" format="d/m/Y" raw-fo
# ‹desc› Juntada realizada por Ministério Público Estadual, através do
# ‹ tipo_movimento>Juntada‹/tipo_movimento>
# ‹rotuloMovimento>Uma petição protocolizada anteriormente na Vara,
# ‹/ andamento>
# ‹andamento categoria="Outros">
# «descricao›Indica ocorrências diversas no processo. - - Intimação
# ‹data hash="052f9858ff87ed448e1f9ab79f9700a3" format="d/m/Y" raw-fo
# ‹ desc› Intimação considerada em 13/10/2021, mediante ciência e consi

for id, desc in enumerate(tree.findall(".//descricao")) :
   desc.set('id', str(id))

tree.write("exemplo_1 xm1")

# < body>
# ‹processo>
# ‹Classe>Acompanhamento de Cumprimento de Decis&#227;0</classe>
# ‹ situacao>ANDAMENTO</ situacao>
# «distribuicao format="d/m/Y" raw-format="d/m/Y" raw-value="31/01/
# <juizo>3&#170; Vara Criminal de Socorro‹/juizo >
# < fase>EM CUMPRIMENTO</ fase>
# ‹assunto>DIREITO PENAL - Crimes Previstos na Legisla&#231;&#227;0

# ‹partes>
# ‹parte tipo="R&#233;u" polo="Passivo"›Carlos Luiz Ferreira Lobato
# </partes>
# ‹andamentos>
# ‹andamento catego ="Outros" >
# ****************************************************‹descricao id="®"›Um documento ou peti&#231;&#227;0 protocolizado
# <data hash="308f2d6b271e944e961eba4b5ced92c0" format="d/m/Y" raw-
# ‹desc>Juntada realizada por Minist&#233;rio P&#250;blico Estadual
# ‹ tipo_movimento>Juntada</tipo_movimento>
# ‹rotuloMovimento>Uma peti&#231;8#227;0 protocolizada anteriorment
# ‹/ andamento>
# ‹andamento categoria="Outros"›
# ‹descricao id="1">Indica ocorr&#234;ncias diversas no processo. -
# ‹data hash="052f9858ff87ed448e1f9ab79f9700a3" format="d/m/Y" raw-
# ‹desc> Intima&#231;&#227;0 considerada em 13/10/2021, mediante ci&
# ‹ tipo_movimento>Outras Informa&#231;&#245;es</tipo_movimento>
# ‹ rotuloMovimento>Nenhum gloss&#225;rio definido</rotuloMovimento>
# </ andamento>
# ‹andamento categoria="Outros">
# «descricao id="2"›Quando a intima&#231;&#227;0 &#233; enviada atr
# ‹data hash="5d68596d2e9ad6b7ddbb5270df3f1310" format="d/m/Y" raw-
# ‹desc›Ante o teor das certid&#245;es de p. 49 e 52, emitidas pela

descricao = tree.find('.//descricao[@id="0"]').text
print(descricao)

# Um documento ou petição protocolizado anteriormente a Vara, agora está efetivamente
# incluído no processo. -|- Juntada realizada por Ministério Público Estadual, através
# do Serviço de Intercomunicação - MNI no dia 13/10/2021 às 17:39:23. '