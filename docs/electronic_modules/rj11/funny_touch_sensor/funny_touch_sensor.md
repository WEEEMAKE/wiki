<div align=center>
<h1 class="text-center">多路触摸传感器</h1>
</div> 

## 1. 简要概述

<p class=MsoTitle align=left style='text-align:left;text-indent:36.0pt'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:0pt;
background:white'>多路触摸传感器<span lang=EN-US>(Funny Touch Sensor)</span>是一个有<span
lang=EN-US>6</span>路可触摸的模块，模块附带<span lang=EN-US>6</span>个鳄鱼夹，当对应的路被触摸时，对应蓝色<span
lang=EN-US>LED</span>灯会亮起<span lang=EN-US>,</span>否则熄灭。使用它可以制作多触摸控的作品，比如水果钢琴等。</span></p>

## 2. 参数规格

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压</td><td>5V DC</td>
</tr>
<tr>
    <td>接口类型</td><td>RJ11</td>
</tr>
<tr>
    <td>通讯方式</td><td>WM单总线</td>
</tr>
<tr>
    <td>触发路数</td><td>6路</td>
</tr>
<tr>
    <td>触发方式</td><td>重复触发</td>
</tr>
<tr>
    <td>工作温度</td><td>-20℃~70℃</td>
</tr>
<tr>
    <td>尺寸大小</td><td>55mm*24mm*20mm(长*宽*高)</td>
</tr>
</table>



## 3. 编程指南

### 3.1. 模块功能及图形化编程指南

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有<span lang=EN-US>WeeeCode</span>、<span lang=EN-US>Mixly_Arduino</span>、<span
lang=EN-US>MakeCode</span>等，其图形化编程大同小异，区别不会很大。</span></p>
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需传参数</th><th>图形化编程块举例</th>
</tr>
<tr>
    <td>判断某路是否被触摸（布尔值）</td><td>	
(2个参数）端口、路数选择</td><td></font><img src="docs/electronic_modules/rj11/funny_touch_sensor/20200306-151745.png"></td>
</tr>
<tr>
    <td>被触时返回特定的值

单独触摸1：1

单独触摸2：2

单独触摸3：4

单独触摸4：8

单独触摸5：16

单独触摸6：32

如果同时触摸多路，返回值为单路值之和，例如：同时触摸1、3、5，返回值就是1+4+16=21

</td><td>(1个参数）端口</td><td></font><img src="docs/electronic_modules/rj11/funny_touch_sensor/20200306-151738.png"></td>

</table>


<p class=MsoNormal align=left style='text-align:left;text-indent:21.0pt'><span
lang=EN-US style='color:white'>&nbsp;</span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体'>&nbsp;</span><span style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>图形化编程示例：</span></p>


###  3.2. 文本代码编程指南 

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>Arduino</span><span style='font-size:
16.0pt;font-family:宋体'>编程示例：</span></p>


<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:4;tab-size:4;"><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">"</span><br> <br>WeFunnyTouchSensor <span style="color:#5fb4b4;">funnytouch</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">PORT_A</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#6699cc;font-style:italic;">uint8_t</span> value <span style="color:#f97b58;">=</span> <span style="color:#f9ae58;">0</span><span style="color:#a6acb9;">;</span> <br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span> <br><span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">begin</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">9600</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span><br>  value <span style="color:#f97b58;">=</span> funnytouch<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readValue</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br> <br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span><span style="color:#ffffff;">(</span>value<span style="color:#f97b58;">&amp;</span><span style="color:#f9ae58;">0x</span><span style="color:#f9ae58;">01</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">></span><span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>     Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">Touch </span><span style="color:#99c794;">1 </span><span style="color:#99c794;">Pressed</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span><span style="color:#ffffff;">(</span>value<span style="color:#f97b58;">&amp;</span><span style="color:#f9ae58;">0x</span><span style="color:#f9ae58;">02</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">></span><span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>     Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">Touch </span><span style="color:#99c794;">2 </span><span style="color:#99c794;">Pressed</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>   <span style="color:#ffffff;">}</span><br>   <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span><span style="color:#ffffff;">(</span>value<span style="color:#f97b58;">&amp;</span><span style="color:#f9ae58;">0x</span><span style="color:#f9ae58;">04</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">></span><span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>     Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">Touch </span><span style="color:#99c794;">3 </span><span style="color:#99c794;">Pressed</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span><span style="color:#ffffff;">(</span>value<span style="color:#f97b58;">&amp;</span><span style="color:#f9ae58;">0x</span><span style="color:#f9ae58;">08</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">></span><span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>     Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">Touch </span><span style="color:#99c794;">4 </span><span style="color:#99c794;">Pressed</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>   <span style="color:#ffffff;">}</span><br>   <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span><span style="color:#ffffff;">(</span>value<span style="color:#f97b58;">&amp;</span><span style="color:#f9ae58;">0x</span><span style="color:#f9ae58;">10</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">></span><span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>     Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">Touch </span><span style="color:#99c794;">5 </span><span style="color:#99c794;">Pre</span><br><span style="color:#99c794;">     </span><span style="color:#99c794;">ssed</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span><span style="color:#ffffff;">(</span>value<span style="color:#f97b58;">&amp;</span><span style="color:#f9ae58;">0x</span><span style="color:#f9ae58;">20</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">></span><span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>     Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">Touch </span><span style="color:#99c794;">6 </span><span style="color:#99c794;">Pressed</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>   <span style="color:#ffffff;">}</span> <br>   <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">100</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span></div>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>更多使用实例请前往论坛学习：多路触摸传感器使用实例（建设中）</span></p>

##  4. 注意事项

