compile:
	python compile.py

backup:
	tar -cvf source.tar *.py

restore:
	tar -xvf source.tar

Depoly:
	tar -cvf source.tar *.py
	python compile.py
	rm -rf *.py
	
run:
	python main.py

clean:
	rm -rf *.pyc

clean_source:
	rm -rf *.py
