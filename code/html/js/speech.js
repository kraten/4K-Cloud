if (annyang) {
	function askToSpeak(){
		say("What can I help you with?");
	}

	// Commands and functions for Annyang to use
	var greetingFunction = function(tag) {
		command = tag;
		console.log(tag);
		// Call init() function in socket_speech.js
		init();
		SpeechKITT.setAbortCommand(annyang.abort);
		SpeechKITT.abortRecognition();
	}
	// 'ok system' is the hotword that we used and can be changed
	var welcome = {'ok system *tag': greetingFunction};  

	annyang.addCallback('start', askToSpeak);
	//annyang.addCallback('end', SpeechKITT.abortRecognition);
	

	// Add our commands to annyang
	annyang.addCommands(welcome);

	//SpeechKITT.setStartCommand('say');
	

	// Tell KITT to use annyang
	SpeechKITT.annyang();

	// Define a stylesheet for KITT to use
	SpeechKITT.setStylesheet('/css/flat.css');

	// Render KITT's interface
	SpeechKITT.vroom();
}
