[![HitCount](http://hits.dwyl.io/ro6ley/django_ec2.svg)](http://hits.dwyl.io/ro6ley/django_ec2)

# Django AWS (Integrating Django, EC2, S3, & RDS)

This repository contains the code for this [blogpost](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/).

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- [ ] [Docker](https://www.docker.com/products/docker-desktop)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application
Running the App
```
> git clone https://github.com/raunak-r/django_ec2.git

Open Docker (WINDOWS, See DockerFile first 3 lines.)
> cd <path>/django_ec2/
> docker build -t django_ec2 -f .\deployment\dockerfile .
> docker run -p 8000:8000 django_ec2
Visit localhost:8000 on Chrome.
```

### Setting Up EC2
1. Launch EC2 instance as outlined in this [article](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/)
2. Download .pem file (this is the private key for the ec2)
3. Open WSL
```
> cp private key to the wsl .ssh folder
> chmod 400
>  ssh -i private-key.pem ec2-username@ec2-link.amazonaws.com

> sudo yum upgrade
> sudo yum install git

> git clone https://github.com/raunak-r/django_ec2.git
> docker build -t django_ec2 -f ./deployment/dockerfile .
> docker run -p 8000:8000 django_ec2
Visit ip-addr:8000/ on Chrome on Local
```

## OLD COMMANDS FROM Ro6ley's README

### Setting up everything for your development

1. Clone the repository
```
$ git clone https://github.com/ro6ley/django_ec2.git
```

2. Check into the cloned repository
```
$ cd django_ec2
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
> sudo apt install postgresql postgresql-contrib
> sudo apt-get install postgresql
> sudo apt-get install python-psycopg2
> sudo apt-get install libpq-dev
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

5. Start the Django API
```
$ python manage.py runserver
```

6. Navigate to `http://localhost:8000`

7. Build the Docker image:
```
$ docker build . -t django_ec2
```

8. Publish the Docker image to Dockerhub:
```
$ docker tag django_ec2 <DOCKERHUB_USERNAME>/django_ec2
$ docker push <DOCKERHUB_USERNAME>/django_ec2
```

9. Deploy on AWS EC2 as outlined in this [article](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/)
