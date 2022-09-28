<div align=center>
<h1 class="text-center">旋转电位器模块</h1>
</div>

## 1. 简要概述 

<html><body>

<p class=MsoTitle align=left style='text-align:left;text-indent:36.0pt'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:0pt;
background:white'>旋转电位器模块（<span lang=EN-US>Sliding Potentiometer Module</span>）是基于一个最大阻值为<span
lang=EN-US> 10K</span>Ω 的线性旋转可变电阻，返值范围：<span lang=EN-US>0~255</span>，附带<span
lang=EN-US>8</span>颗蓝色<span lang=EN-US>LED</span>灯，值越大亮的灯越多。</span><span
lang=EN-US>&nbsp;</span><span style='font-size:16.0pt;font-family:宋体;
color:#222222;letter-spacing:0pt;background:white'>可用于电机无极调速、线性值输入等。</span></p>

<p class=MsoTitle align=left style='text-align:left;text-indent:36.0pt'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:0pt;
background:white'>模块值输出定义：</span></p>
</body></html>

  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=600 height=300 id="图片 1" src="docs\electronic_modules\rj11\potentiometer_module\20200304-172149.png"></span></p>

##  2. 参数规格

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
    <td>可变电阻</td><td>旋转线性10KΩ</td>
</tr>
    <tr>
    <td>输出值范围</td><td>0~255</td>
</tr>
    <tr>
    <td>指示灯</td><td>8颗蓝LED</td>
</tr>
    <tr>
    <td>旋转角度</td><td>280度</td>
</tr>
</table>

</div>
</body></html>

## 3. 编程指南 

### 3.1. 模块功能及图形化编程指南

<html><body>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>该模块支持的图形化编程平台有<span lang=EN-US>WeeeCode</span>、<span lang=EN-US>Mixly_Arduino</span>、<span
lang=EN-US>Makecode</span>等，其图形化编程大同小异，区别不会很大。</span></p>
<table class="imagetable" style="display: table; text-align: left;">
 <tr>
  <th>
  <p><b><span>模块功能</span></b></p>
  </th>
  <th>
  <p><b><span>需传参数</span></b></p>
  </th>
  <th>
  <p>图形化编程块举例</span></b></p>
  </th>
 </tr>
 <tr>
  <td >
  <p>输出值<span>0~255</span></span></p>
  </td>
  <td>
      </p>(1</span><span>个参数）端口</span></p>
  </td>
  <td>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=207 height=50 id="图片 1" src="docs\electronic_modules\rj11\potentiometer_module\20200304-162308.png"></span></p>
  </td>
 </tr>
</table>



</div>

<p class=MsoNormal align=left style='text-align:left;text-indent:21.0pt'><span
lang=EN-US style='color:white'>&nbsp;</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>图形化编程示例：</span></p>
</body></html>

  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=500 height=380 id="图片 1" src="docs\electronic_modules\rj11\potentiometer_module\20200304-162633.png"></span></p>


### 3.2. 文本代码编程指南

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>Arduino</span><span style='font-size:
16.0pt;font-family:宋体'>编程示例：</span></p>
</body></html>

<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:4;tab-size:4;"><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">"</span><br> <br>WePotentiometer <span style="color:#5fb4b4;">Potentiometer</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">PORT_A</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br> <br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span>  <br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">begin</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">9600</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span> <br><span style="color:#ffffff;">{</span><br>  Potentiometer<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">OpenLED</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">print</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">Analog </span><span style="color:#99c794;">Value </span><span style="color:#99c794;">is: </span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span>Potentiometer<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">readAnalog</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span> <br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">1000</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  Potentiometer<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">CloseLED</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">1000</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span><br>     </div>


</sxh>

\\
<html><body>

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体'>&nbsp;</span><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体'>更多使用实例请前往论坛学习：PM2.5传感器使用实例（建设中）</span></p>
</body></html>