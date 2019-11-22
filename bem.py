from textwrap import wrap
class bem:
    def __init__(self, CD_TIPO_BEM_CANDIDATO, DS_TIPO_BEM_CANDIDATO, DS_BEM_CANDIDATO, VR_BEM_CANDIDATO):
        self.__CD_TIPO_BEM_CANDIDATO = CD_TIPO_BEM_CANDIDATO
        self.__DS_TIPO_BEM_CANDIDATO = DS_TIPO_BEM_CANDIDATO
        self.__DS_BEM_CANDIDATO = DS_BEM_CANDIDATO
        self.__VR_BEM_CANDIDATO = VR_BEM_CANDIDATO

    def get_CD_TIPO_BEM_CANDIDATO(self):
        return self.__CD_TIPO_BEM_CANDIDATO
    def get_DS_TIPO_BEM_CANDIDATO(self):
        return self.__DS_TIPO_BEM_CANDIDATO
    def get_DS_BEM_CANDIDATO(self):
        return self.__DS_BEM_CANDIDATO
    def get_VR_BEM_CANDIDATO(self):
        return self.__VR_BEM_CANDIDATO

    def __str__(self):
        texto = (self.get_CD_TIPO_BEM_CANDIDATO() + ' -- ' + self.get_DS_TIPO_BEM_CANDIDATO() + ' -- ' + self.get_VR_BEM_CANDIDATO() +
        ' Descrição: ' + wrap(text = self.get_DS_BEM_CANDIDATO(), width = 30))
        return texto
    
    def __repr__(self):
        return self.__str__()

    def coincide(self, bem):
        if(self.get_VR_BEM_CANDIDATO == bem.get_VR_BEM_CANDIDATO() and self.get_DS_BEM_CANDIDATO() == bem.get_DS_BEM_CANDIDATO()):
            return True
        return False

    def maior(self, bem):
        if(self.get_VR_BEM_CANDIDATO > bem.get_VR_BEM_CANDIDATO()):
            return self
        elif(self.get_VR_BEM_CANDIDATO < bem.get_VR_BEM_CANDIDATO()):
            return bem
        else:
            if(self.get_CD_TIPO_BEM_CANDIDATO > bem.get_CD_TIPO_BEM_CANDIDATO()):
                return self
            elif(self.get_CD_TIPO_BEM_CANDIDATO < bem.get_CD_TIPO_BEM_CANDIDATO()):
                return bem
            else:
                if(self.get_DS_BEM_CANDIDATO() > bem.get_DS_BEM_CANDIDATO()):
                    return self
                return bem