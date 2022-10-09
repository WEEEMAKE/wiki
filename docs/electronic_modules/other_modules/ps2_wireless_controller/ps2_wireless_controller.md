# PS2无线手柄使用手册

## 1 概述

<p class=MsoTitle align=left style='text-align:left'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体;mso-bidi-font-family:Calibri;color:#222222;
background:white'>&nbsp;&nbsp; 2.4G</span><span style='font-size:16.0pt;
font-family:宋体;mso-bidi-font-family:Calibri;color:#222222;background:white'>无线遥控手柄通过<span
class=SpellE><span lang=EN-US>USBhost</span></span>模块和主控板通讯，使用是必须连同<span
class=SpellE><span lang=EN-US>USBhost</span></span>模块一起用。</span></p>
<p class=MsoTitle align=left style='text-align:left'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体;mso-bidi-font-family:Calibri;color:#222222;
background:white'>&nbsp;&nbsp;</span><span style='font-size:16.0pt;
font-family:宋体;mso-bidi-font-family:Calibri;color:#222222;background:white'>手柄外观及按位介绍：<span
class=SpellE><span lang=EN-US></span></span><span
class=SpellE><span lang=EN-US></span></span></span></p>

<div align=center>
<img src="docs\electronic_modules\other_modules\ps2_wireless_controller\20200225-154139.png">
</div>

<div align=center>
<img src="docs\electronic_modules\other_modules\ps2_wireless_controller\20200225-154618.png">
</div>


## 2 参数规格 

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>供电方式</td><td>2节7号电池</td>
</tr>
    <tr>
    <td>手柄外形</td><td>PS2</td>
</tr>
    <tr>
    <td>接收器</td><td>USB</td>
</tr>
    <tr>
    <td>通信频段</td><td>2.4G</td>
</tr>
    <tr>
    <td>电源指示灯</td><td>红色LED</td>
</tr>
    <tr>
    <td>模式指示灯</td><td>绿色LED</td>
</tr>
    <tr>
    <td>传输距离</td><td>10m</td>
</tr>
    <tr>
    <td>摇杆数量</td><td>2个</td>
</tr>
    <tr>
    <td>按键数量</td><td>15个</td>
</tr>
    <tr>
    <td>尺寸大小</td><td>138mm*98mm*60mm（长*宽*高）</td>
</tr>
</table>

## 3 使用指南

### 3.1 手柄使用说明

<p class=MsoTitle align=left style='text-align:left;text-indent:31.0pt;
mso-char-indent-count:2.0'><span lang=EN-US style='font-size:16.0pt;font-family:
宋体;mso-bidi-font-family:Calibri;color:#222222;background:white'>1</span><span
style='font-size:16.0pt;font-family:宋体;mso-bidi-font-family:Calibri;color:#222222;
background:white'>、手柄通电后，上方的红色电源指示灯<span lang=EN-US>(POWER)</span>会常亮，进入休眠或者关闭状态时灭掉。<span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoTitle align=left style='text-align:left;text-indent:31.0pt;
mso-char-indent-count:2.0'><span lang=EN-US style='font-size:16.0pt;font-family:
宋体;mso-bidi-font-family:Calibri;color:#222222;background:white'>2</span><span
style='font-size:16.0pt;font-family:宋体;mso-bidi-font-family:Calibri;color:#222222;
background:white'>、一般情况下，只要<span lang=EN-US>USB</span>接收器通电，手柄会自动连接。<span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoTitle align=left style='text-align:left;text-indent:31.0pt;
mso-char-indent-count:2.0'><span lang=EN-US style='font-size:16.0pt;font-family:
宋体;mso-bidi-font-family:Calibri;color:#222222;background:white'>3</span><span
style='font-size:16.0pt;font-family:宋体;mso-bidi-font-family:Calibri;color:#222222;
background:white'>、配对成功后，按“<span lang=EN-US>MODE</span>”键，选择手柄发送模式，有<span
lang=EN-US>2</span>种模式可以切换，同时对应“<span lang=EN-US>MODE LED</span>”指示灯亮起或熄灭。<b>我们的程序采用其中摇杆输出模拟值的方式，也就是这个<span
style='background:yellow;mso-highlight:yellow'>绿灯常亮的模式</span>，用户注意切换好。</b><span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoTitle align=left style='text-align:left;text-indent:31.0pt;
mso-char-indent-count:2.0'><span lang=EN-US style='font-size:16.0pt;font-family:
宋体;mso-bidi-font-family:Calibri;color:#222222;background:white'>4</span><span
style='font-size:16.0pt;font-family:宋体;mso-bidi-font-family:Calibri;color:#222222;
background:white'>、手柄特性：此手柄具有自动休眠省电模式。在开启无配对状态下，<span lang=EN-US>30s</span>后启动省电模式；开启并配对完成的状态下，<span
lang=EN-US>5</span>分钟无按键按下，启动省电模式。此时只要按下<span lang=EN-US>START</span>就能激活。<span
lang=EN-US><o:p></o:p></span></span></p>


