<div align=center>
<h1 class="text-center">ELF 328P主控板</h1>
</div>

## **1-简要概述**

<p>
    <span style="color: rgb(51, 51, 51); background-color: rgb(255, 255, 255); font-size: 24px; font-family: 宋体, SimSun;">&nbsp; ELF主控板是一款基于Arduino平台的主控板，它性能强劲，可扩展性强，带有很强的DIY属性,可轻松适用于大班教学、机器人比赛、中小型DIY项目等，最具特色的是该主控板是可更换主控MCU的，目前已经支持MEGA-328P和MEGA-2560两种MCU更换。主控MCU可拆卸更换，在一定程度上比直接将MCU焊接在主发板上更具优势，毕竟当你当前MCU资源不够用的时候，你只需要更换一个MCU模块，而不必将整块主控板换掉。</span>
</p>

> [!Note]
> <font size=5>现已将ELF主控底板升级至2.0版本，可支持切换为ESP32主控，可参考[ELF ESP32 Pro](/docs/electronic_modules/main_control_board/elf_esp32_pro/elf_esp32_pro.md)。</font>

## **2-主板外观**

### **2.1-MCU模块**

<p>
    <span style="color: rgb(51, 51, 51); background-color: rgb(255, 255, 255); font-size: 24px; font-family: 宋体, SimSun;">&nbsp; ELF主控板目前支持2种类型的MCU更换：MEGA-328P和MEGA-2560,它们的外观如下图：</span>
</p>

<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_328p/mega_mcu.png">
</div>

### **2.2-插接上MEGA-328P模块**

<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_328p/elf_mega_328p.png">
</div>

## **3-接口布局**

<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_328p/elf_interface_layout.png">
</div>

## **4-硬件参数**

<!-- CSS goes in the document HEAD or added to your external stylesheet -->
<style type="text/css">
table.imagetable {
    font-family: verdana,arial,sans-serif;
    font-size:20px;
    color:#333333;
    border-width: 1px;
    border-color: #999999;
    border-collapse: collapse;
}
table.imagetable th {
    background:#b5cfd2 url('cell-blue.jpg');
    border-width: 2px;
    padding: 8px;
    border-style: solid;
    border-color: #999999;
    text-align: center;
}
table.imagetable td {
    background:#dcddc0 url('cell-grey.jpg');
    border-width: 2px;
    padding: 8px;
    border-style: solid;
    border-color: #999999;
    text-align: center;
}
text{
	font-size: 1cm;
	color: #7ec699;
}
</style>

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>项</th><th>值/描述</th>
</tr>
<tr>
    <td>按键模块</td><td>1个板载按键模块</td>
</tr>
<tr>
    <td>RGB灯</td><td>1个板载RGB灯模块</td>
</tr>
<tr>
    <td>蜂鸣器</td><td>1个蜂鸣器模块</td>
</tr>
<tr>
    <td>RJ11接口</td><td>板载4个RJ11接口A、B、C、D，可以很方便的接上WM的RJ11系列电子模块</td>
</tr>
<tr>
    <td>传感器接口</td><td>插针接口1、2，插针型传感器可直接接上使用<br>可转成RJ11接口<br>不适用于插个针型电机驱动模块</td>
</tr>
<tr>
    <td>传感器或电机驱动接口</td><td>插针接口3、4、5、6<br>可转成RJ11接口<br>可适用于插个针型电机驱动模块(编码电机驱动模块、步进电机驱动模块)</td>
</tr>
<tr>
    <td>电机接口</td><td>直流电机接口M1、M2已经板载了直流电机驱动<br>直流电机接口M3~M10需要在相应接口接编码电机驱动模块(编码电机和直流电机复用)<br>编码电机接口3、4、5、6，接上编码电机驱动模块方可使用编码电机<br>步进电机接口3、4、5、6，接上步进电机驱动模块方可使用步进电机</td>
</tr>
<tr>
    <td>MCU接口</td><td>插接MEGA-328P或MEGA-2560或ESP32</td>
</tr>
<tr>
    <td>通信接口</td><td>无线通信接口：接蓝牙模块接口,与PC通信需要蓝牙适配器(Dongle)<br>有线通信接口：USB-B</td>
</tr>
<tr>
    <td>特殊模块扩展接口</td><td>环形RGB-8灯模块<br>当MCU换上MEGA-2560时，接出更多扩展接口</td>
</tr>
<tr>
    <td>电源模块接口</td><td>用于更多扩展功能</td>
</tr>
<tr>
    <td>电源系统</td><td>输入电压<br>工作电压：5V</td>
</tr>
</table>

## **5-IO管脚分配**

### **5.1-常用接口分配明细**

<table class="imagetable" style="display: table; text-align: center;">
<tr>
    <th>项</th><th>ELF</th><th>MEGA-328P/MEGA-2560</th>
</tr>
<tr>
    <td>按键模块</td><td>OnBoard_Button</td><td>D2</td>
</tr>
<tr>
    <td>RGB灯模块</td><td>OnBoard_RGB</td><td>D3</td>
