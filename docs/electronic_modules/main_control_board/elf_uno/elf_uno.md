<div align=center>
<h1 class="text-center">ELF UNO主控板</h1>
</div>


## 1 ELF UNO主控板介绍
<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_uno/elf_uno.jpg" width="50%">
</div>


### 1.1 简要概述
ELF UNO主控板是WEEEMAKE开发的一款针对电机和其他模块驱动控制的开发板套件。主控采用了ATmega328P芯片。主板上提供了丰富的接口，方便接入各种传感器模块，方便二次开发和学习，降低了学习单片机的门槛。


### 1.2 主控芯片介绍
ATMEGA328P-AU，一种集成电路 (IC)，核心处理器是AVR，闪存容量为32KB。

- 高性能、低功耗AVR 8位微控制器
- 先进的RISC体系结构
- 高耐力非易失性内存段
- 微控制器的特殊功能
- 上电复位和可编程布朗出检测
- 内部校准的振荡器
- 外部和内部中断源
- 六个睡眠模式：空闲，ADC降噪、电源保存、关闭、待机状态，和待机扩展


### 1.3 芯片手册
<embed class="pdfobject" src="docs\electronic_modules\main_control_board\elf_uno\Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf" style="overflow: auto; width: 100%; height: 40rem;">

## 2 编程软件介绍
主控板目前支持图形化和C/C++编程。图形化编程使用weeecode软件，C/C++编程使用arduino IDE。入门和体验可以从图形化开始，更详细的weeecode软件介绍可以点击
 [传送门](docs/software_usage/weeecode/weeecode.md) 前往页面进行进一步了解。

## 3 主控板拿到以后首先做什么？🙌

1. 用一根USB-A数据线连接电脑。看到接口旁的红色LED指示灯亮了！✨
<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_uno/202209291806.jpg" width="50%">
</div>

2. 接着连接好我们的TT直流电机和电池，把开关拨到ON。👏
<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_uno/1811.jpg" width="50%">
</div>

3. 打开2.3准备好的示例程序，连接好串口后选择烧录在线调试固件。做到这一步，我们能看到“正在上传，请稍后”字样。😉
<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_uno/1823.png" width="50%">
</div>

4. 等待固件上传完成，完成后点击程序块就可以愉快地玩耍啦！😊（主板正常，操作步骤没有遗漏的情况下，电机会处于转动1s然后停止1s的状态中，两颗板载RGB灯会被点亮）
<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_uno/1833.png" width="50%">
</div>

## 3 主控板还能做什么？🙌
