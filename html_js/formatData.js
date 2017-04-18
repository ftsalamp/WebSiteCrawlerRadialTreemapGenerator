var json;

function getChildrenCount(tree){
	return tree.children.length;
}
		
function createTree(parentUrl, tree){
	var children = [];
			
	for(var i=0; i<json.length; i++){
	var curLink = json[i];
		if(curLink["referer"] == parentUrl){
			//console.log("Found one for "+parentUrl);
			children.push({
				"name" : curLink["url"],
				"children" : [],
				"size" : curLink["Simhash"]
			});
		}
	}
	tree.children = children;
	return tree;
}
	
	
readTextFile("./radial.json", function(text){
	var data = JSON.parse(text);
	console.log(data);
	json = data;
	var parentUrl = json[0]['referer'];
	var tree = {
		"name" : parentUrl,
		"children" : null
	};
	var finalTree = createTree(parentUrl,tree);
	var max_depth = 3;
	
	putChildren(finalTree);
	download('final.json', JSON.stringify(finalTree));
});

function putChildren(finalTree){
	for(var i=0; i<finalTree.children.length; i++){
		finalTree.children[i] = createTree(finalTree.children[i].name,finalTree.children[i]);
    }
            
	for(var i=0; i<finalTree.children.length; i++){
		putChildren(finalTree.children[i]);
    }
}
        
        
        
function download(filename, text) {
	var pom = document.createElement('a');
	pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
	pom.setAttribute('download', filename);

	if (document.createEvent) {
		var event = document.createEvent('MouseEvents');
		event.initEvent('click', true, true);
		pom.dispatchEvent(event);
    } else {
		pom.click();
    }
}
		
function readTextFile(file, callback) {
	var rawFile = new XMLHttpRequest();
	rawFile.overrideMimeType("application/json");
	rawFile.open("GET", file, true);
	rawFile.onreadystatechange = function() {
		if (rawFile.readyState === 4 && rawFile.status == "200") {
        	callback(rawFile.responseText);
        }
    }
	rawFile.send(null);
}


        
