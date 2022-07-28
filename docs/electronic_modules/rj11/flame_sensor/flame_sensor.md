<div align=center>
<h1 class="text-center">火焰传感器</h1>
</div>

## **1-简要介绍**

<html><body>
<p class=MsoTitle style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;letter-spacing:0pt;background:white'>火焰传感器包含三个红外探测头，可以用来探测火源或其它波长在</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:0pt;
background:white'> 760 <span lang=ZH-CN>纳米～</span>940 <span lang=ZH-CN>纳米范围内的光源，探测角度可达</span>
180 <span lang=ZH-CN>度，探测</span>3m<span lang=ZH-CN>以内火源。当检测到火焰时，蓝色指示灯亮，可以应用于灭火机器人、火焰报警器等安全监控项目中。火焰是由各种燃烧生成物、中间物、高温气体、碳氢物质以及无机物质为主体的高温固体微粒构成的。火焰的热辐射具有离散光谱的气体辐射和连续光谱的固体辐射。不同燃烧物的火焰辐射强度、波长分布有所差异，但总体来说，其对应火焰温度的1~2μm近红外波长具有很大的辐射强度</span>,<span
lang=ZH-CN>根据这种特性可制成火焰传感器。【原理摘自百度百科】</span></span></p>
</body></html>

## **2-参数规格**

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
    <td>通信方式</td><td>WM单总线</td>
</tr>
<tr>
    <td>探测距离</td><td>0~3米</td>
</tr>
<tr>
    <td>探头数量</td><td>3个</td>
</tr>
<tr>
    <td>反馈时间</td><td>15us</td>
</tr>
<tr>
    <td>能够检测的光谱带</td><td>940nm</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-模块功能及图形化编程指南**


<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp; </span><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有</span><span style='font-size:16.0pt;font-family:宋体;
color:#222222;background:white'>WeeeCode<span lang=ZH-CN>、编程猫平台、</span>Mixly_Arduino<span
lang=ZH-CN>、</span>MakeCode<span lang=ZH-CN>等，其图形化编程大同小异，区别不会很大。</span></span></p>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>返回各个探头的测量值</td><td>(2个参数）端口、选择探头</td><td><img src="docs\electronic_modules\rj11\flame_sensor\20190517-153038.png"></td>
</tr>
</table>

### **3.2-文本代码编程指南**

<!-- tabs:start -->

### **Arduino-IDE编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>头文件</th><td>WeFlameSensor.h</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeFlameSensor</td><td>WeFlameSensor flame_sensor_A(PORT_A);</td>
</tr>
<tr>
    <th>更新数据</th><td>void readData(void);</td><td>flame_sensor_A.readData();</td>
</tr>
<tr>
    <th>探头S1数据</th><td>uint8_t showSensor1(void);</td><td>flame_sensor_A.showSensor1();</td>
</tr>
<tr>
    <th>探头S2数据</th><td>uint8_t showSensor2(void);</td><td>flame_sensor_A.showSensor2();</td>
</tr>
<tr>
    <th>探头S3数据</th><td>uint8_t showSensor3(void);</td><td>flame_sensor_A.showSensor3();</td>
</tr>
<tr>
    <th>通过传参索引（1~3）获取数据</th><td> uint8_t readValue(uint8_t index);</td><td>flame_sensor_A.readValue(1); //探头S1</td>
</tr>
</table>

> <font size=4 >详情链接 **→** [气压传感器Arduino库-API头文件-WeFlameSensor.h](https://github.com/WEEEMAKE/Weeemake_Libraries_for_Arduino/blob/master/Weeemake/src/WeFlameSensor.h)</font>

### **Micropython-micro:bit-v1编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from elfshield import *</th><th>调用示例</th>
</tr>
<tr>
    <th>传参1~3索引获取数据（0~255）</th><td>flameSensor_readValue(port, index)</td><td>ultrasonic_getDistance(PORT_A, 1)  # 探头S1</td>
</tr>

</table>

### **Micropython-micro:bit-v2/ESP32/mPython/K210编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from WeFlameSensor import *</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeFlameSensor</td><td>flame_sensor_A = WeFlameSensor(PORT_A)</td>
</tr>
<tr>
    <th>更新数据</th><td>updateData()</td><td>flame_sensor_A.updateData()</td>
</tr>
<tr>
    <th>提取数据</th><td>S1,S2,S3</td><td>flame_sensor_A.S1  # 探头S1</td>
</tr>
</table>

> [!NOTE]
> - <font size=5 >PORT_X的引用需要导入库：</font><font size=5 color=green >from WePort import *</font>

<!-- tabs:end -->

### **3.3-模块入手自测**

<font size=4 >模块上手使用，遇到问题时，可用WeeeCode编程测试，测试代码如下：</font>

<div align=center>
<img src="docs/electronic_modules/rj11/flame_sensor/20220428110747.png"></img>
</div>

> <font size=4 >代码下载 **→** <a href = "docs/electronic_modules/rj11/flame_sensor/火焰传感器测试代码.sb3">火焰传感器测试代码.sb3</a></font>

<!-- tabs:start -->

### **使用Arduino-C/C++编程的主控**

<font size=5>火焰传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

### **使用Micropython编程的主控**

<font size=5>火焰传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

<!-- tabs:end -->