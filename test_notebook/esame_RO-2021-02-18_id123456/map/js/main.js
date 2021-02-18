/*!
@authors: Adriano Tumminelli, Marco Emporio, Rosario Di Matteo
*/


var num_modes;
var all_scores=[];
var current_modes=[];
var tot_num_subprob;
var textarea_notes = [];
var documentHash;

window.addEventListener("focus", function(ev)
{
    console.log(ev);
    get_scores();
});

window.addEventListener("load", function(){

    documentHash = hashString(document.documentElement.outerHTML);
    console.log("documentHash: " + documentHash);
    tot_num_subprob = document.querySelectorAll(".select_points").length;
    num_modes=document.querySelector(".submit_mode").length;

    for(var i = 0; i < num_modes; i++) {
        var a = [];
        for(var j = 0; j < tot_num_subprob; j++)
            a.push(0);
        all_scores.push(a);
    }

    //get port from the window url
    const urlParams = new URLSearchParams(window.location.search);
    var port = urlParams.get("port");

    //replace all urls
    if((port && port.match(/^-{0,1}\d+$/)))
    {
        console.log("port", port)
        var links = document.querySelectorAll(".link");
        links.forEach(function(link){
            if(link.href.indexOf("127.0.0.1:8888") != -1)
                link.href = link.href.replace("8888", port + "")
        });
    }


    //add event listeners for textareas
    var areas = document.querySelectorAll(".notes");
    var i = 0;
    areas.forEach(function(element){
        var exercise_index = i;
        element.addEventListener("input", function(){
            textarea_notes[exercise_index] = element.value;
            localStorage.setItem(documentHash + "notes", JSON.stringify(textarea_notes));
        }, false)
        i++;
    })

    //add event listeners for checkbox
    var checkboxes = document.querySelectorAll(".confirm-checkbox");
    checkboxes.forEach(function(checkbox){
        checkbox.addEventListener("change", function(){
            if(checkbox.checked)
            {
                checkbox.previousElementSibling.classList.add("green");
                checkbox.parentElement.parentElement.querySelector(".submit_mode").disabled = true;
            }
            else
            {
                checkbox.previousElementSibling.classList.remove("green");
                checkbox.parentElement.parentElement.querySelector(".submit_mode").disabled = false;
            }

            //attiva il messaggio di errore se non sono state confermate tutte le checkbox
            //var vis = checkAllConfirm() ? "none" : "block";
            //document.getElementById("submit-label").style.display = vis;
        });
    });

    //add event listeners for points selection
    var sel = document.querySelectorAll(".select_points")
    var i = 0;
    sel.forEach(function(element){
        var exercise_index = i;
        var parentAccordion = findSibling(element.parentNode.parentNode.parentNode, "accordion");
        var panel = parentAccordion.nextElementSibling;
        var submit_mode = parentAccordion.querySelector(".submit_mode");
        element.addEventListener("change", function(){
            var current_index_mode = submit_mode.selectedIndex;
            saveScores(exercise_index, current_index_mode, element.selectedIndex);
            updateTotalScoreAll();
        })
        i++;
    })

    //add event listeners for submit-mode selection
    var sel = document.querySelectorAll(".submit_mode");
    var i = 0;
    sel.forEach(function(element){
        element.addEventListener("change", function(){

            updateScores();
            saveSubmitModes();
            changeLink();
            updateTotalScoreAll();
        });
        i++;
    })

    //accordion
    var acc = document.getElementsByClassName("accordion");
    var i;
    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function(event) {

             //prevent click on select nodes
             if(event.target.tagName.toLowerCase() == "select" ||
                event.target.classList.contains("confirm-checkbox") ||
                event.target.tagName.toLowerCase() == "option")
                return;


            //event.preventDefault();
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.maxHeight)
            {
                setIconOpen(this, true);
                panel.style.maxHeight = null;
            }
            else
            {
                setIconOpen(this, false);
                panel.style.maxHeight = panel.scrollHeight + "px";
            }

            //expand parent
            this.parentElement.style.maxHeight = this.parentElement.scrollHeight + "px";
        });
    }

    //numeric inputs
    var numberInputs = document.getElementsByClassName("number");
    for (i = 0; i < numberInputs.length; i++) {
        setInputFilter(numberInputs[i], function(value){
            return /^\d*$/.test(value);
        });
    }

    load();
}, false);

