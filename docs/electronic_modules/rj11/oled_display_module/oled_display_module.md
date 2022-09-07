<div align=center>
<h1 class="text-center">0.96寸OLED显示屏</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/rj11/oled_display_module/20200316-181627.png" width=30%>
</div>

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;0.96寸OLED显示屏是基于一个尺寸为0.96英寸的OLED显示屏所设计的电子模块，显示屏在电子制作项目中起着重要作用，让数据可视化，实时显示监测数据信息。</span>
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
    <td>分辨率</td><td>128*64</td>
</tr>
<tr>
    <td>控制芯片</td><td>SSD1306</td>
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
    <td>设置字体大小</td><td>（2个参数）端口、返值数据类型</td><td><img src="docs/electronic_modules/rj11/oled_display_module/20200316-170927.png"></td>
</tr>
<tr>
    <td>显示字符</td><td>（4个参数）端口、X坐标、Y坐标、字符</td><td><img src="docs/electronic_modules/rj11/oled_display_module/20200316-170932.png"></td>
</tr>
<tr>
    <td>显示数字</td><td>（4个参数）端口、X坐标、Y坐标、数字</td><td><img src="docs/electronic_modules/rj11/oled_display_module/20200316-170936.png"></td>
</tr>
<tr>
    <td>清屏</td><td>（1个参数）端口</td><td><img src="docs/electronic_modules/rj11/oled_display_module/20200316-170946.png"></td>
</tr>
</table>

