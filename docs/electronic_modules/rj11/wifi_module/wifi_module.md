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

  <p class=MsoNormal align=center style='text-align:center'><img width=300
  height=300 id="图片 15" src="docs\electronic_modules\rj11\wifi_module\20190828-160219.png"></p>

<html><body>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压</td><td>DC 5V(内置3.3V电平转换)</td>
</tr>
    <tr>
    <td>接口类型</td><td>RJ11</td>
</tr>
    <tr>
    <td>通信方式</td><td>WM单总线</td>
</tr>
    <tr>
    <td>WIFI芯片</td><td>ESP8266</td>
</tr>
    <tr>
    <td>状态指示灯</td><td>当wifi连接成功时，蓝灯常亮</td>
</tr>
    <tr>
    <td>尺寸大小</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
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
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需传参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>设置wifi信息</td><td>(3个参数）端口、wifi名称、wifi密码</td><td><p class=MsoNormal align=center style='text-align:center'><img width=590
  height=65 id="图片 8" src="docs\electronic_modules\rj11\wifi_module\20190828-171102.png"></p></td>
</tr>
    <tr>
    <td>初始化为从机模式</td><td>(3个参数）端口、IP地址、通信端口号</td><td>  <p class=MsoNormal align=center style='text-align:center'><img width=693
  height=63 id="图片 9" src="docs\electronic_modules\rj11\wifi_module\20190828-171108.png"></p></td>
</tr>
    <tr>
    <td>初始化为TCP模式</td><td>(3个参数）端口、IP地址、通信端口号</td><td>  <p class=MsoNormal><img width=675 height=64 id="图片 10"
  src="docs\electronic_modules\rj11\wifi_module\20190828-171115.png"></p></td>
</tr>
    <tr>
    <td>初始化为AP模式</td><td>(2个参数）端口、信道号</td><td>  <p class=MsoNormal align=center style='text-align:center'><img width=424
  height=64 id="图片 1" src="docs\electronic_modules\rj11\wifi_module\20190828-171121.png"></p></td>
</tr>
    <tr>
    <td>初始化为STA模式</td><td>(1个参数）端口</td><td>  <p class=MsoNormal align=center style='text-align:center'><img width=326
  height=60 id="图片 11" src="docs\electronic_modules\rj11\wifi_module\20190828-171126.png"></p></td>
</tr>
    <tr>
    <td>判断是否接收到数据（布尔值）</td><td>(1个参数）端口</td><td>  <p class=MsoNormal align=center style='text-align:center'><img width=340
  height=48 id="图片 13" src="docs\electronic_modules\rj11\wifi_module\20190828-171132.png"></p></td>
</tr>
    <tr>
    <td>判断是否连接完成分配好IP地址(布尔值)</td><td>(1个参数）端口</td><td>  <p class=MsoNormal align=center style='text-align:center'><img width=359
  height=48 id="图片 12" src="docs\electronic_modules\rj11\wifi_module\20190828-171139.png"></p></td>
</tr>
    <tr>
    <td>用于对接收到的数据作比较</td><td>	
(2个参数）端口、需要对比的字符串</td><td>  <p class=MsoNormal align=center style='text-align:center'><img width=408
  height=49 id="图片 14" src="docs\electronic_modules\rj11\wifi_module\20190828-171145.png"></p></td>
</tr>
    <tr>
    <td>接收到数据、IP地址等数据的内容</td><td>(2个参数）端口、内容</td><td>  <p class=MsoNormal align=center style='text-align:center'><img width=363
  height=151 id="图片 15" src="docs\electronic_modules\rj11\wifi_module\20190828-171151.png"></p></td>
</tr>
</table>
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