import pandas as pd

from toolkit.main import Toolkit

test= Toolkit()

test_done = test.whole_quality_control(input_data="data/preCARE.csv")
test_done.to_csv ("data/CARE_test.csv", index = False, header=True)