// Configure a few settings for webcam 
Webcam.set({
	width: 640,
	height: 480,
	image_format: 'jpeg',
	jpeg_quality: 90
});

// Display webcam live stream in this id element
Webcam.attach( '#my_camera' );

// Declare global variable
var frame_uri;

function take_snapshot(){
	// Take snapshot and get image data
	Webcam.snap( function(data_uri) {
		// Store captured image uri in global variable
		frame_uri = data_uri;
	});
}
