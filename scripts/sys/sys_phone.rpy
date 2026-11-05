default phone_number = ""
init -1 python:

    class PolinaPhone:
        def __init__(self):
            self.db = {}
            self.state = 0 
            self.overused = set()
        
        def GetLabel(self, number):
            if number in self.db:
                if number not in self.overused:
                    return self.db[number]
                else:
                    return self.db["overused"]
            if len(number) == 5 and number != "10050":
                return self.db[None]
            if len(number) > 5:
                return self.db[None]
            return None
        
        def RegisterNumber(self, number, label):
            self.db[number] = label
        
        def OveruseNumber(self, number):
            self.overused.add(number)
        
        def ResetOveruse(self):
            self.overused = set()


    def phone_Add(digit):
        global phone_number
        dig = str(digit)
        phone_number += dig

    def phone_Clear():
        global phone_number
        phone_number = ""

    def phone_Overuse():
        global phone_number, polina_phone
        polina_phone.OveruseNumber(phone_number)

    def phone_display():
        global phone_number
        return phone_number






label init_phone:















    python:

        polina_phone.RegisterNumber(None, "event_m_polina_phone.wrong")           
        polina_phone.RegisterNumber("overused", "event_m_polina_phone.overused")  

        polina_phone.RegisterNumber("30395", "event_m_polina_phone.continue")     
        polina_phone.RegisterNumber("31587", "event_m_polina_phone.roma")         
        polina_phone.RegisterNumber("31758", "event_m_polina_phone.matuhin")      
        polina_phone.RegisterNumber("31677", "event_m_polina_phone.katya")        
        polina_phone.RegisterNumber("34381", "event_m_polina_phone.ksenia")       
        polina_phone.RegisterNumber("31042", "event_m_polina_phone.semen")        
        polina_phone.RegisterNumber("20337", "event_m_polina_phone.tikhonov")     

        polina_phone.RegisterNumber("36722", "event_m_polina_phone.militia")      
        polina_phone.RegisterNumber("32492", "event_m_polina_phone.polina")       
        polina_phone.RegisterNumber("23326", "event_m_polina_phone.byash")        
        polina_phone.RegisterNumber("01", "event_m_polina_phone.fire_dep")        
        polina_phone.RegisterNumber("02", "event_m_polina_phone.militia")         
        polina_phone.RegisterNumber("03", "event_m_polina_phone.ambulance")       
        polina_phone.RegisterNumber("04", "event_m_polina_phone.gas")             


        polina_phone.RegisterNumber("32866", "event_m_polina_phone.pingvin")
        polina_phone.RegisterNumber("31112", "event_m_polina_phone.veber")
        polina_phone.RegisterNumber("31448", "event_m_polina_phone.gris")
        polina_phone.RegisterNumber("32603", "event_m_polina_phone.kuplinov")
        polina_phone.RegisterNumber("32810", "event_m_polina_phone.rin")
        polina_phone.RegisterNumber("100500", "event_m_polina_phone.stopitsot")
        polina_phone.RegisterNumber("38891", "event_m_polina_phone.tatirzha")
        polina_phone.RegisterNumber("33306", "event_m_polina_phone.dipins")
        polina_phone.RegisterNumber("33000", "event_m_polina_phone.bratishkin")
        polina_phone.RegisterNumber("30007", "event_m_polina_phone.planya")
        polina_phone.RegisterNumber("37070", "event_m_polina_phone.solek")
        polina_phone.RegisterNumber("31148", "event_m_polina_phone.chroma")
        polina_phone.RegisterNumber("31948", "event_m_polina_phone.bulaev")

        polina_phone.RegisterNumber("41141", "event_m_polina_phone.bebei")
        polina_phone.RegisterNumber("34749", "event_m_polina_phone.migla")
        polina_phone.RegisterNumber("31788", "event_m_polina_phone.kras")
        polina_phone.RegisterNumber("31846", "event_m_polina_phone.sofi")
        polina_phone.RegisterNumber("20550", "event_m_polina_phone.melnik")
        polina_phone.RegisterNumber("36666", "event_m_polina_phone.mazelov")
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
