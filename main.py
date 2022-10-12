import pandas as pd
import yaml
from pyperseo.functions import milisec as milisec


class Hefesto:

    def transform_shape(path_datainput,path_config_file,path_output_file):

        configuration = None

        # Import YAML template for each CDE's static term:
        with open("template/template_model.yaml") as file:
            template = yaml.load(file, Loader=yaml.FullLoader)

        # Import data input:
        df_data = pd.read_csv(path_datainput)

        # Import YAML config file:
        with open(path_config_file) as file:
            configuration = yaml.load(file, Loader=yaml.FullLoader)

        
        resulting_df = pd.DataFrame()
        row_df = {}

        # Iterate each row from data input
        # check each YAML object from configuration file to set the parameters
        for row in df_data.iterrows():

            for config in configuration.items():

                # Create a unique stamp per new row to about them to colapse:
                milisec_point = milisec()

                row_df.update({milisec_point: {'model':config[0]}})
                
                # Add YAML template static information
                for cde in template.items():
                    if cde[0] == row_df[milisec_point]["model"]:
                        row_df[milisec_point].update(cde[1])

                # Relate each YAML parameter with original data input
                for element in config[1]["columns"].items():
                    for r in row[1].index:
                        if r == element[1]:
                            dict_element = {element[0]:row[1][r]}
                            row_df[milisec_point].update(dict_element)
                
                # Add new dict with extracted information into a Data frame
                final_row_df = pd.DataFrame(row_df[milisec_point], index=[1])
                resulting_df = pd.concat([resulting_df, final_row_df])
        

        # Export to CSV
        resulting_df.to_csv (path_output_file, index = False, header=True)
