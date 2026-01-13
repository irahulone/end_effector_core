import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16


import serial
arduino_obj = serial.Serial(
port='/dev/ttyS0',
baudrate=57600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1)


class motor_driver(Node):

    def __init__(self):
        super().__init__('gripper_node')
        
        self.grp_state = 7
        self.grp_des_force = 0
        
        self.subscription = self.create_subscription(
            Int16,
            'ee/gripper1/state',
            self.cmd_callback,
            5)
        self.subscription  # prevent unused variable warning
        
        self.sub_grp_force = self.create_subscription(
            Int16,
            'ee/gripper1/desiered_force',
            self.cmd_callback_des_force,
            5)
        self.sub_grp_force  # prevent unused variable warning

    def move_motors(self):    
        payload1 = str(int(self.grp_state)) + "," + str(int(self.grp_des_force))
        #print(payload1)
        arduino_obj.write(str.encode(payload1))

    def cmd_callback(self, msg):    # master serial_write
        self.grp_state = msg.data
        self.move_motors()

    def cmd_callback_des_force(self, msg):
        self.grp_des_force = msg.data

def main(args=None):
    rclpy.init(args=args)
    gripper_subscriber = motor_driver()
    rclpy.spin(gripper_subscriber)
    gripper_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
