from Hefesto.main import Hefesto
import yaml

# Import YAML configuration file with all parameters:
with open("data/config.yaml") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)

test = Hefesto.transform_shape(path_datainput ="data/exemplarCDEdata.csv", configuration=configuration)
test.to_csv ("data/result.csv", index = False, header=True)