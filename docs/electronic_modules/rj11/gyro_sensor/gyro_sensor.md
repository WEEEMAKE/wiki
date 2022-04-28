<div align=center>
<h1 class="text-center">陀螺仪传感器</h1>
</div>

## **1-简要介绍**

<html><body>
<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>陀螺仪传感器是基于整合了</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>3<span
lang=ZH-CN>轴陀螺仪</span>+3<span lang=ZH-CN>轴加速度运动处理</span>IC MPU-6050<span
lang=ZH-CN>所设计的传感器，它可以做机器人运动检测、姿态检测等操作。可以应用在自平衡小车、四轴飞行器、机器人及移动设备上。</span></span><span
style='font-family:宋体'><o:p></o:p></span></p>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>三轴方向参考：</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'><o:p></o:p></span></p>
</body></html>

<div align=center>
<img src="docs\electronic_modules\rj11\gyro_sensor\20190517-191957.png">
</div>
<div align=center>
<img src="docs\electronic_modules\rj11\gyro_sensor\20200303-164449.png">
</div>

> [!NOTE]
> <font size=4 >陀螺仪模块的加速度指的是以轴为中心，旋转所产生的速度变化，即旋转加速度；角度也是如此，是以轴为中心，旋转所产生的角度变化。</font>

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
    <td>工作温度</td><td>0℃~+70℃</td>
</tr>
<tr>
    <td>3轴角速度全格感测范围</td><td>±2000°/sec</td>
</tr>
<tr>
    <td>3轴加速度全格感测范围</td><td>±2g</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-模块功能及图形化编程指南**

<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有<span lang=EN-US><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>WeeeCode</span></span><span
style='box-sizing: border-box;font-variant-ligatures: normal;font-variant-caps: normal;
orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>、<span lang=EN-US>Mixly_Arduino</span></span><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>等，其图形化编程大同小异，区别不会很大。</span></span><span
lang=EN-US style='font-size:16.0pt;font-family:华文楷体'>&nbsp;</span></p>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>获取某个轴上的旋转角度值/旋转加速度值</td><td>(3个参数）端口、角度量/加速度量选择、轴选择</td><td><img src="docs\electronic_modules\rj11\gyro_sensor\20200303-155558.png"></td>
</tr>
</table>

<!-- > [!NOTE]
> <font size=4 >目前支持陀螺仪传感器的平台：</font>
> - [x] Arduino系列主控 -->

### **3.2-文本代码编程指南**

<!-- tabs:start -->
<!-- 
### **Arduino-IDE编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>头文件</th><td>WeTouchSensor.h</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeTouchSensor</td><td>WeTouchSensor touch_sensor_A(PORT_A);</td>
</tr>
<tr>
    <th>模式设置（默认连续触发）</th><td>void setMode(uint8_t value);</td><td>touch_sensor_A.setMode(1);</td>
</tr>
<tr>
    <th>获取数据(布尔值)</th><td>uint8_t touched(void);</td><td>touch_sensor_A.touched();</td>
</tr>
</table>

> <font size=4 >详情链接 **→** [单路触摸传感器Arduino库-API头文件-WeTouchSensor.h](https://github.com/WEEEMAKE/Weeemake_Libraries_for_Arduino/blob/master/Weeemake/src/WeTouchSensor.h)</font>

### **Micropython-micro:bit-v1编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from elfshield import *</th><th>调用示例</th>
</tr>
<tr>
    <th>获取数据(布尔值)</th><td>touchSensor_read(port)</td><td>touchSensor_read(PORT_A)</td>
</tr>

</table>

### **Micropython-micro:bit-v2/ESP32/mPython/K210编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from WeSingleTouch import *</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeSingleTouch</td><td>touch_sensor_A = WeSingleTouch(PORT_A)</td>
</tr>
<tr>
    <th>获取数据(布尔值)</th><td>getValue()</td><td>touch_sensor_A.getValue()</td>
</tr>
</table>

> [!NOTE]
> - <font size=5 >PORT_X的引用需要导入库：</font><font size=5 color=green >from WePort import *</font>

<!-- tabs:end -->

### **3.3-模块入手自测**

<font size=4 >模块上手使用，遇到问题时，可用WeeeCode编程测试，测试代码如下：</font>

<div align=center>
<img src="docs\electronic_modules\rj11\touch_sensor\20220428120015.png"></img>
</div>

> <font size=4 >代码下载 **→** <a href = "docs\electronic_modules\rj11\touch_sensor\单路触摸传感器测试代码.sb3">单路触摸传感器测试代码.sb3</a></font>

<!-- tabs:start -->

### **使用Arduino-C/C++编程的主控**

<font size=5>单路触摸传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

### **使用Micropython编程的主控**

<font size=5>单路触摸传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font> -->

<!-- tabs:end -->


