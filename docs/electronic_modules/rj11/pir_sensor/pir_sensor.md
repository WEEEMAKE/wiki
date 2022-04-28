<div align=center>
<h1 class="text-center">人体红外传感器</h1>
</div>

## **1-简要介绍**

<div align=center>
<img src="docs\electronic_modules\rj11\pir_sensor\20190517-142034.png">
</div>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>人体红外传感器</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>(PIR Sensor)</span><span
style='font-size:11.5pt;font-family:"Helvetica",sans-serif;color:#222222;
background:white'> </span><span lang=ZH-CN style='font-size:16.0pt;font-family:
宋体;color:#222222;background:white'>是用来检测人或动物身体上发出的红外辐射的模块，最大测量范围为</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'> 5m<span
lang=ZH-CN>。如果有人在量程内运动，板上的红色</span> LED <span lang=ZH-CN>会被点亮。</span><o:p></o:p></span></p>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>使用参考：人体感应灯</span></p>

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
    <td>工作温度</td><td>-20℃~+70℃</td>
</tr>
<tr>
    <td>触发方式</td><td>可重复触发</td>
</tr>
<tr>
    <td>检测角度</td><td>100°</td>
</tr>
<tr>
    <td>检测距离</td><td>最大5米</td>
</tr>
<tr>
    <td>LED指示灯</td><td>1个(蓝色)</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-模块功能及图形化编程指南**
<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp; </span><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有</span><span style='font-size:16.0pt;font-family:宋体;
color:#222222;background:white'><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>WeeeCode</span><span lang=ZH-CN><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>、编程猫平台、</span></span><span
style='box-sizing: border-box;font-variant-ligatures: normal;font-variant-caps: normal;
orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>Mixly_Arduino</span><span lang=ZH-CN><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>、</span></span><span
style='box-sizing: border-box;font-variant-ligatures: normal;font-variant-caps: normal;
orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>MakeCode</span><span lang=ZH-CN><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>等，其图形化编程大同小异，区别不会很大。</span></span></span></p>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>获取传感器是否触发（布尔值）</td><td>(1个参数）端口</td><td><img src="docs\electronic_modules\rj11\pir_sensor\20190517-144315.png"></td>
</tr>
</table>

### **3.2-文本代码编程指南**

<!-- tabs:start -->

### **Arduino-IDE编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>头文件</th><td>WePIRSensor.h</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WePIRSensor</td><td>WePIRSensor pir_A(PORT_A);</td>
</tr>
<tr>
    <th>获取数据(布尔值)</th><td>uint8_t readSensor(void);</td><td>pir_A.readSensor();</td>
</tr>
</table>

> <font size=4 >详情链接 **→** [人体红外传感器Arduino库-API头文件-WePIRSensor.h](https://github.com/WEEEMAKE/Weeemake_Libraries_for_Arduino/blob/master/Weeemake/src/WePIRSensor.h)</font>

### **Micropython-micro:bit-v1编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from elfshield import *</th><th>调用示例</th>
</tr>
<tr>
    <th>获取数据(布尔值)</th><td>PIRsensor_read(port)</td><td>PIRsensor_read(PORT_A)</td>
</tr>

</table>

### **Micropython-micro:bit-v2/ESP32/mPython/K210编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from WePIRSensor import *</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WePIRSensor</td><td>pir_A = WePIRSensor(PORT_A)</td>
</tr>
<tr>
    <th>获取数据(布尔值)</th><td>getValue()</td><td>pir_A.getValue()</td>
</tr>
</table>

> [!NOTE]
> - <font size=5 >PORT_X的引用需要导入库：</font><font size=5 color=green >from WePort import *</font>

<!-- tabs:end -->

### **3.3-模块入手自测**

<font size=4 >模块上手使用，遇到问题时，可用WeeeCode编程测试，测试代码如下：</font>

<div align=center>
<img src="docs\electronic_modules\rj11\pir_sensor\20220428113548.png"></img>
</div>

> <font size=4 >代码下载 **→** <a href = "docs\electronic_modules\rj11\pir_sensor\人体红外传感器测试代码.sb3">人体红外传感器测试代码.sb3</a></font>

<!-- tabs:start -->

### **使用Arduino-C/C++编程的主控**

<font size=5>人体红外传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

### **使用Micropython编程的主控**

<font size=5>人体红外传感器支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

<!-- tabs:end -->

