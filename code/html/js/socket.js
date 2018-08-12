var wsUri = "ws://192.168.43.98:8765";
var output;

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
 	doSend(frame_uri);
}

function onMessage(evt) {
	if (evt.data != 'failed') {
		document.cookie = "secret=" + evt.data;
		window.location = "cgi-bin/list_services.py";
		websocket.close();
	} else {
	    writeToScreen('<span style = "color: blue;">Failed: Try to login again</span>');
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
document.getElementById("btn-img-auth").addEventListener("click", init);
