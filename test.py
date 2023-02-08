from Hefesto.main import Hefesto
import yaml

test = Hefesto(datainput = "../data/input.csv")
transform = test.transform_Fiab()
transform.to_csv ("../data/CDEresult_final.csv", index = False, header=True)