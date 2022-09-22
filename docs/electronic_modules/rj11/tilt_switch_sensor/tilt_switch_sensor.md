<div align=center>
<h1 class="text-center">倾斜开关传感器</h1>
</div>


## **1-简要概述**

<div align=center>
<img src="docs\electronic_modules\rj11\tilt_switch_sensor\tilt_switch_sensor.png" width=30%>
</div>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; 倾斜开关传感器用来检测是否倾斜，当传感器向右或向左倾斜时会有相应的指示灯显示。垂直悬挂的倾斜开关探头在受到外力作用且偏离垂直位置17度以上时，倾斜开关内部的金属球触点动作，常闭触点断开。当外力撤消后，倾斜开关回复到垂直状态，金属球触点复又闭合。

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; 应用示例：水平测量仪等
</span>
</p>



## **2-参数规格**

<!-- Table goes in the document BODY -->

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>项</th><th>值/描述</th>
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
    <td>开关个数</td><td>2个</td>
</tr>
<tr>
    <td>开关方式</td><td>机械式</td>
</tr>
<tr>
    <td>尺寸大小</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>


## **3-编程指南**

### 3.1. 模块功能及图形化编程指南 

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp; </span><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有WeeeCode、编程猫平台、Mixly_Arduino、MakeCode等，其图形化编程大同小异，区别不会很大。</span></span></span></p>


<div align=center>
<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='border-collapse:collapse'>
 <tr>
  <td width=257 valign=top style='width:192.65pt;border:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:华文楷体;color:windowtext;
  background:white'>模块功能</span></b></p>
  </td>
  <td width=223 valign=top style='width:166.95pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:华文楷体;color:windowtext;
  background:white'>需传参数</span></b></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=ZH-CN style='font-size:14.0pt;font-family:华文楷体;color:windowtext;
  background:white'>图形化编程块举例</span></b><b style='box-sizing: border-box;
  font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;
  widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
  text-decoration-color: initial;word-spacing:0px'><span style='box-sizing: border-box'><span
  style='font-size:14.0pt;font-family:华文楷体;color:windowtext;background:white'>(</span><span
  lang=ZH-CN><span style='box-sizing: border-box'>其他平台图形化编程块大同小异</span></span><span
  style='box-sizing: border-box'>)</span></span></b></p>
  </td>
 </tr>
 <tr style='height:98.9pt'>
  <td width=257 style='width:192.65pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0in 5.4pt 0in 5.4pt;height:98.9pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:windowtext;background:white'>返回两个开关的开关值</span></p>
  </td>
  <td width=223 style='width:166.95pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:98.9pt'>
  <p class=MsoNormal><span style='font-size:14.0pt;font-family:华文楷体;color:windowtext;
  background:white'>(2<span lang=ZH-CN><span style='box-sizing: border-box;
  font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;
  widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
  text-decoration-color: initial;word-spacing:0px'>个参数）端口、需要判断的状态</span></span></span></p>
  </td>
  <td width=462 valign=top style='width:346.5pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0in 5.4pt 0in 5.4pt;height:98.9pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='color:windowtext'><img width=407 height=136 id="图片 2"
  src="docs\electronic_modules\rj11\tilt_switch_sensor\20200220-144052.png"></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='text-indent:21.0pt'>&nbsp;</p>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>图形化编程示例：</span></p>
<p class=MsoNormal align=center style='text-align:center'><span
  style='color:windowtext'><img width=568 height=605 id="图片 2"
  src="docs\electronic_modules\rj11\tilt_switch_sensor\20200219-163015.png"></span></p>

## **3.2-文本代码编程指南**
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>Arduino编程示例：</span></p>


```
#include<WeELF328P.h>
WeTiltSwitch tilt_D(PORT_D);
WeRGBLed rgb_led_board(OnBoard_RGB);
uint8_t tilt_D_value;
void setup(){
	delay(1000);
}
void loop(){
	tilt_D_value = tilt_D.readSensor();
	if(tilt_D_value == 2){
        rgb_led_board.setColor(1, 20, 0, 0);
        rgb_led_board.show();
    }else if(tilt_D_value == 1){
        rgb_led_board.setColor(1, 0, 0, 20);
        rgb_led_board.show();
    }else{
        rgb_led_board.setColor(1, 0, 0, 0);
        rgb_led_board.show();
    }
    delay(100);
}
```





<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>更多使用实例请前往论坛学习：倾斜开关使用示例</span></p>
