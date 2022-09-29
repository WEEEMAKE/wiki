<div align=center>
<h1 class="text-center">42步进电机</h1>
</div>

## 1. 电机概述

<html><body>
<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;line-height:105%;font-family:宋体'>42</span><span
style='font-size:16.0pt;line-height:105%;font-family:宋体'>步进电机指步进电机的尺寸，混合式步进电机一般是方形的，法兰外框尺寸是<span
lang=EN-US>42mm*42mm</span>；永磁式步进电机一般是圆形的，电机机身外径是<span lang=EN-US>42mm</span>，<span
lang=EN-US>Weeemake</span>平台使用的是第一种。外观图如下：</span></p>
</body></html>

  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US><img width=1138
  height=335 id="图片 1" src="docs\electronic_modules\motor\42_stepper_motor\20200310-173248.png"></span></p>



<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
line-height:105%;font-family:宋体'>步进电机可用于精确运动的场景，如写字机器人、绘画机器人、 <span lang=EN-US>3D</span>打印机等。</span></p>
</body></html>

## 2. 电机参数

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>额定电压</td><td>DC 12V</td>
</tr>
<tr>
    <td>电流</td><td>1.7A/PHSE</td>
</tr>
    <tr>
    <td>相位</td><td>双相</td>
</tr>
    <tr>
    <td>步进角度</td><td>1.8±5%步</td>
</tr>
    <tr>
    <td>静力矩</td><td>40N·cm</td>
</tr>
    <tr>
    <td>保持力矩</td><td>2.2N·cm Max</td>
</tr>
    <tr>
    <td>转矩

</td><td>54G·cm2</td>
</tr>
</table>

</div>
</body></html>



## 3. 编程指南

<html><body>

<p class=MsoNormal style='text-indent:32.15pt'><b><span style='font-size:16.0pt;
line-height:105%;font-family:宋体;color:#222222;background:white'>请参考步进电机驱动模块编程指南。
</body></html>

## 4. 注意事项

<p class=MsoNormal style='text-indent:32.0pt;mso-char-indent-count:2.0'><span
style='font-size:16.0pt;mso-ascii-font-family:Helvetica;mso-hansi-font-family:
Helvetica;mso-bidi-font-family:Helvetica;color:#222222;background:white'>不能长时间快速正反转，这样会造成电流过大，发热量大，烧毁模块上的驱动芯片。</span></p>
</body></html>