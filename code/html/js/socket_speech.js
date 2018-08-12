var wsUri = "ws://192.168.43.98:8760";
var output;
var command;

function init() {
	output = document.getElementById("output");
	createWebSocket();
}

function createWebSocket() {
	websocket = new WebSocket(wsUri);

	websocket.onopen = function(evt) {
		onOpen(evt)
	};

	websocket.onmessage = function(evt) {
		onMessage(evt)
	};

	websocket.onerror = function(evt) {
		onError(evt)
	};
}

function onOpen(evt) {
 	// writeToScreen("CONNECTED");
 	doSend(command);
}

function onMessage(evt) {
	if (evt.data != 'failed') {
		//if (evt.data != 'No match found') {
			console.log(evt.data);
			window.location = evt.data;
		//}
		//else{
		//	console.log('I am unable to understand your query. Please speak again!')
		//}
		//writeToScreen('<span style = "color: blue;">Success</span>');
		websocket.close();
	} else {
	    console.log(evt.data);
		//writeToScreen('<span style = "color: blue;">Failed</span>');
	    websocket.close();
	}
}

function onError(evt) {
 	//writeToScreen('<span style="color: red;">ERROR:</span> ' + evt.data);
}

function doSend(message) {
 	//writeToScreen("SENT: " + message);
 	websocket.send(message);
}

function writeToScreen(message) {
	var pre = document.createElement("p");
	pre.style.wordWrap = "break-word";
	pre.innerHTML = message;
	output.appendChild(pre);
}

//window.addEventListener("load", init, false);
//document.getElementById("btn-img-auth").addEventListener("click", init);
