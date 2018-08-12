#!/usr/bin/python36
import cookie


def show_body_content():
	print('''
        
		  <div class="section">
		      <div class="container text-center">
		        <div class="row">
		          <div class="col-md-8 ml-auto mr-auto text-center">
		            <div class="card card-nav-tabs text-center">
		              <div class="card-header card-header-primary">
		                Platform as a Service (PaaS)
		              </div>
		            <div class="card-body">
		            	<br>
						

		            	<form action='paas.py'>
						  <div class="form-group" onclick="listPythonModules()">
						    <label for="exampleFormControlSelect1">Select Platform</label>
						    <select class="form-control" name='package_name' id="exampleFormControlSelect1">
						      <option>Select</option>
						      <option id="python_select" value='python36' >Python</option>
						      <option>JAVA</option>
						      <option>HTML/CSS</option>
						      <option>C/C++</option>
						    </select>
						  </div>

						  <br>
						  <div class="form-group"  id='python_tr' style="display:none">
						    <label for="exampleFormControlSelect2">Select Python Modules</label>
						    <div id="exampleFormControlSelect2">

								  <div class="form-check form-check-inline">
								  <br>
								  <label class="form-check-label">
								    <input class="form-check-input" type="checkbox" id="inlineCheckbox1"  name='module_name' value='python_numpy'> Numpy
								    <span class="form-check-sign">
								        <span class="check"></span>
								    </span>
								  </label>
								</div>
							
								<div class="form-check form-check-inline">
								  <label class="form-check-label">
								    <input class="form-check-input" type="checkbox" id="inlineCheckbox2" name='module_name' value='python_pandas'> Pandas
								    <span class="form-check-sign">
								        <span class="check"></span>
								    </span>
								  </label>
								</div>

								<div class="form-check form-check-inline">
								  <label class="form-check-label">
								    <input class="form-check-input" type="checkbox" id="inlineCheckbox3" name='module_name' value='python_matplotlib'> Matplotlib
								    <span class="form-check-sign">
								        <span class="check"></span>
								    </span>
								  </label>
								</div>

								<div class="form-check form-check-inline">
								  <label class="form-check-label">
								    <input class="form-check-input" type="checkbox" id="inlineCheckbox4" name='module_name' value='python_opencv-python'> Opencv
								    <span class="form-check-sign">
								        <span class="check"></span>
								    </span>
								  </label>
								</div>

								<div class="form-check form-check-inline">
								  <label class="form-check-label">
								    <input class="form-check-input" type="checkbox" id="inlineCheckbox5" name='module_name' value='python_scikit-learn'> scikit-learn
								    <span class="form-check-sign">
								        <span class="check"></span>
								    </span>
								  </label>
								</div>

							   </div>
							</div>
						<br>

						  <button type="submit" class="btn btn-primary">Submit</button>
						</form>



		            </div>
				  </div>
		        </div>
		      </div>
		    </div>
		  </div>

		  <div>
		  	<script>
				function listPythonModules() {
				  var checkBox = document.getElementById("python_select");
				  var python_tr = document.getElementById("python_tr");

				  if (checkBox.selected == true){
				    python_tr.style.display = "block";
				  } else {
				    python_tr.style.display = "none";
				  }
				}
			</script>



            <!-- Add socket JS library -->
            <script src="/js/socket_speech.js"></script>

            <!-- Add speech synthesizer JS library -->
            <script src="/js/say.js"></script>

            <!-- Add speech recognition JS library -->
            <script src="/js/annyang.min.js"></script>

            <!-- Add speech recognition GUI JS library -->
            <script src="/js/speechkitt.min.js"></script>

            <!-- Add speech processor JS library -->
            <script src="/js/speech.js"></script>
        </div>
        ''')


def show_start_content():
	f = open('../html/start_content.txt', 'r')
	print(f.read())
	f.close()


def show_end_content():
	f = open('../html/end_content.txt', 'r')
	print(f.read())
	f.close()


def print_headers():
	print("content-type: text/html \n")

def redirect_login():
	print("""
		<script>window.location = "/login.html";</script>
		""")


def auth_user():
	ck_usr = cookie.auth_client()
	if ck_usr == True:
		pass
	else: 
		redirect_login()


def main():
	print_headers()
	auth_user()
	show_start_content()
	show_body_content()
	show_end_content()


main()