import sys
import re 
import math
import copy
import xml.etree.ElementTree as ET
import numpy
from itertools import compress 
import random

path = sys.argv[1]
default_color_node = "#000000"
default_color_edge = "#828282"
size_node = 3
size_edge = 3
graph_data = { 'nodes': [], 'edges': [] } #struttura da passare a sigma-graph.js per costruire grafo

#parsing dell'xml dopo averlo letto e creazione array con nodi e archi
tree = ET.parse(path)
root = tree.getroot()
original_nodes = []
original_edges = []
dict_nodes = {}
multiple_line = {}
hidden_nodes = {}
s_edges = set()
i=0
dict_edges = {}
dict_be = {}
dict_n = {}


for node in root.iter('{http://graphml.graphdrawing.org/xmlns}node'):    
    for label in node.iter('{http://www.yworks.com/xml/yfiles-common/3.0}Label.Text'):
        dict_n.update({node.attrib.get('id'):{'label':label.text,'x':0,'y':0}})
        dict_nodes.update({node.attrib.get('id'):label.text})
        original_nodes.append(dict_nodes[node.attrib.get('id')])
    for c in node.iter('{http://www.yworks.com/xml/yfiles-common/3.0}RectD'):
        dict_n[node.attrib.get('id')]['x'] = float(c.attrib.get('X'))
        dict_n[node.attrib.get('id')]['y'] = float(c.attrib.get('Y'))

for edge in root.iter('{http://graphml.graphdrawing.org/xmlns}edge'):
    dict_edges.update({edge.attrib.get('id'):{'source_id':edge.attrib.get('source'),'target_id':edge.attrib.get('target'),'source':dict_nodes.get(edge.attrib.get('source')),'target':dict_nodes.get(edge.attrib.get('target')),'label':None, 'type':None,'broken':False}})
    original_edges.append(edge.attrib.get('id'))
    for label in edge.iter('{http://www.yworks.com/xml/yfiles-common/3.0}Label.Text'):
        dict_edges[edge.attrib.get('id')]['label'] = label.text
    for type in edge.iter('{http://www.yworks.com/xml/yfiles-common/3.0}GraphMLReference'):
        if(type.attrib.get('ResourceKey') == '6'):
            dict_edges[edge.attrib.get('id')]['type'] = 'line'
        else:
            dict_edges[edge.attrib.get('id')]['type'] = 'arrow'
    multiple_line.update({edge.attrib.get('id'):[]})
    multiple_line[edge.attrib.get('id')].append(dict_nodes[edge.attrib.get('source')])
    for b in edge.iter('{http://www.yworks.com/xml/yfiles-common/3.0}Bend'):
        dict_edges[edge.attrib.get('id')]['broken'] = True
        s_edges.add(edge.attrib.get('id'))
        hidden_nodes.update({'hidden'+str(i):b.attrib.get('Location')})
        i = i+1
        multiple_line[edge.attrib.get('id')].append(b.attrib.get('Location'))
    multiple_line[edge.attrib.get('id')].append(dict_nodes[edge.attrib.get('target')])

new_d = {}
for key in multiple_line:
    new_d.update({key:[]})

for key in multiple_line:
    tmp = res = list(zip(multiple_line[key], multiple_line[key][1:] + multiple_line[key][:1]))
    new_d[key] = tmp
    tmp = None


new_ml = {} 
for key in new_d:
    new_ml.update({key:[]})
    for n in new_d[key]:
        if n[0] in original_nodes and n[1] in original_nodes:
            new_ml[key].append((n[0],n[1]))
        if n[0] in original_nodes and n[1] not in original_nodes:
            new_ml[key].append((n[0],list(hidden_nodes.keys())[list(hidden_nodes.values()).index(n[1])]))
        if n[1] in original_nodes and n[0] not in original_nodes:
            new_ml[key].append((list(hidden_nodes.keys())[list(hidden_nodes.values()).index(n[0])],n[1]))
        if n[1] not in original_nodes and n[0] not in original_nodes:
            new_ml[key].append((list(hidden_nodes.keys())[list(hidden_nodes.values()).index(n[0])],list(hidden_nodes.keys())[list(hidden_nodes.values()).index(n[1])]))

for e in new_ml:
    new_ml[e].pop()

ml_copy = copy.deepcopy(new_ml)
for e in ml_copy:
    if e not in s_edges:
        del new_ml[e]

for n in hidden_nodes:
    hidden_nodes[n] = hidden_nodes[n].split(',')

tmp_h_edges= list(new_ml.values())
hidden_edges = []
for sublist in tmp_h_edges:
    for item in sublist:
        hidden_edges.append(item)

#dict per posizione dell'arco spezzato e per la lunghezza dell'arco principale
dict_pos = {}
parent_len = {}
for key in new_ml:
    for e in new_ml[key]:
        dict_be.update({e:key})
        dict_pos.update({e:new_ml[key].index(e)})
        parent_len.update({e:len(new_ml[key])})

