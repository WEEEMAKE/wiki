import time
from WePort import *
from WeBluetoothController import *
from We36EncoderMotor import *
from WeServoMotorDrive import *
from WeMultipleLineFollower import *
from WeImageRecognition import *
from WeUltrasonicSensor import *
from buzzer import BUZZER
from machine import Pin
from machine import PWM

buzzer_14 = BUZZER(14)
pwm26 = PWM(Pin(26),freq=500)  # PORT_4

b = WeBluetoothController(PORT_D)
motor_1 = We36EncoderMotor(PORT_A, 1)
motor_2 = We36EncoderMotor(PORT_A, 2)
motor_3 = We36EncoderMotor(PORT_B, 1)
motor_4 = We36EncoderMotor(PORT_B, 2)
motor_5 = We36EncoderMotor(PORT_C, 1)
motor_6 = We36EncoderMotor(PORT_C, 2)
servo_driver = WeServoMotorDrive(PORT_5)
multiple_lineFollower = WeMultipleLineFollower(PORT_3)
image_recognition = WeImageRecognition(PORT_1)
ultrasonic_6 = WeUltrasonicSensor(PORT_6)

# 机械手初始状态
def servo_init():
    servo_driver.servo_write(1,30)
    time.sleep_ms(500)
    servo_driver.servo_write(2,35)
    time.sleep_ms(500)
    servo_driver.servo_write(3,155)

# 机械手夹取
def servo_catch():
    servo_driver.servo_write(1,80)
    time.sleep(0.5)
    servo_driver.servo_write(2,30)
    time.sleep_ms(500)

# 机械手松开
def servo_release():
    servo_driver.servo_write(2,40)
    time.sleep_ms(500)
    servo_driver.servo_write(1,30)
    time.sleep_ms(500)

# 车-停止
def stop():
    motor_1.stop()
    motor_2.stop()
    motor_3.stop()
    motor_4.stop()

# 车-左转
def turn_left(speed):
    motor_1.run(speed)
    motor_2.run(-speed)
    motor_3.run(-speed)
    motor_4.run(speed)

# 车-右转
def turn_right(speed):
    motor_1.run(-speed)
    motor_2.run(speed)
    motor_3.run(speed)
    motor_4.run(-speed)

# 车-左转
def turn_left1(speed):
    motor_1.run(speed)
    motor_2.stop()
    motor_3.run(-speed)
    motor_4.stop()

# 车-右转
def turn_right1(speed):
    motor_1.run(-speed)
    motor_2.stop()
    motor_3.run(speed)
    motor_4.stop()

# 车-后退
def backward(speed):
    motor_1.stop()
    motor_2.run(-speed)
    motor_3.run(speed)
    motor_4.stop()

# 车-前进
def forward(speed):
    motor_1.stop()
    motor_2.run(speed)
    motor_3.run(-speed)
    motor_4.stop()

# 车-左移
def shift_left(speed):
    motor_1.run(speed)
    motor_2.stop()
    motor_3.stop()
    motor_4.run(-speed)

# 车-右移
def shift_right(speed):
    motor_1.run(-speed)
    motor_2.stop()
    motor_3.stop()
    motor_4.run(speed)

# 车-左前方
def left_front(speed):
    motor_1.run(speed)
    motor_2.run(speed)
    motor_3.run(-speed)
    motor_4.run(-speed)

# 车-右后方
def right_rear(speed):
    motor_1.run(-speed)
    motor_2.run(-speed)
    motor_3.run(speed)
    motor_4.run(speed)

# 车-右前方
def right_front(speed):
    motor_1.run(-speed)
    motor_2.run(speed)
    motor_3.run(-speed)
    motor_4.run(speed)

# 车-左后方
def left_rear(speed):
    motor_1.run(speed)
    motor_2.run(-speed)
    motor_3.run(speed)
    motor_4.run(-speed)

# 开启拾取方块
def pick_up_blob():
    motor_5.run(255)
    motor_6.run(-255)

# 停止拾取方块
def stop_pick_up_blob():
    motor_5.run(0)
    motor_6.run(0)

# 发射初始化
def shoot_init():
    pwm26.duty(500)
    time.sleep(1)
    pwm26.duty(1000)
    time.sleep(1)
    pwm26.duty(530)

# 启动发射
def shoot():
    pwm26.duty(800)

# 停止发射
def stop_shoot():
    pwm26.duty(530)

