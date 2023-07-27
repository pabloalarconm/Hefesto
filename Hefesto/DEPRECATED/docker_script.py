from Hefesto.main import Hefesto
from perseo.main import get_files
from os import listdir, getcwd
import pandas as pd

mypath = getcwd()+ "/data"
all_files = get_files(mypath,"csv")
final_df = pd.DataFrame()

for a in all_files:

    input_path = mypath + "/" + a
    output_path = mypath + "/CDE.csv"

    # Test
    test = Hefesto(datainput = input_path)
    transform = test.transform_Fiab()
    final_df = pd.concat([final_df, transform])

final_df.to_csv (output_path, index = False, header=True)