</tr>
<tr>
    <td>蜂鸣器</td><td>OnBoard_Buzzer</td><td>D11</td>
</tr>
<tr>
    <td rowspan="4" colspan="1">RJ11接口</td><td>PORT_A</td><td>D9</td>
</tr>
<tr>
    <td>PORT_B</td><td>D10</td>
</tr>
<tr>
    <td>PORT_C</td><td>D12</td>
</tr>
<tr>
    <td>PORT_D</td><td>D4</td>
</tr>
<tr>
    <td rowspan="2" colspan="1">传感器接口</td><td>PORT_1</td><td>A0</td>
</tr>
<tr>
    <td>PORT_2</td><td>A1</td>
</tr>
<tr>
    <td rowspan="4" colspan="1">传感器/电机驱动接口</td><td>PORT_3</td><td>A5</td>
</tr>
<tr>
    <td>PORT_4</td><td>A4</td>
</tr>
<tr>
    <td>PORT_5</td><td>A3</td>
</tr>
<tr>
    <td>PORT_6</td><td>A2</td>
</tr>
<tr>
    <td rowspan="2" colspan="1">电机接口</td><td>M1</td><td>D6,D7</td>
</tr>
<tr>
    <td>M2</td><td>D5,D8</td>
</tr>
<tr>
    <td>蓝牙接口</td><td>RX/TX</td><td>D0,D1</td>
</tr>
</table>

### **5.2-特殊模块扩展接口**

#### **5.2.1-特殊模块之环形RGB-8模块**

<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_328p/rgb_ring_module.png">
</div>

#### **5.2.2-特殊模块之MEGA-2560扩展模块**

<p>
    <span style="color: rgb(51, 51, 51); background-color: rgb(255, 255, 255); font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 当换上MEGA-2560 MCU模块，为了更方便扩展，Weeemake为之配备一个扩展板，可以同时支持更多的电子模块。</span>
</p>

<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_328p/mega_2560_shield.png">
</div>

##### **5.2.2.1-MEGA-2560扩展板正反面外观**

<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_328p/mega_2560_shield_front.png">
<p style="text-align: center;">
    <span style="color: rgb(51, 51, 51); background-color: rgb(255, 255, 255); font-size: 24px; font-family: 宋体, SimSun;">正面</span>
</p>
<img src="docs/electronic_modules/main_control_board/elf_328p/mega_2560_shield_obverse.png">
<p style="text-align: center;">
    <span style="color: rgb(51, 51, 51); background-color: rgb(255, 255, 255); font-size: 24px; font-family: 宋体, SimSun;">反面</span>
</p>
</div>

##### **5.2.2.2-MEGA-2560扩展板接口布局**

<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_328p/mega_2560_shield_interface_layout.png">
</div>

##### **5.2.2.3-MEGA-2560扩展板参数列表**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>项</th><th>值/描述</th>
</tr>
<tr>
    <td>RJ11接口</td><td>增加4个RJ11接口E、F、G、H<br>可以接更多WM的RJ11系列电子模块</td>
</tr>
<tr>
    <td>传感器或编码电机驱动接口</td><td>插针接口7、8、9<br>可转成RJ11接口<br>可适用于插个针型编码电机驱动模块</td>
</tr>
<tr>
    <td>舵机/灯带接口</td><td>舵机接口或RGB灯带接口</td>
</tr>
<tr>
    <td>通信接口</td><td>无线2.4G通信接口：PS2无线手柄<br>无线蓝牙通信接口</td>
</tr>
<tr>
    <td>电源系统</td><td>输入电压：DC6~12V<br>工作电压：5V</td>
</tr>
</table>

##### **5.2.2.4-MEGA-2560扩展板IO口分配**

<div align=center>
<img src="docs/electronic_modules/main_control_board/elf_328p/special_module_expansion_interface.png">
</div>

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>项</th><th>2560扩展板</th><th>MEGA-2560</th>
</tr>
<tr>
    <td rowspan="5" colspan="1">RJ11接口</td><td>PORT_E</td><td>A7</td>
<tr>
<tr>
    <td>PORT_F</td><td>A6</td>
</tr>
<tr>
    <td>PORT_F</td><td>A6</td>
</tr>
<tr>
    <td>PORT_G</td><td>A8</td>
</tr>
<tr>
    <td rowspan="3" colspan="1">传感器或编码电机驱动接口</td><td>PORT_7</td><td>A10</td>
</tr>
<tr>
    <td>PORT_8</td><td>A11</td>
</tr>
<tr>
    <td>PORT_9</td><td>19</td>
</tr>
<tr>
    <td rowspan="2" colspan="1">舵机/灯带接口</td><td>PORT_10</td><td>21</td>
</tr>
<tr>
    <td>PORT_11</td><td>20</td>
</tr>
<tr>
    <td>无线2.4G接口</td><td>USB HOST</td><td>D50,D51</td>
</tr>
<tr>
    <td>无线蓝牙接口</td><td>RX/TX</td><td>D0,D1</td>
</tr>
</table>