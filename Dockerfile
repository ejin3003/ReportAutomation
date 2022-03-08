# Docker File: Automation of docker image creation
# 1. Create a file named "Dockerfile"
# 2. Add instructions in Dockerfile
# 3. Build dockerfile to create image
# 4. Run image to create container

# User the python 3 image as the base image
FROM python:3

MAINTAINER Jason Tyson <ejin3003@gmail.com>

# Copy all the files in the current directory, into the newely created app-directory
COPY . /app

# Set the current working directory
WORKDIR /app

CMD python msg.py

# Copy the app files from host machine to image filesystem
# First argument applies to the hos machine: "COPY ..."
# Second argument applies to the image: "./"
#COPY requirements.txt ./

# Set directory for future

