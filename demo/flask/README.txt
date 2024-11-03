# https://developers.redhat.com/articles/2023/08/17/how-deploy-flask-application-python-gunicorn?sc_cid=7013a000003So3aAAC

cd src

# step 1:
flask --app app run

# step 2:
gunicorn --config gunicorn_config.py app:app

# testing
$ curl -XPOST -d "text=# Hello World!" localhost:8080
<h1>Hello World!</h1>

# step 3:
docker build -t hello-flask:1.0.0 .

