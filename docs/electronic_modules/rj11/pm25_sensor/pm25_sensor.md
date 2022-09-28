<div align=center>
<h1 class="text-center">PM2.5传感器 </h1>
</div>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=198 height=206 id="图片 1" src="docs\electronic_modules\rj11\pm25_sensor\20190803-154125.png">

## 1. 简要概述 

<p class=MsoTitle align=left style='text-align:left;text-indent:36.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:
0pt;background:white'>PM2.5</span><span style='font-size:16.0pt;font-family:
宋体;color:#222222;letter-spacing:0pt;background:white'>传感器（<span lang=EN-US>PM2.5
Sensor</span>）是基于益杉科技型号为<span lang=EN-US>CP-15-A4-CG</span>的<span lang=EN-US>PM2.5</span>传感器，该传感器采用激光陷阱散射原理，通过激光能量陷阱束缚空气中不同粒径的悬浮颗粒物。该传感器经经过益杉科技独有的数据双频采集专利技术进行筛分，得出颗粒物的等效粒径及不同粒径的颗粒物数量，最终通过算法计算出颗粒物质量浓度。除此之外，传感器的激光、风扇，均可控制开和关。</span><span
lang=EN-US>&nbsp;</span></p>

##  2. 参数规格 

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
    <td>传感器商标</td><td>益杉科技</td>
</tr>
<tr>
    <td>传感器型号</td><td>CP-15-A4-CG</td>
</tr>
<tr>
    <td>传感器材料</td><td>ABS</td>
</tr>
<tr>
    <td>传感器材料晶体结构</td><td>激光</td>
</tr>
<tr>
    <td>传感器尺寸</td><td>45.2*35.6*23.1mm</td>
</tr>
<tr>
    <td>测量范围</td><td>0.3-10μm</td>
</tr>
<tr>
    <td>量程</td><td>0-6000μg/m³</td>
</tr>
<tr>
    <td>相对一致性</td><td>±10μg/m3或±10%读数</td>
</tr>
<tr>
    <td>工作温度</td><td>-10~50℃</td>
</tr>
<tr>
    <td>工作湿度</td><td>5-80%RH</td>
</tr>
</table>



## 3. 编程指南 

### 3.1. 模块功能及图形化编程指南

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有<span lang=EN-US>WeeeCode</span>、<span lang=EN-US>Mixly_Arduino</span>等，其图形化编程大同小异，区别不会很大。</span></p>
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需传参数</th><th>图形化编程块举例</th>
</tr>
<tr>
    <td>返回传感器的检测值</td><td>(2个参数）端口、颗粒物直径选择</td><td><p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=572 height=146 id="图片 1" src="docs\electronic_modules\rj11\pm25_sensor\20200304-141741.png"></span></p></td>
</tr>
</table>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>图形化编程示例：</span></p>
<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=799 height=336 id="图片 1" src="docs\electronic_modules\rj11\pm25_sensor\20200304-142736.png">

### 3.2. 文本代码编程指南 

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>Arduino</span><span style='font-size:
16.0pt;font-family:宋体'>编程函数：</span></p>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>函数名</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>功能</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>WePM25Sensor (uint8_t port)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>设置端口</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>setFanLaser(bool isOn)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>设置<span lang=EN-US>PM2.5</span>模块上面的风扇和激光头开关</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>readPm1_0Concentration(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PM1.0 ug/m^3</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>readPm2_5Concentration(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PM2.5 ug/m^3</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>readPm10Concentration(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PM10 ug/m^3</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>read0_3NumIn100ml(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>0.1L</span><span style='font-size:14.0pt'>空气中直径在<span
  lang=EN-US>0.3um</span>的颗粒物个数</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>read0_5NumIn100ml(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>0.1L</span><span style='font-size:14.0pt'>空气中直径在<span
  lang=EN-US>0.5um</span>的颗粒物个数</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>read1_0NumIn100ml(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>0.1L</span><span style='font-size:14.0pt'>空气中直径在<span
  lang=EN-US>1.0um</span>的颗粒物个数</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>read2_5NumIn100ml(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>0.1L</span><span style='font-size:14.0pt'>空气中直径在<span
  lang=EN-US>2.5um</span>的颗粒物个数</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>read5_0NumIn100ml(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>0.1L</span><span style='font-size:14.0pt'>空气中直径在<span
  lang=EN-US>5.0um</span>的颗粒物个数</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>read10NumIn100ml(void)</span></p>
  </td>
  <td width=394 valign=top style='width:295.45pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>0.1L</span><span style='font-size:14.0pt'>空气中直径在<span
  lang=EN-US>10um</span>的颗粒物个数</span></p>
  </td>
 </tr>
</table>
<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>&nbsp;</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>Arduino</span><span style='font-size:
16.0pt;font-family:宋体'>编程示例：</span></p>


<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:4;tab-size:4;"><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">"</span><br> <br>WePM25Sensor <span style="color:#5fb4b4;">pm25Sensor</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">PORT_D</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br> <br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span>  <br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">begin</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">115200</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">2000</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  pm25Sensor<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">setFanLaser</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">1</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">100</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span> <br><span style="color:#ffffff;">{</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">SensorData </span><span style="color:#99c794;">: </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span>pm25Sensor<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readPm2_5Concentration</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;"> </span><span style="color:#99c794;">ug</span><span style="color:#99c794;">/</span><span style="color:#99c794;">m^3</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">200</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span></div>



<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>更多使用实例请前往论坛学习：PM2.5传感器使用实例（建设中）</span></p>


