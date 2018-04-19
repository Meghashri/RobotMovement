#!/usr/bin/python
import json
import sys
import enum

asteroidPosition = {'x': 0, 'y': 0}

class Robo:
    def __init__(self,xValue,yValue,intialdirection):
      self.position = {'x': xValue, 'y':yValue}
      self.direction = intialdirection
      return;

    def printRoboDetails(self):
      print ('{"type": "robot" , "position": {"x":',self.position['x'],'"y":',self.position['y'],'}, "bearing":"', self.direction,'"}')
      return;
      
    def moveForward(self):
      if self.direction == "west":
          self.position['x'] = self.position['x'] - 1
      elif self.direction == "east":
          self.position['x'] = self.position['x']+ 1
      elif self.direction == "north":
          self.position['y'] = self.position['y'] + 1
      elif self.direction == "south":
          self.position['y'] = self.position['y'] - 1       
      return;
        
    def turnLeft(self):
      if self.direction == "north":
        self.direction = "west"
      elif self.direction == "south":
        self.direction = "east"
      elif self.direction == "east":
        self.direction = "north"
      elif self.direction == "west":
        self.direction = "south"
      return;
        
    def turnRight(self):
      if self.direction == "north":
        self.direction = "east"
      elif self.direction == "south":
        self.direction = "west"
      elif self.direction == "east":
        self.direction = "south"
      elif self.direction == "west":
        self.direction = "north"
      return;
         
        
### =========class defn done===============================

## TESTING CODE
      
#####===================LETS TEST (TDD)======================

class RoboTest:
    roboMockObject = Robo(0,0,"none") #has-a relationship to create mocks/stubs
    expectedPosition = {"x":0,"y":0}
    expectedDirection = "NONE"

    #To test if the robot turns to the right direction on its left
    def turnLeftTest(self,turns):
        for counter in range(0,turns):
            self.roboMockObject.turnLeft()
        self.roboMockObject.printRoboDetails()
        if self.expectedDirection == self.roboMockObject.direction:
            print('test case passed');
        else:
            print('test case failed');
        return

    #To test if the robot turns to the right direction on its right
    def turnRightTest(self,turns):
        for counter in range(0,turns):
            self.roboMockObject.turnRight()
        self.roboMockObject.printRoboDetails()
        if self.expectedDirection == self.roboMockObject.direction:
            print('test case passed');
        else:
            print('test case failed');
        return

    #To Test if robot moves to right coordinates with given moves
    def moveForwardTest(self,steps):
        for counter in range(0,steps):
            self.roboMockObject.moveForward()
        self.roboMockObject.printRoboDetails()
        if self.expectedPosition['x'] == self.roboMockObject.position['x'] and self.expectedPosition['y'] == self.roboMockObject.position['y']:
            print('test case passed');
        else:
            print('test case failed');
        return

    #To test if robot turns,moves and arrives at expected coordinates and is facing expected direction
    def moveTurnTest(self,instructionList):
        for inst in instructionList:
            if inst == "turn-left":
                self.roboMockObject.turnLeft()
            elif inst == "turn-right":
                self.roboMockObject.turnRight()
            elif inst == "move-forward":
                self.roboMockObject.moveForward()

        self.roboMockObject.printRoboDetails()         
        if self.expectedPosition['x'] == self.roboMockObject.position['x'] and self.expectedPosition['y'] == self.roboMockObject.position['y'] and self.expectedDirection == self.roboMockObject.direction:
            print('test case passed');
        else:
            print('test case failed');
        return
    
#=================================================================================
#main
#=============================================================

#Reading using input Json file
#inputdata = json.load(open(sys.argv))
inputdata = json.load(open('inputdat.json'))
#--> if using a stored file for input json
roboObjPresent = False
roboObject = Robo(0,0, "none")

for record in inputdata:
  if record['type'] == "asteroid":
    asteroidPosition = record['size']
  elif record['type'] == "new-robot":
    if roboObjPresent:
      roboObject.printRoboDetails()
    value = record['position']
    roboObject.position['x'] = value['x']
    roboObject.position['y'] = value['y']
    roboObject.direction = record['bearing']
    roboObjPresent = True
  elif record['type'] == "move" and roboObjPresent:
    if record['movement'] == "turn-left":
      roboObject.turnLeft()
    if record['movement'] == "turn-right": 
      roboObject.turnRight()
    if record['movement'] == "move-forward": 
      roboObject.moveForward()
      
if roboObjPresent:
  roboObject.printRoboDetails()


  print('--------------------UNIT TEST TC OUTPUT BELOW--------------------')

  #RUN UNIT Test cases using roboMockObject, inject values to mock obj and pass it to function under test.
  #If result matches with esxpectd value the test pass or fail
  #above test cases can be used to test with all combinations of values to test robo class
  mockTest1 = RoboTest();
  mockTest1.roboMockObject.direction = "north"
  mockTest1.expectedDirection = "south"
  mockTest1.turnLeftTest(2)

  mockTest2 = RoboTest();
  mockTest2.roboMockObject.direction = "west"
  mockTest2.expectedDirection = "south"
  mockTest2.turnRightTest(3)

  mockTest3 = RoboTest();
  mockTest3.roboMockObject.position['x'] = 3
  mockTest3.roboMockObject.position['y'] = 0
  mockTest3.roboMockObject.direction = "north"
  mockTest3.expectedPosition = {'x':3,'y':5}
  mockTest3.moveForwardTest(5)

  mockTest4 = RoboTest();
  mockTest4.roboMockObject.position['x'] = 2
  mockTest4.roboMockObject.position['y'] = 2
  mockTest4.roboMockObject.direction = "east"
  instructlist = ['move-forward', 'turn-left', 'move-forward', 'turn-right', 'turn-right'];
  mockTest4.expectedPosition = {'x':3,'y':3}
  mockTest4.expectedDirection = "south"
  mockTest4.moveTurnTest(instructlist)

  
  
  
             
   
         
    
    
