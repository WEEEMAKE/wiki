<div align=center>
<h1 class="text-center">限位开关模块</h1>
</div>

## 1. 简要概述

<html><body>

<p class=MsoTitle align=left style='text-align:left;text-indent:36.0pt'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:0pt;
background:white'>限位开关模块是一款物理开关，与机械结构结合使用，可起限位作用，当触发时，它会输出一个电平信号给控制端。</span></p>
<p class=MsoTitle align=left style='text-align:left;text-indent:36.0pt'><span
style='font-size:16.0pt;font-family:宋体;color:#222222;letter-spacing:0pt;
background:white'>模块外观：</span></p>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=681 height=435 id="图片 1" src="docs\electronic_modules\rj11\switch_module\20200313-152430.png"></span></p>

</body></html>

##  2. 参数规格

<html><body>

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
    <td>开关方式</td><td>机械式</td>
</tr>
    <tr>
    <td>开关个数</td><td>1个</td>
</tr>
    <tr>
    <td>输出信号</td><td>数字信号（0/1）</td>
</tr>
    <tr>
    <td>开关寿命</td><td>≥10000次</td>
</tr>
    <tr>
    <td>尺寸大小</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>



</div>
</body></html>

##  3. 编程指南 



###  3.1. 模块功能及图形化编程指南 

<html><body>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>图形化编程指南以<span lang=EN-US>WeeeCode 3.0</span>图形化软件为例，其图形化编程大同小异，区别不会很大。</span></p>
<table class="imagetable" style="display: table; text-align: left;">
 <tr>
  <td>模块功能</td>
  <td>需传参数</td>
  <td>图形化编程块举例</td>
 </tr>
 <tr>
  <td>输出开关信号</td>
  <td>(1个参数）端口</td>
  <td>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=246 height=51 id="图片 1" src="\docs\electronic_modules\rj11\switch_module\20200313-151320.png"></span></p>
  </td>
 </tr>
</table>


</div>

<p class=MsoNormal align=left style='text-align:left;text-indent:21.0pt'><span
lang=EN-US style='color:white'>&nbsp;</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体;color:#222222;background:white'>图形化编程示例：</span></p>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=409 height=325 id="图片 1" src="docs\electronic_modules\rj11\switch_module\20200313-151306.png"></span></p>

</body></html>

### 3.2. 文本代码编程指南 

<html><body>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体;color:#222222;background:white'>Arduino编程示例：</span></p>
</body></html>

<div style="white-space:pre;font-family:Consolas;color:#d8dee9;background-color:#303841;-moz-tab-size:4;tab-size:4;"><span style="color:#c695c6;">#include</span> <span style="color:#5fb4b4;">"</span><span style="color:#99c794;">WeELF328P.h</span><span style="color:#5fb4b4;">"</span><br>WeLimitSwitch <span style="color:#5fb4b4;">limitSwitch</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">PORT_A</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">setup</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span> <br><span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">begin</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">9600</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span><br><span style="color:#c695c6;font-style:italic;">void</span> <span style="color:#5fb4b4;">loop</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><br><span style="color:#ffffff;">{</span><br>  <span style="color:#c695c6;">if</span><span style="color:#ffffff;">(</span>limitSwitch<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">read</span><span style="color:#ffffff;">(</span><span style="color:#ffffff;">)</span><span style="color:#f97b58;">==</span><span style="color:#f9ae58;">1</span><span style="color:#ffffff;">)</span><br>  <span style="color:#ffffff;">{</span><br>    Serial<span style="color:#a6acb9;">.</span><span style="color:#6699cc;">println</span><span style="color:#ffffff;">(</span><span style="color:#5fb4b4;">"</span><span style="color:#99c794;">limitSwitch </span><span style="color:#99c794;">DOWN</span><span style="color:#5fb4b4;">"</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br>  <span style="color:#ffffff;">}</span><br>  <span style="color:#6699cc;">delay</span><span style="color:#ffffff;">(</span><span style="color:#f9ae58;">100</span><span style="color:#ffffff;">)</span><span style="color:#a6acb9;">;</span><br><span style="color:#ffffff;">}</span></div>
</sxh>