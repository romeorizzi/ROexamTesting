# Read cofiguration file
file = open(r'exercise_2/config_exercise_2.yaml')
yaml_list = yaml.load(file, Loader=yaml.FullLoader)
yaml_table_path = yaml_list.get("table")
yaml_text = yaml_list.get("text")
res_path = yaml_list.get("res")

#yaml_tools = yaml_list.get("tools")

#yaml_js_path = yaml_list.get("js_file")