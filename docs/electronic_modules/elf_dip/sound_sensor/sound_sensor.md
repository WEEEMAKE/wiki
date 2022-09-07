<div align=center>
<h1 class="text-center">声音传感器</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/elf_dip/sound_sensor/F944B39C-1A9A-49ad-811F-AC3EC77A5893.png" width=30%>
</div>

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;声音传感器（Sound Sensor）以麦克风为基础（将声信号转换为电信号），其可用来对周围环境中的声音强度进行检测，检测到的音量通过运算放大器放大，然后传输给主控处理。使用它可做一些交互性项目，例如声控开关，音量控制小车竞速等。</span>
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
    <td>通信方式</td><td>模拟值读取</td>
</tr>
<tr>
    <td>运算放大器</td><td>SD06</td>
</tr>
</table>

## **3-编程指南**
### **3.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>返回探头的检测值(0~900)</td><td>(1个参数）端口</td><td><img src="docs/electronic_modules/elf_dip/sound_sensor/20200220-164947.png"></td>
</tr>
</table>

