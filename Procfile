web: \ 
	cd api && \
	pip install -r requirements.txt && \
	python3 -m venv venv && source venv/bin/activate && \
	gunicorn "main:create_app()"