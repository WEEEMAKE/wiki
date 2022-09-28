<div align=center>
<h1 class="text-center">手势识别传感器</h1>
</div>

<p class=MsoNormal align=center style='text-align:center'><img width=496
  height=196 id="图片 7" src="docs\electronic_modules\rj11\gesture_sensor\20190807-104621.png"></p>

## 1. 模块介绍

<p class=MsoTitle align=left style='text-align:left'><span style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>&nbsp; <span lang=ZH-CN>本模块是一款在给定参考方向后，能检测手势向前移动、向后移动、向左移动、向右移动、向下移动等</span>5<span
lang=ZH-CN>种手势运动状态的模块，解放你的双手。</span></span></p>

## 2. 参数规则

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压</td><td>DC 5V</td>
</tr>
<tr>
    <td>接口类型</td><td>RJ11</td>
</tr>
<tr>
    <td>通讯方式</td><td>WM单总线</td>
</tr>
<tr>
    <td>手势识别种类</td><td>前、后、左、右、下，共5种手势</td>
</tr>
<tr>
    <td>状态指示灯</td><td>5个状态指示灯</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>


## 3. 使用指南

### 3.1. 模块使用说明

<p class=MsoNormal><span style='font-size:16.0pt;font-family:宋体;color:black;
background:white'>&nbsp;&nbsp; <span lang=ZH-CN>该模块使用时，手离传感器距离在</span><b><span
style='background:yellow'>5~20cm</span></b><span lang=ZH-CN>之间，太近容易误判。</span></span></p>

### 3.2. 功能模块及WeeeCode图形化编程指南

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需传参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>判断手势是否与所一致选(布尔值)</td><td>(2个参数）端口、选择手势方向</td><td>  <p class=MsoNormal align=center style='text-align:center'><img width=496
  height=196 id="图片 7" src="docs\electronic_modules\rj11\gesture_sensor\20190807-105359.png"></p></td>
</tr>
</table>

### 3.3. 文本代码编程指南 

## 4. 注意事项 

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp;(1)<span
lang=ZH-CN>本模块属于光学器件，保存时需要注意防尘防潮。使用时，需保持传感器表面的清洁度，以免导致测量不准。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp;(2)<span
lang=ZH-CN>手势移动不能太快，也不能太慢。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp;(3)<span
lang=ZH-CN>由于传感器是红外光学器件，不宜在阳光强，或者环境中红外光强的环境中使用。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp;(4)<span
lang=ZH-CN>当周围环境光发生明显变化时，或者识别错误率较高时，建议给模块断电后重新上电。</span></span></p>
