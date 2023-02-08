from Hefesto.main import Hefesto
from perseo.main import get_files
from os import listdir, getcwd



mypath = getcwd()+ "/data"
all_files = get_files(mypath,"csv")

for a in all_files:

    input_path = mypath + "/" + a
    output_path = mypath + "/CDE_resulting_" + a

    # Test
    test = Hefesto(datainput = input_path)
    transform = test.transform_Fiab()
    transform.to_csv (output_path, index = False, header=True)