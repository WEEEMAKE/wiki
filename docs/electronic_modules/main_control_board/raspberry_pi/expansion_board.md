# 树莓派扩展板说明

## 1、简介

<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt'>ELF</span><span style='font-size:16.0pt'>树莓派扩展板是一款基于<span
lang=EN-US>arduino</span>平台的主控型扩展板，采用<span lang=EN-US>MEGA328P</span>芯片，通过串口和树莓派通讯，同时也可以和电脑通讯，从而实现多种应用场景。该扩展板性能强劲，可扩展性强，带有很强的<span
lang=EN-US>DIY</span>属性，既可以接<span lang=EN-US>weeemake</span>平台所有电子模块，又可通过扩展接市场上大部分开源电子模块，极大的扩展了树莓派的应用。扩展板提供了强大的供电能力，可直接给任意型号的树莓派供电，能应用于各种人工智能比赛、教学、<span
lang=EN-US>DIY</span>智能搭建等项目。</span></p>
</body></html>

## 2、扩展板外观

<div align=center>
<img src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-184231.png">
</div>

## 3、硬件参数



<html><body>



<div align=center>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0 width=812
 style='width:609.15pt;border-collapse:collapse;border:none'>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:15.0pt'>名称</span></b></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:15.0pt'>描述</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>按键模块</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>板载按键<span lang=EN-US>1</span>个</span></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>扩展板复位开关</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>1</span><span style='font-size:14.0pt'>个</span></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>RJ11</span><span style='font-size:14.0pt'>接口</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>4</span><span style='font-size:14.0pt'>个（<span
  lang=EN-US>A</span>、<span lang=EN-US>B</span>、<span lang=EN-US>C</span>、<span
  lang=EN-US>D</span>）</span></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>传感器或电机驱动接口</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>4</span><span style='font-size:14.0pt'>个插针接口（<span
  lang=EN-US>1</span>、<span lang=EN-US>2</span>、<span lang=EN-US>3</span>、<span
  lang=EN-US>4</span>）可接插针传感器或电机驱动模块</span></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>电机接口</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>8</span><span style='font-size:14.0pt'>个直流电机接口（<span
  lang=EN-US>M1-M8</span>）</span></p>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>或<span lang=EN-US>4</span>个编码电机接口（<span lang=EN-US>1-4</span>）</span></p>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>或<span lang=EN-US>4</span>个步进电机接口（<span lang=EN-US>1-4</span>）</span></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>通讯接口</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>1</span><span style='font-size:14.0pt'>个<span
  lang=EN-US>usb</span>电脑接口、<span lang=EN-US>1</span>个树莓派串口接口</span></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>IO</span><span style='font-size:14.0pt'>扩展接口</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>可接<span lang=EN-US>IO</span>扩展模块</span></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>电源系统</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>输入电压：<span lang=EN-US>DC6-12V</span></span></p>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>工作电压：<span lang=EN-US>DC5V</span></span></p>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>5V</span><span style='font-size:14.0pt'>输出电流：<span
  lang=EN-US>6A</span>（<span lang=EN-US>MAX</span>）</span></p>
  </td>
 </tr>
 <tr>
  <td width=245 valign=center style='width:183.9pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>尺寸</span></p>
  </td>
  <td width=567 valign=center style='width:15.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>86*56*32</span><span style='font-size:14.0pt'>（长<span
  lang=EN-US>*</span>宽<span lang=EN-US>*</span>高）</span></p>
  </td>
 </tr>
</table>

</div>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-size:16.0pt'>注意：由于扩展板输出功率较大，外接电源放电电流应在<span
lang=EN-US>3A</span>以上。</span></p>
</body></html>

## 4、IO分配

