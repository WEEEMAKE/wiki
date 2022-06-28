<div align=center>
<h1 class="text-center">继电器模块</h1>
</div>

## **1-简要概述**

<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:等线'>继电器模块板载固定继电器元器件，它是一种可用小电流控制大电流运作的一种“自动开关<span lang=EN-US>”</span>，</span><span
style='font-size:10.5pt;font-family:"Arial",sans-serif;color:#333333;
background:white'> </span><span style='font-size:16.0pt;font-family:等线'>故在电路中起着自动调节、安全保护、转换电路等作用。</span></p>

## **2-参数规格**

<!-- CSS goes in the document HEAD or added to your external stylesheet -->
<style type="text/css">
table.imagetable {
    font-family: verdana,arial,sans-serif;
    font-size:20px;
    color:#333333;
    border-width: 1px;
    border-color: #999999;
    border-collapse: collapse;
}
table.imagetable th {
    background:#b5cfd2 url('cell-blue.jpg');
    border-width: 2px;
    padding: 8px;
    border-style: solid;
    border-color: #999999;
    text-align: center;
}
table.imagetable td {
    background:#dcddc0 url('cell-grey.jpg');
    border-width: 2px;
    padding: 8px;
    border-style: solid;
    border-color: #999999;
    text-align: center;
}
text{
	font-size: 1cm;
	color: #7ec699;
}
</style>

<!-- Table goes in the document BODY -->
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
    <td>最大切换电压</td><td>250VAC/30VDC</td>
</tr>
<tr>
    <td>额定通过电流</td><td>10A</td>
</tr>
<tr>
    <td>指示灯</td><td>2个蓝色LED指示状态</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>设置继电器导通状态<br>NC打开：COM与NC通<br>NC关闭：COM与NO通</td><td>（2个参数）端口、状态</td><td><img src="docs/electronic_modules/rj11/relay_module/20200302-121113.png"></td>
</tr>
</table>

### **3.2-文本代码编程**