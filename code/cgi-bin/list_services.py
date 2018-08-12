#!/usr/bin/python36
import cookie


def show_body_content():
  print('''
        <div class="text-center">
          <div class="row">
            <div class="col-md-8 ml-auto mr-auto">
              <h2 class="title">Let&apos;s talk about services</h2>
              <h5 class="description">Cloud Computing is a process of delivering/enabling scalable, expandable and almost perfectly elastic software services using internet technologies.</h5>
            </div>
          </div>
          <div class="features">
            <div class="row">
              <div class="col-md-4">
                <div class="info">
                  <div class="icon icon-info">
                    <i class="material-icons">gamepad</i>
                  </div>
                  <a href='get_saas.py'>
                  <h4 class="info-title">Software as a Service</h4>
                  <p>Software as a service is a software distribution model in which a third-party provider hosts applications and makes them available to customers over the Internet.</p>
                  </a>
                </div>
              </div>
              <div class="col-md-4">
                <div class="info">
                  <div class="icon icon-success">
                    <i class="material-icons">code</i>
                  </div>
                  <a href='get_paas.py'>
                  <h4 class="info-title">Platform as a Service</h4>
                  <p>Platform as a service provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the infrastructure.</p>
                  </a>
                </div>
              </div>
              <div class="col-md-4">
                <div class="info">
                  <div class="icon icon-danger">
                    <i class="material-icons">layers</i>
                  </div>
                  <a href='get_caas.py'>
                  <h4 class="info-title">Container as a Service</h4>
                  <p>Containers-as-a-Service is an emerging services offering for container-based virtualization in which providers offer a complete framework to customers ..</p>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <div class="features">
            <div class="row">
              <div class="col-md-4">
                <div class="info">
                  <div class="icon icon-rose">
                    <i class="material-icons">cloud_circle</i>
                  </div>
                  <a href='get_staas.py'>
                  <h4 class="info-title">Storage as a Service</h4>
                  <p>Storage as a service is a business model in which a company leases or rents its storage infrastructure to another company or individuals to store data.</p>
                  </a>
                </div>
              </div>
              <div class="col-md-4">
                <div class="info">
                  <div class="icon icon-warning">
                    <i class="material-icons">storage</i>
                  </div>
                  <a href='get_hadoop_cluster.py'>
                  <h4 class="info-title">Automate Setup Hadoop Cluster</h4>
                  <p>Automating hadoop cluster needs time and incorporate complexity. Use our service to automate hadoop setup with oneclick..</p>
                  </a>
                </div>
              </div>
              <div class="col-md-4">
                <div class="info">
                  <div class="icon icon-primary">
                    <i class="material-icons">memory</i>
                  </div>
                  <a href='get_hadoop_cluster.py'>
                  <h4 class="info-title">Automate Setup Map Reduce Cluster</h4>
                  <p>Automating hadoop map reduce cluster needs time and incorporate complexity. Use our service to automate map-reduce setup with oneclick..</p>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div> 

        <div>
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