from class_informationerror import InformationError
class data:
    def __init__(self,DD = None,MM = None,AAAA = None):
        event = False
        self._DD = DD
        self._MM = MM
        self._AAAA = AAAA
        #try:
        self.__verifica()
        '''except:
            #se houver exception, evento ocorrido recebe verdadeiro
            event = True
        
        if event == True:
            #se houver ocorrido algum evento de excessão chama InformationError
            raise InformationError()'''
        
    #determina se há erro de data
    def __verifica(self):
        #bloco de testes
        self.__testeDD()
        self.__testeMM()
        self.__testeAAAA()
        #verifica se é bissexto ou não
        if self._AAAA % 4 == 0:
            if self._AAAA % 100 == 0:
                if self._AAAA % 400 == 0:
                    self.__tamanhoano = 366
                    self.__listameses = [31,29,31,30,31,30,31,31,30,31,30,31]
                else:
                    self.__tamanhoano = 365
                    self.__listameses = [31,28,31,30,31,30,31,31,30,31,30,31]
            else:
                self.__tamanhoano = 366
                self.__listameses = [31,29,31,30,31,30,31,31,30,31,30,31] 
        else:
            self.__tamanhoano = 365
            self.__listameses = [31,28,31,30,31,30,31,31,30,31,30,31]
        #fim
        if self._DD > self.__listameses[self._MM-1]: raise InformationError()
        
    def __testeDD(self):
        if self._DD < 1 or self._DD > 31 or type(self._DD) != int: raise InformationError()
    def __testeMM(self):
        if self._MM < 1 or self._MM > 12 or type(self._MM) != int: raise InformationError()
    def __testeAAAA(self):
        if self._AAAA < 1 or type(self._AAAA) != int: raise InformationError()
        
    #propertyzone
    @property
    def MM(self):return self._MM
    @property
    def DD(self):return self._DD
    @property
    def AAAA(self):return self._AAAA
    @property
    def listameses(self):pass
    @property
    def tamanhoano(self):pass
    @property
    def tamanhomes(self):pass
    #setterzone
    @DD.setter
    def DD(self,DD):
        self._DD = DD
        self.__testeDD()
    @MM.setter
    def MM(self,MM):
        self._MM = MM
        self.__testeMM()
    @AAAA.setter
    def AAAA(self,AAAA):
        self._AAAA = AAAA
        self.__testeano()
    @listameses.setter
    def listameses(self,NLM):pass
    @tamanhoano.setter
    def tamanhoano(self,NTA):pass
    @tamanhomes.setter
    def tamanhomes(self,NTM):pass
    #fim
    def __str__(self):
        return str(self._DD) + "/" + str(self._MM) + "/" + str(self._AAAA)

class tempo:
    def __init__(self,HH = 0,MIN = 0,SS = 0):
        event = False
        self._HH = HH
        self._MIN = MIN
        self._SS = SS
        try:
            self.__verifica()
        except:
            event = True

        if event == True:
            raise InformationError()

    #determina se há erro de tempo
    def __verifica(self):
        self.__testeHH()
        self.__testeMIN()
        self.__testeSS()

    def __testeHH(self):
        if self._HH < 0 or self._HH > 23 or type(self._HH) != int: raise InformationError()
    def __testeMIN(self):
        if self._MIN < 0 or self._MIN > 59 or type(self._MIN) != int: raise InformationError()
    def __testeSS(self):
        if self._SS < 0 or self._SS > 59 or type(self._SS) != int: raise InformationError()

    #porpertyzone
    @property
    def HH(self):return self._HH
    @property
    def MIN(self):return self._MIN
    @property
    def SS(self):return self._SS
    #setterzone
    @HH.setter
    def HH(self,HH):
        self._HH = HH
        self.__testeHH()
    @MIN.setter
    def MIN(self,MIN):
        self._MIN = MIN
        self.__testeMIN()
    @SS.setter
    def SS(self,SS):
        self._SS = SS
        self.__testeSS()
    #fim

    def __str__(self):
        return str(self._HH) + ":" + str(self._MIN) + ":" + str(self._SS)

class datahora(data,tempo):
    def __init__(self,DD = None,MM = None,AAAA = None,HH=0,MIN=0,SS=0):
        data.__init__(self, DD, MM, AAAA)
        tempo.__init__(self, HH, MIN, SS)

    def __str__(self):
        return str(self._DD) + "/" + str(self._MM) + "/" + str(self._AAAA) + " " +str(self._HH) + ":" + str(self._MIN) + ":" + str(self._SS)
