#!/usr/bin/python36
import cookie


def show_html():	
	print("""
		<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <link rel="apple-touch-icon" sizes="76x76" href="/assets/img/apple-icon.png">
  <link rel="icon" type="image/png" href="/assets/img/favicon.png">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <title>
    4K Cloud Technology Services
  </title>
  <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />
  <!--     Fonts and icons     -->
  <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Roboto+Slab:400,700|Material+Icons" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css">
  <!-- CSS Files -->
  <link href="/assets/css/material-kit.css?v=2.0.3" rel="stylesheet" />
  <!-- CSS Just for demo purpose, don't include it in your project -->
  <link href="/assets/demo/demo.css" rel="stylesheet" />
</head>

<body class="index-page sidebar-collapse">
  <nav class="navbar navbar-transparent navbar-color-on-scroll fixed-top navbar-expand-lg" color-on-scroll="100" id="sectionsNav">
    <div class="container">
      <div class="navbar-translate">
        <a class="navbar-brand" href="/index.html">
          4K Technology </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
          <span class="navbar-toggler-icon"></span>
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="dropdown nav-item">
            <a href="#" class="dropdown-toggle nav-link" data-toggle="dropdown">
              <i class="material-icons">apps</i>Cloud Services
            </a>
            <div class="dropdown-menu dropdown-with-icons">
              <a href="#" class="dropdown-item">
                <i class="material-icons">gamepad</i> Software as a Service
              </a>
              <a href="#" class="dropdown-item">
                <i class="material-icons">code</i> Platform as a Service
              </a>
			  <a href="#" class="dropdown-item">
                <i class="material-icons">layers</i> Container as a Service
              </a>
			  <a href="#" class="dropdown-item">
                <i class="material-icons">cloud_circle</i> Storage as a Service
              </a>
            </div>
          </li>
		  
		  <li class="dropdown nav-item">
            <a href="#" class="dropdown-toggle nav-link" data-toggle="dropdown">
              <i class="material-icons">storage</i>Big Data
            </a>
            <div class="dropdown-menu dropdown-with-icons">
              <a href="#" class="dropdown-item">
                <i class="material-icons">layers</i> Automate Hadoop
              </a>
              <a href="#" class="dropdown-item">
                <i class="material-icons">memory</i> Automate Map Reduce
              </a>
            </div>
          </li>
		  
		<li class="nav-item" style="display:none">
                <a class="nav-link" href="/login.html">
              <i class="fa fa-sign-in"></i> Login
            <div class="ripple-container"></div></a>
          </li>
		  
		  <li class="nav-item" style="display:none">
			<a href="#pablo" class="btn btn-rose btn-raised btn-round btn-sm" data-toggle="dropdown">
			  Register
			</a>
		  </li>

		  <li class="dropdown nav-item" style="display:block">
                    <a href="#pablo" class="profile-photo dropdown-toggle nav-link" data-toggle="dropdown">
                      <div class="profile-photo-small">
                        <img src="/assets/img/faces/avatar.jpg" alt="Circle Image" class="rounded-circle img-fluid">
                      </div>
                    <div class="ripple-container"></div></a>
                    <div class="dropdown-menu dropdown-menu-right">
                      <h6 class="dropdown-header">Dropdown header</h6>
                      <a href="#pablo" class="dropdown-item">Me</a>
                      <a href="#pablo" class="dropdown-item">Settings and other stuff</a>
                      <a href="#pablo" class="dropdown-item">Sign out</a>
                    </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div class="page-header header-filter clear-filter purple-filter" data-parallax="true" style="background-image: url('/assets/img/bg2.jpg');">
    <div class="container">
      <div class="row">
        <div class="col-md-8 ml-auto mr-auto">
          <div class="brand">
            <h1>4K Tech Solutions</h1>
            <h3>Automate stuff at your fingertips</h3>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="main main-raised">
    <div class="section section-basic">
      <div class="container"> 
        
		  <div class="section">
		      <div class="container text-center">
		        <div class="row">
		          <div class="col-md-8 ml-auto mr-auto text-center">
		            <div class="card card-nav-tabs text-center">
		              <div class="card-header card-header-primary">
		                Storage as a Service (STaaS)
		              </div>
		            <div class="card-body">
		            	<br>
						<form action='staas.py'>
							<div class="form-group">
							    <label for="username">Username</label>
							    <input type="text" class="form-control" id="username" name='u'>
							 </div>
							  <div class="form-group">
							    <label for="size">Size in GB</label>
							    <input type="text" class="form-control" id="size" name='s' placeholder="2G">
							  </div>
							<button type="submit" class="btn btn-primary">Submit</button>
						</form> 


		            </div>
				  </div>
		        </div>
		      </div>
		    </div>
		  </div>



      </div>
    </div>
  </div>
  
  
  <footer class="footer" data-background-color="black">
    <div class="container">
      <nav class="float-left">
        <ul>
          <li>
            <a href="#">
              Home
            </a>
          </li>
          <li>
            <a href="#">
              About Us
            </a>
          </li>
          <li>
            <a href="#">
              Services
            </a>
          </li>
          <li>
            <a href="#">
              Licenses
            </a>
          </li>
        </ul>
      </nav>
      <div class="copyright float-right">
        &copy;
        <script>
          document.write(new Date().getFullYear())
        </script>, made with <i class="material-icons">favorite</i> by
        <a href="#" target="_blank">4K</a> Developers
      </div>
    </div>
  </footer>
  <!--   Core JS Files   -->
  <script src="/assets/js/core/jquery.min.js" type="text/javascript"></script>
  <script src="/assets/js/core/popper.min.js" type="text/javascript"></script>
  <script src="/assets/js/core/bootstrap-material-design.min.js" type="text/javascript"></script>
  <script src="/assets/js/plugins/moment.min.js"></script>
  <!--	Plugin for the Datepicker, full documentation here: https://github.com/Eonasdan/bootstrap-datetimepicker -->
  <script src="/assets/js/plugins/bootstrap-datetimepicker.js" type="text/javascript"></script>
  <!--  Plugin for the Sliders, full documentation here: http://refreshless.com/nouislider/ -->
  <script src="/assets/js/plugins/nouislider.min.js" type="text/javascript"></script>
  <!-- Control Center for Now Ui Kit: parallax effects, scripts for the example pages etc -->
  <script src="/assets/js/material-kit.js?v=2.0.3" type="text/javascript"></script>
  <script>
    $(document).ready(function() {
      //init DateTimePickers
      materialKit.initFormExtendedDatetimepickers();

      // Sliders Init
      materialKit.initSliders();
    });


    function scrollToDownload() {
      if ($('.section-download').length != 0) {
        $("html, body").animate({
          scrollTop: $('.section-download').offset().top
        }, 1000);
      }
    }
  </script>
</body>

</html>
	""")


def redirect_login():
	print("""
		<script>window.location = "/login.html";</script>

		""")



# IMPORTANT: Disable SELINUX

print('content-type: text/html')
#print(cookie.set_cookie('kb'))
print()


ck_usr = cookie.auth_client()
if ck_usr == True:
	show_html()
else: 
	redirect_login()