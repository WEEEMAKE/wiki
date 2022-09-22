<div align=center>
<h1 class="text-center">数码管模块</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/rj11/four_digital_dispaly_module/20200306-162304.png" width=30%>
</div>

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;颜色识别传感器(Color Sensor)是基于罗姆系列的色彩传感器BH1745NUC，其为带I2C总线16位数字颜色传感IC,它将检测到的红色、绿色、蓝色光转换为数字值。</span>
</p>

## **2-参数规格**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>项</th><th>值/描述</th>
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
    <td>工作温度</td><td>-40℃~85 ℃</td>
</tr>
<tr>
    <td>位数</td><td>4位</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm * 24mm * 18.5mm（长*宽*高）</td>
</tr>
</table>

## **3-编程指南**
### **3.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>显示数字(-999~9999)</td><td>（2个参数）端口、数字</td><td><img src="docs/electronic_modules/rj11/four_digital_dispaly_module/20200303-111729.png"></td>
</tr>
<tr>
    <td>显示字符</td><td>（2个参数）端口、字符</td><td><img src="docs/electronic_modules/rj11/four_digital_dispaly_module/6A59DA87-058E-4964-ACB7-C13140739F54.png"></td>
</tr>
</table>

