<div align=center>
<h1 class="text-center">RGB-8环形灯模块</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/elf_dip/rgb8_moudle/CECB5A9A-040F-4d6a-88BF-D1A7324754B2.png">
</div>

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;RGB-8模块包含8颗可调全彩RGB LED灯，每颗LED的颜色可以由红(R)、绿(G)、蓝(B)三个颜色分量来决定，RGB LED本身内部集成控制芯片，只需要1根信号线就可以实现每颗灯的全彩控制。可以使用该模块实现彩色跑马灯、彩虹灯等效果。</span>
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
    <td>工作温度</td><td>-25℃~80℃</td>
</tr>
<tr>
    <td>灯的型号</td><td>WS2812</td>
</tr>
<tr>
    <td>通信方式</td><td>RGB特有控制协议</td>
</tr>
<tr>
    <td>最大电流</td><td>每个60mA，共480mA</td>
</tr>
</table>

## **3-编程指南**
### **3.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>设置RGB灯的颜色</td><td>(4个参数）灯的位置、RGB灯颜色参数</td><td><img src="docs/electronic_modules/elf_dip/rgb8_moudle/20200224-183215.png"></td>
</tr>
</table>

> [!NOTE]
> <div><p>
    <strong><span style="font-size: 24px; font-family: 宋体, SimSun;">该模块只适配ELF大主控固定插槽，如下图：</span></strong>
</p>
<p style="text-align: center;">
    <strong><span style="font-size: 24px; font-family: 宋体, SimSun;"><img src="docs/electronic_modules/elf_dip/rgb8_moudle/7D917E8B-E814-4e44-931D-2F55673AAA5D.png"/></span></strong>
</p>
<p>
    <strong><span style="font-size: 24px; font-family: 宋体, SimSun;">备注：Arduino平台控制管脚为D13。</span></strong>
</p>
</div>