### 3.2 按键编程宏定义

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;mso-yfti-tbllook:1184;mso-padding-alt:0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><b><span
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>宏定义名</span></b><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><b><span
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>值</span></b><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><b><span
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>图形化编程表示</span></b><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><b><span
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>描述</span></b><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_START</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>1</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>START</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键<span
  lang=EN-US>START</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_SELECT</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>2</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>SELECT</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键<span
  lang=EN-US>SELECT</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_MODE</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>3</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>MODE</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键<span
  lang=EN-US>MODE</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_BUTTON_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>4</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>BUTTON_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>左摇杆按键</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeOYSTICK_BUTTON_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>5</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>BUTTON_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>右摇杆按键</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_RIGHT_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>6</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>RIGHT_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>十字按键右键</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_LEFT_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>7</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>LEFT_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>十字按键左键</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_UP_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>8</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>UP_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>十字按键上键</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:9'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_DOWN_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>9</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>DOWN_L</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>十字按键下键</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:10'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_UP_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>10</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>UP_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键<span
  lang=EN-US>Y</span></span><span lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:11'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_RIGHT_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>11</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>RIGHT_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键
  <span lang=EN-US>B</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:12'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_DOWN_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>12</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>DOWN_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键
  <span lang=EN-US>A</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:13'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_LEFT_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>13</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>LEFT_R</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键
  <span lang=EN-US>X</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:14'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_L1</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>14</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>L1</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键
  <span lang=EN-US>L1</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:15'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_R1</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>15</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>R1</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键
  <span lang=EN-US>R1</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:16'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_L2</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>16</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>L2</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键
  <span lang=EN-US>L2</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:17;mso-yfti-lastrow:yes'>
  <td width=271 valign=top style='width:203.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>WeJOYSTICK_R2</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=86 valign=top style='width:64.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>17</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=188 valign=top style='width:140.95pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle align=center style='text-align:center'><span lang=EN-US
  style='font-size:16.0pt;mso-bidi-font-family:Calibri'>R2</span><span
  lang=EN-US style='mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
  </td>
  <td width=258 valign=top style='width:193.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoTitle><span style='font-size:16.0pt;mso-bidi-font-family:Calibri'>按键
  <span lang=EN-US>R2</span></span><span lang=EN-US style='mso-bidi-font-family:
  Calibri'><o:p></o:p></span></p>
  </td>
 </tr>
</table>


### 3.3 功能模块及WeeeCode图形化编程指南



