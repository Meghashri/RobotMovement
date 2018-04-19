# RobotMovement
Simulating robot movement in 2D 

For Docker container
sudo docker build --tag roboimage:0.1 .
Sending build context to Docker daemon  73.22kB
Step 1/5 : FROM python:3
 ---> efb6baa1169f
Step 2/5 : WORKDIR /dockerTrial
Removing intermediate container 386b110578b1
 ---> 1b40ad149f0d
Step 3/5 : ADD . /dockerTrial
 ---> 71e54daeb8e0
Step 4/5 : CMD ["echo", "ImageCreated& abt To launch"]
 ---> Running in a564fa46f717
Removing intermediate container a564fa46f717
 ---> c928ca2a8bc4
Step 5/5 : CMD ["python3", "robo.py"]
 ---> Running in 5107eef01e69
Removing intermediate container 5107eef01e69
 ---> da92f1839435
Successfully built da92f1839435
Successfully tagged roboimage:0.1

sudo docker run roboimage:0.1
{"type": "robot" , "position": {"x": 1 "y": 3 }, "bearing":" north "}
{"type": "robot" , "position": {"x": 5 "y": 1 }, "bearing":" east "}
--------------------UNIT TEST TC OUTPUT BELOW--------------------
{"type": "robot" , "position": {"x": 0 "y": 0 }, "bearing":" south "}
test case passed
{"type": "robot" , "position": {"x": 0 "y": 0 }, "bearing":" south "}
test case passed
{"type": "robot" , "position": {"x": 3 "y": 5 }, "bearing":" north "}
test case passed
{"type": "robot" , "position": {"x": 3 "y": 3 }, "bearing":" south "}
test case passed
