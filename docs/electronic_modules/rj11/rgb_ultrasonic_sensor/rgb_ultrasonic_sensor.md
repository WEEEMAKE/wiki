
<div align=center>
<h1 class="text-center">RGB超声波传感器</h1>
</div>

# **1. 简介**

<font size=5>RGB超声波传感器是一个用来测量距离的电子模块，测量范围是 4 cm 到 500 cm。可以用来帮助小车避开障碍或其他有关测距避障的项目。超声波发射器向某一方向发射超声波，在发射的同时开始计时，超声波在空气中传播，途中碰到障碍物就立即返回来，超声波接收器收到反射波就立即停止计时。声波在空气中的传播速度为 340m/s，根据计时器记录的时间 t，就可以计算出发射点距障碍物的距离 s，即：s=340*t/2。</font>

>  <font size=4>应用参考：避障小车，手持测距仪，水位监测，超声波计数器等。</font>

<font size=5>目前平台有2种RGB超声波模块：</font>
<!-- tabs:start -->

## **RGB Ultrasonic Sensor**

![q](rgb_ultrasonic_sensor.png)

## **Mini RGB Ultrasonic Sensor**


<!-- tabs:end -->

# **2. 参数规格**

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
<table class="imagetable">
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
# **3. 编程指南**
## **3.1 模块功能及图形化编程指南**

<font size=5>该模块支持的图形化编程平台有WeeeCode、编程猫平台、Mixly_Arduino、MakeCode等，其图形化编程大同小异，区别不会很大。</font>

<!-- Table goes in the document BODY -->
<table class="imagetable">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>测量距离（3~500cm）</td><td>(1个参数)端口</td><td><img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/img_1.png"></img></td>
</tr>
<tr>
    <td>设置内置RGB灯</td><td>（5个参数）端口、灯的位置、RGB三原色分量值</td><td><img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/img_2.png"></img></td>
</tr>
<tr>
    <td>LED灯设置（Mini RGB超声波模块独有）</td><td>（3个参数）端口、灯的位置、LED灯状态</td><td><img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/img_3.png"></img></td>
</tr>
</table>

## **3.2 文本代码编程指南**

<include src="js/10751382_ByGGIUaTpIGYGIXJPOzLagrkl/Brush_Python.html"></include>


## **3.3 模块入手自测**

---
# **4. 注意事项**
> [!NOTE]
> <font size=5 color=red>RGB超声波传感器上集成有6颗RGB灯，功耗相对比较大，使用时最好外接电源。</font>