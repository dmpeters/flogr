from fabric.api import local, task
from fabric.operations import prompt
from fabric.contrib.console import confirm

@task
def init():
	# Touch README
	local('rm README.md')
	readme = prompt('Enter breif description for README: ').lower()
	local('echo "%s" > README.md' % (readme))
	
	# Set Up App
	app_name = prompt("Enter App Name: ").lower()
	local("mkdir -p %s/{api,resources,services,tasks}" % (app_name))
	local("cd %s && for DIR in $(find . -type d); do touch $DIR/__init__.py; done" % (app_name))
	
	# Set Up Static Media
	media = prompt("Setup Static Media (Y/N): ")
	if(media == "Y"):
		local("mkdir -p public/{css,js,img}")
		local("mkdir -p public/css/src && mkdir -p public/js/lib")
		local("cd public && for DIR in $(find . -type d); do touch $DIR/empty; done")
	else:
		pass
	
	# Setup Git
	local("rm -rf .git/ && git init && git add .")
	commit = prompt("Git Commit Message: ").lower()
	local("git commit -m %s" % (commit))
	origin = prompt("Add Origin: ")
	local("git remote add origin %s && git push -u origin master" % (origin))


@task
def run(target="run.py"):
    local("python {}".format(target))

'''
TODO: Fabric task for api
TODO: Fabric task for resources
TODO: Fabric task for services
TODO: Fabric task for tasks
'''