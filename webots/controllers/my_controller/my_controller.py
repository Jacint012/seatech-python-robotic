"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor

class smashBotMotor(Motor):

    def __init__(self, name=None):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
          

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
        self.__front_right_wheel_motor.setVelocity(-10)
        self.__rear_right_wheel_motor.setVelocity(-10)
        self.__front_left_wheel_motor.setVelocity(10)
        self.__rear_left_wheel_motor.setVelocity(10)

    def turnleft(self):
        self.__front_right_wheel_motor.setVelocity(10)
        self.__rear_right_wheel_motor.setVelocity(10)
        self.__front_left_wheel_motor.setVelocity(-10)
        self.__rear_left_wheel_motor.setVelocity(-10)


class smashBot(Robot):
    def __init__(self, speed=None):
        super().__init__()
        self.__motors=smashBotMotors()
       

    def run(self, direction=None):
        if direction=='F':
            self.__motors.goforward()
        elif direction=='B':
            self.__motors.goback()
            
    

# create the Robot instance.
robot = smashBot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    robot.run('B')
    robot.getDevice('imu compass')

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
