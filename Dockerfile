#My first dockerFile
FROM python:3

#set working directory to robo
WORKDIR /dockerTrial

#copy the current directory contents into the container 
ADD . /dockerTrial 

#Run robo.py when the container launches
CMD ["echo", "ImageCreated& abt To launch"]
CMD ["python3", "robo.py"]

