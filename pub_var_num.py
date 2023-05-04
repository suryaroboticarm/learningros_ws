#!/usr/bin/python3
import rospy
from publishers.msg import Num
import random

def talker():
    rospy.init_node("pub_setof_num_py", anonymous=True)
    publisher = rospy.Publisher("pub_setof_num_topic", Num, queue_size=10)
    rate = rospy.Rate(10)
    number = Num()

    while not rospy.is_shutdown():
        number.num_1 = random.randint(1,10)
        number.num_2 = random.randint(20,30)
        number.name = "surya"
        number.float_1 = 4.1
        number.array_1 = [1,5,6,8,9]
        publisher.publish(number)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException: pass
