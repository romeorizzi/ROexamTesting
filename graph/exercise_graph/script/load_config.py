#!/usr/bin/python

import sys

num_exe = sys.argv[1]

# Read cofiguration file

file = open(r'exercise_graph/config_exercise_graph.yaml')
yaml_list = yaml.load(file, Loader=yaml.FullLoader)
yaml_exercise = yaml_list.get("exe_"+str(num_exe))
yaml_text = yaml_exercise.get('text')
yaml_graph_path = yaml_exercise.get('graph')
ymal_sub_ex = yaml_exercise.get("dataextra")
yaml_tools = yaml_exercise.get("tools")
yaml_js_path = yaml_list.get("js_file")

if(ymal_sub_ex != 'none'):
    file1 = open(ymal_sub_ex, 'r')
    yaml_list_1 = yaml.load(file1, Loader=yaml.FullLoader)
    yaml_ex_ottimo = yaml_list_1.get("edge_sol_ottime")
 