<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:black;background:
white'>该模块支持的图形化编程平台目前有<span lang=EN-US>WeeeCode 3.0</span>，其图形化编程指南如下：</span></p>
<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=257 valign=top style='width:193.1pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>模块功能</span></b></p>
  </td>
  <td width=222 valign=top style='width:166.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>需传参数</span></b></p>
  </td>
  <td width=654 valign=top style='width:490.8pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>图形化编程块举例</span></b></p>
  </td>
 </tr>
 <tr style='height:79.55pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt;height:79.55pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>判断搜选按键是否被按下<span
  lang=EN-US>(</span>布尔值<span lang=EN-US>)</span></span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:79.55pt'>
  <p class=MsoNormal><span lang=EN-US style='font-size:14.0pt;font-family:华文楷体;
  color:black;background:white'>(1</span><span style='font-size:14.0pt;
  font-family:华文楷体;color:black;background:white'>个参数）选择按键</span></p>
  </td>
  <td width=654 valign=top style='width:490.8pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:79.55pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=306 height=378 id="图片 12" src="docs\electronic_modules\other_modules\ps2_wireless_controller\20200225-172647.png"></span></p>
  </td>
 </tr>
 <tr style='height:79.55pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt;height:79.55pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>返回摇杆模拟值（<span
  lang=EN-US>0~255</span>）</span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:79.55pt'>
  <p class=MsoNormal><span lang=EN-US style='font-size:14.0pt;font-family:华文楷体;
  color:black;background:white'>(2</span><span style='font-size:14.0pt;
  font-family:华文楷体;color:black;background:white'>个参数）选择摇杆、选择方向轴</span></p>
  </td>
  <td width=654 valign=top style='width:490.8pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:79.55pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=350 height=126 id="图片 13" src="docs\electronic_modules\other_modules\ps2_wireless_controller\20200225-172654.png"></span></p>
  </td>
 </tr>
</table>
<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;font-family:宋体'>&nbsp;&nbsp;<o:p></o:p></span></p>

<p class=MsoNormal style='text-indent:31.0pt;mso-char-indent-count:2.0'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:-.5pt;
background:white'>图形化编程示例<span lang=EN-US>:<o:p></o:p></span></span></p>

<div align=center>
<img src="docs\electronic_modules\other_modules\ps2_wireless_controller\20200225-175121.png">
</div>

### 3.4 文本代码编程指南

<p class=MsoNormal style='text-indent:31.0pt;mso-char-indent-count:2.0'><span
lang=EN-US style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:
-.5pt;background:white'>Arduino</span><span style='font-size:16.0pt;font-family:
宋体;color:#222222;letter-spacing:-.5pt;background:white'>功能函数说明<span lang=EN-US>:<o:p></o:p></span></span></p>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>函数名<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border:solid windowtext 1.0pt;
  border-left:none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>功能<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>WeUSBHost(uint8_t receivePin,
  uint8_t transmitPin)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>设置软串口的<span lang=EN-US>2</span>个管脚。<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>init(int8_t type)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>初始化模块，此处填<span lang=EN-US>USB2_0<o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>loop(void)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>开始检测<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>ButtonPressed(uint8_t button)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>检测某个按键是否按下<span lang=EN-US>(</span>参数参考按键编程宏定义<span
  lang=EN-US>)<o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>readAnalog(uint8_t button)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>读取模拟值<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>joystickRx(void)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>右摇杆<span lang=EN-US>X</span>方向的值<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>joystickRy(void)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>右摇杆<span lang=EN-US>Y</span>方向的值<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>joystickLx(void)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>左摇杆<span lang=EN-US>X</span>方向的值<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:9;mso-yfti-lastrow:yes'>
  <td width=532 valign=top style='width:399.2pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>joystickLy(void)<o:p></o:p></span></p>
  </td>
  <td width=431 valign=top style='width:323.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-font-kerning:1.0pt'>左摇杆<span lang=EN-US>Y</span>方向的值<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
</table>


<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;font-family:宋体;
color:#222222;letter-spacing:-.5pt;background:white'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='text-indent:31.0pt;mso-char-indent-count:2.0'><span
lang=EN-US style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:
-.5pt;background:white'>Arduino</span><span style='font-size:16.0pt;font-family:
宋体;color:#222222;letter-spacing:-.5pt;background:white'>编程示例<span lang=EN-US>:<o:p></o:p></span></span></p>


