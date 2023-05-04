#!/usr/bin/python3
import rospy
from std_msgs.msg import Float32

if __name__ == "__main__":
	rospy.init_node("pub_num_py",anonymous=True)
	publisher = rospy.Publisher("pub_num_topic", Float32, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		number = 3.14
		publisher.publish(number)
		rate.sleep()
