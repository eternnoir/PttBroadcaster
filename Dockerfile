#
# Python Dockerfile
#

# Pull base image.
FROM dockerfile/ubuntu

# Install Python.
RUN apt-get install -y python python-dev python-pip python-virtualenv

ADD . /src
RUN mkdir -p /shlib/PyrserPTT

RUN git clone https://github.com/eternnoir/PyrserPTT.git /shlib/PyrserPTT

RUN cd /shlib/PyrserPTT; python /shlib/PyrserPTT/setup.py install

RUN pip install -r /src/requirements.txt

# Define default command.
CMD ["python","/src/runserver.py"]
