import sys
import json
import re

def json_to_nx_struct(data):

    #data = json.loads(graph)
    nodes = [] #all nodes
    edges = [] #all edges
    first_set_nodes = [] #red nodes
    second_set_nodes =[] #yellow nodes
    first_set_edges = [] #red edges
    second_set_edges = [] #yellow edges
    directed_edges = []
    undirected_edges = []
    weights = []
    for node in data['nodes']:
        if not node.get('piece'):
            nodes.append(node.get('label'))

    for node in data['nodes']:
        if node.get('color') == '#FF5722' and not node.get('piece'):
            first_set_nodes.append(node.get('label'))
    for node in data['nodes']:
        if node.get('color') == '#FFD600' and not node.get('piece'):
            second_set_nodes.append(node.get('label'))

    #not considering broken edges
    broken_edges = []
    broken_weights = []
    broken_color = []
    broken_first = []
    broken_second = []
    broken_type = []
    broken_dir = []
    broken_undir = []
    redw_broken = []
    yelloww_broken = []
    for edge in data['edges']:
        if re.search('hidden*',edge.get('source')) or re.search('hidden*',edge.get('target')):
            broken_edges.append((edge.get('source'),edge.get('target')))
            if re.search('hidden*',edge.get('source')) and not re.search('hidden*',edge.get('target')):
                broken_color.append(edge.get('color'))
            if not re.search('hidden*',edge.get('source')) and re.search('hidden*',edge.get('target')):
                broken_type.append(edge.get('type'))
            if edge.get('weight') != None:
                broken_weights.append(edge.get('weight'))
            if edge.get('weight') != None and edge.get('color') == '#FF5722':
                redw_broken.append(edge.get('weight'))
            if edge.get('weight') != None and edge.get('color') == '#FFD600':
                yelloww_broken.append(edge.get('weight'))
            continue
        edges.append((edge.get('source'),edge.get('target')))
        weights.append(edge.get('weight'))
        if edge.get('color') == '#FF5722':
            first_set_edges.append((edge.get('source'),edge.get('target'),int(edge.get('weight'))))
        if edge.get('color') == '#FFD600':
            second_set_edges.append((edge.get('source'),edge.get('target'),int(edge.get('weight'))))
        if edge.get('type') == 'arrow':
            directed_edges.append((edge.get('source'),edge.get('target'),int(edge.get('weight'))))
        if edge.get('type') == 'line':
            undirected_edges.append((edge.get('source'),edge.get('target'),int(edge.get('weight'))))

    tmp_e = []
    for edge in broken_edges:
        for e in edge:
            if not re.search('hidden*',e):
                tmp_e.append(e)
    tmp_broken = []

    for i in range(0,len(tmp_e),2):
        tmp_broken.append((tmp_e[i],tmp_e[i+1]))

    for i in range(0,len(tmp_broken)):
        if broken_color[i]=='#FF5722':
            broken_first.append(tmp_broken[i])
        if broken_color[i]=='#FFD600':
            broken_second.append(tmp_broken[i])
        if broken_type[i] == 'arrow':
            broken_dir.append(tmp_broken[i])
        if broken_type[i] == 'line':
            broken_undir.append(tmp_broken[i])

    weighted_edges = []	
    weighted_red_b = []
    for i in range(0,len(broken_first)):
        w = (int(redw_broken[i]),)
        weighted_red_b.append(broken_first[i]+w)
    weighted_yellow_b = []
    for i in range(0,len(broken_second)):
        w = (int(yelloww_broken[i]),)
        weighted_yellow_b.append(broken_second[i]+w)

    for i in range(0,len(edges)):
        l_e = edges[i]
        w = (int(weights[i]),)
        weighted_edges.append(l_e+w)

    w_b_de = []
    w_b_unde = []
    for i in range(0,len(tmp_broken)):
        if tmp_broken[i] in broken_dir:
            w = ((int(broken_weights[i]),))
            w_b_de.append(tmp_broken[i]+w)
        if tmp_broken[i] in broken_undir:
            w = ((int(broken_weights[i]),))
            w_b_unde.append(tmp_broken[i]+w)


    first_set_edges = first_set_edges+weighted_red_b
    second_set_edges = second_set_edges+weighted_yellow_b
    directed_edges = directed_edges+w_b_de
    undirected_edges = undirected_edges + w_b_unde
    
    graph_dict = {'nodes':nodes,'first_set_nodes':first_set_nodes,'second_set_nodes':second_set_nodes,'edges':weighted_edges,'dir_edges':directed_edges,'undir_edges':undirected_edges,'first_set_edges':first_set_edges,'second_set_edges':second_set_edges}
    return graph_dict
