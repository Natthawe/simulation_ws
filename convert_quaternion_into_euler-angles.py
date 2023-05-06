import math
M_PI = 3.14159265359
def euler_from_quaternion(x, y, z, w):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in radians (counterclockwise)
    pitch is rotation around y in radians (counterclockwise)
    yaw is rotation around z in radians (counterclockwise)
    """
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)
    print("(Roll) Radians-to-Degrees ->",roll_x*(180/M_PI))

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)
    print("(Pitch)Radians-to-Degrees ->",pitch_y*(180/M_PI))


    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)
    print("(Yaw)  Radians-to-Degrees ->",yaw_z*(180/M_PI))


    return roll_x, pitch_y, yaw_z # in radians

print(euler_from_quaternion(0, 0, 0.7072, 0.7072))    #Suppose a robot is on a flat surface. It has the following quaternion