from Hefesto.main import Hefesto
import yaml

# Test 1:

test = Hefesto(datainput = "data/INPUT_DATA.csv")
transform = test.transformFiab()
transform.to_csv ("../data/OUTPUT_DATA.csv", index = False, header=True)