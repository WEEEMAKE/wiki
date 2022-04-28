<div align=center>
<h1 class="text-center">电子指南针传感器</h1>
</div>

## **1-简要介绍**

<div align=center>
<img src="docs\electronic_modules\rj11\compass_sensor\20190511-122900.png">
</div>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>电子指南针传感器是基于高精度三轴磁传感器芯片 </span><b><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>QMC5883L</span></b><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:#222222;background:white'>，它采用第三代</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>AMR<span
lang=ZH-CN>磁传感技术，具有高精度、低功耗、高可靠性等特点，该芯片可应用于这些领域：</span></span><span
style='font-family:宋体'><o:p></o:p></span></p>

<p class=MsoListParagraph style='margin-left:78.0pt;text-indent:-.25in'><span
style='font-size:16.0pt;font-family:宋体;color:#222222'>·<span lang=ZH-CN
style='background:white'>实现无人机等移动终端的高精度定位导航需求；</span></span><span
style='font-family:宋体'><o:p></o:p></span></p>

<p class=MsoListParagraph style='margin-left:78.0pt;text-indent:-.25in'><span
style='font-size:16.0pt;font-family:宋体;color:#222222'>·<span lang=ZH-CN
style='background:white'>实现无人停车场的高可靠性自动停车监测功能；</span></span><span
style='font-family:宋体'><o:p></o:p></span></p>

<p class=MsoListParagraph style='margin-left:78.0pt;text-indent:-.25in'><span
style='font-size:16.0pt;font-family:宋体;color:#222222'>·<span lang=ZH-CN
style='background:white'>满足其他高精度工业控制和汽车电子要求；</span></span><span
style='font-family:宋体'><o:p></o:p></span></p>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>本模块可以检测周围的磁场强度，使运动的装置或设备转动到指定的方向，比如安装在小车上，可以控制小车转动到指定方向或沿着指定方向行走。</span><span
style='font-family:宋体'><o:p></o:p></span></p>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>三轴方向参考：</span><span
style='font-family:宋体'><o:p></o:p></span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='mso-no-proof:yes'><img border=0 width=448 height=447 id="_x0000_i1026"
src="docs\electronic_modules\rj11\compass_sensor\20190511-154735.png"
title="定向方向参考"></span></p>


## 2-**参数规格**

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
    <td>传感器型号</td><td>QMC5883L</td>
</tr>
<tr>
    <td>工作温度</td><td>-40℃~+85℃</td>
</tr>
<tr>
    <td>定向精度</td><td>1° ~ 2°</td>
</tr>
<tr>
    <td>模块尺寸</td><td>100mm*32mm*30mm(长*宽*高)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-模块功能及编程指南**

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp; </span><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有</span><span style='font-size:16.0pt;font-family:宋体;
color:#222222;background:white'>WeeeCode<span lang=ZH-CN>、</span>Mixly_Arduino<span lang=ZH-CN>等，其图形化编程大同小异，区别不会很大。</span></span></p>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>获取某个轴上的航向角度值</td><td>(2个参数）端口、轴选择</td><td><img src="docs\electronic_modules\rj11\compass_sensor\20190511-161322.png"></td>
</tr>
</table>

### **3.2-文本代码编程指南**

<!-- tabs:start -->

### **Arduino-IDE编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>头文件</th><td>WeCompassSensor.h</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeCompassSensor</td><td>WeCompassSensor compass_A(PORT_A);</td>
</tr>
<tr>
    <th>测X轴</th><td>int16_t getHeadS(void);</td><td>compass_A.getHeadS();</td>
</tr>
<tr>
    <th>测Y轴</th><td>int16_t getHeadY(void);</td><td>compass_A.getHeadY();</td>
</tr>
<tr>
    <th>测Z轴</th><td>int16_t getHeadZ(void);</td><td>compass_A.getHeadZ();</td>
</tr>
</table>

> <font size=4 >详情链接 **→** [电子指南针传感器Arduino库-API头文件-WeCompassSensor.h](https://github.com/WEEEMAKE/Weeemake_Libraries_for_Arduino/blob/master/Weeemake/src/WeCompassSensor.h)</font>

### **Micropython-micro:bit-v1编程API**

<div align=center>
<font size=7 color=red>不支持</font>
</div>

### **Micropython-micro:bit-v2/ESP32/mPython/K210编程API**

<div align=center>
<font size=7 color=red>不支持</font>
</div>

<!-- tabs:end -->

### **3.3-模块入手测试**

<font size=4 >模块上手使用，遇到问题时，可用WeeeCode编程测试，测试代码如下：</font>

<div align=center>
<img src="docs\electronic_modules\rj11\compass_sensor\20220427174723.png"></img>
</div>

> <font size=4 >代码下载 **→** <a href = "docs\electronic_modules\rj11\compass_sensor\电子指南针传感器测试代码.sb3">电子指南针传感器测试代码.sb3</a></font>

<!-- tabs:start -->

### **使用Arduino-C/C++编程的主控**

<font size=5>气压传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

### **使用Micropython编程的主控**

<font size=5>气压传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

<!-- tabs:end -->
---

## **4-注意事项**

<html><body>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>（</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>1<span
lang=ZH-CN>）由于磁传感器是感应地磁的，所以该模块使用时，周围不宜有强磁性的物体；</span><o:p></o:p></span></p>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>（</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>2<span
lang=ZH-CN>）模块上的</span>8<span lang=ZH-CN>颗蓝色</span>LED<span lang=ZH-CN>灯环对应的是</span>X<span
lang=ZH-CN>轴的变化，且亮灯指示的是南方。</span><o:p></o:p></span></p>

</body></html>