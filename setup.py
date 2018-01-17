#https://docs.python.org/2/distutils/examples.html
from distutils.core import setup
versionDict = {}
with open( "version.py" ) as fp:
    exec( fp.read() , versionDict )
version = versionDict[ '__version__' ]
setup( \
	name = 'WebAPIs' , 
	version = versionDict[ '__version__' ] ,
	author = 'Adam D Scott' ,
	author_email = 'adam@adamscottphd.com' ,
	maintainer = 'Adam D Scott' ,
	maintainer_email = 'adam@adamscottphd.com' ,
	url = 'https://github.com/AdamDS/WebAPIs' ,
	description = 'Web-based APIs toolkit' ,
	long_description = 'Basic toolkit for web-based APIs.' ,
	download_url = 'https://github.com/AdamDS/WebAPIs/archive/' + \
		version + '.tar.gz' ,
	classifiers = [ \
		"License :: OSI Approved :: MIT License " , 
		"Programming Language :: Python" , 
		"Programming Language :: Python :: 2.7" , 
		"Development Status :: 4 - Beta" , 
		"Intended Audience :: Developers" , 
		"Topic :: Internet" , 
	] ,
	license = 'MIT' ,
	package_dir = { 'webapi' : 'webapi' , 
	} ,
	packages = [ \
		'webapi' ,
		'webapi.webapi' ,
	] , #each of the directories with modules (aka packages)
	requires = [ \
		'AdvancedHTMLParser' ,
		'requests' ,
	] , #auto installs with pip install
)
