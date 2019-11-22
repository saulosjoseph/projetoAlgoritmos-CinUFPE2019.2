#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Saulo Joseph"
__version__ = "0.1.0"
__license__ = "MIT"

import csv
import candidato
import lista
import bem
import cronometro
import time

class controle():
    def __init__(self):
        self.__lista_de_candidatos = lista.DoublyLinkedList()
        self.__lista_de_bens = lista.DoublyLinkedList()
        self.__lista_de_candidatos_uf = lista.DoublyLinkedList()
        self.__lista_de_candidatos_partido = lista.DoublyLinkedList()
        self.__lista_de_candidato_nao_eleito = lista.DoublyLinkedList()
        self.__lista_de_candidato_eleito = lista.DoublyLinkedList()
        self.__lista_de_candidato_valor = lista.DoublyLinkedList()
        self.__lista_de_candidato_cargo = lista.DoublyLinkedList()
        self.__lista_de_candidato_cidade = lista.DoublyLinkedList()

    def get_lista_de_candidatos_uf(self):
        return self.__lista_de_candidatos_uf

    def get_lista_de_candidatos_partido(self):
        return self.__lista_de_candidatos_partido
    
    def get_lista_de_candidato_nao_eleito(self):
        return self.__lista_de_candidato_nao_eleito

    def get_lista_de_candidato_eleito(self):
        return self.__lista_de_candidato_eleito

    def get_lista_de_candidato_valor(self):
        return self.__lista_de_candidato_valor

    def get_lista_de_candidato_cargo(self):
        return self.__lista_de_candidato_cargo

    def get_lista_de_candidato_cidade(self):
        return self.__lista_de_candidato_cidade
    
    
    def carregar_candidatos(self, caminho_candidatos):     
        with open(caminho_candidatos) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #contador = 0            
                    #for param in row:                    
                    #    print('param : ' + param + ' index: ' + str(contador))
                    #    contador += 1
                    line_count += 1
                else:
                    ANO_ELEICAO = row[2]
                    SG_UF = row[10]
                    CD_CARGO = row[13]
                    DS_CARGO = row[14]
                    NM_CANDIDATO = row[17]
                    SQ_CANDIDATO = row[15]
                    NR_CANDIDATO = row[16]
                    NR_CPF_CANDIDATO = row[20]
                    NM_URNA_CANDIDATO = row[18]
                    NM_PARTIDO = row[29]
                    NR_PARTIDO = row[27]
                    SG_PARTIDO = row[28]
                    CD_OCUPACAO = row[49]
                    DS_OCUPACAO = row[50]
                    DT_NASCIMENTO = row[38]
                    DS_GENERO = row[42]
                    DS_GRAU_INSTRUCAO = row[44]
                    DS_ESTADO_CIVIL = row[46]
                    SG_UF_NASCIMENTO = row[35]
                    NM_MUNICIPIO_NASCIMENTO = row[37]
                    DS_SIT_TOT_TURNO = row[53]
                    DS_SITUACAO_CANDIDATURA = row[23]
                    candidato_objeto = candidato.candidato(
                        ANO_ELEICAO, SG_UF, CD_CARGO, DS_CARGO, NM_CANDIDATO, SQ_CANDIDATO, NR_CANDIDATO, 
                        NR_CPF_CANDIDATO, NM_URNA_CANDIDATO, NM_PARTIDO, NR_PARTIDO, SG_PARTIDO, CD_OCUPACAO, 
                        DS_OCUPACAO, DT_NASCIMENTO, DS_GENERO, DS_GRAU_INSTRUCAO, DS_ESTADO_CIVIL, SG_UF_NASCIMENTO,
                        NM_MUNICIPIO_NASCIMENTO, DS_SIT_TOT_TURNO, DS_SITUACAO_CANDIDATURA)
                    self.__lista_de_candidatos.add(candidato_objeto)

    def carregar_bens(self, caminho_bens):
        with open(caminho_bens) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # contador = 0            
                    # for param in row:                    
                    #     print('param : ' + param + ' index: ' + str(contador))
                    #     contador += 1
                    line_count += 1
                else:
                    CD_TIPO_BEM_CANDIDATO = row[13]
                    DS_TIPO_BEM_CANDIDATO = row[14]
                    DS_BEM_CANDIDATO = row[15]
                    VR_BEM_CANDIDATO = row[16]
                    SQ_CANDIDATO = row[11]
                    bem_objeto = bem.bem(CD_TIPO_BEM_CANDIDATO, DS_TIPO_BEM_CANDIDATO, DS_BEM_CANDIDATO, VR_BEM_CANDIDATO)
                    candidato = self.encontrarCandidato(SQ_CANDIDATO)
                    candidato.incluirBem(bem_objeto)

    def encontrarCandidato(self, SQ_CANDIDATO):
        candidato_atual = self.__lista_de_candidatos.getHead()
        while candidato_atual.getNext() is not None:            
            if(candidato_atual.getValue().get_SQ_CANDIDATO() == SQ_CANDIDATO):
                #print(candidato_atual.getValue().get_SQ_CANDIDATO())
                return candidato_atual.getValue()
            candidato_atual = candidato_atual.getNext()
        if(candidato_atual.getValue().get_SQ_CANDIDATO() == SQ_CANDIDATO):
            return candidato_atual.getValue()
        return False

    def mostrar(self):
        print(self.__lista_de_candidatos.show())

    def imprimir(self):
        with open(r'C:\Users\Agile\Documents\UFPE\algoritmos\PROJETO\src\execução\consulta_cand_2014_AL.txt', 'a') as the_file:
            the_file.write(self.__lista_de_candidatos.show() + '\n')

    def imprimirCronometro(self, tipo, tempo):
        with open(r'C:\Users\Agile\Documents\UFPE\algoritmos\PROJETO\src\execução\cronometro.txt', 'a') as the_file:
            the_file.write(tipo + ': ' + tempo + '\n')

    def imprimirAgora(self):
        agora = time.asctime( time.localtime(time.time()) )
        with open(r'C:\Users\Agile\Documents\UFPE\algoritmos\PROJETO\src\execução\cronometro.txt', 'a') as the_file:
            the_file.write('=====\n' + agora + '\n')

    def pegarPorPartido(self, partido):
        nova_lista_de_candidatos = self.__lista_de_candidatos_partido
        candidato_atual = self.__lista_de_candidatos.getHead()
        while candidato_atual.getNext() is not None:            
            if(candidato_atual.getValue().get_SG_PARTIDO() == partido):
                #print(candidato_atual.getValue().get_SQ_CANDIDATO())
                nova_lista_de_candidatos.add(candidato_atual)
            candidato_atual = candidato_atual.getNext()
        if(candidato_atual.getValue().get_SG_PARTIDO() == partido):
            nova_lista_de_candidatos.add(candidato_atual)
        return nova_lista_de_candidatos.show()

    def pegarPorUf(self, uf):
        nova_lista_de_candidatos = self.__lista_de_candidatos_uf
        candidato_atual = self.__lista_de_candidatos.getHead()
        while candidato_atual.getNext() is not None:            
            if(candidato_atual.getValue().get_SG_UF() == uf):
                #print(candidato_atual.getValue().get_SQ_CANDIDATO())
                nova_lista_de_candidatos.add(candidato_atual)
            candidato_atual = candidato_atual.getNext()
        if(candidato_atual.getValue().get_SG_UF() == uf):
            nova_lista_de_candidatos.add(candidato_atual)
        return nova_lista_de_candidatos.show()

    def pegarPorCidade(self, cidade):
        nova_lista_de_candidatos = self.__lista_de_candidato_cidade
        candidato_atual = self.__lista_de_candidatos.getHead()
        while candidato_atual.getNext() is not None:            
            if(candidato_atual.getValue().get_NM_MUNICIPIO_NASCIMENTO() == cidade):
                #print(candidato_atual.getValue().get_SQ_CANDIDATO())
                nova_lista_de_candidatos.add(candidato_atual)
            candidato_atual = candidato_atual.getNext()
        if(candidato_atual.getValue().get_NM_MUNICIPIO_NASCIMENTO() == cidade):
            nova_lista_de_candidatos.add(candidato_atual)
        return nova_lista_de_candidatos.show()

    def pegarPorCargo(self, cargo):
        nova_lista_de_candidatos = self.__lista_de_candidato_cargo
        candidato_atual = self.__lista_de_candidatos.getHead()
        while candidato_atual.getNext() is not None:            
            if(candidato_atual.getValue().get_CD_CARGO() == cargo):
                #print(candidato_atual.getValue().get_SQ_CANDIDATO())
                nova_lista_de_candidatos.add(candidato_atual)
            candidato_atual = candidato_atual.getNext()
        if(candidato_atual.getValue().get_CD_CARGO() == cargo):
            nova_lista_de_candidatos.add(candidato_atual)
        return nova_lista_de_candidatos.show()

    def pegarPorValor(self, valor):
        valor = 'R$ ' + valor
        nova_lista_de_candidatos = self.__lista_de_candidato_valor
        candidato_atual = self.__lista_de_candidatos.getHead()
        while candidato_atual.getNext() is not None:            
            if(candidato_atual.getValue().valor_total_bens() < valor):
                #print(candidato_atual.getValue().get_SQ_CANDIDATO())
                nova_lista_de_candidatos.add(candidato_atual)
            candidato_atual = candidato_atual.getNext()
        if(candidato_atual.getValue().valor_total_bens() < valor):
            nova_lista_de_candidatos.add(candidato_atual)
        return nova_lista_de_candidatos.show()

    def pegarEleito(self):
        valor = 'R$ ' + valor
        nova_lista_de_candidatos = self.__lista_de_candidato_eleito
        candidato_atual = self.__lista_de_candidatos.getHead()
        while candidato_atual.getNext() is not None:            
            if(candidato_atual.getValue().get_DS_SIT_TOT_TURNO() == 'ELEITO'):
                #print(candidato_atual.getValue().get_SQ_CANDIDATO())
                nova_lista_de_candidatos.add(candidato_atual)
            candidato_atual = candidato_atual.getNext()
        if(candidato_atual.getValue().get_DS_SIT_TOT_TURNO() == 'ELEITO'):
            nova_lista_de_candidatos.add(candidato_atual)
        return nova_lista_de_candidatos.show()

    def pegarNaoEleito(self):
        valor = 'R$ ' + valor
        nova_lista_de_candidatos = self.__lista_de_candidato_nao_eleito
        candidato_atual = self.__lista_de_candidatos.getHead()
        while candidato_atual.getNext() is not None:            
            if(candidato_atual.getValue().get_DS_SIT_TOT_TURNO() is not 'ELEITO'):
                #print(candidato_atual.getValue().get_SQ_CANDIDATO())
                nova_lista_de_candidatos.add(candidato_atual)
            candidato_atual = candidato_atual.getNext()
        if(candidato_atual.getValue().get_DS_SIT_TOT_TURNO() is not 'ELEITO'):
            nova_lista_de_candidatos.add(candidato_atual)
        return nova_lista_de_candidatos.show()

        


if __name__ == "__main__":
    """ This is executed when run from the command line """
    cronometro_total = cronometro.Cronometro()
    cronometro_total.iniciar()
    cronometro = cronometro.Cronometro()
    controle = controle()
    controle.imprimirAgora()
    cronometro.iniciar()
    controle.carregar_candidatos(r'C:\Users\Agile\Documents\UFPE\algoritmos\PROJETO\consulta_cand_2014\consulta_cand_2014_AL.csv')
    cronometro.parar()
    controle.imprimirCronometro('carregar candidatos', cronometro.exibir())
    cronometro.zerar()
    cronometro.iniciar()
    controle.carregar_bens(r'C:\Users\Agile\Documents\UFPE\algoritmos\PROJETO\bem_candidato_2014\bem_candidato_2014_AL.csv')
    cronometro.parar()
    controle.imprimirCronometro('carregar bens', cronometro.exibir())
    cronometro.zerar()
    cronometro.iniciar()
    controle.imprimir()
    cronometro.parar()
    controle.imprimirCronometro('imprimir', cronometro.exibir())
    controle.pegarPorPartido('PCB')
    print(controle.get_lista_de_candidatos_partido())
    cronometro_total.parar()
    controle.imprimirCronometro('total', cronometro_total.exibir())
    