# 步进电机驱动模块

##  1. 简要概述 

<html><body>

<p class=MsoNormal style='text-indent:32.0pt;mso-char-indent-count:2.0'><span
style='font-size:16.0pt'>步进电机驱动（<span lang=EN-US>Stepper Motor Driver</span>）模块是用来驱动双极步进电机的。原理上一个脉冲信号，步进电机就转动一定的固定角度（不考虑细分）。所以此模块配合步进电机可以用于一些需要精确控制运动的地方。模块内置<span
lang=EN-US>MCU</span>，可以通过软件设置细分数，也可以通过单总线来控制电机，不需要主控实时控制。<span lang=EN-US><o:p></o:p></span></span></p>
</body></html>

##  2. 参数规格 

<html><body>

<div align=center>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;mso-yfti-tbllook:1184;mso-padding-alt:0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
  <td width=259 valign=top style='width:194.3pt;border-top:solid #5B9BD5 3.0pt;
  border-left:solid #5B9BD5 3.0pt;border-bottom:solid white 2.25pt;border-right:
  none;background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>参数</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:solid #5B9BD5 3.0pt;
  border-left:none;border-bottom:solid white 2.25pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>值<span lang=EN-US>/</span>描述</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1'>
  <td width=259 valign=top style='width:194.3pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>MCU</span><span
  style='font-size:18.0pt;font-family:宋体;color:white'>工作电压</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>DC 5V</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2'>
  <td width=259 valign=top style='width:194.3pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>接口类型</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>插针与<span lang=EN-US>ELF</span>主控板适配使用</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3'>
  <td width=259 valign=top style='width:194.3pt;border:solid white 1.0pt;
  border-left:solid #5B9BD5 3.0pt;background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>通信方式</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:solid white 1.0pt;
  border-left:none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>WM</span><span
  style='font-size:18.0pt;font-family:宋体;color:white'>单总线</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4'>
  <td width=259 valign=top style='width:194.3pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>驱动芯片</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>DRV8825</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5'>
  <td width=259 valign=top style='width:194.3pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>驱动电压<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>DC 8.2V~12V<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6'>
  <td width=259 valign=top style='width:194.3pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>驱动电流</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>1.75A</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7'>
  <td width=259 valign=top style='width:194.3pt;border:solid white 1.0pt;
  border-left:solid #5B9BD5 3.0pt;background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>峰值电流</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:solid white 1.0pt;
  border-left:none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>2.5A</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8'>
  <td width=259 valign=top style='width:194.3pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  mso-border-top-alt:solid white 1.0pt;background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>最高细分<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  mso-border-top-alt:solid white 1.0pt;background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>32</span><span
  style='font-size:18.0pt;font-family:宋体;color:white'>细分<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:9'>
  <td width=259 valign=top style='width:194.3pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  mso-border-top-alt:solid white 1.0pt;background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>驱动电机<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  mso-border-top-alt:solid white 1.0pt;background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>双极<span lang=EN-US>4</span>线步进电机<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:10;mso-yfti-lastrow:yes'>
  <td width=259 valign=top style='width:194.3pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid #5B9BD5 3.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>尺寸大小</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid #5B9BD5 3.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>--mm*--mm*--mm(</span><span
  style='font-size:18.0pt;font-family:宋体;color:white'>长<span lang=EN-US>*</span>宽<span
  lang=EN-US>*</span>高<span lang=EN-US>)</span></span></p>
  </td>
 </tr>
</table>
</div>
</body></html>

##  3. 功能特性 

<html><body>

