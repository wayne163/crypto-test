# -*- coding: utf-8 -*-
import os,sys
path_list = ['static/ic/js/','static/works-gopro/js/']
file_list = ['app/','lib/','main.js']
dir_list = [
	{
		'base_path': 'static/ic/js/',
		'file_list': ['app/','lib/','main.js']
	},
	{
		'base_path': 'static/works-gopro/js/',
		'file_list': ['app/','lib/','main.js']
	}
]

def reset():
	os.system('git reset --hard')
	os.system('git pull')

def deploy():
	command = 'rm -rf '
	for dirname in dir_list:
		for f in dirname['file_list']:
			print command+dirname['base_path']+f
			os.system(command+dirname['base_path']+f)


if __name__ == '__main__': 
	if len(sys.argv) <2:
		print 'lost argument'
		sys.exit(0)
	pwd = sys.argv[1]
	if pwd == 'auto3d':
		reset()
		deploy()
		print 'success'
	else:
		print 'wrong password'
