<div align=center>
<h1 class="text-center">光线传感器</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/elf_dip/light_sensor/EFF2054D-EA63-4842-85EF-59B94EAE5954.png" width=30%>
</div>

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;光线传感器（Light Sensor）是基于半导体的光电效应原理做成的传感器（将光信号转换为电信号），其可以对传感器周围环境的光强度进行检测，将光的强弱转换为电信号，传输给主控。</span>
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
    <td>接口类型</td><td>插针与ELF主控板适配使用</td>
</tr>
<tr>
    <td>工作温度</td><td>-30℃~70℃</td>
</tr>
</table>

## **3-编程指南**
### **3.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>返回探头的检测值(0~1023)</td><td>(1个参数）端口</td><td><img src="docs/electronic_modules/elf_dip/light_sensor/20200220-162841.png"></td>
</tr>
</table>

