prepare:
	-rm -rf web
	mkdir -p web/.zips

unzip:
	cd web && unzip .zips/**

start_server:
	python3 main.py

serve_web_page:
	cd web && python3 -m http.server 8080

open_web_page:
	python3 -m webbrowser http://0.0.0.0:8080