#dizionario contenente archi spezzati e relative info
dict_he = {}
i = 0
for b_e in hidden_edges:
    if dict_pos[b_e] == int(parent_len[b_e]/2):
        dict_he.update({'h'+str(i):{'source':b_e[0],'target':b_e[1],'parent':dict_be[b_e],'label':dict_edges[dict_be[b_e]]['label'],'type':'line','position':dict_pos[b_e]}})
    elif dict_pos[b_e] == int(parent_len[b_e])-1 and dict_edges[dict_be[b_e]]['type']=='arrow':
        dict_he.update({'h'+str(i):{'source':b_e[0],'target':b_e[1],'parent':dict_be[b_e],'label':None,'type':'arrow','position':dict_pos[b_e]}})
    else:
        dict_he.update({'h'+str(i):{'source':b_e[0],'target':b_e[1],'parent':dict_be[b_e],'label':None,'type':'line','position':dict_pos[b_e]}})
    i = i+1

tuple_id = {}
for e in dict_he:
    tuple_id.update({(dict_he[e]['source'],dict_he[e]['target']):e})
#print(tuple_id)
d_cpy = copy.deepcopy(dict_edges)
for e in d_cpy:
    if e in s_edges:
        del dict_edges[e]

unpacked = {}
friends_n = {}
for e in new_ml:
    unpacked.update({e:[]})
    for l in new_ml[e]:
        for t in l:
            unpacked[e].append(t)
for e in unpacked:
    for f in unpacked[e]:
        friends_n.update({f:[]})
for e in unpacked:
    for f in unpacked[e]:
        friends_n[f]=friends_n[f]+unpacked[e]

friends_e = {}
for e in new_ml:
    for f in new_ml[e]:
        friends_e.update({tuple_id[f]:[]})

for e in new_ml:
    for t in new_ml[e]:
        for t2 in new_ml[e]:
            friends_e[tuple_id[t]].append(tuple_id[t2])
            
#friends_n contiene tutti i nodi che appartengono allo stesso arco, quindi quando l'utente colora o rimuove uno di quei nodi devo rimuovere (o colorare)anche gli altri
#friends_e contiene tutti i gli archi che formano un arco piuù grande, quando rimuovo o coloro uno di quelli devo rimuovere anche gli altri 
#se rimuovo source o target devo rimuove arco, se coloro invece no!

###########################################SIGMA JS BUG CORRECTION########################################
#Nodi che hanno la stessa coordinata --> aggiungo delta
x_dict = {}
for n in dict_n:
    x_dict.update({dict_n[n]['x']:[]})
    
for n in dict_n:
    x_dict[dict_n[n]['x']].append(n)

y_dict = {}
for n in dict_n:
    y_dict.update({dict_n[n]['y']:[]})
    
    
for n in dict_n:
    y_dict[dict_n[n]['y']].append(n)

for c in x_dict:
    for i in range(0,len(x_dict[c]),2):
        dict_n[x_dict[c][i]]['x'] = float(dict_n[x_dict[c][i]]['x'])+2
for c in y_dict:
    for i in range(0,len(y_dict[c]),2):
        dict_n[y_dict[c][i]]['y'] = float(dict_n[y_dict[c][i]]['y'])+2

        
x_dicth = {}
for n,value in hidden_nodes.items():
    x_dicth.update({value[0]:[]})
    
for n,value in hidden_nodes.items():
    x_dicth[value[0]].append(n)
    
y_dicth = {}
for n,value in hidden_nodes.items():
    y_dicth.update({value[1]:[]})
    
for n,value in hidden_nodes.items():
    y_dicth[value[1]].append(n)

for c in x_dicth:
    for i in range(0,len(x_dicth[c]),2):
        hidden_nodes[x_dicth[c][i]][0] = float(hidden_nodes[x_dicth[c][i]][0])+2
        
for c in y_dicth:
    for i in range(0,len(y_dicth[c]),2):
        hidden_nodes[y_dicth[c][i]][1] = float(hidden_nodes[y_dicth[c][i]][1])+2
###########################################################################################################


for key in dict_n:
    graph_data['nodes'].append({
        "id": dict_n[key]['label'],
        "label": dict_n[key]['label'],
        "x": dict_n[key]['x'],
        "y": dict_n[key]['y'],
        "size": size_node,
        "hidden": False,
        "color": default_color_node,
        "piece": False
    })
    
for key in hidden_nodes:
    graph_data['nodes'].append({
        "id": key,
        "label": '',
        "x": hidden_nodes[key][0],
        "y": hidden_nodes[key][1],
        "size": 1,
        "hidden": False,
        "color": default_color_edge,
        "enableHovering": False ,
        "borderSize": 0,
        "piece": True
    })

for key in dict_edges:
    graph_data['edges'].append({
        "id": key,
        "source":  dict_edges[key]['source'],
        "target": dict_edges[key]['target'],
        "type": dict_edges[key]['type'],
        "label": dict_edges[key]['label'],
        "weight": dict_edges[key]['label'],
        "color": default_color_edge,
        "size":size_edge,
        "hover_color": "#1e6add",
        "piece": False
    })

for key in dict_he:
    graph_data['edges'].append({
        "id": key,
        "source":  dict_he[key]['source'],
        "target": dict_he[key]['target'],
        "type": dict_he[key]['type'],
        "label": dict_he[key]['label'],
        "weight": dict_he[key]['label'],
        "color": default_color_edge,
        "size":size_edge,
        "hover_color": "#1e6add",
        "piece": True
    })
