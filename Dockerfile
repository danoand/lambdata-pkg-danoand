# Dockerfile
FROM debian

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV SHELL=/bin/bash

# Install basic Python development dependencies
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install python3-pip curl wget -y
RUN pip3 install pipenv

# Install pandas
RUN pip3 install pandas 

# Install personal test package
RUN pip3 install -i https://test.pypi.org/simple/ lambdata-pkg-danoand1

# Download test script
RUN wget https://dsfiles.dananderson.dev/files/test_script.py

# Run the test script
RUN python3 test_script.py