function setIconOpen(element, open)
{
  var classAdd;
  var classRemove;
  if(open) {
    classAdd = 'fa-chevron-down';
    classRemove = 'fa-chevron-up';
  }
  else {
    classAdd = 'fa-chevron-up';
    classRemove = 'fa-chevron-down';
  }

  var child = element.querySelector("." + classRemove);
  if(child)
  {
    child.classList.remove(classRemove);
    child.classList.add(classAdd);
  }
}

// controlla se tutte le checkbox sono checked
function checkAllConfirm(){
    var checkboxes = document.querySelectorAll(".confirm-checkbox");
    var success = true;
    checkboxes.forEach(function(checkbox){
         if(!checkbox.checked)
            success = false;
    });
    return success;
}

function readTextFile(file, func)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                func(rawFile.responseText);
            }
        }
    }
    rawFile.send(null);
}

//update total score of every exercise
function updateTotalScoreAll(){
    var exercises = document.querySelectorAll(".main_exercise")
    exercises.forEach(function(exercise)
    {
        var panel = exercise.nextElementSibling;

        //update selected points (autostimati)
        var sel = panel.querySelectorAll(".select_points");
        var sum=0;
        sel.forEach(function(sel){
            sum += parseInt(sel.value);
        })
        exercise.querySelector(".maxpoints").innerHTML = sum;

        //update punti certi (verificatore)
        var cert = panel.querySelectorAll(".certpoints");
        var sum = 0;
        cert.forEach(function(cert){
            sum += parseInt(cert.innerHTML);
        })
        exercise.querySelector(".certpoints").innerHTML = sum;

    });
}

function exportMap()
{
    //attiva il messaggio di errore se non sono state confermate tutte le checkbox
    /*if(!checkAllConfirm())
    {
        var vis = checkAllConfirm() ? "none" : "block";
        document.getElementById("submit-label").style.display = vis;
        alert("Conferma gli esercizi prima di esportare")
        return;
    }*/

    console.log("exporting map");
    var exercises = document.querySelectorAll(".main_exercise");
    var out_exercises = [];
    var out_confirm_list = "";
    var check_consegna = true;
    exercises.forEach(function(ex){
        var checkbox = ex.querySelector(".confirm-checkbox");
        if(checkbox.checked){
            var pointsElements = ex.querySelectorAll(".maxpoints");
            var total_score = parseInt(pointsElements[0].innerHTML)
            var total_score_max = parseInt(pointsElements[1].innerHTML)
            var submit_mode_idx = ex.querySelector(".submit_mode").selectedIndex;
            var submit_mode = ex.querySelector(".submit_mode").options[submit_mode_idx].innerHTML;
            var ex_name = ex.getElementsByTagName("h3")[0].innerHTML;
            check_consegna  = true;
        }
        else {
            var pointsElements = ex.querySelectorAll(".maxpoints");
            var total_score = "0"
            var total_score_max = parseInt(pointsElements[1].innerHTML)
            var submit_mode_idx = "Nessuno";
            var submit_mode = "Non Consegnato";
            var ex_name = ex.getElementsByTagName("h3")[0].innerHTML;
            check_consegna=false;
        }
        //console.log("total_score" + total_score+"/"+total_score_max, submit_mode, submit_mode_idx);

        var panel = ex.nextElementSibling;
        var tasksAccordions = panel.querySelectorAll(".accordion");
        out_tasks = []
        tasksAccordions.forEach(function(taskAccordion){

            var task_score = parseInt(taskAccordion.querySelector(".select_points").value)
            var task_max_score = parseInt(taskAccordion.querySelector(".maxpoints").innerHTML)

            var task_panel = taskAccordion.nextElementSibling;
            var task_notes = task_panel.querySelector(".notes").value
            out_tasks.push({
                "score" : task_score,
                "score_max" : task_max_score,
                "notes" : task_notes
            });
            //console.log("    score:" + task_score+"/"+task_max_score, task_notes)
        })
        out_exercises.push({
            "exercise_name" : ex_name,
            "total_score": total_score,
            "total_score_max": total_score_max,
            "submit_mode": submit_mode,
            "submit_mode_index": submit_mode_idx,
            "tasks" : out_tasks,
            })
        

        out_confirm_list+=(ex_name+" : " + submit_mode+"\n")
    })


    var out_string = JSON.stringify(out_exercises, null, 2);
    //console.log(out_string, encodeURI(out_string));
    saveMapWithServer(out_string,out_confirm_list);

}

