<div align=center>
<h1 class="text-center">多路巡线传感器</h1>
</div>

## **1-简要概述**
<div align=center>
<img src="docs/electronic_modules/rj11/multiple_linefollower/multiple_linefollower.png" width=30%>
</div>

<font size=4>本模块采用5个抗干扰红外截止型照度传感器，灵敏度高，线性好，温度稳定性好，内置光学滤镜，可以有效滤除红外光的干扰。相比于红外对管的巡线传感器，本模块可以用于室外或者室内靠近阳光的地方，也能较好巡线。内置5个白色LED灯用于照明，内置mcu用于快速检测，内置5个蓝色LED灯用于提示黑白线，内置一个可调电阻，方便用户直接调试阈值。本模块采用WM单总线通讯，可以反馈5个模拟值，也可以反馈5个高低值。</font>


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
    <td>光照传感器</td><td>5个</td>
</tr>
<tr>
    <td>照明灯</td><td>5个</td>
</tr>
<tr>
    <td>黑白指示灯</td><td>5个</td>
</tr>
<tr>
    <td>可调电阻</td><td>1个</td>
</tr>
<tr>
    <td>模块尺寸</td><td>100mm*62mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-使用指南**

<font size=4>模块安装平行于地面，距离地面高度最好1-2CM，也可以根据现场调整到最灵敏的高度（黑白线数值相差最大）。模块插上RJ11线通电后即可开启工作，可以直接读取5路巡线的模拟数值，然后程序自行判断，也可以读取5路巡线的高低值。这个5个高低值可以通过调节模块上的可调电阻器，来调整比较的阈值，模块上蓝色LED灯也会随之变化，当检测到“白线”时对应的灯亮。</font>

## **4-编程指南**
### **4.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>读取一次多路巡线传感器的值，<br>可以理解为更新一次数据，否则将一直是上一次的数值。<br>更新数据需选择是数字值（0和1）还是模拟值（0-255）。
</td><td>（2个参数）端口、返值数据类型</td><td><img src="docs/electronic_modules/rj11/multiple_linefollower/img.png"></td>
</tr>
<tr>
    <td>返回5个传感器S1-S5其中一个的数值，可以将这个数值打印出来，<br>也可以用于比较。显示的值跟上面语句块选择的是数字值还是模拟值有关。
</td><td>（2个参数）端口、探头编号</td><td><img src="docs/electronic_modules/rj11/multiple_linefollower/img_1.png"></td>
</tr>
<tr>
    <td>打开或关闭模块上用于照明的白色LED灯，根据现场光照条件，<br>用户可以自行决定是否打开。模块默认打开。
</td><td>（2个参数）端口、探头编号</td><td><img src="docs/electronic_modules/rj11/multiple_linefollower/img_2.png"></td>
</tr>
</table>

## **5-注意事项**
> [!NOTE]
> <font size=5>传感器虽然灵敏度较高，但只检测灰度值，对于灰度对比相差大的颜色能较好区别，对于灰度对比不大（可能看起来颜色差别比较大）的场景，则不能替代颜色传感器用于比较。</font>
