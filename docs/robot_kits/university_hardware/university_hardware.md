# 大学比赛硬件器材使用说明

> 本文档介绍了此次比赛器材中电子模块和软件的基本使用方法。电子模块由4大部分组成，其中包括：
>
> - 电源系统
>	 - [电源管理模块](docs/electronic_modules/other_modules/power_management_module/power_management_module.md)
>	 - [击打模块](docs\electronic_modules\other_modules\hit_module\hit_module.md)
>	 - [无刷电机驱动模块](docs/electronic_modules/rj11/brushless_motor_adapter/brushless_motor_adapter.md)
> - 控制系统
> 	- [ELF ESP32 Pro主控板](docs/electronic_modules/main_control_board/elf_esp32_pro/elf_esp32_pro.md)
> 	- [蓝牙手柄](docs/electronic_modules/other_modules/bluetooth_controller/bluetooth_controller.md)
> 	- [蓝牙模块](docs/electronic_modules/other_modules/bluetooth_module/bluetooth_module.md)
> - 动力系统
> 	- [大功率编码电机驱动模块](docs/electronic_modules/rj11/36encoder_motor_driver/36encoder_motor_driver.md)
> 	- [6路舵机驱动模块](docs/electronic_modules/rj11/six_servo_driver_module/six_servo_driver_module.md)
> 	- 无刷电调
> 	- [36编码电机](docs\electronic_modules\motor\36mm_encoder_motor\36mm_encoder_motor.md)
> 	- 无刷马达
> 	- [舵机](docs/electronic_modules/motor/mg995_sovor/mg995_sovor.md)
> 	- 25/37电机等
> - 传感系统
> 	- [图像识别传感器](docs/electronic_modules/rj11/imagerecognition_sensor_v2/imagerecognition_sensor_v2.md)
> 	- [多路巡线传感器](docs/electronic_modules/rj11/multiple_linefollower/multiple_linefollower.md)
> 	- [超声波传感器](docs/electronic_modules/rj11/rgb_ultrasonic_sensor/rgb_ultrasonic_sensor.md)


## 电源系统

电源系统模块的功能是给整个小车提供电源，分为2部分——主供电线路和无刷电机供电线路，每个线路都需要独立电池充电，因此整台车辆最少需要2个电池。主供电线路由电源管理模块和击打模块组成，电池通过TX60接口接入电源管理模块，然后再通过TX30连接线（下图所示）给大功率编码电机驱动模块供电，最多可以连接4个。4个接口功能等同，可以任意选择接入。

<div align=center>
<img src="docs\robot_kits\university_hardware\1750.png">
</div> 

通过DC005（下图所示）连接线给主控板和6路舵机驱动模块供电。板上的2个DC接口等同，可以任意选择接入。

<div align=center>
<img src="docs\robot_kits\university_hardware\1751.png">
</div> 

板上有4个2510接口，用于连接击打模块，通过2510连接线（下图所示）任意连接3个即可。

<div align=center>
<img src="docs\robot_kits\university_hardware\1752.png">
</div> 

如果连接长度不够，可以使用2510延长线（下图所示）。

<div align=center>
<img src="docs\robot_kits\university_hardware\1753.png">
</div> 

无刷电机驱动模块也是通过TX60接口与电池连接，只为2个无刷电机供电，该模块只做电源和信号的转接，不做处理，具体的使用方法详见模块介绍。

需要注意的是：购买锂电池时，需要接口为TX60，这样才能接入模块。

另外，电源管理模块会根据时间和击打情况自动通断电源，任意一个击打模块上感受到击打都会切断电源，但无刷电机驱动模块是独立的，不受影响。

击打模块是根据震动量来测试被击打情况的，固定在车身时，需要防止机身的震动导致误判，中间可以垫海绵胶或者隔空处理，这个根据各自情况来调整。

 

 

## 控制系统

控制系统由一个主控板和蓝牙遥控套件组成，主控板采用了ESP32内存8M的模组，硬件支持图形化编程和python编程。蓝牙遥控套件由手柄和接收模块组成，接收模块通过RJ11线（下图所示）和主控板通信。

注意固定接收模块时，最好放置在小车金属框架外围，以减小金属框架对蓝牙信号的干扰。

<div align=center>
<img src="docs\robot_kits\university_hardware\1754.png">
</div>  

## 动力系统

动力系统由3块驱动板和各种电机组成。驱动模块与主控的信号连接采用RJ11线，大功率编码电机驱动与36电机直接采用6Pin连接线（下图所示，实际线材颜色有黑和白）。

<div align=center>
<img src="docs\robot_kits\university_hardware\1755.png">
</div>  



## 传感系统

标配中由3个传感器组成，图像识别传感器用于在自动赛中识别积木块上的二维码，多路巡线传感器用于自动赛中辨别地上的线条，超声波传感器用于自动赛中识别道路中的物块，这些传感器都通过RJ11线和主控板通信。当然，用户可以根据自己的思路来设计得分方案，在比赛规则允许的条件下自行发挥。

 

## 软件示例代码说明

官方提供了一个简易的搭建和得分方案，本程序时在此基础上编写的。程序分为2部分，首先是自动阶段的程序（分2部分，在2台车上跑），然后是手动阶段的程序。

 

 

 

 

 

 