function saveMapWithServer(content,ex_info) {
    if(confirm(ex_info)){
        var client = new XMLHttpRequest();
        console.log(window.location.href)
        client.open("GET", "../server_command?type=save&data=" + encodeURI(content), true);
        client.send();
        client.onreadystatechange = function() {
            if(this.readyState == this.HEADERS_RECEIVED) {
                //basic download in case of error
                var idx = client.statusText.indexOf(' ');
                if(idx != -1)
                {
                    var cmd = client.statusText.substr(0, idx); // "72"
                    var message = client.statusText.substr(idx+1); // "tocirah sneab"

                    if(cmd == "done"){
                        alert(message);
                        //alert("Archivio dell'esame generato correttamente (lo trovi nella cartella 'consegna_esameRO-2020-07-27', sorella del folder entro il quale hai svolto il tuo esame. Se vuoi riprodurre una nuova consegna devi prima rimuovere o spostare questa cartella.)\n\nProcedi subito alla tua sottomissione e chiusura dell'esame (istruzion nel file 'firma_anticipata.txt' che trovi nella cartella 'consegna_esameRO-2020-07-27')")
                    }
                    else if(cmd == "directory_error"){
                        alert(message);
                    }
                    else{
                        download(content,"mappa_esportata.yaml", "text/plain;charset=utf-8");
                        alert(client.statusText + " Mappa scaricata sul browser, ricordati di inviarla insieme all'esame.")
                    }
                }
                else{
                    alert(client.statusText);
                }
            }
        }
    }
}

///chiede al server i punteggi dei verificatori
function get_scores(content) {
    var client = new XMLHttpRequest();
    console.log(window.location.href)
    client.open("GET", "../server_command?type=get_scores&data=0", true);
    client.send();
    client.onreadystatechange = function() {
        if(this.readyState == this.HEADERS_RECEIVED) {

            var points = JSON.parse(client.statusText);
            console.log(points);
            var exercises = document.querySelectorAll(".main_exercise")
            i = 0;
            exercises.forEach(function(exercise)
            {
                ex_points = points[i]; //punteggi dei subtask dell'esercizio i
                console.log("ex_points: ",ex_points)
                if(ex_points != null)
                {
                    var panel = exercise.nextElementSibling;

                    //update punti certi (verificatore)
                    var j = 0;
                    var cert = panel.querySelectorAll(".certpoints");
                    cert.forEach(function(cert) {
                        if(ex_points[j] != -1)
                            cert.innerHTML = ex_points[j];
                        j++
                    })

                }

                i++;
            });

            updateTotalScoreAll();
        }
    }
}

function download(content, fileName, contentType) {
    var a = document.createElement("a");
    var file = new Blob([content], {type: contentType});
    a.href = URL.createObjectURL(file);
    a.download = fileName;
    a.click();
}

function findParent(element, className)
{
    element = element.parentNode;
    while(element)
    {
        if(element.classList && element.classList.contains(className))
            break;

        element = element.parentNode;
    }
    return element;
}


function findSibling(element, className)
{
    element = element.previousSibling;
    while(element)
    {
        if(element.classList && element.classList.contains(className))
            break;

        element = element.previousSibling;
    }
    return element;
}

