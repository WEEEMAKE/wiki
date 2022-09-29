<div align=center>
<h1 class="text-center">9g舵机</h1>
</div>

## 1. 舵机概述

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;line-height:105%;font-family:宋体'>9</span><span
style='font-size:16.0pt;line-height:105%;font-family:宋体'>克舵机是一种简单的，常用的标准伺服电机，可使用在机器人头部，机械手，云台等，用于小型轻型场景。</span></p>
</body></html>

## 2. 电机参数

<html><body>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压范围</td><td>DC 3.8~6.0V</td>
</tr>
    <tr>
    <td>工作电流</td><td>80mA~100mA</td>
</tr>
    <tr>
    <td>待机电流</td><td>5mA</td>
</tr>
    <tr>
    <td>极限角度</td><td>210°±5%</td>
</tr>
    <tr>
    <td>工作扭矩</td><td>1.3到1.7kg/cm</td>
</tr>
    <tr>
    <td>信号周期</td><td>20ms</td>
</tr>
    <tr>
    <td>信号高电平时间范围</td><td>1000到2000 us/周期</td>
</tr>
</table>




</div>
</body></html>



## 3. 编程指南

### 3.1. 模块功能及图形化编程指南

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
line-height:105%;font-family:等线;color:#666666;background:white'>该电机支持的图形化编程平台有</span><span
lang=EN-US style='font-size:16.0pt;line-height:105%;font-family:"Helvetica",sans-serif;
color:#666666;background:white'><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>WeeeCode</span></span><span style='font-size:16.0pt;line-height:105%;
font-family:等线;color:#666666;background:white'><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>、编程猫平台、</span></span><span
lang=EN-US style='font-size:16.0pt;line-height:105%;font-family:"Helvetica",sans-serif;
color:#666666;background:white'><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>Mixly_Arduino</span></span><span style='font-size:16.0pt;line-height:105%;
font-family:等线;color:#666666;background:white'><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>、</span></span><span
lang=EN-US style='font-size:16.0pt;line-height:105%;font-family:"Helvetica",sans-serif;
color:#666666;background:white'><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>MakeCode</span></span><span style='font-size:16.0pt;line-height:105%;
font-family:等线;color:#666666;background:white'><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>等，其图形化编程大同小异，区别不会很大。</span></span></p>
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需传参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>驱动舵机运作</td><td>（2个参数）所接端口、角度(0~180)</td><td>  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US><img width=310
  height=70 id="图片 1" src="docs\electronic_modules\motor\9g_sovor\20200310-185655.png"></span></p></td>
</tr>
</table>

</div>

<p class=MsoNormal style='text-indent:36.0pt'><span lang=EN-US
style='font-size:5.0pt;line-height:105%;font-family:等线;color:#666666;
background:yellow'>&nbsp;</span></p>

<p class=MsoNormal style='text-indent:36.0pt'><span style='font-size:16.0pt;
line-height:105%;font-family:等线;color:#666666;background:white'>图形化编程示例：</span></span></p>
</body></html>

  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US><img width=328
  height=340 id="图片 1" src="docs\electronic_modules\motor\9g_sovor\20200310-185643.png"></span></p>

### 3.2. 文本代码编程指南

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:等线'>Arduino编程示例：</span></p>
</body></html>

<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:4;tab-size:4;"><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">"</span><br><br>Servo weservo<span style="color:#a6acb9;">;</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span> <br><span style="color:#ffffff;">{</span><br>    weservo<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">attach</span><span style="color:#ffffff;">(</span>PORT_1<span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span><br>  weservo<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">write</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">0</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span>                  <span style="color:#a6acb9;">//</span><span style="color:#a6acb9;"> </span><span style="color:#a6acb9;">sets </span><span style="color:#a6acb9;">the </span><span style="color:#a6acb9;">servo </span><span style="color:#a6acb9;">position </span><span style="color:#a6acb9;">according </span><span style="color:#a6acb9;">to </span><span style="color:#a6acb9;">the </span><span style="color:#a6acb9;">scaled </span><span style="color:#a6acb9;">value </span><span style="color:#a6acb9;">0-180</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">2000</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span>                           <span style="color:#a6acb9;">//</span><span style="color:#a6acb9;"> </span><span style="color:#a6acb9;">waits </span><span style="color:#a6acb9;">for </span><span style="color:#a6acb9;">the </span><span style="color:#a6acb9;">servo </span><span style="color:#a6acb9;">to </span><span style="color:#a6acb9;">get </span><span style="color:#a6acb9;">there </span><br>  weservo<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">write</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">180</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">2000</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span> <br><span style="color:#ffffff;">}</span></div>

</sxh>

## 4. 注意事项

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;line-height:105%;font-family:宋体;color:#222222;
background:white'>1</span><span style='font-size:16.0pt;line-height:105%;
font-family:宋体;color:#222222;background:white'>、不能长时间快速正反转，这样会造成电流过大，发热量大，烧毁舵机。</span><span
lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;line-height:105%;font-family:宋体;color:#222222;
background:white'>2</span><span style='font-size:16.0pt;line-height:105%;
font-family:宋体;color:#222222;background:white'>、不能长时间堵转，这样会造成电流过大，发热量大，烧毁舵机。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;line-height:105%;font-family:宋体;color:#222222;
background:white'>3</span><span style='font-size:16.0pt;line-height:105%;
font-family:宋体;color:#222222;background:white'>、电源正负极不能接错。</span></p>
</body></html>