<p class=MsoListParagraph style='margin-left:42.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt'>内置<span class=SpellE><span lang=EN-US>mcu</span></span>，只需要<span
lang=EN-US>1</span>个端口就可以控制步进电机<span lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoListParagraph style='margin-left:42.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt'>内置可调电位器可调节电机电流输出，改变步进电机扭矩<span lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoListParagraph style='margin-left:42.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt'>支持软件设置全、<span lang=EN-US>1/2</span>、<span lang=EN-US>1/4</span>、<span
lang=EN-US>1/8</span>、<span lang=EN-US>1/16</span>、<span lang=EN-US>1/32</span>细分<span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoListParagraph style='margin-left:42.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt'>芯片具有过流过热保护<span lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoListParagraph style='margin-left:42.0pt;text-indent:-21.0pt;
mso-list:l0 level1 lfo1'><![if !supportLists]><span lang=EN-US
style='font-size:14.0pt;font-family:Wingdings;mso-fareast-font-family:Wingdings;
mso-bidi-font-family:Wingdings'><span style='mso-list:Ignore'>l<span
style='font:7.0pt "Times New Roman"'>&nbsp; </span></span></span><![endif]><span
style='font-size:14.0pt'>采用<span class=GramE>排针排母</span>组合方式，防止反接<span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoListParagraph style='margin-left:42.0pt;text-indent:-21.0pt;
mso-list:l0 level1 lfo1'><![if !supportLists]><span lang=EN-US
style='font-size:14.0pt;font-family:Wingdings;mso-fareast-font-family:Wingdings;
mso-bidi-font-family:Wingdings'><span style='mso-list:Ignore'>l<span
style='font:7.0pt "Times New Roman"'>&nbsp; </span></span></span><![endif]><span
style='font-size:14.0pt'>模块体积小巧，接插方便<span lang=EN-US><o:p></o:p></span></span></p>
</body></html>

##  4. 连接方式 

<html><body>

<p class=MsoNormal align=left style='text-align:left;text-indent:32.0pt;
mso-char-indent-count:2.0'><span style='font-size:16.0pt'>本模块目前只能用于<span
lang=EN-US>ELF</span>主控板上，可以接插在<span lang=EN-US>ELF</span>主控板上的<span
lang=EN-US>port3-port6</span>共<span lang=EN-US>4</span>个口上。<span lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><span
style='mso-no-proof:yes'><img width=393 height=168 id="_x0000_i1029"
src="https://www.weeemake.com.cn/wiki/lib/exe/fetch.php?media=wm_wiki:compass_sensor:pasted:20190511-16132.png"></span></span></p>

<p class=MsoNormal align=left style='text-align:left;text-indent:32.0pt;
mso-char-indent-count:2.0'><span style='font-size:16.0pt'>步进电机接插在<span
lang=EN-US>ELF</span>主控板的橘红色端子上，一个步进电机驱动接一个步进电机。<span lang=EN-US><o:p></o:p></span></span></p>
</body></html>

##  5. 编程指南 

###  5.1. 模块功能及图形化编程指南 

<html><body>

</body></html>

###  5.2. 文本代码编程指南 

<html><body>

<p class=MsoTitle style='text-indent:31.0pt'><span lang=EN-US style='font-size:
16.0pt;font-family:等线'>Arduino</span><span style='font-size:16.0pt;font-family:
等线'>编程函数：</span></p>