function load()
{
    //load selected submit modes for each exercise
    var sub = localStorage.getItem(documentHash + 'submit_mode');
    if(sub)
    {
        var loaded_submit_modes = JSON.parse(sub);
            var selected_modes = document.querySelectorAll(".submit_mode")
            var i = 0;
            selected_modes.forEach(function(element){
            element.selectedIndex = loaded_submit_modes[i];
            i++;
        });
    }

    //load all scores
    var pts =localStorage.getItem(documentHash + "points");
    if(pts) {
        all_scores = JSON.parse(pts);
        updateScores();
    }

    //load notes
    var notes = localStorage.getItem(documentHash + "notes");
    if(notes) {
        textarea_notes = JSON.parse(notes);
        //add event listeners for textareas
        var areas = document.querySelectorAll(".notes");
        var i = 0;
        areas.forEach(function(element){
            var exercise_index = i;
            if(textarea_notes[exercise_index])
                element.value = textarea_notes[exercise_index];
            i++;
        })
    }

    updateTotalScoreAll();
}

//change jupyter link based on the selected submition mode
function changeLink() {
    var exercises = document.querySelectorAll(".main_exercise")
    exercises.forEach(function(exercise) {
        actual_mode=exercise.querySelector(".submit_mode").selectedIndex;
        str_actual_mode=actual_mode.toString()
        new_link=exercise.querySelector('[name ='+"\""+str_actual_mode+"\""+']');
        //new_link=exercise.getElementsByTagName(str_actual_mode)
        value=new_link.value
        var link = exercise.getElementsByClassName("link")
        link[0].setAttribute("href",value);
        //console.log(link)
        //link.href=value
        //var prov2 = exercise.getElementsByClassName("link");
        //console.log(prov2)
    })
}

      //load selected score for each exercise
function updateScores() {
      var selected_points = document.querySelectorAll(".select_points")
      var sub_ex_index = 0;
      selected_points.forEach(function(element) {
          var panel = element.parentNode.parentNode.parentNode;
          var accordion = findSibling(panel, "accordion")
          var exercise_submitmode = accordion.querySelector(".submit_mode").selectedIndex;
          element.selectedIndex = all_scores[exercise_submitmode][sub_ex_index];
          sub_ex_index++;
      });
}

function saveSubmitModes() {
    //save submit modes
    var arr_save = [];
    var selected_modes = document.querySelectorAll(".submit_mode");
    var i = 0;
    selected_modes.forEach(function(element) {
        arr_save[i] = element.selectedIndex;
        i++;
    });
    localStorage.setItem(documentHash + 'submit_mode', JSON.stringify(arr_save))
}

/// save in the scores matrix the updated the current selected value index
function saveScores(exercise_index, mode_index, selected_value_index) {
    //save updated score
    all_scores[mode_index][exercise_index] = selected_value_index;
    localStorage.setItem(documentHash + 'points', JSON.stringify(all_scores))
}

function clearStorage(){
    if (confirm('Sei sicuro di voler cancellare tutto?')) {
        localStorage.clear();
        window.location.href = window.location.href;
    }
}
// Restricts input for the given textbox to the given inputFilter function.
function setInputFilter(textbox, inputFilter) {
    ["input", "keydown", "keyup", "mousedown", "mouseup", "select", "contextmenu", "drop"].forEach(function(event) {
        textbox.addEventListener(event, function() {
        if (inputFilter(this.value)) {
            this.oldValue = this.value;
            this.oldSelectionStart = this.selectionStart;
            this.oldSelectionEnd = this.selectionEnd;
        } else if (this.hasOwnProperty("oldValue")) {
            this.value = this.oldValue;
            this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
        } else {
            this.value = "";
        }
        });
    });
}

function hashString(str) {
    var hash = 0, len = str.length
    if (len == 0) return hash;
    for (var i = 0; i < len; i++) {
        hash = hash * 31 + str.charCodeAt(i);
        hash = hash & hash;
    }
    return hash;
}
