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