#!/usr/bin/python36
import cgi
import cookie
import subprocess as sp


def get_ip(iface):
	ip_cmd = "ifconfig {} | grep inet | head -n 1 | awk '{print $2}'".format(iface)
	ip = (sp.getoutput(iface))[1]
	return ip


def create_dockerfile(os_name, package_list, module_list):
	df_path = '/var/www/cgi-bin/Dockerfile'
	df_content = 'FROM python_paas:v5\n'

	for package in package_list:
		df_content += 'RUN yum install {} -y\n'.format(package)

	for module in module_list:
		if 'python' in module:
			module = (module.split('_'))[1]
			df_content += 'RUN pip3 install {}\n'.format(module)

	# print(df_content)
	# Create dockerfile and set permissions
	sp.getoutput('sudo touch ' + df_path)
	sp.getoutput('sudo chown apache ' + df_path)

	# Write df_content to Dockerfile
	f = open(df_path, 'w')
	f.write(df_content)
	f.close()

	sp.getoutput("sudo cp Dockerfile /var/www/html/downloads/Dockerfile")


def create_paas_container():
	container_name='paas1'

	# Command to switch ansible directory
	change_dir_cmd = "cd ansible"
	run_playbook_cmd = "sudo ansible-playbook ./playbooks/paas.yml --extra-vars 'cname={}'".format(container_name)
	container_status = sp.getstatusoutput(change_dir_cmd + '&&' + run_playbook_cmd)
	print(container_status[1])
	if container_status[0] == 0:
		print('''
			<script LANGUAGE='JavaScript'>
			window.alert('Your development platform setup is done..');
			window.location.href='show_container.py?ip=192.168.43.98&port=1234';
		</script>
		''')
	

def get_form_values():
	form = cgi.FieldStorage()
	os_name = 'centos'
	#os_name = form.getvalue('os_name')
	package_list = form.getvalue('package_name')
	module_list = form.getvalue('module_name')

	# If package_list is a string, convert it to list
	if 'str' in str(type(package_list)):
		package_list = [package_list]

	# If module_list is a string, convert it to list
	if 'str' in str(type(module_list)):
		module_list = [module_list]

	return os_name, package_list, module_list


def show_body_content():
	print('''
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
	
	os_name, package_list, module_list = get_form_values()
	create_dockerfile(os_name, package_list, module_list)
	create_paas_container()
	
	show_start_content()
	show_body_content()
	show_end_content()

main()