

from src.mlproject import logger
import json
from pathlib import  Path


import yaml


# @ensure_annotations
# def read_yaml(path_to_yaml : Path) -> ConfigBox:
# #     """
#     reads yaml file and returns
#     Args:
#         path_to_yaml (str): path like input

#     Raises:
#         ValueError : if yaml file is empty
#         e : empty file
#     Retuns:
#         ConfigBox : configBox type
#     :param path_to_yaml:
#     :return:
#     """

#     try:
#         with open(path_to_yaml) as yaml_file:
#             content = yaml.safe_load(yaml_file)
#             logger.info("yaml file : {} loaded successfully".format(yaml_file))
#             return ConfigBox(content)
#     except BoxValueError:
#         raise ValueError('yaml file is empty')
#     except Exception as e:
#         raise e
    
# a = read_yaml(Path("temp.yaml"))
# logger.info('There is information for data validaiton{}'.format(a.data_validation.keys()))
# logger.info('There is an information for main file{}'.format(a.temp))

with open("artifacts\data_validation\status.txt",'r') as file:
    content = file.read()
    
if "Validation status : True" in content:
    logger.info('Ready for transformation')
else:
    logger.info('Validate your data first')