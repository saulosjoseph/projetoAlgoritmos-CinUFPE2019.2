import lista

class candidato:
    def __init__(self, ANO_ELEICAO, SG_UF, CD_CARGO, DS_CARGO, NM_CANDIDATO, SQ_CANDIDATO, NR_CANDIDATO, 
                NR_CPF_CANDIDATO, NM_URNA_CANDIDATO, NM_PARTIDO, NR_PARTIDO, SG_PARTIDO, CD_OCUPACAO, 
                DS_OCUPACAO, DT_NASCIMENTO, DS_GENERO, DS_GRAU_INSTRUCAO, DS_ESTADO_CIVIL, SG_UF_NASCIMENTO,
                NM_MUNICIPIO_NASCIMENTO, DS_SIT_TOT_TURNO, DS_SITUACAO_CANDIDATURA):
        self.__ANO_ELEICAO = ANO_ELEICAO
        self.__SG_UF = SG_UF
        self.__CD_CARGO = CD_CARGO
        self.__DS_CARGO = DS_CARGO
        self.__NM_CANDIDATO= NM_CANDIDATO
        self.__SQ_CANDIDATO = SQ_CANDIDATO
        self.__NR_CANDIDATO = NR_CANDIDATO
        self.__NR_CPF_CANDIDATO = NR_CPF_CANDIDATO
        self.__NM_URNA_CANDIDATO = NM_URNA_CANDIDATO
        self.__NM_PARTIDO = NM_PARTIDO
        self.__NR_PARTIDO = NR_PARTIDO
        self.__SG_PARTIDO = SG_PARTIDO
        self.__CD_OCUPACAO= CD_OCUPACAO
        self.__DS_OCUPACAO = DS_OCUPACAO
        self.__DT_NASCIMENTO = DT_NASCIMENTO
        self.__DS_GENERO = DS_GENERO
        self.__DS_GRAU_INSTRUCAO = DS_GRAU_INSTRUCAO
        self.__DS_ESTADO_CIVIL = DS_ESTADO_CIVIL
        self.__SG_UF_NASCIMENTO = SG_UF_NASCIMENTO
        self.__NM_MUNICIPIO_NASCIMENTO = NM_MUNICIPIO_NASCIMENTO
        self.__DS_SIT_TOT_TURNO = DS_SIT_TOT_TURNO
        self.__DS_SITUACAO_CANDIDATURA = DS_SITUACAO_CANDIDATURA
        self.__lista_bens = lista.DoublyLinkedList()

    def get_ANO_ELEICAO(self):
        return self.__ANO_ELEICAO
    def set_ANO_ELEICAO(self, ANO_ELEICAO):
        self.__ANO_ELEICAO = ANO_ELEICAO   
    def get_SG_UF(self):
        return self.__SG_UF
    def set_SG_UF(self, SG_UF):
        self.__SG_UF = SG_UF
    def get_CD_CARGO(self):
        return self.__CD_CARGO
    def set_CD_CARGO(self, CD_CARGO):
        self.__CD_CARGO = CD_CARGO
    def get_DS_CARGO(self):
        return self.__DS_CARGO
    def set_DS_CARGO(self, DS_CARGO):
        self.__DS_CARGO = DS_CARGO
    def get_NM_CANDIDATO(self):
        return self.__NM_CANDIDATO
    def set_NM_CANDIDATO(self, NM_CANDIDATO):
        self._NM_CANDIDATO = NM_CANDIDATO
    def get_NM_URNA_CANDIDATO(self):
        return self.__NM_URNA_CANDIDATO
    def set_NM_URNA_CANDIDATO(self, NM_URNA_CANDIDATO):
        self.__NM_URNA_CANDIDATO = NM_URNA_CANDIDATO
    def get_NR_CANDIDATO(self):
        return self.__NR_CANDIDATO
    def get_SG_PARTIDO(self):
        return self.__SG_PARTIDO
    def get_NM_MUNICIPIO_NASCIMENTO(self):
        return self.__NM_MUNICIPIO_NASCIMENTO
    def get_SG_UF_NASCIMENTO(self):
        return self.__SG_UF_NASCIMENTO
    def get_lista_bens(self):
        return self.__lista_bens
    def get_NR_CPF_CANDIDATO(self):
        return self.__NR_CPF_CANDIDATO()
    def get_SQ_CANDIDATO(self):
        return self.__SQ_CANDIDATO
    

    def __str__(self):
        texto = (self.get_NM_URNA_CANDIDATO() + ' -- ' + self.get_NR_CANDIDATO() + ' -- ' + self.get_SG_PARTIDO() + '\n' +
        self.get_DS_CARGO() + ' (' + self.get_SG_UF() + ') ' + self.get_NM_MUNICIPIO_NASCIMENTO() + ' (' + self.get_SG_UF_NASCIMENTO() +
        ') ' + '\n' + 'Resumo dos bens: ' + '\n' + '   -Total declarado: ' + self.valor_total_bens() + '\n' + 
        '   -Total por tipo de bem: ' + str(self.get_lista_bens()) + '\n')
        return texto
    
    def __repr__(self):
        return self.__str__()

    def coincide(self, candidato):
        if(self.get_NM_CANDIDATO == candidato.get_NM_CANDIDATO() and self.get_NR_CPF_CANDIDATO() == candidato.get_NR_CPF_CANDIDATO()):
            return True
        return False
        
    def incluirBem(self, bem):
        self.get_lista_bens().add(bem)

    def valor_total_bens(self):
        bem_atual = self.get_lista_bens().getHead()
        valor_total = 0
        while bem_atual is not None:
            valor_total += bem_atual.get_VR_BEM_CANDIDATO()
            bem_atual = bem_atual.getNext()
        return valor_total