<div align=center>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>函数名<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-left:none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>功能<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span class=SpellE><span
  class=GramE><span lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:
  等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:
  minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;
  mso-font-kerning:1.0pt'>WeStepperMotor</span></span></span><span class=GramE><span
  lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:
  minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;
  mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:
  1.0pt'>(</span></span><span lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:
  等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:
  minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;
  mso-font-kerning:1.0pt'>uint8_t port)<o:p></o:p></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>设置端口<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span class=SpellE><span
  class=GramE><span lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:
  等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:
  minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;
  mso-font-kerning:1.0pt'>setMicroStep</span></span></span><span class=GramE><span
  lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:
  minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;
  mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:
  1.0pt'>(</span></span><span lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:
  等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:
  minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;
  mso-font-kerning:1.0pt'>uint8_t value)<o:p></o:p></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>设置细分数<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span class=SpellE><span
  class=GramE><span lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:
  等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:
  minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;
  mso-font-kerning:1.0pt'>setSpeed</span></span></span><span class=GramE><span
  lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:
  minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;
  mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:
  1.0pt'>(</span></span><span lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:
  等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:
  minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;
  mso-font-kerning:1.0pt'>uint8_t speed)<o:p></o:p></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>设置电机加速度（<span
  lang=EN-US>0-254</span>）<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span class=SpellE><span
  class=GramE><span lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:
  等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:
  minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;
  mso-font-kerning:1.0pt'>moveTo</span></span></span><span class=GramE><span
  lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:
  minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;
  mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:
  1.0pt'>(</span></span><span lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:
  等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:
  minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;
  mso-font-kerning:1.0pt'>long value)<o:p></o:p></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>移动到多少步<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span class=GramE><span
  lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:
  minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;
  mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:
  1.0pt'>move(</span></span><span lang=EN-US style='font-size:14.0pt;
  mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
  等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-latin;mso-font-kerning:1.0pt'>long value)<o:p></o:p></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>移动多少步<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span class=SpellE><span
  lang=EN-US style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:
  minor-latin;mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;
  mso-hansi-font-family:等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:
  1.0pt'>setPositionOrigin</span></span><span lang=EN-US style='font-size:14.0pt;
  mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;mso-fareast-font-family:
  等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:等线;mso-hansi-theme-font:
  minor-latin;mso-font-kerning:1.0pt'>(void)<o:p></o:p></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>设置<span
  lang=EN-US>0</span>点<span lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>stop(void)<o:p></o:p></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>停止运动<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8;mso-yfti-lastrow:yes'>
  <td width=277 valign=top style='width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>run(void)<o:p></o:p></span></p>
  </td>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;mso-ascii-font-family:等线;mso-ascii-theme-font:minor-latin;
  mso-fareast-font-family:等线;mso-fareast-theme-font:minor-fareast;mso-hansi-font-family:
  等线;mso-hansi-theme-font:minor-latin;mso-font-kerning:1.0pt'>开始运动<span
  lang=EN-US><o:p></o:p></span></span></p>
  </td>
 </tr>
</table>

</div>

<p class=MsoTitle style='text-indent:31.0pt'><span lang=EN-US style='font-size:
16.0pt;font-family:等线'>&nbsp;</span></p>

<p class=MsoTitle style='text-indent:31.0pt'><span lang=EN-US style='font-size:
16.0pt;font-family:等线'>Arduino</span><span style='font-size:16.0pt;font-family:
等线'>编程示例：</span></p>
</body></html>

<sxh cpp; first-line: 1;highlight: [89,92]; title: stepper_motor_test.ino>

```
#include "WeELF328P.h"

WeStepperMotor stepperMotor(PORT_3);
void setup()
{  
  stepperMotor.setMicroStep(8);  //1,2,4,8,16,32
  stepperMotor.setSpeed(160);    //0-254
}
void loop() 
{ 
  stepperMotor.moveTo(1600);
  delay(3000);
  stepperMotor.moveTo(0);
  delay(3000);
}
```

</sxh>

##  6. 注意事项 

<html><body>

<p class=MsoNormal style='text-indent:36.0pt'><span lang=EN-US
style='font-size:16.0pt'>1</span><span style='font-size:16.0pt'>、模块上的电位器可以调节驱动电流，输出电流越大，芯片发热越大，要注意散热，如果发热很大就需要更大的散热片。对于步进电机，应该按照负载来调节电流，过大和过小的电流都有可能使电机无法正常运行。<span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal style='text-indent:36.0pt'><span lang=EN-US
style='font-size:16.0pt'>2</span><span style='font-size:16.0pt'>、要保证散热片和驱动芯片接触良好，步进电机驱动发热量很大，即使电机不动也处于发热状态，所以不要弄掉散热片。<span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal style='text-indent:36.0pt'><span lang=EN-US
style='font-size:16.0pt'>3</span><span style='font-size:16.0pt'>、搭建好的装置，最好不要拖动机构，让步进电机快速运动，这样会造成电机反向发点，运动越快，发电量越高，有可能会烧毁模块和主控板。</span><span
lang=EN-US style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>&nbsp;</span><span lang=EN-US style='font-size:16.0pt'><o:p></o:p></span></p>
</body></html>