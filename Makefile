all: mainwindow.py studentswindow.py

mainwindow.py: mainwindow.ui
	pyuic4 mainwindow.ui -o mainwindow.py

studentswindow.py: students.ui
	pyuic4 students.ui -o studentswindow.py

run: all
	python main.py

clean: 
	rm *.pyc
	rm *~
