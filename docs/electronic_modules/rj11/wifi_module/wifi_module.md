<div align=center>
<h1 class="text-center">WIFI模块</h1>
</div>

##  1. 模块介绍 

<html><body>

<p class=MsoTitle align=left style='text-align:left'><span style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>&nbsp; <span lang=ZH-CN>本</span><span
class=SpellE>wifi</span><span lang=ZH-CN>模块基于</span>ESP8266<span lang=ZH-CN>基础上进行的二次开发，把一些功能进行了封装，使用简单的指令就可以设置好局域网，轻松实现物联网的搭建。本模块可以实现</span><span
class=SpellE>wifi</span><span lang=ZH-CN>模块做主机、从机以及连接外网通讯的功能，不需要繁琐的</span>AT<span
lang=ZH-CN>指令或网页设置，就可以实现</span>1<span lang=ZH-CN>对</span>1<span lang=ZH-CN>，</span>1<span
lang=ZH-CN>对多，多对多连接的设置。</span><o:p></o:p></span></p>
</body></html>

##  2. 参数规格 

  <p class=MsoNormal align=center style='text-align:center'><img width=854
  height=600 id="图片 15" src="docs\electronic_modules\rj11\wifi_module\20190828-160219.png"></p>

<html><body>

<div align=center>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=238 valign=top style='width:178.5pt;border-top:solid #5B9BD5 3.0pt;
  border-left:solid #5B9BD5 3.0pt;border-bottom:solid white 2.25pt;border-right:
  none;background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:宋体;color:white'>参数</span></b></p>
  </td>
  <td width=552 valign=top style='width:5.75in;border-top:solid #5B9BD5 3.0pt;
  border-left:none;border-bottom:solid white 2.25pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:宋体;color:white'>值</span></b><b><span
  style='font-size:18.0pt;font-family:宋体;color:white'>/<span lang=ZH-CN>描述</span></span></b></p>
  </td>
 </tr>
 <tr>
  <td width=238 valign=top style='width:178.5pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:宋体;color:white'>工作电压</span></b></p>
  </td>
  <td width=552 valign=top style='width:5.75in;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>DC 5V(<span lang=ZH-CN>内置</span>3.3V<span
  lang=ZH-CN>电平转换</span>)</span></p>
  </td>
 </tr>
 <tr>
  <td width=238 valign=top style='width:178.5pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:宋体;color:white'>接口类型</span></b></p>
  </td>
  <td width=552 valign=top style='width:5.75in;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>RJ11</span></p>
  </td>
 </tr>
 <tr>
  <td width=238 valign=top style='width:178.5pt;border:solid white 1.0pt;
  border-left:solid #5B9BD5 3.0pt;background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:宋体;color:white'>通信方式</span></b></p>
  </td>
  <td width=552 valign=top style='width:5.75in;border-top:solid white 1.0pt;
  border-left:none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>WM<span lang=ZH-CN>单总线</span></span></p>
  </td>
 </tr>
 <tr>
  <td width=238 valign=top style='width:178.5pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:none;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:18.0pt;font-family:宋体;color:white'>WIFI<span lang=ZH-CN>芯片</span></span></b></p>
  </td>
  <td width=552 valign=top style='width:5.75in;border:none;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>ESP8266</span></p>
  </td>
 </tr>
 <tr>
  <td width=238 style='width:178.5pt;border:solid white 1.0pt;border-left:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:宋体;color:white'>状态指示灯</span></b></p>
  </td>
  <td width=552 valign=top style='width:5.75in;border-top:solid white 1.0pt;
  border-left:none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:18.0pt;font-family:宋体;color:white'>当</span><span
  style='font-size:18.0pt;font-family:宋体;color:white'>wifi<span lang=ZH-CN>连接成功时，蓝灯常亮</span></span></p>
  </td>
 </tr>
 <tr>
  <td width=238 valign=top style='width:178.5pt;border-top:none;border-left:
  solid #5B9BD5 3.0pt;border-bottom:solid white 1.0pt;border-right:solid white 1.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:18.0pt;font-family:宋体;color:white'>尺寸大小</span></b></p>
  </td>
  <td width=552 valign=top style='width:5.75in;border-top:none;border-left:
  none;border-bottom:solid white 1.0pt;border-right:solid #5B9BD5 3.0pt;
  background:#5B9BD5;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:18.0pt;font-family:宋体;color:white'>55mm*24mm*18.5mm(<span
  lang=ZH-CN>长</span>*<span lang=ZH-CN>宽</span>*<span lang=ZH-CN>高</span>)</span></p>
  </td>
 </tr>
</table>

</div>
</body></html>

## 3. 使用指南

### 3.1. 功能模块及WeeeCode图形化编程指南

<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp; </span><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;background:white'>该模块支持的图形化编程平台目前有</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>WeeeCode
3.0<span lang=ZH-CN>，其图形化编程指南如下：</span></span></p>

