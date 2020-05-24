/*
Position of element in flags_for_js at moment not used
Used try and catch
0: select_color_node
1: drag_node: possibility to drag the node
2: remove_edge: delete a selected edge
3: remove_node: delete a selected node
4: add_node: add a node
5: add_edge: add an edge
6: choice: possibility to chioice between yes or no 
7: edit_label: label on edge or node are editable (TODO)
*/
/*
For camera e drag node use no_editable
0: camera
1: drag node
*/
var g = $graph_data;
var not_editable = $data;
var default_color_node = "#000000";
var default_color_edge = "#828282";
var color_first_set = "#FF5722";
var color_second_set = "#FFD600";
var size_edge = 1;
var size_node = 2;
var directed = false;
var $n = $exercise;
var $s_cell = $submit_cell

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

$s = new sigma({
    graph: g,
    renderer: {
        container: document.getElementById('$container'),
        type: 'canvas'
    },
    settings: {
        minNodeSize: 2,
        maxNodeSize: 6,
        minEdgeSize: 6,
        maxEdgeSize: 6,
        minArrowSize: 1,
        zoomMin: 0.01,
        zoomMax: 5,
        zoomingRatio: 0.9,
        enableEdgeHovering: true,
        doubleClickEnabled: false,
        defaultNodeColor: default_color_node,
        edgeHoverColor: 'edge',
        defaultNodeHoverColor: "#4CAF50",
        defaultEdgeHoverColor: "#1e6add",
        borderSize: 0,
        doubleClickEnabled: false,
        arrowSizeRatio: 5,
        sideMargin: 15,
        autoRescale: ['nodePosition', 'nodeSize', 'edgeSize'],
        rescaleIgnoreSize: true,
        enableHovering: true,
        autoResize: false,
        defaultEdgeLabelSize: 12,
        defaultLabelSize: 12,
        labelThreshold: 2,
        //edgeHoverPrecision:10,
        edgeHoverSizeRatio: 1,
        edgeHoverExtremities: false,
        edgeLabelSize: 'proportional',
        labelSizeRatio: 3,
        defaultLabelSize: 17
    }
});

//pezzi di arco
var ef = $ef;
var nf = $nf;

var dict_ef = JSON.parse(ef.replace(/'/g, "\""));
var dict_nf = JSON.parse(nf.replace(/'/g, "\""));
function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

if (not_editable[0] == "true") {
    $s.settings('enableCamera', false)
    $s.settings('enableHovering', false)
}

if (not_editable[1] != "true") {
    sigma.plugins.dragNodes($s, $s.renderers[0]);
}
var kernel = IPython.notebook.kernel;
var nodes_added = 1
var edges_added = 1
var remove_node = false
var remove_edge = false
var source = false
var target = false
var set_one = false // red 
var set_two = false // yellow
var unselect_set = false // black

/////////////////////////////////////////CLICK EVENT\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

$s.bind('clickNode', function(e) {
    var node = e.data.node;
    var nodeId = node.id
    if (target && directed) {
        var new_edge_id = "e_a_" + source_id + "" + nodeId
        $s.graph.addEdge({
            id: new_edge_id,
            source: source_id,
            target: nodeId,
            type: "arrow",
            label: "1",
            weight: "1",
            color: default_color_edge,
            size: size_edge,
            hover_color: "#4CAF50"
        });
        $s.refresh()
        source_id = null
        target_id = null
        target = false
        directed = false
    }
    if (target) {
        var new_edge_id = "e_a_" + source_id + "" + nodeId
        $s.graph.addEdge({
            id: new_edge_id,
            source: source_id,
            target: nodeId,
            type: "line",
            label: "1",
            weight: "1",
            color: default_color_edge,
            size: size_edge,
            hover_color: "#4CAF50"
        });
        $s.refresh()
        source_id = null
        target_id = null
        target = false
    } else if (source) {
        source_id = nodeId
        source = false
        target = true
    } else if (remove_node) {
        for (n in dict_nf) {
            if (n == nodeId) {
                for (f of new Set(dict_nf[n])) {
                    var true_node = $s.graph.nodes(f)
                    try {
                        if (true_node.piece) {
                            $s.graph.dropNode(f)
                        }
                    } catch {
                        continue
                    }
                }
            }
        }
        $s.graph.dropNode(nodeId)
        $s.refresh()
        remove_node = false
        return
    } else if (set_one) {
        node.color = current_color;
        $s.refresh()
    } else if (set_two) {
        node.color = current_color;
        $s.refresh()
    } else if (unselect_set) {
        node.color = current_color;
        $s.refresh()
    }
});

var to_drop = []

$s.bind('clickEdge', function(event) {
    var edge = event.data.edge;
    var edgeId = edge.id
    if (edge.piece && remove_edge) {
        for (key in dict_ef) {
            if (key == edgeId) {
                for (f of dict_ef[key]) {
                    var e = $s.graph.edges(f)
                    var source = $s.graph.nodes(e.source)
                    var target = $s.graph.nodes(e.target)
                    if (source.piece) {
                        to_drop.push(source.id)
                    }
                    if (target.piece) {
                        to_drop.push(target.id)
                    }
                    $s.graph.dropEdge(f)
                }
            }
        }
        to_drop_set = new Set(to_drop)
        for (node of to_drop_set) {
            $s.graph.dropNode(node)
        }
        to_drop_set = new Set()
        to_drop = []
        remove_edge = false
        $s.refresh()

    }
    if (remove_edge) {
        $s.graph.dropEdge(edgeId)
        $s.refresh()
        to_remove_e = false
        return
    } else if (set_one) {
        for (key in dict_ef) {
            if (key == edgeId) {
                for (f of dict_ef[key]) {
                    var e = $s.graph.edges(f)
                    e.color = current_color
                    var source = $s.graph.nodes(e.source)
                    var target = $s.graph.nodes(e.target)
                    if (source.piece) {
                        source.color = current_color
                    }
                    if (target.piece) {
                        target.color = current_color
                    }
                }
            }
        }
        edge.color = current_color;
        $s.refresh()
    } else if (set_two) {
        for (key in dict_ef) {
            if (key == edgeId) {
                for (f of dict_ef[key]) {
                    var e = $s.graph.edges(f)
                    e.color = current_color
                    var source = $s.graph.nodes(e.source)
                    var target = $s.graph.nodes(e.target)
                    if (source.piece) {
                        source.color = current_color
                    }
                    if (target.piece) {
                        target.color = current_color
                    }
                }
            }
        }
        edge.color = current_color;
        $s.refresh()
    } else if (unselect_set) {
        for (key in dict_ef) {
            if (key == edgeId) {
                for (f of dict_ef[key]) {
                    var e = $s.graph.edges(f)
                    e.color = default_color_edge
                    var source = $s.graph.nodes(e.source)
                    var target = $s.graph.nodes(e.target)
                    if (source.piece) {
                        source.color = default_color_edge
                    }
                    if (target.piece) {
                        target.color = default_color_edge
                    }
                }
            }
        }
        edge.color = default_color_edge;
        $s.refresh()
    } else if (set_weight) {
        change_label(edge)
        $s.refresh()
    }
});

function change_label(edge) {
    var new_weight = prompt("Enter new weight", "1");
    new_weight = parseInt(new_weight)
    if (new_weight != null && new_weight > 0) {
        edge.weight = "" + new_weight;
        edge.label = edge.label + "/" + new_weight
    } else {
        new_weight = edge.weight

        ("Bad value!");
    }
}

try {
    //set weight
    document.getElementById("btn_set_weight" + $n).addEventListener("click", function() {
        set_one = false
        remove_edge = false
        set_two = false
        unselect_set = false
        source = false
        target = false
        set_weight = true

    });
} catch (e) {};


try {
    //add edge
    document.getElementById("btn_add_e" + $n).addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        source = true
        target = false
        set_weight = false
    });
} catch (e) {};


try {
    //add edge
    document.getElementById("btn_add_e_dir" + $n).addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        source = true
        target = false
        directed = true
        set_weight = false

    });
} catch (e) {};


