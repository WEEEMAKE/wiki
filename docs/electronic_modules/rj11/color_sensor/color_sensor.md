<div align=center>
<h1 class="text-center">颜色识别传感器</h1>
</div>

## **1-简要概述**

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>颜色识别传感器</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>(Color
Sensor)<span lang=ZH-CN>是基于罗姆系列的色彩传感器</span>BH1745NUC<span lang=ZH-CN>，其为带</span>I2C<span
lang=ZH-CN>总线</span>16<span lang=ZH-CN>位数字颜色传感</span>IC,<span lang=ZH-CN>它将检测到的红色、绿色、蓝色光转换为数字值。</span></span></p>

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
    <td>检测距离</td><td>3~10cm</td>
</tr>
<tr>
    <td>高亮白色补光LED灯</td><td>2个</td>
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
    <td>设置高亮白色补光LED灯亮灭</td><td>（2个参数）端口、LED灯状态</td><td><img src="docs/electronic_modules/rj11/color_sensor/20190517-170642.png"></td>
</tr>
<tr>
    <td>做白平衡操作</td><td>（1个参数）端口</td><td><img src="docs/electronic_modules/rj11/color_sensor/20190517-171116.png"></td>
</tr>
<tr>
    <td>读取需要的分量值</td><td>2个参数）端口、分量值选择</td><td><img src="docs/electronic_modules/rj11/color_sensor/20190517-171141.png"></td>
</tr>
</table>

