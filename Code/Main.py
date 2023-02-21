print("      Hello Sir,                                  ")
print("1------ Sir Model Of COVID                        ")
print("2------- User Defined Sir Model Of COVID          ")
print("3-------- Cummilative SirModel Of Covid           ")
print("4------- UserDefined Cummilative SirModel Of Covid")
print("5-------- Covid Deaths In India                   ")
print("6-------- Covid Infected People In India          ")
print("7-------- Covid Cured Patients In India           ")
print("8-------- Comparison of Viruses                   ")
print("---------------------------------------------------------------------")
demo=int(input("|                       EnterChoice:"))
print("|                                                                    |")
while(True):
    if(demo == 1):
        import SirModel
        SirModel.initalvalues()
        break
    if(demo == 2):
        import UserDefSirModel
        x = UserDefSirModel.MyClass()
        break
    if(demo == 3):
        import SIrModelCum
        SIrModelCum.initalvalues()
        break
    if(demo == 4):
        import UserDefSirModelCum
        x = UserDefSirModelCum.MyClass()
        break
    if(demo == 5):
        import CovidDeathIndia
        break
    if(demo == 6):
        import CovidCasesIndia
        break
    if(demo == 7):
        import CovidRecovIndia
        break
    if(demo == 8):
        
        
        import ComparisonOfVirus
        break
    else:
        break
print("---------------------------------------------------------------------")    

    
        

    
