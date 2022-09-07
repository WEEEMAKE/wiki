<div align=center>
<h1 class="text-center">LED面板矩阵屏</h1>
</div>

## **1-简要概述**

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;LED面板矩阵屏是由蓝色LED灯排成矩阵组成的, 可以控制显示数字，字母或符号,目前Weeemake电子模块平台有2款尺寸的LED矩阵屏，尺寸分别是7*21和5*14。</span>
</p>

<!-- tabs:start -->

### **7x21**

<div align=center>
<img src="docs/electronic_modules/rj11/led_panel_dispaly_module/F6C90219-0BAE-4368-9348-822CEA7B2EE6.png" width=30%>
</div>

### **5x14**

<div align=center>
<img src="docs/electronic_modules/rj11/led_panel_dispaly_module/520738AF-7F56-4a10-BCDD-800D300DA135.png" width=30%>
</div>

<!-- tabs:end -->

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
    <td>灯颜色</td><td>蓝色</td>
</tr>
</table>

## **3-编程指南**
### **3.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>显示数字(-999~9999)</td><td>(3个参数）屏尺寸、端口、数字</td><td><img src="docs/electronic_modules/rj11/led_panel_dispaly_module/20200316-153030.png"></td>
</tr>
<tr>
    <td>以时间格式显示</td><td>(5个参数）屏尺寸、端口、时、冒号、分</td><td><img src="docs/electronic_modules/rj11/led_panel_dispaly_module/20200316-153039.png"></td>
</tr>
<tr>
    <td>显示字符</td><td>(5个参数）屏尺寸、端口、X轴、Y轴、字符</td><td><img src="docs/electronic_modules/rj11/led_panel_dispaly_module/20200316-153045.png"></td>
</tr>
<tr>
    <td>显示图像</td><td>(4个参数）端口、X轴、Y轴、点位图</td><td><img src="docs/electronic_modules/rj11/led_panel_dispaly_module/20200316-153051.png"></td>
</tr>
<tr>
    <td>控制某一单像素点亮灭</td><td>(5个参数）屏尺寸、端口、状态、X轴、Y轴</td><td><img src="docs/electronic_modules/rj11/led_panel_dispaly_module/20200316-153058.png"></td>
</tr>
<tr>
    <td>清屏</td><td>(2个参数）屏尺寸、端口</td><td><img src="docs/electronic_modules/rj11/led_panel_dispaly_module/20200316-153104.png"></td>
</tr>
</table>

