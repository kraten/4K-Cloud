import face_recognition

def whoiam(filename):
	# Picture of Registered Client
	picture_of_me = face_recognition.load_image_file('./images/users/kb.jpg')
	my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

	# Picture of client to authenticate
	unknown_picture = face_recognition.load_image_file(filename)
	unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

	# Now we can see the two face encodings are of the same person with `compare_faces`!
	results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
	return results[0]
