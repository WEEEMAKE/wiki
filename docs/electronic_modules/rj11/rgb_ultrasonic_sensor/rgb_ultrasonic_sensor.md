
<div align=center>
<h1 class="text-center">RGB超声波传感器</h1>
</div>

## **1-简要介绍**

<font size=4>RGB超声波传感器是一个用来测量距离的电子模块，测量范围是 4 cm 到 500 cm。可以用来帮助小车避开障碍或其他有关测距避障的项目。超声波发射器向某一方向发射超声波，在发射的同时开始计时，超声波在空气中传播，途中碰到障碍物就立即返回来，超声波接收器收到反射波就立即停止计时。声波在空气中的传播速度为 340m/s，根据计时器记录的时间 t，就可以计算出发射点距障碍物的距离 s，即：s=340*t/2。</font>

>  <font size=4>应用参考：避障小车，手持测距仪，水位监测，超声波计数器等。</font>

<font size=5>目前平台有2种RGB超声波模块：</font>
<!-- tabs:start -->

## **RGB Ultrasonic Sensor**

<div align=center>
<img src="docs\electronic_modules\rj11\rgb_ultrasonic_sensor\rgb_ultrasonic_sensor.png">
</div>

## **Mini RGB Ultrasonic Sensor**

<font size=5>图片未上传</font>

<!-- tabs:end -->

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
    <td>通信方式</td><td>WM单总线协议</td>
</tr>
<tr>
    <td>超声波频率</td><td>42kHz</td>
</tr>
<tr>
    <td>测距精度</td><td>1cm</td>
</tr>
<tr>
    <td>测距范围</td><td>3cm~500cm</td>
</tr>
<tr>
    <td>输出数据</td><td>距离值(单位：厘米)</td>
</tr>
<tr>
    <td>RGB灯</td><td>探头内置，发射端、接收端各3颗</td>
</tr>
<tr>
    <td>LED灯</td><td>Mini版特有，模块左右各1颗黄色LED灯</td>
</tr>
<tr>
    <td>模块尺寸</td><td>100mm*32mm*30mm(长*宽*高)</td>
</tr>
</table>

---
## **3. 编程指南**
### **3.1 模块功能及图形化编程指南**

<font size=4>该模块支持的图形化编程平台有WeeeCode、编程猫平台、Mixly_Arduino、MakeCode等，其图形化编程大同小异，区别不会很大。</font>

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>测量距离（3~500cm）</td><td>(1个参数)端口</td><td><img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/img_1.png"></img></td>
</tr>
<tr>
    <td>驱动探头内置RGB灯</td><td>（5个参数）端口、灯的位置、RGB三原色分量值</td><td><img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/img_2.png"></img></td>
</tr>
<tr>
    <td>驱动LED灯(Mini RGB超声波模块可用)</td><td>（3个参数）端口、灯的位置、LED灯状态</td><td><img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/img_3.png"></img></td>
</tr>
</table>

### **3.2 文本代码编程指南**

<!-- tabs:start -->

#### **Arduino-IDE编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>头文件</th><td>WeUltrasonicSensor.h</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeUltrasonicSensor</td><td>WeUltrasonicSensor ultrasonic_A(PORT_A);</td>
</tr>
<tr>
    <th>测距</th><td>double distanceCm(void);</td><td>ultrasonic_A.distanceCm();</td>
</tr>
<tr>
    <th>驱动探头内置RGB灯</th><td>void setColor(uint8_t index, uint8_t red, uint8_t green, uint8_t blue);</td><td>ultrasonic_A.setColor(3, 255, 255, 255);</td>
</tr>
<tr>
    <th>驱动LED灯(Mini RGB超声波模块可用)</th><td>void setLed(uint8_t index, bool isOn);</td><td>ultrasonic_A.setLed(3, true);</td>
</tr>
</table>

> <font size=4 >详情链接 **→** [RGB超声波传感器Arduino库-API头文件-WeUltrasonicSensor.h](https://github.com/WEEEMAKE/Weeemake_Libraries_for_Arduino/blob/master/Weeemake/src/WeUltrasonicSensor.h)</font>

#### **Micropython-micro:bit-v1编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from elfshield import *</th><th>调用示例</th>
</tr>
<tr>
    <th>测距</th><td>ultrasonic_getDistance(port)</td><td>ultrasonic_getDistance(PORT_A)</td>
</tr>
<tr>
    <th>驱动探头内置RGB灯</th><td>ultrasonic_setColor(port, index, red, green, blue)</td><td>ultrasonic_setColor(PORT_A, 3, 255, 255, 255)</td>
</tr>
</table>

#### **Micropython-micro:bit-v2/ESP32/mPython/K210编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from WeUltrasonicSensor import *</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeUltrasonicSensor</td><td>ultrasonic_A = WeUltrasonicSensor(PORT_A)</td>
</tr>
<tr>
    <th>测距</th><td>distanceCM()</td><td>ultrasonic_A.distanceCM()</td>
</tr>
<tr>
    <th>驱动探头内置RGB灯</th><td>rgbShow(index, red, green, blue)</td><td>ultrasonic_A.rgbShow(3, 255, 255, 255)</td>
</tr>
</table>

> [!NOTE]
> - <font size=5 >PORT_X的引用需要导入库：</font><font size=5 color=green >from WePort import *</font>

<!-- tabs:end -->

### **3.3 模块入手自测**

<font size=4 >模块上手使用，遇到问题时，可用WeeeCode编程测试，测试代码如下：</font>

<div align=center>
<img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/test_code_1_zh.png"></img>
</div>

> <font size=4 >代码下载 **→** <a href = "docs/electronic_modules/rj11/rgb_ultrasonic_sensor/RGB%E8%B6%85%E5%A3%B0%E6%B3%A2%E4%BC%A0%E6%84%9F%E5%99%A8%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81.sb3">RGB超声波传感器测试代码.sb3</a></font>

<!-- tabs:start -->

### **使用Arduino-C/C++编程的主控**

<font size=5>RGB超声波传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

### **使用Micropython编程的主控**

<font size=5>RGB超声波传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

<!-- tabs:end -->
---
## **4. 注意事项**

> [!NOTE]
> <font size=5 color=red>RGB超声波传感器上集成有6颗RGB灯，功耗相对比较大，使用时最好外接电源。</font>

