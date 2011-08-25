mainwindow: mainwindow.ui
	pyuic4 mainwindow.ui -o mainwindow.py

run: mainwindow
	python main.py
