<div align=center>
<h1 class="text-center">智能红外模块</h1>
</div>

## 1. 模块介绍

<html><body>

<p class=MsoTitle align=left style='text-align:left'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>本智能红外模块能学习各类电器的红外遥控并存储记录。学习完后，可以编程控制各类电器，结合物联网，使各类电器可以实现远程控制，以及实时监测电器开关状态。</span></p>
</body></html>

## 2. 参数规格

  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=705	 height=407
  src="\docs\electronic_modules\rj11\smart_ir_module\20201103-144351.png"></span></p>


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
    <td>通信方式</td><td>WM单总线</td>
</tr>
    <tr>
    <td>MCU芯片</td><td>N76E003</td>
</tr>
    <tr>
    <td>状态指示灯</td><td>进入学习状态时亮，学习完灭</td>
</tr>
    <tr>
    <td>数码管</td><td>编号0~F(0~15)， 共可学习16个按键</td>
</tr>
    <tr>
    <td>功能按钮</td><td>短按切换编号，长按进入学习状态</td>
</tr>
    <tr>
    <td>红外接收</td><td>一体化红外接收传感器</td>
</tr>
    <tr>
    <td>红外发射</td><td>红外发射管*3</td>
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
<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:black;background:
white'>该模块支持的图形化编程平台目前有<span lang=EN-US>WeeeCode 3.x</span>，其图形化编程指南如下：</span></p>
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需传参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>红外学习并编号</td><td>(2个参数）端口、编号（0~15）</td><td>  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=364 height=64
  src="\docs\electronic_modules\rj11\smart_ir_module\20201103-145132.png"></span></p></td>
</tr>
<tr>
    <td>发送对应编号的红外信息</td><td>(2个参数）端口、编号（0~15）</td><td>  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=364 height=64
  src="\docs\electronic_modules\rj11\smart_ir_module\20201103-145132.png"></span></p></td>
</tr>
</table>



</div>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:white'>&nbsp;</span><span
style='font-size:16.0pt;font-family:宋体'>编程示例：</span><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal style='margin-left:24.0pt'><b><span style='font-size:16.0pt'>①</span></b><b><span style='font-size:16.0pt'>红外按键学习：</span></b></p>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt'>方法一：给模块供电，通过按模块上的按钮，短按切换编号，长按进入学习状态，进入学习状态之后蓝色状态指示灯会亮起，这时把你需要学习遥控器的按钮对着模块上的红外接收头按一次，当蓝色状态指示灯熄灭，说明已经学习完成。</span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt'>（备注：数码管显示<span
lang=EN-US>0~F</span>，其中的<span lang=EN-US>A</span>，<span lang=EN-US>b</span>，<span
lang=EN-US>C</span>，<span lang=EN-US>d</span>，<span lang=EN-US>E</span>，<span
lang=EN-US>F</span>对应<span lang=EN-US>10</span>，<span lang=EN-US>11</span>，<span
lang=EN-US>12</span>，<span lang=EN-US>13</span>，<span lang=EN-US>14</span>，<span
lang=EN-US>15</span>。）</span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt'>方法二：使用编程的方法。这个建议使用在线模式，现将在线调试固件刷入主控板，然后使用<b>智能红外模块的接收积木</b>，输入一个编号（<span
lang=EN-US>0~15</span>），点击运行，模块就进入学习状态，这时把你需要学习遥控器的按钮对着模块上的红外接收头按一次，当蓝色状态指示灯熄灭，说明已经学习完成。例如，想要将某家电的开关的遥控按钮学习并编号为<span
lang=EN-US>1</span>，则：</span></p>
<p class=MsoNormal align=center style='text-align:center;text-indent:21.0pt'><span
lang=EN-US><img width=362 height=62 id="图片 4" src="\docs\electronic_modules\rj11\smart_ir_module\20201103-152322.png"></span></p>


<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt'>演示视频：</span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt'>&nbsp;</span></p>

<p class=MsoNormal style='text-indent:16.0pt'><b><span style='font-size:16.0pt'>②红外按键发送：</span></b></p>

<p class=MsoTitle style='text-indent:16.0pt'><b><span style='font-size:16.0pt;
font-family:等线;letter-spacing:0pt'>能有效进行这个操作的前提是，你在此之前已经将某个按钮学习并编号。</span></b></p>
<p class=MsoTitle align=center style='text-align:center;text-indent:28.0pt'><span
lang=EN-US><img width=399 height=375 id="图片 5" src="\docs\electronic_modules\rj11\smart_ir_module\20201103-152244.png"></span></p>


</body></html>

### 3.2. 文本代码编程指南



<html><body>

</body></html>