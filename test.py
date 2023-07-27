from Hefesto.main import Hefesto
import yaml

# Test 1
test = Hefesto(datainput = "data/INPUT_DATA.csv")
transform = test.transformFiab()
transform.to_csv ("data/OUTPUT_DATA.csv", index = False, header=True)


# Test 2
with open("data/CDEconfig.yaml") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)

test = Hefesto(datainput = "data/INPUT_DATA2.csv")
transform = test.transformShape(configuration=configuration, clean_blanks = True) #, clean_blanks=False
# label = test.get_label("output_type")
# url_from_label= test.get_uri("output_type_label","ncit")
# repl= test.replacement("output_type_label", "Date","DateXXX", duplicate=False)
transform.to_csv ("data/OUTPUT_DATA2.csv", index = False, header=True)




# Test 1:

test = Hefesto(datainput = "data/INPUT_DATA.csv")
transform = test.transformFiab()
transform.to_csv ("../data/OUTPUT_DATA_new.csv", index = False, header=True)

# Test 2:

with open("data/CDEconfig.yaml") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)

test = Hefesto(datainput = "/data/INPUT_DATA2.csv")
transform = test.transformShape(configuration=configuration, clean_blanks = True) #, clean_blanks=False
# label = test.get_label("output_type")
# url_from_label= test.get_uri("output_type_label","ncit")
# repl= test.replacement("output_type_label", "Date","DateXXX", duplicate=False)
transform.to_csv ("/data/OUTPUT_DATA2_new.csv", index = False, header=True)