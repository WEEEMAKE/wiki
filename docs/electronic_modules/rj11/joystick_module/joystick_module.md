<div align=center>
<h1 class="text-center">全向摇杆模块</h1>
</div>

# 全向摇杆模块 

## 1. 模块概述 

<html><body>

<p class=MsoNormal style='text-indent:36.0pt'><span style='font-size:16.0pt;
font-family:宋体;color:#222222;background:white'>全向摇杆模块<span lang=EN-US>(Joystick
Module)</span>包含一个全向摇杆，该模块上使用一个<span lang=EN-US>STC15</span>系列单片机检测摇杆的位置信息，然后通过<span
lang=EN-US>WM</span>单总线与主控通信。该模块可应用在控制小车的移动方向或其他摇杆操控类等方面的应用。</span></p>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>XY轴方向参考：</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'><o:p></o:p></span></p>
</body></html>

  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=601 height=401 id="图片 1" src="docs\electronic_modules\rj11\joystick_module\20200303-171911.png"></span></p>

## 2. 参数规格

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=172 valign=top style='width:129.0pt;border-top:solid #5B9BD5 3.0pt;
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
 <tr>
  <td width=172 valign=top style='width:129.0pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>工作电压</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>DC 5V</span></p>
  </td>
 </tr>
 <tr>
  <td width=172 valign=top style='width:129.0pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>接口类型</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>RJ11</span></p>
  </td>
 </tr>
 <tr>
  <td width=172 valign=top style='width:129.0pt;border:solid white 1.0pt;
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
 <tr>
  <td width=172 valign=top style='width:129.0pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>十字摇杆</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>由两个电位器及平衡环组成</span></p>
  </td>
 </tr>
 <tr>
  <td width=172 valign=top style='width:129.0pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>模拟输出</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>2</span><span
  style='font-size:18.0pt;font-family:宋体;color:white'>个模拟值<span lang=EN-US>(X</span>轴<span
  lang=EN-US>,Y</span>轴<span lang=EN-US>)</span></span></p>
  </td>
 </tr>
 <tr>
  <td width=172 valign=top style='width:129.0pt;border:solid white 1.0pt;
  border-left:solid #5B9BD5 3.0pt;background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>尺寸大小</span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:solid white 1.0pt;
  border-left:none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:18.0pt;font-family:宋体;color:white'>55mm*24mm*18.5mm(</span><span
  style='font-size:18.0pt;font-family:宋体;color:white'>长<span lang=EN-US>*</span>宽<span
  lang=EN-US>*</span>高<span lang=EN-US>)</span></span></p>
  </td>
 </tr>
</table>
</div>
</body></html>

## 3. 编程指南 

### 3.1. 模块功能及图形化编程指南

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有<span lang=EN-US><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>WeeeCode</span></span><span
style='box-sizing: border-box;font-variant-ligatures: normal;font-variant-caps: normal;
orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>、编程猫平台、</span><span lang=EN-US><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>Mixly_Arduino</span></span><span
style='box-sizing: border-box;font-variant-ligatures: normal;font-variant-caps: normal;
orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>、</span><span lang=EN-US><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>MakeCode</span></span><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>等，其图形化编程大同小异，区别不会很大。</span></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=257 valign=top style='width:192.65pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>模块功能</span></b></p>
  </td>
  <td width=223 valign=top style='width:166.95pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>需传参数</span></b></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>图形化编程块举例<span
  lang=EN-US><span style='box-sizing: border-box'>(</span></span><span
  style='box-sizing: border-box'>其他平台图形化编程块大同小异</span><span lang=EN-US><span
  style='box-sizing: border-box'>)</span></span></span></b></p>
  </td>
 </tr>
 <tr>
  <td width=257 style='width:192.65pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>获取<span
  lang=EN-US>X/Y</span>轴模拟值</span></p>
  </td>
  <td width=223 style='width:166.95pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US style='font-size:14.0pt;font-family:华文楷体;
  color:black;background:white'>(2</span><span style='font-size:14.0pt;
  font-family:华文楷体;color:black;background:white'><span style='box-sizing: border-box;
  font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;
  widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
  text-decoration-color: initial;word-spacing:0px'>个参数）端口、轴向选择</span></span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=310 height=134 id="图片 1" src="docs\electronic_modules\rj11\joystick_module\20200224-165559.png"></span></p>
  </td>
 </tr>
</table>


</div>
<p class=MsoNormal align=center style='text-align:center;text-indent:21.0pt'>&nbsp;</p>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>图形化编程示例：</span></p>
</body></html>

  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=468 height=386 id="图片 1" src="docs\electronic_modules\rj11\joystick_module\	20200224-170000.png"></span></p>

### 3.2. 文本代码编程指南

<html><body>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>Arduino编程示例：</span></p>

</body></html>

<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:4;tab-size:4;"><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">"</span><br><br>WeJoystick <span style="color:#5fb4b4;">joystick</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">PORT_A</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span>  <br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">begin</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">9600</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span> <br><span style="color:#ffffff;">{</span><br>  joystick<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readData</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">X= </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>joystick<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">showX</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">Y= </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>joystick<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">showY</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">100</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span></div>

</sxh>

\\
<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>更多使用实例请前往论坛学习：全向摇杆模块使用实例（建设中）</span></p>
</body></html>