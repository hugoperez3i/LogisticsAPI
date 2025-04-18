Setup:
	zypper install -y python3
test:
	python3 -m unittest discover tests
delete:
	rm -rf __pycache__ && rm -rf tests/__pycache__
	clear