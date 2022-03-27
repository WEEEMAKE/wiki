
<div class="text-center">
<h1 class="text-center">RGB超声波传感器</h1>
</div>

## 1. 简介

<div align=center>
<img src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/rgb_ultrasonic_sensor.png">
</div>

<html><body>
<p class=MsoNormal  style='text-align:left'><span
  lang=ZH-CN style='font-size:14.0pt;color:windowtext'>RGB超声波传感器是一个用来测量距离的电子模块，测量范围是 4 cm 到 500 cm。可以用来帮助小车避开障碍或其他有关测距避障的项目。超声波发射器向某一方向发射超声波，在发射的同时开始计时，超声波在空气中传播，途中碰到障碍物就立即返回来，超声波接收器收到反射波就立即停止计时。声波在空气中的传播速度为 340m/s，根据计时器记录的时间 t，就可以计算出发射点距障碍物的距离 s，即：s=340*t/2。</span></p>
  <p class=MsoNormal  style='text-align:left'><span
  lang=ZH-CN style='font-size:14.0pt;color:windowtext'>同时，该模块的超声波探头内置有RGB全彩LED灯。</span></p>
</body></html>

>  应用参考：避障小车，手持测距仪，水位监测，超声波计数器等。

## 2. 参数规格

<div align=center>

<table class=MsoTable15List5DarkAccent5 border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border-top:solid #5B9BD5 3.0pt;
  border-left:solid #5B9BD5 3.0pt;border-bottom:solid white 2.25pt;border-right:
  none;background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:等线;color:white'>参数</span></b></p>
  </td>
  <td width=333 valign=top style='width:250.1pt;border-top:solid #5B9BD5 3.0pt;
  border-left:none;border-bottom:solid white 2.25pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:等线;color:white'>值</span></b><b><span
  style='font-size:18.0pt;color:white'>/</span></b><b><span lang=ZH-CN
  style='font-size:18.0pt;font-family:等线;color:white'>描述</span></b></p>
  </td>
 </tr>
 <tr style='height:17.1pt'>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt;height:17.1pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>工作电压</span></b></p>
  </td>
  <td width=333 valign=top style='width:250.1pt;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt;height:17.1pt'>
  <p class=MsoNormal><span style='font-size:16.0pt;color:white'>DC 5V</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>通信方式</span></b></p>
  </td>
  <td width=333 valign=top style='width:250.1pt;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-size:16.0pt;color:white'>WM</span><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>单总线协议</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid white 1.0pt;
  border-left:solid #5B9BD5 3.0pt;background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>超声波频率</span></b></p>
  </td>
  <td width=333 valign=top style='width:250.1pt;border-top:solid white 1.0pt;
  border-left:none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-size:16.0pt;color:white'>42kHz</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>测距精度</span></b></p>
  </td>
  <td width=333 valign=top style='width:250.1pt;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-size:16.0pt;color:white'>1cm</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid white 1.0pt;
  border-left:solid #5B9BD5 3.0pt;background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>测距范围</span></b></p>
  </td>
  <td width=333 valign=top style='width:250.1pt;border-top:solid white 1.0pt;
  border-left:none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-size:16.0pt;color:white'>3cm~500cm</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>输出数据</span></b></p>
  </td>
  <td width=333 valign=top style='width:250.1pt;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span lang=ZH-CN style='font-size:16.0pt;font-family:等线;
  color:white'>距离值（单位：厘米）</span></p>
  </td>
 </tr>
 <tr>
  <td width=277 valign=top style='width:207.4pt;border:solid white 1.0pt;
  border-left:solid #5B9BD5 3.0pt;background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>尺寸大小</span></b></p>
  </td>
  <td width=333 valign=top style='width:250.1pt;border-top:solid white 1.0pt;
  border-left:none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-size:16.0pt;color:white'>100mm*32mm*30mm(</span><span
  lang=ZH-CN style='font-size:16.0pt;font-family:等线;color:white'>长</span><span
  style='font-size:16.0pt;color:white'>*</span><span lang=ZH-CN
  style='font-size:16.0pt;font-family:等线;color:white'>宽</span><span
  style='font-size:16.0pt;color:white'>*</span><span lang=ZH-CN
  style='font-size:16.0pt;font-family:等线;color:white'>高</span><span
  style='font-size:16.0pt;color:white'>)</span></p>
  </td>
 </tr>
