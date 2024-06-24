from model.model import Model

myModel = Model()
myModel._creaGrafo("France", "2015")
print(myModel.getGraphDetails())
volumi = myModel.getVolumiVendite()
"""for v in volumi:
    print(v)"""
percorso, pesoPercorso = myModel.getPercorso(4)
print(pesoPercorso)
for p in percorso:
    print(p)
