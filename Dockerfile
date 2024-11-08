FROM ubuntu:latest
# run as root
USER root

RUN apt-get update \
    #  && apt install mongodb \
    && apt-get install -y python3-pip python3-dev

WORKDIR /asande-api-api

COPY ./requirements.txt /asande-api/requirements.txt
# We copy just the requirements.txt first to leverage Docker cache
# COPY ./Pipifile /project_404

#COPY ./pip.ini /etc/pip.conf
#RUN apk add build-base
#CMD ['yum', 'install python3-devel mysql-devel']
#RUN python3 -m pip install --upgrade pip

#RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt



COPY . /asande-api-api
#RUN chmod 777 ./mongo-db-install.sh

# Install MongoDB
#RUN apt-get install wget
#RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
#RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
#RUN apt-get update
#RUN apt-get install -y mongodb-org
ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]
#ENTRYPOINT [ "/bin/sh", "mongo-db-install.sh" ]

# run as non-root

#CMD [ "python3", "app.py" ]