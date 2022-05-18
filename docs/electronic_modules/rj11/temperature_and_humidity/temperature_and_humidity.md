<div align=center>
<h1 class="text-center">温湿度传感器</h1>
</div>

## **1-简要介绍**

<div align=center>
<img src="docs\electronic_modules\rj11\temperature_and_humidity\20190515-154203.png">
</div>

<html><body>
<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>温湿度传感器是基于数字温湿度传感器</span><b><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:yellow'>DH11</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>的一款传感器，它是一种集温度、湿度一体的复合传感器，它能把温度和湿度物理量通过温、湿度敏感元件和相应电路转化成方便计算机、</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>PLC<span
lang=ZH-CN>、智能仪表等数据采集设备直接读取的数字量。</span>DHT11<span lang=ZH-CN>由电阻式感湿器件和</span>NTC<span
lang=ZH-CN>系数感温器件构成，具有校准数字信号输出功能，采用单总线串行接口，输出数据一共</span>5<span lang=ZH-CN>个字节，分别表示：湿度整数位、湿度小数位，温度整数位、温度小数位及校验和，其中检验和为湿度与温度之和的最低八位数据。</span></span></p>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>本模块可用于气象台，温湿度调节器等。</span><span
style='font-family:宋体'><o:p></o:p></span></p>

<p class=MsoNormal align=center style='text-align:center'></p>
</body></html>

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
    <td>接口类型</td><td>RJ11</td>
</tr>
<tr>
    <td>温度测量</td><td>测量范围-40℃~60℃，测量精度0.1℃，误差±1℃（0~60℃）</td>
</tr>
<tr>
    <td>湿度测量</td><td>测量范围0% ~ 99%RH，测量精度1%RH，误差±5%RH（0~50℃）</td>
</tr>
<tr>
    <td>信号采样周期</td><td>1秒</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>



## **3-编程指南**

### **3.1-图形化编程**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>返回测量的温度值、湿度值</td><td>(2个参数）端口、需要获取的值</td><td><img src="docs\electronic_modules\rj11\temperature_and_humidity\20190515-155326.png"></img></td>
</tr>
</table>

### **3.2-文本代码编程**

### **3.3-模块入手自测**
