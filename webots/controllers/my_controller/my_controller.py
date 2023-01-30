"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor, Lidar, GPS
import time
class smashBotMotor(Motor):

    def __init__(self, name=None):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        print(self.getMaxVelocity())
          

class smashBotMotors():

    def __init__(self, speed=None):
       self.__front_right_wheel_motor = smashBotMotor('front right wheel motor')
       self.__rear_right_wheel_motor = smashBotMotor('rear right wheel motor')
       self.__front_left_wheel_motor = smashBotMotor('front left wheel motor')
       self.__rear_left_wheel_motor = smashBotMotor('rear left wheel motor')
    
    def goforward(self):
        self.__front_right_wheel_motor.setVelocity(10)
        self.__rear_right_wheel_motor.setVelocity(10)
        self.__front_left_wheel_motor.setVelocity(10)
        self.__rear_left_wheel_motor.setVelocity(10)
    
    def goback(self):
        self.__front_right_wheel_motor.setVelocity(-10)
        self.__rear_right_wheel_motor.setVelocity(-10)
        self.__front_left_wheel_motor.setVelocity(-10)
        self.__rear_left_wheel_motor.setVelocity(-10)

    def turnright(self):
        self.__front_right_wheel_motor.setVelocity(0)
        self.__rear_right_wheel_motor.setVelocity(0)
        self.__front_left_wheel_motor.setVelocity(10)
        self.__rear_left_wheel_motor.setVelocity(10)

    def turnleft(self):
        self.__front_right_wheel_motor.setVelocity(10)
        self.__rear_right_wheel_motor.setVelocity(10)
        self.__front_left_wheel_motor.setVelocity(0)
        self.__rear_left_wheel_motor.setVelocity(0)

    

class GPSSens(GPS):
    def __init__(self):
        super().__init__('gps')
       
    def getGPSValue(self):
        return self.getValues()

    def checkGPS(self):
        
        border={
            "left":-3.5,
            "right":3.5,
            "front":3.5,
            "back":-3.5
        }
        limit=0.3

        Coordinates=self.getValues()
        long=[]
        
        for key,value in border.items():
            long.append(abs(Coordinates[0]-border[key]))
            long.append(abs(Coordinates[1]-border[key]))
           
        longs = min(long)
        if(longs<limit):
            #print(True)
            
            return True
        else:
            #print(False)
            
            return False
        

class LidarSens(Lidar):
    def __init__(self):
        super().__init__('lidar')
        #self.enablePointCloud()

    def getLidarValue(self):
        return self.getRangeImage()

class DistanceSens():
    def __init__(self):
        self.__front_left_distance_sensor = DistanceSensor('front left distance sensor')
        self.__front_right_distance_sensor = DistanceSensor('front right distance sensor')
        self.__rear_left_distance_sensor = DistanceSensor('rear left distance sensor')
        self.__rear_right_distance_sensor = DistanceSensor('rear right distance sensor')

    
    def getDistanceValue(self):
        return [self.__front_left_distance_sensor.getValue(),
        self.__front_right_distance_sensor.getValue(),
        self.__rear_left_distance_sensor.getValue(),
        self.__rear_right_distance_sensor.getValue()]

class smashBot(Robot):
    def __init__(self, speed=None):
        super().__init__()
        self.__motors=smashBotMotors()
        self.distances=DistanceSens()
        self.lidars=LidarSens()
        self.gps=GPSSens()

       

    def run(self, direction):
        if direction=="F":
            self.__motors.goforward()
        elif direction=="B":
            self.__motors.goback()
        elif direction=="L":
            self.__motors.turnleft()
        elif direction=="R":
            self.__motors.turnright()
            

# create the Robot instance.
robot = smashBot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
  #robot.run("F")
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    
    #print(robot.distances.getDistanceValue())
    #print(robot.lidars.getLidarValue())
    #print(robot.compass.getCompassValue())
    gps_value=robot.gps.getGPSValue()
    msg="Gps valeur:"
    for each_val in gps_value:
        msg += " {0:0.5f}".format(each_val)
    #print(msg)
    
    robot.run("F")

    if(robot.gps.checkGPS()==True):
        robot.run("R")
    else:
        robot.run("F")
    
        
            
        
 


        

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    

# Enter here exit cleanup code.
