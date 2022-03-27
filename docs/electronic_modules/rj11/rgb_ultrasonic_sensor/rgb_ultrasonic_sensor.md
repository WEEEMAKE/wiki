
<div align=center>
<h1 class="text-center">RGB超声波传感器</h1>
</div>

# **1. 简介**

<div align=center>
<img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/rgb_ultrasonic_sensor.png">
</div>

<font size=5>RGB超声波传感器是一个用来测量距离的电子模块，测量范围是 4 cm 到 500 cm。可以用来帮助小车避开障碍或其他有关测距避障的项目。超声波发射器向某一方向发射超声波，在发射的同时开始计时，超声波在空气中传播，途中碰到障碍物就立即返回来，超声波接收器收到反射波就立即停止计时。声波在空气中的传播速度为 340m/s，根据计时器记录的时间 t，就可以计算出发射点距障碍物的距离 s，即：s=340*t/2。</font>

>  <font size=4>应用参考：避障小车，手持测距仪，水位监测，超声波计数器等。</font>

<font size=5>目前平台有2种RGB超声波模块</font>
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

# **3. 编程指南**
## 3.1 模块功能及图形化编程指南

<div class=WordSection1>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
14.0pt;font-family:等线'>该模块支持的图形化编程平台有</span><span style='font-size:14.0pt'>WeeeCode</span><span
lang=ZH-CN style='font-size:14.0pt;font-family:等线'>、编程猫平台、</span><span
style='font-size:14.0pt'>Mixly_Arduino</span><span lang=ZH-CN style='font-size:
14.0pt;font-family:等线'>、</span><span style='font-size:14.0pt'>MakeCode</span><span
lang=ZH-CN style='font-size:14.0pt;font-family:等线'>等，其图形化编程大同小异，区别不会很大。</span></p>

<div>

<div align=center>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=176 style='width:131.9pt;border:solid windowtext 1.0pt;padding:
  0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:等线;color:windowtext'>模块功能</span></b></p>
  </td>
  <td width=371 valign=top style='width:278.45pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 0in 0in 0in'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:等线;color:windowtext'>需传参数</span></b></p>
  </td>
  <td width=482 style='width:361.8pt;border:solid windowtext 1.0pt;border-left:
  none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:等线;color:windowtext'>图形化编程块举例</span></b><b><span
  style='font-size:14.0pt;color:windowtext'>(</span></b><b><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>其他平台图形化编程块大同小异</span></b><b><span
  style='font-size:14.0pt;color:windowtext'>)</span></b></p>
  </td>
 </tr>
 <tr style='height:1.0in'>
  <td width=176 style='width:131.9pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>测量距离（</span><span
  style='font-size:14.0pt;color:windowtext'>3~500cm</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>）</span></p>
  </td>
  <td width=371 style='width:278.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 0in 0in 0in;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>（</span><span
  style='font-size:14.0pt;color:windowtext'>1</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>个参数）端口</span></p>
  </td>
  <td width=482 style='width:361.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='color:windowtext'><img width=174 height=36
  src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/P1.png"></span></p>
  </td>
 </tr>
 <tr style='height:1.0in'>
  <td width=176 style='width:131.9pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>设置内置</span><span
  style='font-size:14.0pt;color:windowtext'>RGB</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>灯</span></p>
  </td>
  <td width=371 style='width:278.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 0in 0in 0in;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>（</span><span
  style='font-size:14.0pt;color:windowtext'>5</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>个参数）端口、灯的位置、</span><span
  style='font-size:14.0pt;color:windowtext'>RGB</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>三原色分量值</span></p>
  </td>
  <td width=482 valign=top style='width:361.8pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:14.0pt;color:windowtext'><img width=468 height=173
  src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/P2.png"></span></b></p>
  </td>
 </tr>
 <tr style='height:1.0in'>
  <td width=176 style='width:131.9pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;color:windowtext'>LED</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>灯设置（</span><span
  style='font-size:14.0pt;color:windowtext'>Mini RGB</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>超声波模块独有）</span></p>
  </td>
  <td width=371 style='width:278.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 0in 0in 0in;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>（</span><span
  style='font-size:14.0pt;color:windowtext'>3</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>个参数）端口、灯的位置、</span><span
  style='font-size:14.0pt;color:windowtext'>LED</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>灯状态</span></p>
  </td>
  <td width=482 style='width:361.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='color:windowtext'><img width=335 height=54
  src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/P3.png"></span></p>
  </td>
 </tr>
</table>

</div>

<p class=MsoNormal>&nbsp;</p>

</div>

</div>

## **3.2 文本代码编程指南**
# **4. 注意事项**

<font size=5>RGB超声波传感器上集成有6颗RGB灯，功耗相对比较大，使用时最好外接电源。</font>


