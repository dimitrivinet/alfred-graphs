prepare:
	-rm -rf web
	mkdir -p web/.zips

unzip:
	cd web && unzip .zips/**

start_server:
	python3 main.py