<html><body>
<div align=center>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width=812
 style='width:609.15pt;border-collapse:collapse'>
 <tr>
  <td width=179 style='width:134.3pt;border:solid windowtext 1.0pt;padding:
  0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:15.0pt'>模块</span></b></p>
  </td>
  <td width=293 style='width:219.7pt;border:solid windowtext 1.0pt;border-left:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:15.0pt'>接口</span></b></p>
  </td>
  <td width=340 style='width:9.0cm;border:solid windowtext 1.0pt;border-left:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=EN-US style='font-size:15.0pt'>IO</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=179 style='width:134.3pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>按键模块</span></p>
  </td>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>Button</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>A7</span></p>
  </td>
 </tr>
 <tr>
  <td width=179 rowspan=4 style='width:134.3pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>RJ11</span><span style='font-size:14.0pt'>接口</span></p>
  </td>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PORT_A</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>D4</span></p>
  </td>
 </tr>
 <tr>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PORT_B</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>D5</span></p>
  </td>
 </tr>
 <tr>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PORT_C</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  border-center:none'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>D6</span></p>
  </td>
 </tr>
 <tr>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;border-center:none'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PORT_D</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  border-center:none'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>D9</span></p>
  </td>
 </tr>
 <tr>
  <td width=179 rowspan=4 style='width:134.3pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>传感器或电机接口</span></p>
  </td>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PORT_1</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>A0</span></p>
  </td>
 </tr>
 <tr>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PORT_2</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>A1</span></p>
  </td>
 </tr>
 <tr>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PORT_3</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>D2</span></p>
  </td>
 </tr>
 <tr>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>PORT_4</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>D3</span></p>
  </td>
 </tr>
 <tr>
  <td width=179 style='width:134.3pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>串口通讯</span></p>
  </td>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>GPIO15(RX)</span><span style='font-size:14.0pt'>、<span
  lang=EN-US>GPIO14(TX)(</span>树莓派<span lang=EN-US>)</span></span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>D7</span><span style='font-size:14.0pt'>、<span
  lang=EN-US>D8(arduino)</span></span></p>
  </td>
 </tr>
 <tr>
  <td width=179 style='width:134.3pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>IO</span><span style='font-size:14.0pt'>扩展接口（<span
  lang=EN-US>arduino</span>）</span></p>
  </td>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>8Pin+2*5Pin</span><span style='font-size:14.0pt'>排针孔</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>D0</span><span style='font-size:14.0pt'>、<span
  lang=EN-US>D1</span>、<span lang=EN-US>D4</span>、<span lang=EN-US>D5</span>、<span
  lang=EN-US>D6</span>、<span lang=EN-US>D9</span>、<span lang=EN-US>D10</span>、<span
  lang=EN-US>D11</span>、<span lang=EN-US>D12</span>、<span lang=EN-US>D13</span>、<span
  lang=EN-US>A2</span>、<span lang=EN-US>A3</span>、<span lang=EN-US>A4</span>、<span
  lang=EN-US>A5</span>、<span lang=EN-US>RST</span>、<span lang=EN-US>DTR</span>、<span
  lang=EN-US>5V</span>、<span lang=EN-US>GND</span></span></p>
  </td>
 </tr>
 <tr>
  <td width=179 style='width:134.3pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt'>树莓派扩展接口（树莓派）</span></p>
  </td>
  <td width=293 style='width:219.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>5Pin</span><span style='font-size:14.0pt'>排针孔</span></p>
  </td>
  <td width=340 style='width:9.0cm;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt'>GPIO2(SDA1)</span><span style='font-size:14.0pt'>、<span
  lang=EN-US>GPIO3(SCL1)</span>、<span lang=EN-US>GPIO4</span>、<span lang=EN-US>3.3V</span>、<span
  lang=EN-US>GND</span></span></p>
  </td>
 </tr>
</table>

</div>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;color:white'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-size:16.0pt'>注意：<span lang=EN-US>RJ11</span>接口和电机接口与<span
lang=EN-US>IO</span>扩展接口有些重复，不能同时使用。光线<span lang=EN-US>/</span>声音等需要测量模拟量的插针传感器模块，只能接口<span
lang=EN-US>port1</span>和<span lang=EN-US>port2</span>口。</span></p>
</body></html>

## 5、编程块介绍

<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt'>树莓派相关人工智能指令块如下：</span></p>
<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US><img width=283 height=62
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-190847.png"></span><span
style='font-size:16.0pt'>输入树莓派需要连接的路由器账号密码。只要输入一次，树莓派会自动记录，下次开机自动连接此账号，如需更改时再次调入即可。</span></p>


<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US><img width=150 height=40
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191004.png"></span><span
style='font-size:16.0pt'>运行此语句块时，树莓派会自动录音<span lang=EN-US>10</span>秒。没有检测到说话返回<span
lang=EN-US>0</span></span></p>


