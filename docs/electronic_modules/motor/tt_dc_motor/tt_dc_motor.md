<div align=center>
<h1 class="text-center">TT直流电机</h1>
</div>

## 1. 电机概述

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;line-height:105%;font-family:宋体'>TT</span><span
style='font-size:16.0pt;line-height:105%;font-family:宋体'>直流电机是一款被广泛应用于电子<span
lang=EN-US>DIY</span>，机器人制作，智能车制作环节重点动力装置，其组装简单，扩展性能强，价格低廉等诸多特点，因此受到广大师生和电子爱好者的喜欢。</span></p>
</body></html>

  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US><img width=622
  height=512 id="图片 1" src="docs\electronic_modules\motor\tt_dc_motor\20200310-151819.png"></span></p>

## 2. 电机参数
<table class="imagetable" style="display: table; text-align: left;">
<tr>
<th> 参数         </th>    <th> 值/描述   </th>              
</tr>
<tr>
<td> 额定电压  </td>   <td> 9.6 VDC          </td>       
</tr>
<tr>
<td> 工作电压范围 </td> <td> 7.0~10.0 VDC  </td>            
</tr>
<tr>
<td> 空载电流 </td>     <td> ≤150mA     </td>                
</tr>
<tr>
<td> 空载转速   </td>   <td> 14500RPM±10%      </td>          
</tr>
<tr>
<td> 减速比      </td>  <td> 48:1（减速输出302RPM左右） </td>
</tr>
<tr>
<td> 堵转转矩   </td>   <td> ≥75gf.cm      </td>        
</tr>
<tr>
<td> 堵转电流    </td>  <td> ≤1.8A </td>    
</tr>
</table>
</body></html>

## 3. 编程指南

### 3.1. 模块功能及图形化编程指南

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
line-height:105%;font-family:等线;color:#666666;background:white'>该电机支持的图形化编程平台有</span></span><span
lang=EN-US style='font-size:16.0pt;line-height:105%;font-family:"Helvetica",sans-serif;
color:#666666;background:white'><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>WeeeCode</span></span><span style='font-size:16.0pt;line-height:105%;
font-family:等线;color:#666666;background:white'><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>、编程猫平台、</span></span><span
lang=EN-US style='font-size:16.0pt;line-height:105%;font-family:"Helvetica",sans-serif;
color:#666666;background:white'><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>Mixly_Arduino</span></span><span style='font-size:16.0pt;line-height:105%;
font-family:等线;color:#666666;background:white'><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>、</span></span><span
lang=EN-US style='font-size:16.0pt;line-height:105%;font-family:"Helvetica",sans-serif;
color:#666666;background:white'><span style='box-sizing: border-box;font-variant-ligatures: normal;
font-variant-caps: normal;orphans: 2;text-align:start;widows: 2;-webkit-text-stroke-width: 0px;
text-decoration-style: initial;text-decoration-color: initial;word-spacing:
0px'>MakeCode</span></span><span style='font-size:16.0pt;line-height:105%;
font-family:等线;color:#666666;background:white'><span style='box-sizing: border-box;
font-variant-ligatures: normal;font-variant-caps: normal;orphans: 2;text-align:
start;widows: 2;-webkit-text-stroke-width: 0px;text-decoration-style: initial;
text-decoration-color: initial;word-spacing:0px'>等，其图形化编程大同小异，区别不会很大。</span></span></p>

<table class="imagetable" style="display: table; text-align: left;">
 <tr>
  <th>模块功能</th>
  <th>需传参数</th>
  <th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
 </tr>
 <tr>
    <td>驱动电机运作</td><td>（2个参数）所接端口、速度(-255~255)

</td><td> <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US><img width=328
  height=64 id="图片 1" src="docs\electronic_modules\motor\tt_dc_motor\20200310-150145.png"></span></p></td>
  </td>
 </tr>
</table>


</div>

<p class=MsoNormal style='text-indent:36.0pt'><b><span lang=EN-US
style='font-size:5.0pt;line-height:105%;font-family:等线;color:#ffffff;
background:yellow'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal style='text-indent:36.0pt'><b><span style='font-size:16.0pt;
line-height:105%;font-family:等线;color:#666666;background:yellow'>备注：</span></b><span
style='font-size:16.0pt;line-height:105%;font-family:黑体;color:#666666;
background:white'>电机转速正负定义，电机轴面向人，速度值为正：顺时针转；速度值为负：逆时针转</span></p>

<p class=MsoNormal style='text-indent:36.0pt'><b><span lang=EN-US
style='font-size:5.0pt;line-height:105%;font-family:等线;color:#ffffff;
background:yellow'><o:p>&nbsp;</o:p></span></b></p>


<p class=MsoNormal style='text-indent:36.0pt'><span style='font-size:16.0pt;
line-height:105%;font-family:等线;color:#666666;background:white'>图形化编程示例：</span></span></p>

</body></html>

  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US><img width=328
  height=64 id="图片 1" src="docs\electronic_modules\motor\tt_dc_motor\20200310-150145.png"></span></p>

### 3.2. 文本代码编程指南

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:等线'>Arduino编程示例：</span></p>
</body></html>

<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:4;tab-size:4;"><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">"</span><br><br>WeDCMotor <span style="color:#5fb4b4;">motor1</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">M1</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>WeDCMotor <span style="color:#5fb4b4;">motor2</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">M2</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><br><span style="color:#6699cc;font-style:italic;">uint8_t</span> motorSpeed <span style="color:#f97b58;">=</span> <span style="color:#f9ae58;">100</span><span style="color:#a6acb9;">;</span><br><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span>  <br><span style="color:#ffffff;">}</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span> <br><span style="color:#ffffff;">{</span><br>  motor1<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">run</span><span style="color:#ffffff;">(</span>motorSpeed<span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  motor2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">run</span><span style="color:#ffffff;">(</span>motorSpeed<span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">2000</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  motor1<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">stop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  motor2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">stop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">500</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  motor1<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">run</span><span style="color:#ffffff;">(</span><span style="color:#f97b58;">-</span>motorSpeed<span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  motor2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">run</span><span style="color:#ffffff;">(</span><span style="color:#f97b58;">-</span>motorSpeed<span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">2000</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  motor1<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">stop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  motor2<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">stop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">500</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span></div>

</sxh>

## 4. 注意事项

<html><body>

<p class=MsoNormal style='text-indent:32.0pt;mso-char-indent-count:2.0'><span
style='font-size:16.0pt;mso-ascii-font-family:Helvetica;mso-hansi-font-family:
Helvetica;mso-bidi-font-family:Helvetica;color:#222222;background:white'>不能长时间快速正反转，这样会造成电流过大，发热量大，烧毁模块上的驱动芯片。</span></p>
</body></html>