</table>

</div>

## 3. 编程指南
### 3.1 模块功能及图形化编程指南

<div class=WordSection1>


<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
14.0pt;font-family:等线'>该模块支持的图形化编程平台有</span><span style='font-size:14.0pt'>WeeeCode</span><span
lang=ZH-CN style='font-size:14.0pt;font-family:等线'>、编程猫平台、</span><span
style='font-size:14.0pt'>Mixly_Arduino</span><span lang=ZH-CN style='font-size:
14.0pt;font-family:等线'>、</span><span style='font-size:14.0pt'>MakeCode</span><span
lang=ZH-CN style='font-size:14.0pt;font-family:等线'>等，其图形化编程大同小异，区别不会很大。</span></p>

<div>

<div align=center>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=176 style='width:131.9pt;border:solid windowtext 1.0pt;padding:
  0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:等线;color:windowtext'>模块功能</span></b></p>
  </td>
  <td width=371 valign=top style='width:278.45pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 0in 0in 0in'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:等线;color:windowtext'>需传参数</span></b></p>
  </td>
  <td width=482 style='width:361.8pt;border:solid windowtext 1.0pt;border-left:
  none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:等线;color:windowtext'>图形化编程块举例</span></b><b><span
  style='font-size:14.0pt;color:windowtext'>(</span></b><b><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>其他平台图形化编程块大同小异</span></b><b><span
  style='font-size:14.0pt;color:windowtext'>)</span></b></p>
  </td>
 </tr>
 <tr style='height:1.0in'>
  <td width=176 style='width:131.9pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>测量距离（</span><span
  style='font-size:14.0pt;color:windowtext'>3~500cm</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>）</span></p>
  </td>
  <td width=371 style='width:278.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 0in 0in 0in;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>（</span><span
  style='font-size:14.0pt;color:windowtext'>1</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>个参数）端口</span></p>
  </td>
  <td width=482 style='width:361.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='color:windowtext'><img width=174 height=36
  src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/P1.png"></span></p>
  </td>
 </tr>
 <tr style='height:1.0in'>
  <td width=176 style='width:131.9pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>设置内置</span><span
  style='font-size:14.0pt;color:windowtext'>RGB</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>灯</span></p>
  </td>
  <td width=371 style='width:278.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 0in 0in 0in;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>（</span><span
  style='font-size:14.0pt;color:windowtext'>5</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>个参数）端口、灯的位置、</span><span
  style='font-size:14.0pt;color:windowtext'>RGB</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>三原色分量值</span></p>
  </td>
  <td width=482 valign=top style='width:361.8pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:14.0pt;color:windowtext'><img width=468 height=173
  src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/P2.png"></span></b></p>
  </td>
 </tr>
 <tr style='height:1.0in'>
  <td width=176 style='width:131.9pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:14.0pt;color:windowtext'>LED</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>灯设置（</span><span
  style='font-size:14.0pt;color:windowtext'>Mini RGB</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>超声波模块独有）</span></p>
  </td>
  <td width=371 style='width:278.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 0in 0in 0in;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>（</span><span
  style='font-size:14.0pt;color:windowtext'>3</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>个参数）端口、灯的位置、</span><span
  style='font-size:14.0pt;color:windowtext'>LED</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:等线;color:windowtext'>灯状态</span></p>
  </td>
  <td width=482 style='width:361.8pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:1.0in'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='color:windowtext'><img width=335 height=54
  src="docs/electronic_modules/rj11/rgb_ultrasonic_sensor/P3.png"></span></p>
  </td>
 </tr>
</table>

</div>

<p class=MsoNormal>&nbsp;</p>

</div>

</div>

### 3.2 文本代码编程指南
## 4. 注意事项

<p class=MsoNormal  style='text-align:left'><span
  lang=ZH-CN style='font-size:14.0pt;color:windowtext'><b>RGB超声波传感器上集成有6颗RGB灯，功耗相对比较大，使用时最好外接电源。</b></span></p>