<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=181
height=46
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191100.png"></span><span
style='font-size:16.0pt'>空白处输入汉字或英文，点击该语句块，树莓派会通过喇叭读出来。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=188
height=48
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191142.png"></span><span
style='font-size:16.0pt'>点击该语句块后，树莓派会自动录音<span lang=EN-US>10</span>秒，然后识别你的语句做出回答。点击一次识别一次。注意此语句需要预先设置百度账号才能工作。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=240
height=35
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191224.png"></span><span
style='font-size:16.0pt'>第一个空白处填入百度云的<span lang=EN-US>apikey</span>，第二个空白填入百度云的<span
lang=EN-US>secretkey</span>。只要输入一次，树莓派会自动记录，如需更改时再次调入即可。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=302
height=38
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191308.png"></span><span
style='font-size:16.0pt'>自动识别文本中的汉字、数字、英文和标点符号。树莓派会启动摄像头，自动拍摄。注意此语句需要预先设置百度账号才能工作。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=293
height=36
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191335.png"></span><span
style='font-size:16.0pt'>自动识别图片中动物。树莓派会启动摄像头，自动拍摄，注意此语句需要预先设置百度账号才能工作。按可信度从高到低返回所有结果。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=289
height=36
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191358.png"></span><span
style='font-size:16.0pt'>自动识别图片中的植物。树莓派会启动摄像头，自动拍摄。注意此语句需要预先设置百度账号才能工作。按可信度从高到低返回所有结果。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=297
height=39
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191420.png"></span><span
style='font-size:16.0pt'>自动识别图片中的通用物体。树莓派会启动摄像头，自动拍摄。注意此语句需要预先设置百度账号才能工作。按可信度从高到低返回所有结果。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=298
height=36
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191439.png"></span><span
style='font-size:16.0pt'>人脸识别训练，数字为编号。在人脸识别前，先录入要识别人脸的信息。运行此语句后树莓派会启动摄像头，自动拍摄一幅图像，然后把人脸模型存储起来。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=301
height=34
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191504.png"></span><span
style='font-size:16.0pt'>人脸对比判别。运行此语句后树莓派会启动摄像头，自动拍摄一幅图像，然后和之前存储的人脸模块对比，一致性较高则返回<span
lang=EN-US>ture</span>，失败则返回<span lang=EN-US>false</span>。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=131
height=37
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191523.png"></span><span
style='font-size:16.0pt'>此语句返回人工识别后的结果，无论时语音还是图像，都可以调用此语句，但不包括人脸识别。</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt'><img width=220
height=35
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191559.png"></span><span
style='font-size:16.0pt'>将树莓派人工智能识别后的结果和空白处的文字做对比，如果包含空白处的文字则返回<span
lang=EN-US>true</span>，否则返回<span lang=EN-US>false</span>。</span></p>

</body></html>



## 6、编程语句块基本应用

<html><body>
<p class=MsoNormal><span style='font-size:16.0pt'>树莓派扩展板下载在线调试固件后，就可以即时体验语句块了。（体验之前需要连接<span
lang=EN-US>WiFi</span>，<span lang=EN-US>WiFi</span>连接部分请看树莓派<span lang=EN-US>AI</span>套件语音识别说明）</span></p>

<p class=MsoNormal><span style='font-size:16.0pt'>例如文字转语音，找到“树莓派文本转语音”语句块，如下所示，把需要转换的汉字填入空白处，比如：你好。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
width=308 height=100 src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-191911.png"></span></p>

<p class=MsoNormal><span style='font-size:16.0pt'>然后鼠标点击积木块，此时，积木块周围变成黄色，过一会，喇叭会播放转换后的语音。积木块执行完成，周围的黄色消失。</span></p>

<p class=MsoNormal><span style='font-size:16.0pt'>例如语音转文字，在软件中找到“树莓派识别语音”和“树莓派识别结果”语句块。点击“树莓派识别语音”语句块，然后对麦克风说话。</span></p>

<p class=MsoNormal><span style='font-size:16.0pt'>结束说话一段时间，语句块下面会反馈结果，<span
lang=EN-US>ture</span>代表识别成功，<span lang=EN-US>false</span>代表不成功。如下图中所示。识别成功后点击“树莓派识别结果”，结果就会显示在下面了。比如说“你好”。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
width=181 height=101 src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-192002.png"><img width=79 height=44
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-192024.png"><img width=159 height=102
src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-192036.png"></span></p>

<p class=MsoNormal><span style='font-size:16.0pt'>例如物体识别，包括通用物体识别、动物识别、植物识别、文字识别。点击对应的积木块前，将摄像头对准要识别的物体，点击后，树莓派会启动摄像头拍摄一幅照片，然后传到云端。识别到物体时，该积木块会提示<span
lang=EN-US>ture</span>。否则提示<span lang=EN-US>false</span>。</span></p>

<p class=MsoNormal><span style='font-size:16.0pt'>结果仍然是点击“树莓派识别结果”积木块，下面就会显示识别到的几种结果。比如拍一个圆珠笔的照片，可能会反馈如下结果。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
width=340 height=144 src="docs\electronic_modules\main_control_board\raspberry_pi\20201030-192129.png"></span></p>
</body></html>

## 7、供电方式和模块连接方式


<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt'>可以给扩展板提供<span
lang=EN-US>6-12V</span>的直流电源，放电电流最好大于<span lang=EN-US>3A</span>，否则可能会造成树莓派供电不足而死机。</span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt'>套件中的喇叭接入树莓派耳机接口，开机后半分钟会自动播报分配的<span
lang=EN-US>IP</span>地址（预先输入过<span lang=EN-US>wifi</span>账号密码）。</span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt'>摄像头和麦克风接入树莓派上任何一个<span
lang=EN-US>usb</span>口，树莓派会自动识别。最好摄像头接<span lang=EN-US>usb2.0</span>上面那个接口，麦克风接<span
lang=EN-US>usb3.0</span>下面那个接口。</span></p>
</body></html>