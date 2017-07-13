from class_informationerror import InformationError
from class_datahora import datahora, data

class cartao:
    def __init__(self, numerocartao=0, validade=None, titular="", ccv=0):
        #chamar função que verifica a validade da informação 
        self._numerocartao = numerocartao
        self._validade = validade
        self._titular = titular
        self._ccv = ccv
        self.__verifica()

    def __verifica(self):
        #verificação de numerocartao
        if type(self._numerocartao) != int:
            raise InformationError()
        if self._numerocartao > 9999999999999999 or self._numerocartao < 0:
            raise InformationError()
        #verificação de validade
        if type(self._validade) != data:
            raise InformationError()
        #verificação de titular
        if type(self._titular) != str:
            raise InformationError()
        for x in list(self._titular):
            for num in range(9):
                if x == str(num):
                    raise InformationError()
        #verificação de ccv
        if type(self._ccv) != int:
            raise InformationError()
        if self._ccv < 100 or self._ccv > 999:
            raise InformationError()
        
    #propertyzone
    @property
    def numerocartao(self):return self._numerocartao
    @property
    def validade(self):return self._validade
    @property
    def titular(self):return self._titular
    @property
    def ccv(self):return self._ccv
    #setterzone
    @numerocartao.setter
    def numerocartao(self):pass
    @validade.setter
    def validade(self):pass
    @titular.setter
    def titular(self):pass
    @ccv.setter
    def ccv(self):pass
    #fim
    
    def __str__(self):
        return "Cartão: "+str(self._numerocartao)+". Valido até: "+str(self._validade)+"."
