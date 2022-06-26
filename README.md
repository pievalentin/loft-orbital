# Getting started
## Locally
Install depedencies
```bash
poetry install
```
Init the db
```bash
make migrate
```
Now you can run the django server
```bash
make runserver
```
For the fullstack please refer to the docker setup

## Docker
You need docker and docker-compose on your machine.


This command will run all the needed process in the foreground

```bash
make up
```
Press `^C` to exit

## Optional tasks


- [x] [CI See here](/.github/workflows/django.yml)
- [x] Future possible changes:

  Instead of having a process to read temps which is not monitored. It would be better to use a propre scheduled task.
  Celery could be a good fit but the doc is not clear if it can support always on task.
  I would also switch away from sqlite to postgresql. 
- [x] Deployment to prod:

  To deploy to prod, I would use kubernetes. To kickstart the config we can use `kompose` and tailor the config to the specific of our cluster.
  Otherwise if the scaling that k8s offer is not needed, a vps running docker-compose with traefik can be sufficient.
  I woudl also use the recommended prod config for the db and django web server. At the moment they all run on dev mode.