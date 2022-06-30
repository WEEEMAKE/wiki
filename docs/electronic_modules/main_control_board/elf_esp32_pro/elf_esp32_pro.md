<div align=center>
<h1 class="text-center">ELF ESP32 Pro主控板</h1>
</div>

## **1-简要概述**

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;ELF ESP32 Pro主控板的核心板由ESP32-WROOM-32D模组构成，在ELF V2.0板子上使用，可直接进行编程，下载固件等操作。核心板共引出了21个功能管脚，板载1个复位按键，和一个可控LED灯。</span>
</p>

## **2-主板外观**

<div align="center">
<img src = "docs/electronic_modules/main_control_board/elf_esp32_pro/IMG_20220630_113447.jpg" width=40%>
<img src="docs/electronic_modules/main_control_board/elf_esp32_pro/IMG_20220630_120309.jpg" width=40%>
</div>

## **3-接口布局**

<div align="center">
<img src = "docs/electronic_modules/main_control_board/elf_esp32_pro/3AFEA579-90DE-45e2-B436-36521F306125.png">
</div>

> [!Attention]
> <div><p>
    <strong><span style="font-size: 24px; font-family: 宋体, SimSun;">当使用Micropython编程时，蓝牙接口禁止使用，因为Micropython的REPL已经占用该串口。此时如果想使用蓝牙模块，需要使用蓝牙转接模块，需要注意的是，通过蓝牙转接模块接在RJ11上蓝牙模块只能接收数据，不支持发送数据，WeeeCode目前只支持对蓝牙手柄的编程。</span></strong>
</p>
<p>
    <strong><span style="font-size: 24px; font-family: 宋体, SimSun;">蓝牙转接模块：（<a href="#/docs/electronic_modules/rj11/wireless_adapter_module/wireless_adapter_module" target="_blank">模块详情</a>）</span></strong>
</p>
<p style="text-align: center;">
    <strong><span style="font-size: 24px; font-family: 宋体, SimSun;"><img src="docs/electronic_modules/rj11/wireless_adapter_module/35D730A2-87CB-49fd-AFA1-4EFEEE388A44.png"/></span></strong>
</p>
</div>

## **4-ESP32核心板硬件参数**

<!-- CSS goes in the document HEAD or added to your external stylesheet -->
<style type="text/css">
table{
    margin: auto;
}
table.imagetable {
    font-family: verdana,arial,sans-serif;
    font-size:20px;
    color:#333333;
    border-width: 5px;
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
<table class="imagetable" style="display: table; text-align: center;">
<tr>
    <th>项</th><th>值/描述</th>
</tr>
<tr>
    <td>输入电压</td><td>DC 5V</td>
</tr>
<tr>
    <td>工作电压</td><td>3.3V</td>
</tr>
<tr>
    <td>主控芯片</td><td>ESP32-WROOM-32D模组 8M</td>
</tr>
<tr>
    <td>复位按键</td><td>1个</td>
</tr>
<tr>
    <td>可编程LED灯</td><td>1个（蓝色）(IO15)</td>
</tr>
<tr>
    <td>排针排母</td><td>28针（防反接设计）</td>
</tr>
<tr>
    <td>模块尺寸</td><td>33mm*28mm(长*宽)</td>
</tr>
</table>

## **5-ESP32在ELF V2.0上的IO管脚分配**

<table class="imagetable" style="display: table; text-align: center;">
<tr>
    <th>项</th><th>ELF V2.0</th><th>ESP32</th>
</tr>
<tr>
    <td>按键模块</td><td>OnBoard_Button</td><td>IO18</td>
</tr>
<tr>
    <td>RGB灯模块</td><td>OnBoard_RGB</td><td>IO12</td>
</tr>
<tr>
    <td>蜂鸣器</td><td>OnBoard_Buzzer</td><td>IO14</td>
</tr>
<tr>
    <td rowspan="4" colspan="1">RJ11接口</td><td>PORT_A</td><td>IO17</td>
</tr>
<tr>
    <td>PORT_B</td><td>IO16</td>
</tr>
<tr>
    <td>PORT_C</td><td>IO13</td>
</tr>
<tr>
    <td>PORT_D</td><td>IO27</td>
</tr>
<tr>
    <td rowspan="2" colspan="1">传感器接口</td><td>PORT_1</td><td>IO32</td>
</tr>
<tr>
    <td>PORT_2</td><td>IO33</td>
</tr>
<tr>
    <td rowspan="4" colspan="1">传感器/电机驱动接口</td><td>PORT_3</td><td>IO25</td>
</tr>
<tr>
    <td>PORT_4</td><td>IO26</td>
</tr>
<tr>
    <td>PORT_5</td><td>IO4</td>
</tr>
<tr>
    <td>PORT_6</td><td>IO2</td>
</tr>
<tr>
    <td rowspan="2" colspan="1">电机接口</td><td>M1</td><td>IO21,IO22</td>
</tr>
<tr>
    <td>M2</td><td>IO19,IO23</td>
</tr>
<tr>
    <td>蓝牙接口</td><td>RX/TX</td><td>IO1,IO3</td>
</tr>
</table>

## **6-使用指南&编程**

<p>
    <span style="font-size: 24px;"><span style="font-family: 宋体;">&nbsp; 主控板支持图形化编程和</span>python<span style="font-family: 宋体;">编程，也支持</span>arduino<span style="font-family: 宋体;">编程（需自己添加库）。在</span>weeecode<span style="font-family: 宋体;">下编程时，主控板需选择</span>WEEEMAKE ELF ESP32Pro<span style="font-family: 宋体;">，当在中间写好图形化代码时，点击右上方的代码开关，右边会变为</span>python<span style="font-family: 宋体;">代码区，当然也可以直接写</span>python<span style="font-family: 宋体;">代码（点击用</span>IDE<span style="font-family: 宋体;">打开）。然后点击连接串口，上传或者调试程序，就可以看到结果了。</span></span>
</p>

## **7-注意事项**

> [!Attention]
> <div><p>
    <span style="font-size: 24px;">&nbsp; &nbsp; &nbsp; &nbsp;ESP32<span style="font-family: 宋体;">的</span>IO2<span style="font-family: 宋体;">也就是</span>ELF<span style="font-family: 宋体;">的</span>PORT6<span style="font-family: 宋体;">口在烧录固件程序的时候要注意要为低电平，否则无法下载程序，</span>WM<span style="font-family: 宋体;">的传感器模块大部分默认是高电平的，所以<span style="font-family: 宋体;">烧录固件程序</span>时</span>PORT6<span style="font-family: 宋体;">口最好不要插任何模块。</span></span>
</p>
<p>
    <span style="font-size: 24px;"><span style="font-family: 宋体;">&nbsp;核心模块的安装，复位按键应靠近</span>USB<span style="font-family: 宋体;">接口方向。</span></span>
</p></div>