# 巡线
def follower_line(speed):
    multiple_lineFollower.updateData(0)
    if multiple_lineFollower.S1==0 and multiple_lineFollower.S3==0:
        forward(speed)
    elif multiple_lineFollower.S1==1 and multiple_lineFollower.S3==0:
        turn_left(speed)
    elif multiple_lineFollower.S1==0 and multiple_lineFollower.S3==1:
        turn_right(speed)

stop()
servo_init()
shoot_init()
stop_pick_up_blob()

image_recognition.getAprilTag(1)
time.sleep(1)
buzzer_14.tone(262, 500)
print("start")
speed = 100
follower_flag=0
flag=0
while True:
    b.loop()
    if b.buttonPressed(b.WeBUTTON_MINUS):
        speed = 50
    elif b.buttonPressed(b.WeBUTTON_BL):
        speed = 100
    elif b.buttonPressed(b.WeBUTTON_PLUS):
        speed = 150
    elif b.buttonPressed(b.WeBUTTON_MODE):
        speed = 200
    elif b.buttonPressed(b.WeBUTTON_HOME):
        speed = 250
    if b.buttonPressed(b.WeBUTTON_ZR):
        follower_flag=0
    elif b.buttonPressed(b.WeBUTTON_R):
        follower_flag=1

    if follower_flag == 1:
        while True:
            b.loop()
            if b.buttonPressed(b.WeBUTTON_ZR):
                follower_flag=0
                flag=0
                stop()
                break

            follower_line(speed)
            distance = ultrasonic_6.distanceCM()
            if distance>6 and distance <15:
                speed = 80
            elif distance<=6:
                stop()
                time.sleep_ms(300)
                servo_catch()
                speed = 100
                flag=1
                break

        while (flag != 0):
            b.loop()
            if b.buttonPressed(b.WeBUTTON_ZR):
                stop()
                flag=0
                follower_flag=0
                break
            follower_line(speed)
            if multiple_lineFollower.S1==1 and  multiple_lineFollower.S2==1 and multiple_lineFollower.S3==1:
                stop()
                backward(100)
                time.sleep_ms(320)
                stop()
                time.sleep_ms(100)
                servo_release()
                time.sleep_ms(500)
                backward(100)
                time.sleep_ms(300)
                stop()
                #follower_flag=0
                flag=2
                break

        servo_init()
        servo_driver.servo_write(3,95)
        shift_right(100)
        time.sleep(1.6)
        forward(100)
        time.sleep(2)
        stop()
        while (flag != 0):
            b.loop()
            if b.buttonPressed(b.WeBUTTON_ZR):
                follower_flag=0
                flag=0
                stop()
                break

            if image_recognition.getAprilTag(1):
                print(image_recognition.centerX, image_recognition.y_degress)

                if image_recognition.centerX >= 80 and image_recognition.centerX <= 90 and (image_recognition.y_degress <= 10 or image_recognition.y_degress >= 350):
                    flag=3
                    print("flag",flag)
                    break

                if image_recognition.centerX < 80:
                    shift_left(80)
                    time.sleep_ms(80)
                    stop()
                elif image_recognition.centerX > 90:
                    shift_right(80)
                    time.sleep_ms(80)
                    stop()
                if image_recognition.y_degress > 270 and image_recognition.y_degress < 350:
                    turn_right1(60)
                    time.sleep_ms(80)
                    stop()
                elif image_recognition.y_degress > 10 and image_recognition.y_degress < 90:
                    turn_left1(60)
                    time.sleep_ms(80)
                    stop()
            time.sleep_ms(100)

        while (flag != 0):
            b.loop()
            if b.buttonPressed(b.WeBUTTON_ZR):
                follower_flag=0
                flag=0
                stop()
                break

            if image_recognition.getAprilTag(1):
                print("Y",image_recognition.centerY)
                if image_recognition.centerY < 78:
                    forward(80)
                    time.sleep_ms(80)
                    stop()
                else:
                    stop()
                    flag=4
                    print("flag",flag)
                    break

            time.sleep_ms(100)

        while (flag != 0):
            b.loop()
            if b.buttonPressed(b.WeBUTTON_ZR):
                follower_flag=0
                flag=0
                stop()
                break

            if image_recognition.getAprilTag(1):
                print(image_recognition.centerX, image_recognition.y_degress)

                if image_recognition.centerX >= 82 and image_recognition.centerX <= 88 and (image_recognition.y_degress <= 10 or image_recognition.y_degress >= 350):
                    flag=3
                    print("flag",flag)
                    break

                if image_recognition.centerX < 82:
                    shift_left(80)
                    time.sleep_ms(80)
                    stop()
                elif image_recognition.centerX > 88:
                    shift_right(80)
                    time.sleep_ms(80)
                    stop()
                if image_recognition.y_degress > 270 and image_recognition.y_degress < 350:
                    turn_right1(60)
                    time.sleep_ms(80)
                    stop()
                elif image_recognition.y_degress > 10 and image_recognition.y_degress < 90:
                    turn_left1(60)
                    time.sleep_ms(80)
                    stop()
            time.sleep_ms(100)
        servo_init()
        time.sleep_ms(500)
        forward(80)
        time.sleep_ms(350)
        stop()
        time.sleep_ms(300)
        servo_catch()
        time.sleep_ms(50)
        backward(100)
        time.sleep_ms(550)
        stop()
        time.sleep_ms(100)
        servo_driver.servo_write(3,95)
        time.sleep_ms(200)
        shift_left(80)
        time.sleep_ms(1000)
        stop()
        image_recognition.getAprilTag(2)
        time.sleep_ms(400)
        image_recognition.getAprilTag(2)
        time.sleep_ms(400)
        while (flag != 0):
            b.loop()
            if b.buttonPressed(b.WeBUTTON_ZR):
                follower_flag=0
                flag=0
                stop()
                break

            if image_recognition.getAprilTag(2):
                print(image_recognition.centerX, image_recognition.y_degress)

                if image_recognition.centerX >= 82 and image_recognition.centerX <= 88 and (image_recognition.y_degress <= 10 or image_recognition.y_degress >= 350):
                    flag=5
                    stop()
                    print("flag",flag)
                    break

                if image_recognition.centerX < 82:
                    shift_left(80)
                    time.sleep_ms(80)
                    stop()
                elif image_recognition.centerX > 88:
                    shift_right(80)
                    time.sleep_ms(80)
                    stop()
                if image_recognition.y_degress > 300 and image_recognition.y_degress < 350:
                    turn_right1(60)
                    time.sleep_ms(80)
                    stop()
                elif image_recognition.y_degress > 10 and image_recognition.y_degress < 55:
                    turn_left1(60)
                    time.sleep_ms(80)
                    stop()
            time.sleep_ms(100)

        while (flag != 0):
            b.loop()
            if b.buttonPressed(b.WeBUTTON_ZR):
                follower_flag=0
                flag=0
                stop()
                break

            if image_recognition.getAprilTag(2):
                print("Y",image_recognition.centerY)
                if image_recognition.centerY < 75:
                    forward(80)
                    time.sleep_ms(80)
                    stop()
                elif image_recognition.centerY > 78:
                    backward(80)
                    time.sleep_ms(50)
                    stop()
                else:
                    flag=6
                    print("flag",flag)
                    break

            time.sleep_ms(100)
        stop()
        servo_driver.servo_write(3,115)
        time.sleep_ms(400)
        servo_driver.servo_write(2,72)
        time.sleep_ms(500)
        servo_driver.servo_write(1,30)
        time.sleep_ms(500)
        servo_init()
        backward(80)
        time.sleep_ms(300)
        stop()
        follower_flag = 0

    else:
        joystick_x = b.readAnalog(b.WeJOYSTICK_LX)
        joystick_y = b.readAnalog(b.WeJOYSTICK_LY)
        #print(joystick_x,joystick_y)
        if joystick_x>100 and joystick_x<140 and joystick_y>250:forward(speed)
        elif joystick_x>100 and joystick_x<140 and joystick_y<10:backward(speed)
        elif joystick_x<10 and joystick_y>100 and joystick_y<140:shift_left(speed)
        elif joystick_x>250 and joystick_y>100 and joystick_y<140:shift_right(speed)
        elif joystick_x>10 and joystick_x<100 and joystick_y>140 and joystick_y<250:left_front(speed)
        elif joystick_x>140 and joystick_x<250 and joystick_y>140 and joystick_y<250:right_front(speed)
        elif joystick_x>10 and joystick_x<100 and joystick_y>10 and joystick_y<100:left_rear(speed)
        elif joystick_x>140 and joystick_x<250 and joystick_y>10 and joystick_y<100:right_rear(speed)
        elif b.buttonPressed(b.WeBUTTON_ZL):turn_left(speed)
        elif b.buttonPressed(b.WeBUTTON_L):turn_right(speed)
        else:stop()

        if b.buttonPressed(b.WeBUTTON_X):pick_up_blob()
        elif b.buttonPressed(b.WeBUTTON_Y):stop_pick_up_blob()

        if b.buttonPressed(b.WeBUTTON_A):shoot()
        elif b.buttonPressed(b.WeBUTTON_B):stop_shoot()
