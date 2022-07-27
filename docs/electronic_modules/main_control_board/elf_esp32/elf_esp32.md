<div align=center>
<h1 class="text-center">ELF ESP32主控板</h1>
</div>

## **1-简要概述**

<font size=5>ELF ESP32主要是针对学习Python而设计的入门级主控板，所用接口既兼容开源系列传感器，又具备防反接属性，可较好用于课后服务方案。主控所使用ESP32模组，同时具备wifi和蓝牙功能，可以接触物联网相关内容。</font>

## **2-主板外观**

<div align="center">
<img src = "docs\electronic_modules\main_control_board\elf_esp32\ELF-ESP32.png" width=40%>
</div>

---
## **3-接口布局**

<div align="center">
<img src = "docs\electronic_modules\main_control_board\elf_esp32\P2.png" >
</div>

## **4-硬件参数**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: center;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>输入电压</td><td>DC 6~10V</td>
</tr>
<tr>
    <td>工作电压</td><td>3.3V</td>
</tr>
<tr>
    <td>主控芯片</td><td>ESP32-WROOM-32模组</td>
</tr>
<tr>
    <td>指示灯</td><td>电源指示灯（红色），电机驱动故障灯（红色）</td>
</tr>
<tr>
    <td>LED灯</td><td>板载LED灯（蓝色）</td>
</tr>
<tr>
    <td>电机驱动</td><td>直流电机*2</td>
</tr>
<tr>
    <td>USB接口</td><td>USB-B</td>
</tr>
<tr>
    <td>电源接口</td><td>DC2.5</td>
</tr>
<tr>
    <td>主控尺寸</td><td>70mm*54mm*15mm(长*宽*高)</td>
</tr>
</table>


---

## **5-原理图**

<embed class="pdfobject" src="docs\electronic_modules\main_control_board\elf_esp32\ESP32_430.pdf" style="overflow: auto; width: 100%; height: 50rem;">

## **6-编程指南**
