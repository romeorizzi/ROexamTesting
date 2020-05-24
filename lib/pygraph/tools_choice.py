#!/usr/bin/python

import sys


problem = sys.argv[1]
html_text = ""
n = problem
# not used at moment
#flags_for_js = ['false', 'false', 'false', 'false', 'false', 'false', 'false', 'false']
not_editable = ['false', 'true']
if problem == 'intro':
    not_editable[0] = 'true'
    not_editable[1] = 'true'
else:
    if ('none' in yaml_tools):
        not_editable[0] = 'true'
        not_editable[1] = 'true'
        
    if('select_color_node' in yaml_tools):
        #flags_for_js[0] = 'true'
        html_text = '''<div>
            <button class="button" id="btn_set_one'''+n+'''">Select</button>
        </div>
        <div>
            <button class="button" id="btn_set_two'''+n+'''">Select</button>
        </div>
        <div>
            <button class="button" id="btn_unselect_set'''+n+'''">Unselect</button>
        </div>'''
    if('drag_node' in yaml_tools):
        not_editable[1] = 'false'
        #flags_for_js[1] = 'true'

    if('remove_edge' in yaml_tools):
        #flags_for_js[2] = 'true'
        html_text = html_text + '''<div>
                <button class="button" id="btn_remove_e'''+n+'''">Remove Edge</button>
            </div>'''

    if('remove_node' in yaml_tools): 
        #flags_for_js[3] = 'true'
        html_text = html_text + '''<div>
                <button class="button" id="btn_remove'''+n+'''">Remove Node</button>
            </div>'''

    if('add_node' in yaml_tools):
        #flags_for_js[4] = 'true'
        html_text = html_text + '''<div>
                <button class="button" id="btn_add'''+n+'''">Add Node</button>
            </div>'''

    if('add_edge' in yaml_tools):
        #flags_for_js[5] = 'true'
        html_text = html_text + '''<div>
                <button class="button" id="btn_add_e'''+n+'''">Add Edge</button>
            </div>'''

    if('add_edge_dir' in yaml_tools):
        #flags_for_js[5] = 'true'
        html_text = html_text + '''<div>
                <button class="button" id="btn_add_e_dir'''+n+'''">Add Edge Dir</button>
            </div>'''  

    if('choice' in yaml_tools): 
        #flags_for_js[6] = 'true'
        html_text = html_text + '''<div>
                <button class="button" id="yes'''+n+'''">Yes</button>
                </div>
                <div>
                <button class="button" id="no'''+n+'''">No</button>
            </div>'''

    if('edit_label' in yaml_tools): 
        #flags_for_js[7] = 'true'
        html_text = html_text + '''<div>
                <button class="button" id="btn_set_weight'''+n+'''">Set weight</button>
                </div>'''

    #if('submit' in yaml_tools): 
        #flags_for_js[7] = 'true'
    #    html_text = html_text + '''<div>
    #            <button class="button" id="submit'''+n+'''">Submit</button>
    #            </div>'''
    
    if('save' in yaml_tools): 
        #flags_for_js[7] = 'true'
        html_text = html_text + '''<div>
                <button class="button" id="save'''+n+'''">Save</button>
                </div>'''
        
        
    if('all' in yaml_tools): 
        #flags_for_js[7] = 'true'
        not_editable[0] = 'false'
        not_editable[1] = 'false'
        html_text =''' <div>
            <button class="button" id="btn_set_one'''+n+'''">Select</button>
        </div>
        <div>
            <button class="button" id="btn_set_two'''+n+'''">Select</button>
        </div>
        <div>
            <button class="button" id="btn_unselect_set'''+n+'''">Unselect</button>
        </div> 
        <div>
            <button class="button" id="btn_remove_e'''+n+'''">Remove Edge</button>
        </div>
        <div>
            <button class="button" id="btn_remove'''+n+'''">Remove Node</button>
        </div>
        <div>
            <button class="button" id="btn_add'''+n+'''">Add Node</button>
        </div>
        <div>
            <button class="button" id="btn_add_e'''+n+'''">Add Edge</button>
        </div>
        <div>
            <button class="button" id="btn_add_e_dir'''+n+'''">Add Edge Dir</button>
        </div>
        <div>
            <button class="button" id="btn_set_weight'''+n+'''">Set weight</button>
        </div>
        <div>
            <button class="button" id="yes'''+n+'''">Yes</button>
        </div>
        <div>
            <button class="button" id="no'''+n+'''">No</button>
        </div>
        <div>
            <button class="button" id="submit'''+n+'''">Submit</button>
        </div>
        '''