try {
    //yes choice
    document.getElementById("yes" + $n).addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        set_weight = false
        command = "choice=True"
        kernel.execute(command)
    });

    //no choice
    document.getElementById("no" + $n).addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        set_weight = false
        command = "choice=False"
        kernel.execute(command)
    });
} catch (e) {};

//add node
try {
    document.getElementById("btn_add" + $n).addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        set_weight = false
        var newNodeId = prompt("Enter node id:", "");
        if (newNodeId != null) {
            try {
                $s.graph.addNode({
                    id: newNodeId,
                    label: newNodeId,
                    x: 1,
                    y: 1,
                    size: size_node
                });
            } catch (u) {
                alert("Node already exists")
                return
            }
        } else {
            alert("Bad value!");
            return
        }
        nodes_added = nodes_added + 1;
        $s.refresh();
    });
} catch (e) {};

try {
    //selezione colori
    document.getElementById("btn_set_one" + $n).style.backgroundColor = color_first_set
    document.getElementById("btn_set_one" + $n).addEventListener("click", function() {
        set_two = false
        unselect_set = false
        set_one = true
        remove_node = false;
        remove_edge = false;
        set_weight = false
        current_color = color_first_set
    });
    var for_bg = document.getElementById("btn_set_two" + $n);
    for_bg.style.backgroundColor = color_second_set;
    for_bg.style.color = "black";
    document.getElementById("btn_set_two" + $n).addEventListener("click", function() {
        set_one = false
        set_two = true
        set_weight = false
        unselect_set = false
        remove_edge = false;
        remove_node = false;
        current_color = color_second_set
    });

    var for_bg = document.getElementById("btn_unselect_set" + $n);
    for_bg.style.backgroundColor = default_color_node;
    document.getElementById("btn_unselect_set" + $n).addEventListener("click", function() {
        set_one = false
        set_two = false
        set_weight = false
        unselect_set = true
        remove_node = false;
        remove_edge = false;
        current_color = default_color_node;
    });
} catch (e) {};

try {
    //remove node
    document.getElementById("btn_remove" + $n).addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        remove_node = true;
        set_weight = false
        remove_edge = false;
    });
} catch (e) {};



//remove edge
try {
    document.getElementById("btn_remove_e" + $n).addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        remove_edge = true;
        remove_node = false;
        set_weight = false;
    });
} catch (e) {};

//al momento del submit creo json relativi al dizionario contenente le modifiche (graphN) e quello relativo al dizionorario per il render
// del grafo in sigma js
try {
    document.getElementById("save" + $n).addEventListener("click", function() {
        alert('Salvato!')
        var svgString = $s.toSVG();
        var command = `
svg = open('exercise_graph/data/tmp/svg` + $n + `.svg', 'w')
svg.write("""` + svgString + `""")
svg.close()
`;
        kernel.execute(command)
        set_one = false
        set_two = false
        unselect_set = false
        remove_edge = false;
        remove_node = false;
        set_weight = false
        var fullgraph = {
            nodes: $s.graph.nodes(),
            edges: $s.graph.edges()
        }
        var graph_s = JSON.stringify(fullgraph);
        var command = `
textfile = open('exercise_graph/data/tmp/graph_data` + $n + `.json', 'w')
textfile.write("""` + graph_s + `""")
textfile.close()
`;
        kernel.execute(command)
        //sleep(50)
        //IPython.notebook.execute_cells([$s_cell+2])
    });
} catch (e) {};