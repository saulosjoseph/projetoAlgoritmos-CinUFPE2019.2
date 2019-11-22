'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Saulo de Sousa Joseph
Email:    ssj2@cin.ufpe.br
Data:        20/08/2019

Descricao:  lista de monitoria Q1


Licenca: The MIT License (MIT)
'''

import time


class Cronometro:
	def __init__(self):
		self.__t0 = 0
		self.__t1 = 0

	def iniciar(self):
		self.__t1 = 0
		self.__t0 = time.perf_counter()
  
	def getT1(self):
		return self.__t1

	def getT0(self):
		return self.__t0

	def setT0(self, t0):
		self.__t0 = t0
  
	def setT1(self, t1):
		self.__t1 = t1

	def __str__(self):
		return self.exibir()

	def __repr__(self):
		return ('t0 = %r, t1 = %r' % (self.getT0(), self.getT1()))

	def parar(self):
		if(self.getT0() > 0):
			self.setT1(time.perf_counter())
		else:
			print('Cronometro não iniciado')

	def zerar(self):
		self.setT0(0)
		self.setT1(0)

	def exibir(self):
		if(self.getT0() > 0):
			if(self.getT1() > 0):
				tempo = self.getT1() - self.getT0()
			else:
				tempo = time.perf_counter() - self.getT0()
			return str(tempo)
		else:
			return('Cronometro não iniciado')