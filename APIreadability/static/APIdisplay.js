var current_data = null;
var link_ids = null;
var largest_stored_key = null;

function sort_list(data_arrays) {
    var largest_array_size = 0;
    var largest_key = [];
    var legacy_largest_key = [];
    current_data["1"] = [];
    var data_size = 0;
    var current_data_size = 0;
    var first_time = true;
    for(var key in data_arrays) {
        data_size++;
    }
    while(current_data_size <= data_size) {
        for(var key in data_arrays) {
            if(find_in_legacy_list(legacy_largest_key, key) == false) {
                console.log(data_arrays[key].length);
                if(data_arrays[key].length > largest_array_size) {
                    // checks to see if the current key is already stored
                    // keeps track of the new largest array size
                    largest_array_size = data_arrays[key].length;
                    // empty the array of largest keys
                    largest_key = [];
                    if(first_time) {
                        largest_stored_key = key;
                    }
                    // push the new largest key into the array
                    largest_key.push(key);
                }
                else if(data_arrays[key].length == largest_array_size) {
                    for(var legacy_key in legacy_largest_key) {
                        if(key == legacy_largest_key[legacy_key]) {
                            break;
                        }
                    }
                    // push the key that is tied with the current largest
                    largest_key.push(key);
                }
            }
        }
        for(var key in largest_key) {
            legacy_largest_key.push(largest_key[key]);
            current_data_size++;
            current_data["1"][largest_key[key]] = data_arrays[largest_key[key]];
        }
        largest_array_size = 0;
    }
}

function find_in_legacy_list(list, current_key) {
    for(var legacy_key in list) {
        if(current_key == list[legacy_key]) {
            return true;
        }
    }
    return false;
}

function create_list() {
    var search = document.getElementById("name").value;
    var loader = document.createElement("div");
    $(loader).attr("class", "loader");
    document.getElementById("left_menu").appendChild(loader);

    // calls the function within app.py 
    $.getJSON("http://127.0.0.1:5000/search_api", {
        API: search
    }, function(data) {
        console.log(data);
        current_data = {};
        current_data["0"] = data["0"];
        sort_list(data["1"]);
        display_all();
        display_all();

        if(data["0"].length == 0) {
            current_data = null;
            // popup?
        }
        else {
            var counter = 0;
            var links = [];
            loader.style.visibility = "hidden";
            for(var key in current_data["1"]) {
                counter++;
                var button = document.createElement("button");
                var button_id = "Word" + counter.toString();
                var text = current_data["1"][key];
                $(button).attr("id", button_id);
                $(button).attr("class", "collapsible");
                document.getElementById("left_list").appendChild(button);
                var question_counter = 0;
                for(var question in text) {
                    question_counter++;
                    var button_node = document.createElement("button");
                    var button_node_id = button_id + "question" + question_counter;
                    $(button_node).attr("id", button_node_id);
                    $(button_node).attr("class", "content");
                    document.getElementById("left_list").appendChild(button_node);
                    document.getElementById(button_node_id).innerHTML = text[question];
                    document.getElementById(button_node_id).addEventListener("click", function() {
                        this.classList.toggle("node_active");
                        console.log("button node click");
                        for(var key in current_data["0"]) {
                            if(key == this.innerHTML) {
                                var search_target = current_data["0"][key];
                                for(var i = 0; i < link_ids.length; i++) {
                                    if(search_target.link(search_target) == document.getElementById(link_ids[i]).innerHTML) {
                                        if(document.getElementById(link_ids[i]).style.display == "none") {
                                            console.log("Display link");
                                            document.getElementById(link_ids[i]).style.display = "block";
                                        }
                                        else {
                                            console.log("Remove link");
                                            document.getElementById(link_ids[i]).style.display = "none";
                                        }
                                    }
                                }
                            }
                        }
                    });
                }
                document.getElementById(button_id).innerHTML = key;
                document.getElementById(button_id).addEventListener("click", function() {
                    this.classList.toggle("active");
                    console.log("button click");
                    var content = this.nextElementSibling;
                    while(content.className != "collapsible") {
                        if (content.style.display === "block") {
                            content.style.display = "none";
                            console.log("close:" + content.innerHTML);
                        } else {
                            content.style.display = "block";
                            console.log("open:" + content.innerHTML);
                        }
                        content = content.nextElementSibling;
                    }
                });
                document.getElementById(button_id).style.visibility = "visible";
            }
        }
    });
}

// displays the links on the right side
function display_all() {
    console.log("display all");
    if(link_ids != null) {
        console.log("not the first time");
        if(link_ids.length > 0) {
            console.log("there are links");
            if(document.getElementById(link_ids[0]).style.display == "block") {
                console.log("there are links displayed");
                for(var i = 0; i < link_ids.length; i++) {
                    document.getElementById(link_ids[i]).style.display = "none";
                }
                document.getElementById("display_all").innerHTML = "Display All Relevant Links";
                return;
            }
        }
    }
    if(current_data != null) {
        var counter = 0;
        link_ids = [];
        for(var key in current_data["0"]) {
            counter++;
            var node = document.createElement("P");
            var text = current_data["0"][key];
            var link_id = "Link" + counter.toString();
            $(node).attr("id", link_id);
            link_ids.push(link_id)
            document.getElementById("right_list").appendChild(node);
            set_links(link_id, text);
            document.getElementById("display_all").innerHTML = "Remove All";
        }
    }
}

function set_links(ID, text) {
    document.getElementById(ID).style.color = "skyblue";
    document.getElementById(ID).style.textDecoration = "underline";
    document.getElementById(ID).style.paddingRight = "15px";
    document.getElementById(ID).innerHTML = text.link(text);
    document.getElementById(ID).style.display = "block";
}