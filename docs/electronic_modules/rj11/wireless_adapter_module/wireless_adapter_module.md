<div align=center>
<h1 class="text-center">蓝牙转接模块</h1>
</div>

## **1-简要概述**

<p style="text-align: center;">
    <img src="docs/electronic_modules/rj11/wireless_adapter_module/35D730A2-87CB-49fd-AFA1-4EFEEE388A44.png" />
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;本模块为蓝牙模块转接板，可用于没有蓝牙接口的主控板或主控扩展板。</span>
</p>

## **2-参数规格**

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
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压</td><td>DC 5V</td>
</tr>
<tr>
    <td>接口类型</td><td>RJ11</td>
</tr>
<tr>
    <td>通信方式</td><td>UART</td>
</tr>
<tr>
    <td>模块尺寸</td><td>48mm*24mm(长*宽)</td>
</tr>
</table>

## **3-使用指南**

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;"></span>
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;把蓝牙模块对应的插入排针排母接口（为防反接，分成排针排母），用RJ11线连接主控板。正常串口通讯需要2个IO口，如果蓝牙模块连接的是蓝牙手柄，则只需要接收数据，不需要发送，直接连上主控板的port口即可（比赛中就是此方案）。</span>
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;"><span style="font-family: 宋体;">&nbsp; &nbsp;如果想蓝牙收发信息，则需要把用</span><span style="font-family: 宋体, SimSun;">RJ11</span><span style="font-family: 宋体;">转杜邦线，然后</span><span style="font-family: 宋体, SimSun;">2</span><span style="font-family: 宋体;">个</span><span style="font-family: 宋体, SimSun;">IO</span><span style="font-family: 宋体;">管脚分别连接</span><span style="font-family: 宋体, SimSun;">2</span><span style="font-family: 宋体;">个</span><span style="font-family: 宋体, SimSun;">port</span><span style="font-family: 宋体;">口。</span>&nbsp;</span>
</p>
<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; &nbsp;该模块设计的初衷是因为<a href="#/docs/electronic_modules/main_control_board/elf_esp32_pro/elf_esp32_pro" target="_blank"><strong>ELF ESP32 Pro</strong></a>使用Micropython编程时，蓝牙接口所使用的串口被REPL占用,不能直接将蓝牙模块插接在板载蓝牙接口处，所以设计该模块，方便使用其他IO口进行串口通信。</span>
</p>

> [!Note]
> <p>
    <strong><span style="font-size: 24px; font-family: 宋体, SimSun;">MicroPython 交互式解释器模式（又名 REPL）</span></strong>
</p>

## **4-编程指南**

> [!Tip]
> <p>
    <font face="宋体, SimSun"><span style="font-size: 24px;"><b>这里编程只针对蓝牙手柄！</b></span></font>
</p>

### **4.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>返回手柄上按键状态值（布尔值）</td><td>（2个参数）端口、按键名称</td><td><img src="docs/electronic_modules/rj11/wireless_adapter_module/img.png"></td>
</tr>
<tr>
    <td>返回手柄上左右遥感的值（0~255）</td><td>（3个参数）端口、摇杆位置、轴方向</td><td><img src="docs/electronic_modules/rj11/wireless_adapter_module/img_1.png"></td>
</tr>
</table>

### **4.2-文本代码编程**

## **5-注意事项**

> [!Attention]
> <p>
    <span style="font-size: 24px;"><strong><span style="font-family: 宋体;">比赛中固定此蓝牙模块时，注意不要放小车内，金属结构容易屏蔽蓝牙信号，最好放置于车身四周，方便接收蓝牙信号。</span></strong></span>
</p>
