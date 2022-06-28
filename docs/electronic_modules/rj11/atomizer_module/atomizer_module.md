<div align=center>
<h1 class="text-center">雾化器模块</h1>
</div>

## **1-简要概述**

<p class=MsoNormal style='text-indent:32.0pt;mso-char-indent-count:2.0'><span
style='font-size:16.0pt;line-height:105%;font-family:等线;mso-ascii-theme-font:
minor-fareast;mso-fareast-theme-font:minor-fareast;mso-hansi-theme-font:minor-fareast'>雾化器模块(Water Atomizer)是一个利用高频超声震动片将液态的物质雾化成气态的模块，因此可制作加湿器等。</span><span
lang=EN-US style='font-family:等线;mso-ascii-theme-font:minor-fareast;mso-fareast-theme-font:
minor-fareast;mso-hansi-theme-font:minor-fareast'></span></p>

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
    <td>输出电压</td><td>24V</td>
</tr>
<tr>
    <td>最大功率</td><td>2W</td>
</tr>
<tr>
    <td>工作频率</td><td>105±5kHz</td>
</tr>
<tr>
    <td>电源芯片</td><td>XL6008</td>
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
    <td>设置雾化器工作状态<br>打开：开始雾化<br>关闭：关闭雾化</td><td>（2个参数）端口、状态</td><td><img src="docs/electronic_modules/rj11/atomizer_module/20200302-162529.png"></td>
</tr>
</table>

### **3.2-文本代码编程**