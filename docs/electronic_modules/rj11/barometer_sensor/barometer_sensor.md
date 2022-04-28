<div align=center>
<h1 class="text-center">气压传感器</h1>
</div>

## **1-简要介绍**

<div align=center>
<img src="docs\electronic_modules\rj11\barometer_sensor\20200313-115217.png"</img>
</div>

<p class=MsoTitle align=left style='text-align:left;text-indent:36.0pt'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:0pt;
background:white'>气压传感器（<span lang=EN-US>Barometer Sensor</span>）是基于高精度、低功耗的气压测量<span
lang=EN-US>MEMS</span>压力传感器——<b><span lang=EN-US>QMP6988</span></b>。该传感器可应用于天气预报、智能手机、无人机、航模等领域。</span></p>

> 案例：[气象站小套件](docs\robot_kits\Weather_Kit\Weather_Kit.md)

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
    <td>通信方式</td><td>WM单总线协议</td>
</tr>
<tr>
    <td>传感器型号</td><td>QMP6988</td>
</tr>
<tr>
    <td>工作温度</td><td>-40℃~+85℃</td>
</tr>
<tr>
    <td>最高气压分辨率</td><td>可达0.6Pa(相当于±125px高度变化)</td>
</tr>
<tr>
    <td>气压测量范围</td><td>30KPa~110KPa</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-模块功能及图形化编程指南**

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有<span lang=EN-US>WeeeCode</span>、<span lang=EN-US>Mixly_Arduino</span>等，其图形化编程大同小异，区别不会很大。</span></p>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>返回传感器的检测值</td><td>(2个参数）端口、所需数据选择</td><td><img src="docs\electronic_modules\rj11\barometer_sensor\20200313-113754.png"></td>
</tr>
</table>

### **3.2-文本代码编程指南**

<!-- tabs:start -->

### **Arduino-IDE编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>头文件</th><td>WeBarometerSensor.h</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeBarometerSensor</td><td>WeBarometerSensor barometer_A(PORT_A);</td>
</tr>
<tr>
    <th>测气压</th><td>float readPressure(void);</td><td>barometer_A.readPressure();</td>
</tr>
<tr>
    <th>测相对高度</th><td>float readHeight(void);</td><td>barometer_A.readHeight();</td>
</tr>
<tr>
    <th>测温度</th><td>float readTemp(void);</td><td>barometer_A.readTemp();</td>
</tr>
</table>

> <font size=4 >详情链接 **→** [气压传感器Arduino库-API头文件-WeBarometerSensor.h](https://github.com/WEEEMAKE/Weeemake_Libraries_for_Arduino/blob/master/Weeemake/src/WeBarometerSensor.h)</font>

### **Micropython-micro:bit-v1编程API**

<div align=center>
<font size=7 color=red>不支持</font>
</div>

### **Micropython-micro:bit-v2/ESP32/mPython/K210编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from WeBarometerSensor import *</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeBarometerSensor</td><td>barometer_A = WeBarometerSensor(PORT_A)</td>
</tr>
<tr>
    <th>测气压</th><td>distanceCM()</td><td>barometer_A.getValue()</td>
</tr>
</table>

> [!NOTE]
> - <font size=5 >目前只开放测气压这个功能</font>
> - <font size=5 >PORT_X的引用需要导入库：</font><font size=5 color=green >from WePort import *</font>

<!-- tabs:end -->


### **3.3-模块入手测试**

<font size=4 >模块上手使用，遇到问题时，可用WeeeCode编程测试，测试代码如下：</font>

<div align=center>
<img src="docs\electronic_modules\rj11\barometer_sensor\20220427165518.png"></img>
</div>

> <font size=4 >代码下载 **→** <a href = "docs\electronic_modules\rj11\barometer_sensor\气压传感器测试代码.sb3">气压传感器测试代码.sb3</a></font>

<!-- tabs:start -->

### **使用Arduino-C/C++编程的主控**

<font size=5>气压传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

### **使用Micropython编程的主控**

<font size=5>气压传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

<!-- tabs:end -->
---
    