<div align=center>
<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=257 valign=top style='width:193.1pt;border:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:华文楷体;color:black;background:
  white'>模块功能</span></b></p>
  </td>
  <td width=222 valign=top style='width:166.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:华文楷体;color:black;background:
  white'>需传参数</span></b></p>
  </td>
  <td width=708 valign=top style='width:531.3pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:华文楷体;color:black;background:
  white'>图形化编程块举例</span></b><b><span style='font-size:14.0pt;font-family:华文楷体;
  color:black;background:white'>(</span><span lang=ZH-CN>其他平台图形化编程块大同小异</span>)</b></p>
  </td>
 </tr>
 <tr style='height:79.55pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:79.55pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>设置</span><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>wifi<span
  lang=ZH-CN>信息</span></span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:79.55pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(3<span lang=ZH-CN>个参数）端口、</span>wifi<span lang=ZH-CN>名称、</span>wifi<span
  lang=ZH-CN>密码</span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:79.55pt'>
  <p class=MsoNormal align=center style='text-align:center'><img width=590
  height=65 id="图片 8" src="docs\electronic_modules\rj11\wifi_module\20190828-171102.png"></p>
  </td>
 </tr>
 <tr style='height:79.55pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:79.55pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>初始化为从机模式</span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:79.55pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(3<span lang=ZH-CN>个参数）端口、</span>IP<span lang=ZH-CN>地址、通信端口号</span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:79.55pt'>
  <p class=MsoNormal align=center style='text-align:center'><img width=693
  height=63 id="图片 9" src="docs\electronic_modules\rj11\wifi_module\20190828-171108.png"></p>
  </td>
 </tr>
 <tr style='height:66.95pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:66.95pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>初始化为</span><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>TCP<span
  lang=ZH-CN>模式</span></span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:66.95pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(3<span lang=ZH-CN>个参数）端口、</span>IP<span lang=ZH-CN>地址、通信端口号</span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:66.95pt'>
  <p class=MsoNormal><img width=675 height=64 id="图片 10"
  src="docs\electronic_modules\rj11\wifi_module\20190828-171115.png"></p>
  </td>
 </tr>
 <tr style='height:55.25pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>初始化为</span><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>AP<span
  lang=ZH-CN>模式</span></span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(2<span lang=ZH-CN>个参数）端口、信道号</span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><img width=424
  height=64 id="图片 1" src="docs\electronic_modules\rj11\wifi_module\20190828-171121.png"></p>
  </td>
 </tr>
 <tr style='height:55.25pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>初始化为</span><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>STA<span
  lang=ZH-CN>模式</span></span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(1<span lang=ZH-CN>个参数）端口 </span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><img width=326
  height=60 id="图片 11" src="docs\electronic_modules\rj11\wifi_module\20190828-171126.png"></p>
  </td>
 </tr>
 <tr style='height:55.25pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>判断是否接收到数据</span></p>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>（布尔值）</span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(1<span lang=ZH-CN>个参数）端口</span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><img width=340
  height=48 id="图片 13" src="docs\electronic_modules\rj11\wifi_module\20190828-171132.png"></p>
  </td>
 </tr>
 <tr style='height:55.25pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>判断是否连接完成分配好</span><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>IP<span
  lang=ZH-CN>地址</span>(<span lang=ZH-CN>布尔值</span>)</span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(1<span lang=ZH-CN>个参数）端口</span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><img width=359
  height=48 id="图片 12" src="docs\electronic_modules\rj11\wifi_module\20190828-171139.png"></p>
  </td>
 </tr>
 <tr style='height:55.25pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>用于对接收到的数据作比较</span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(2<span lang=ZH-CN>个参数）端口、需要对比的字符串</span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><img width=408
  height=49 id="图片 14" src="docs\electronic_modules\rj11\wifi_module\20190828-171145.png"></p>
  </td>
 </tr>
 <tr style='height:55.25pt'>
  <td width=257 style='width:193.1pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>接收到数据、</span><span
  style='font-size:14.0pt;font-family:华文楷体;color:black;background:white'>IP<span
  lang=ZH-CN>地址等数据的内容</span></span></p>
  </td>
  <td width=222 style='width:166.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:black;
  background:white'>(2<span lang=ZH-CN>个参数）端口、内容</span></span></p>
  </td>
  <td width=708 style='width:531.3pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:55.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><img width=363
  height=151 id="图片 15" src="docs\electronic_modules\rj11\wifi_module\20190828-171151.png"></p>
  </td>
 </tr>
</table>


</div>
<p class=MsoNormal align=center style='text-align:center;text-indent:21.0pt'>&nbsp;</p>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体;color:white'>&nbsp;</span><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体'>编程示例：</span></p>
<p class=MsoNormal align=center style='text-align:center;text-indent:21.0pt'>&nbsp;</p>
</body></html>

### 3.2. 文本代码编程指南

## 4. 注意事项

<html><body>
<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>1<span
lang=ZH-CN>、由于此模块传输采用单总线方式，读取和发送数据频率不能太快，太快可能会漏包。建议间隔时间</span>100ms<span
lang=ZH-CN>，或者手动加入漏包重发机制，来保证数据正确接收。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>2<span
lang=ZH-CN>、当更改</span>wifi<span lang=ZH-CN>账号、密码、端口号时最好重新给</span>wifi<span
lang=ZH-CN>模块上一下电，这样才能保证更改完成。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>3<span
lang=ZH-CN>、当多连时，从机如果长时间不通讯会断开和主机的联通，重新连接后可能会重新分配序号。</span></span></p>
</body></html>