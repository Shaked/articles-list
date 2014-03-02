help:                                                            						
	@echo 'Usage:                                                                 		'
	@echo '   make install                     	install unit test packages          	'	
	@echo '   make clean                       	clean coverage folder					'
	@echo '   make test                  		run unit test 							'
	@echo '   make coverage                 	run unit test, coverage and open browser'


install-2.7: 
	sudo pip install pelican
	sudo pip install -U mock
	sudo pip install nose
	sudo pip install coverage

install-3.3: 
	sudo pip3 install pelican
	sudo pip3 install -U mock
	sudo pip3 install nose
	sudo pip3 install coverage

clean: 
	rm -rf cover/

_python3_tests_fix:
	export PYTHONPATH=`pwd` # https://github.com/nose-devs/nose/issues/538 (python3.3 fails to find)

test:  _python3_tests_fix
	nosetests -s

coverage: _python3_tests_fix
	nosetests --cover-html --with-coverage
	open cover/index.html
