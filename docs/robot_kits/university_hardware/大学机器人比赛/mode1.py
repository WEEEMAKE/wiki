
from WePort import *
from We36EncoderMotor import We36EncoderMotor
from WeServoMotorDrive import WeServoMotorDrive
import time
from WeBluetoothController import WeBluetoothController
from machine import Pin
from machine import PWM

encoder36_1_A = We36EncoderMotor(PORT_A, 1)
encoder36_2_A = We36EncoderMotor(PORT_A, 2)
encoder36_1_B = We36EncoderMotor(PORT_B, 1)
encoder36_2_B = We36EncoderMotor(PORT_B, 2)
servoDriver_5 = WeServoMotorDrive(PORT_5)
encoder36_1_C = We36EncoderMotor(PORT_C, 1)
encoder36_2_C = We36EncoderMotor(PORT_C, 2)
bluetooth_controller_D = WeBluetoothController(PORT_D)
_sgvip2 = 0	#速度
_ijqjt3kee19X = 0	#左摇杆-X
_ijqjt3kee19Y = 0	#左摇杆-Y

#	停止()
def _fvgl7m():
	encoder36_1_A.run(0)
	encoder36_2_A.run(0)
	encoder36_1_B.run(0)
	encoder36_2_B.run(0)

#	左转-速度为("speed")
def _ijqsbw19sgvip2fga(_speed):
	encoder36_1_A.run(_speed)
	encoder36_2_A.run(-1 * _speed)
	encoder36_1_B.run(-1 * _speed)
	encoder36_2_B.run(_speed)

#	右转-速度为("speed")
def _gkzsbw19sgvip2fga(_speed):
	encoder36_1_A.run(-1 * _speed)
	encoder36_2_A.run(_speed)
	encoder36_1_B.run(_speed)
	encoder36_2_B.run(-1 * _speed)

#	前进-速度为("speed")
def _g99sez19sgvip2fga(_speed):
	encoder36_1_A.run(0)
	encoder36_2_A.run(_speed)
	encoder36_1_B.run(-1 * _speed)
	encoder36_2_B.run(0)

#	后退-速度为("speed")
def _glqsg019sgvip2fga(_speed):
	encoder36_1_A.run(0)
	encoder36_2_A.run(-1 * _speed)
	encoder36_1_B.run(_speed)
	encoder36_2_B.run(0)

#	左移-速度为("speed")
def _ijqo3f19sgvip2fga(_speed):
	encoder36_1_A.run(_speed)
	encoder36_2_A.run(0)
	encoder36_1_B.run(0)
	encoder36_2_B.run(-1 * _speed)

#	右移-速度为("speed")
def _gkzo3f19sgvip2fga(_speed):
	encoder36_1_A.run(-1 * _speed)
	encoder36_2_A.run(0)
	encoder36_1_B.run(0)
	encoder36_2_B.run(_speed)

#	左前方-速度为("speed")
def _ijqg99k3d19sgvip2fga(_speed):
	encoder36_1_A.run(_speed)
	encoder36_2_A.run(_speed)
	encoder36_1_B.run(-1 * _speed)
	encoder36_2_B.run(-1 * _speed)

#	右后方-速度为("speed")
def _gkzglqk3d19sgvip2fga(_speed):
	encoder36_1_A.run(-1 * _speed)
	encoder36_2_A.run(-1 * _speed)
	encoder36_1_B.run(_speed)
	encoder36_2_B.run(_speed)

#	左后方-速度为("speed")
def _ijqglqk3d19sgvip2fga(_speed):
	encoder36_1_A.run(_speed)
	encoder36_2_A.run(-1 * _speed)
	encoder36_1_B.run(_speed)
	encoder36_2_B.run(-1 * _speed)

#	机械手初始化状态()
def _ke2kogjezg7xhqjgeumnqiyp():
	servoDriver_5.servo_write(1, 30)
	time.sleep(0.5)
	servoDriver_5.servo_write(2, 35)
	time.sleep(0.5)
	servoDriver_5.servo_write(3, 155)

#	发送装置初始化()
def _gk1sg1r0lp66g7xhqjgeu():
	pwm4.duty(500)
	time.sleep(1)
	pwm4.duty(1000)
	time.sleep(1)
	pwm4.duty(530)

#	发射台初始化角度()
def _gk1i6cgkwg7xhqjgeur82ip2():
	servoDriver_5.servo_write(4, 75)

