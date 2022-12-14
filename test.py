from Hefesto.main import Hefesto
import yaml

# Import YAML configuration file with all parameters:
with open("data/CDEconfig.yaml") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)
print(configuration)

test = Hefesto(datainput = "data/OFFICIAL_DATA_INPUT.csv") # , clean_blanks=False
transform = test.transform_shape(configuration=configuration)
# label = test.get_label("outputURI")
# url_from_label= test.get_uri("outputURI_label","ncit")
# repl= test.replacement("outputURI_label", "Date","DateXXX", duplicate=False)
transform.to_csv ("data/result_final.csv", index = False, header=True)