<div align=center>
<h1 class="text-center">雨滴传感器</h1>
</div>

## **1-简要介绍**

<html><body>
<p class=MsoNormal style='text-indent:36.0pt'><span style='font-size:16.0pt;
font-family:宋体;color:#222222;background:white'>雨滴传感器<span lang=EN-US>(Water
Sensor)</span>是通过测量电导率指示传感器是否干燥，潮湿或完全浸入水中。可用于降雨检测、液体泄漏等情景。</span></p>
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
    <td>接口类型</td><td>RJ11</td>
</tr>
<tr>
    <td>通信方式</td><td>WM单总线</td>
</tr>
<tr>
    <td>工作湿度</td><td>10~90% RH(不结露)</td>
</tr>
<tr>
    <td>返值范围</td><td>0~255</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-模块功能及图形化编程指南**

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
color:#222222;background:white'>该模块支持的图形化编程平台有<span lang=EN-US><span
style='box-sizing: border-box;font-variant-ligatures: normal;font-variant-caps: normal;
orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>WeeeCode</span></span><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>、<span lang=EN-US>Mixly_Arduino</span></span><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>、</span><span lang=EN-US><span
style='box-sizing: border-box;font-variant-ligatures: normal;font-variant-caps: normal;
orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>MakeCode</span></span><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>等，其图形化编程大同小异，区别不会很大。</span></span></p>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>读取传感器检测值（0~255）</td><td>（1个参数）端口</td><td><img src="docs\electronic_modules\rj11\water_sensor\20200306-112103.png"></td>
</tr>
</table>

### **3.2-文本代码编程指南**