#	开启拾取方块()
def _irkgmnjjygk6k3dh93():
	pwm4.duty(900)
	encoder36_1_C.run(255)
	encoder36_2_C.run(-255)

#	停止拾取方块()
def _fvgl7mjjygk6k3dh93():
	pwm4.duty(530)
	encoder36_1_C.run(0)
	encoder36_2_C.run(0)

#	遥控控制车-摇杆X("X", "Y", "speed")
def _sitjonjong8msbq19jt3keeX(_X, _Y, _speed):
	if _X > 100 and (_X < 140 and _Y > 245):
		_g99sez19sgvip2fga(_speed)	#前进-速度为
	elif _X > 100 and (_X < 140 and _Y < 10):
		_glqsg019sgvip2fga(_speed)	#后退-速度为
	elif _X < 10 and (_Y > 100 and _Y < 140):
		_ijqo3f19sgvip2fga(_speed)	#左移-速度为
	elif _X > 245 and (_Y > 100 and _Y < 140):
		_gkzo3f19sgvip2fga(_speed)	#右移-速度为
	elif _X > 10 and (_X < 100 and (_Y > 140 and _Y < 245)):
		_ijqg99k3d19sgvip2fga(_speed)	#左前方-速度为
	elif _X > 140 and (_X < 250 and (_Y > 140 and _Y < 245)):
		_gkzglqk3d19sgvip2fga(_speed)	#右后方-速度为
	elif _X > 10 and (_X < 100 and (_Y > 10 and _Y < 100)):
		_ijqglqk3d19sgvip2fga(_speed)	#左后方-速度为
	elif _X > 140 and (_X < 245 and (_Y > 10 and _Y < 100)):
		_gkzglqk3d19sgvip2fga(_speed)	#右后方-速度为
	elif bluetooth_controller_D.buttonPressed(bluetooth_controller_D.WeBUTTON_ZL):
		_ijqsbw19sgvip2fga(_speed)	#左转-速度为
	elif bluetooth_controller_D.buttonPressed(bluetooth_controller_D.WeBUTTON_L):
		_gkzsbw19sgvip2fga(_speed)	#右转-速度为
	else:
		_fvgl7m()	#停止

#	发射台角度调整()
def _gk1i6cgkwr82ip2rnnk1g():
	if bluetooth_controller_D.buttonPressed(bluetooth_controller_D.WeBUTTON_UP):
		servoDriver_5.servo_write(4, 70)
	elif bluetooth_controller_D.buttonPressed(bluetooth_controller_D.WeBUTTON_LEFT):
		servoDriver_5.servo_write(4, 75)
	elif bluetooth_controller_D.buttonPressed(bluetooth_controller_D.WeBUTTON_RIGHT):
		servoDriver_5.servo_write(4, 80)
	elif bluetooth_controller_D.buttonPressed(bluetooth_controller_D.WeBUTTON_DOWN):
		servoDriver_5.servo_write(4, 85)

#	拾取启停控制()
def _jjygk6gmnfvgjong8m():
	if bluetooth_controller_D.buttonPressed(bluetooth_controller_D.WeBUTTON_R):
		_irkgmnjjygk6k3dh93()	#开启拾取方块
	elif bluetooth_controller_D.buttonPressed(bluetooth_controller_D.WeBUTTON_ZR):
		_fvgl7mjjygk6k3dh93()	#停止拾取方块

pwm4 = PWM(Pin(PORT_4),freq=500)
_fvgl7m()	#停止
_ke2kogjezg7xhqjgeumnqiyp()	#机械手初始化状态
_gk1sg1r0lp66g7xhqjgeu()	#发送装置初始化
_gk1i6cgkwg7xhqjgeur82ip2()	#发射台初始化角度
_fvgl7mjjygk6k3dh93()	#停止拾取方块
print("Start")
while True:
	bluetooth_controller_D.loop()
	_sgvip2 = 200	#速度
	_ijqjt3kee19X = bluetooth_controller_D.readAnalog(bluetooth_controller_D.WeJOYSTICK_LX)	#左摇杆-X
	_ijqjt3kee19Y = bluetooth_controller_D.readAnalog(bluetooth_controller_D.WeJOYSTICK_LY)	#左摇杆-Y
	_sitjonjong8msbq19jt3keeX(_ijqjt3kee19X, _ijqjt3kee19Y, _sgvip2)	#遥控控制车-摇杆X
	_jjygk6gmnfvgjong8m()	#拾取启停控制
	_gk1i6cgkwr82ip2rnnk1g()	#发射台角度调整
