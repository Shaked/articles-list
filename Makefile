help:                                                            						
	@echo 'Usage:                                                                 		'
	@echo '   make install                     	install unit test packages          	'	
	@echo '   make clean                       	clean coverage folder					'
	@echo '   make test                  		run unit test 							'
	@echo '   make coverage                 	run unit test, coverage and open browser'


install: 
	sudo pip install -U mock
	udo  pip install nose
	sudo pip install coverage

clean: 
	rm -rf cover/

test: 
	nosetests -s

coverage: 
	nosetests --cover-html --with-coverage
	open cover/index.html
