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

test: 
	PYTHONPATH=.:$(PYTHONPATH) nosetests -s

coverage: 
	PYTHONPATH=.:$(PYTHONPATH) nosetests -s --cover-html --with-coverage
	open cover/index.html
