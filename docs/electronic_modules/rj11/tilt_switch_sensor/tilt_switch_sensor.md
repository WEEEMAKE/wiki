<div align=center>
<h1 class="text-center">倾斜开关传感器</h1>
</div>


## **1-简要概述**

<div align=center>
<img src="docs\electronic_modules\rj11\tilt_switch_sensor\tilt_switch_sensor.png" width=30%>
</div>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; 倾斜开关传感器用来检测是否倾斜，当传感器向右或向左倾斜时会有相应的指示灯显示。垂直悬挂的倾斜开关探头在受到外力作用且偏离垂直位置17度以上时，倾斜开关内部的金属球触点动作，常闭触点断开。当外力撤消后，倾斜开关回复到垂直状态，金属球触点复又闭合。

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; 应用示例：水平测量仪等
</span>
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
    <td>开关个数</td><td>2个</td>
</tr>
<tr>
    <td>开关方式</td><td>机械式</td>
</tr>
<tr>
    <td>尺寸大小</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>


## **3-编程指南**

### 3.1. 模块功能及图形化编程指南 

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp; </span><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有WeeeCode、编程猫平台、Mixly_Arduino、MakeCode等，其图形化编程大同小异，区别不会很大。</span></span></span></p>  

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>返回两个开关的开关值
</td><td>(2个参数）端口、需要判断的状态</td><td><img src="docs\electronic_modules\rj11\tilt_switch_sensor\20200220-144052.png"></td>
</tr>
</table>


<p class=MsoNormal style='text-indent:21.0pt'>&nbsp;</p>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>图形化编程示例：</span></p>
<p class=MsoNormal align=center style='text-align:center'><span
  style='color:windowtext'><img width=568 height=605 id="图片 2"
  src="docs\electronic_modules\rj11\tilt_switch_sensor\20200219-163015.png"></span></p>

## **3.2-文本代码编程指南**

<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:4;tab-size:4;">    <span style="color:#c695c6;">#include</span><span style="color:#5fb4b4;">&lt;</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">></span><br>    WeTiltSwitch <span style="color:#5fb4b4;">tilt_D</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">PORT_D</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    WeRGBLed <span style="color:#5fb4b4;">rgb_led_board</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">OnBoard_RGB</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    <span style="color:#6699cc;font-style:italic;">uint8_t</span> tilt_D_value<span style="color:#a6acb9;">;</span><br>    <span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">{</span><br>    <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">1000</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    <span style="color:#ffffff;">}</span><br>    <span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">{</span><br>    tilt_D_value <span style="color:#f97b58;">=</span> tilt_D<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readSensor</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    <span style="color:#c695c6;">if</span><span style="color:#ffffff;">(</span>tilt_D_value <span style="color:#f97b58;">==</span> <span style="color:#f9ae58;">2</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">{</span><br>            rgb_led_board<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">setColor</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">1</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">20</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">0</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>            rgb_led_board<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">show</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>        <span style="color:#ffffff;">}</span><span style="color:#c695c6;">else</span> <span style="color:#c695c6;">if</span><span style="color:#ffffff;">(</span>tilt_D_value <span style="color:#f97b58;">==</span> <span style="color:#f9ae58;">1</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">{</span><br>            rgb_led_board<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">setColor</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">1</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">0</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">0</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">20</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>            rgb_led_board<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">show</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>        <span style="color:#ffffff;">}</span><span style="color:#c695c6;">else</span><span style="color:#ffffff;">{</span><br>            rgb_led_board<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">setColor</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">1</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">0</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">0</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>            rgb_led_board<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">show</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>        <span style="color:#ffffff;">}</span><br>        <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">100</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    <span style="color:#ffffff;">}</span></div>