<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:2;tab-size:2;"><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">"</span><br><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">SoftwareSerial.h</span><span style="color:#5fb4b4;">"</span><br><br>WeUSBHost <span style="color:#5fb4b4;">PS2</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">A3</span><span style="color:#a6acb9;">,</span> <span style="color:#f9ae58;">A2</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span>  <span style="color:#a6acb9;">//</span><span style="color:#a6acb9;">A3,A2 </span><span style="color:#a6acb9;">for </span><span style="color:#a6acb9;">328P</span><br><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">begin</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">9600</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">init</span><span style="color:#ffffff;">(</span>USB2_0<span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span>  <br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">10</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span><br><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span><br>  PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_START<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">START </span><span style="color:#99c794;">is </span><span style="color:#99c794;">pressed!</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_SELECT<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">SELECT </span><span style="color:#99c794;">is </span><span style="color:#99c794;">pressed!</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_MODE<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">MODE </span><span style="color:#99c794;">is </span><span style="color:#99c794;">pressed!</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_BUTTON_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">BUTTON_L </span><span style="color:#99c794;">is </span><span style="color:#99c794;">pressed!</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_BUTTON_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">BUTTON_R </span><span style="color:#99c794;">is </span><span style="color:#99c794;">pressed!</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_UP_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">L </span><span style="color:#99c794;">UP </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_UP_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_DOWN_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">L </span><span style="color:#99c794;">DOWN </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_DOWN_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_LEFT_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">L </span><span style="color:#99c794;">LEFT </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_LEFT_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_RIGHT_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">L </span><span style="color:#99c794;">RIGHT </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_RIGHT_L<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>   <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_L1<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">L1 </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_L1<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_R1<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">R1 </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_R1<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_L2<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">L2 </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_L2<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_R2<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">R2 </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_R2<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_UP_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">R </span><span style="color:#99c794;">UP </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_UP_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_DOWN_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">R </span><span style="color:#99c794;">DOWN </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_DOWN_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_LEFT_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">R </span><span style="color:#99c794;">LEFT </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_LEFT_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span> <span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">ButtonPressed</span><span style="color:#ffffff;">(</span>WeJOYSTICK_RIGHT_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">R </span><span style="color:#99c794;">RIGHT </span><span style="color:#99c794;">is </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span>WeJOYSTICK_RIGHT_R<span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br><br>  <span style="color:#c695c6;">if</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">joystickRx</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">!=</span><span style="color:#f9ae58;">128</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">PS2_RX </span><span style="color:#99c794;">value </span><span style="color:#99c794;">is: </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">joystickRx</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">joystickRy</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">!=</span><span style="color:#f9ae58;">127</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">PS2_RY </span><span style="color:#99c794;">value </span><span style="color:#99c794;">is: </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">joystickRy</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">joystickLx</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">!=</span><span style="color:#f9ae58;">128</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">PS2_LX </span><span style="color:#99c794;">value </span><span style="color:#99c794;">is: </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">joystickLx</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#c695c6;">if</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">joystickLy</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">!=</span><span style="color:#f9ae58;">127</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">PS2_LY </span><span style="color:#99c794;">value </span><span style="color:#99c794;">is: </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>PS2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">joystickLy</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br><span style="color:#ffffff;">}</span><br></div>

## 4 注意事项

<p class=MsoNormal style='text-indent:31.0pt;mso-char-indent-count:2.0'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:-.5pt;
background:white'>手柄和<span lang=EN-US>USB</span>接收器是配套使用的，手柄只连接出厂配套的<span
lang=EN-US>USB</span>接收器，不能连接其它手柄的<span lang=EN-US>USB</span>接收器，所以不要弄丢接收器。<span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal style='text-indent:31.0pt;mso-char-indent-count:2.0'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:-.5pt;
background:white'>如果多个手柄同时使用时，可能会出现信号干扰，造成手柄连接中断的情况，此时尽量和其它手柄接、收器拉开距离，使干扰降低。<span
lang=EN-US><o:p></o:p></span></span></p>
