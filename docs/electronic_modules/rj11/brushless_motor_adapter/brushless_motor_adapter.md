<div align=center>
<h1 class="text-center">无刷电机驱动模块</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/rj11/brushless_motor_adapter/brushless_motor_adapter.png" width=40%>
</div>

<p style="text-align: justify; text-indent: 0em;">
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;本模块为比赛专用模块，为驱动2个由无刷电机组成的击球模块而设计。</span>
</p>
<p style="text-align: justify; text-indent: 0em;">
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;本模块主要由一个电源输入接口两个电源输出接口和2个无刷电机信号接口组成，2个无刷电机的控制信号由RJ11接口输入。</span>
</p>
<p style="text-align: justify; text-indent: 0em;">
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;模块电源由拨动开关控制，用户可以不用频繁拔插电源接口，方便调试。</span>
</p>

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
    <td>模块工作电压</td><td>DC 5V</td>
</tr>
<tr>
    <td>电源输入电压</td><td>DC 6-12V</td>
</tr>
<tr>
    <td>电源控制开关</td><td>1个</td>
</tr>
<tr>
    <td>电源指示灯</td><td>2个</td>
</tr>
<tr>
    <td>控制无刷电机</td><td>2个</td>
</tr>
<tr>
    <td>模块尺寸</td><td>88mm*40mm(长*宽)</td>
</tr>
</table>

## **3-使用指南**

<p>
    <span style="font-size: 24px;"><span style="font-family: 宋体;">&nbsp; &nbsp;本模块用拨动开关控制无刷电机电调的电源，电源输入接口</span>XT60<span style="font-family: 宋体;">为，输入也是</span>XT60<span style="font-family: 宋体;">，先把电调的电源和控制线接到模块上，注意控制线的不要接反了，一般是红色</span>VCC<span style="font-family: 宋体;">，棕色</span>/<span style="font-family: 宋体;">黑色为</span>GND<span style="font-family: 宋体;">，黄色</span>/<span style="font-family: 宋体;">白色为信号。</span></span>
</p>
<p>
    <span style="font-size: 24px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; RJ11<span style="font-family: 宋体;">的控制信号给到</span>2<span style="font-family: 宋体;">个无刷电机控制端是一样的，所以</span>2<span style="font-family: 宋体;">个电机是一起运动一起停。</span></span>
</p>
<p>
    <span style="font-family: 宋体; font-size: 24px;">模块编程：</span>
</p>

> [!Note]
> <p>
    <span style="font-family: 宋体; font-size: 24px;"><b>这里所提的编程针对的是具有电调的无刷电机。</b></span>
</p>



## **4-注意事项**

> [!Attention]
> <p style="text-align: justify; text-indent: 0em;">
    <span style="font-size: 24px; color: rgb(255, 0, 0);"><span style="font-size: 24px; font-family: 宋体;"><b>注意电机的功率不能太大，电流最好不要超过</span><span style="font-size: 24px; font-family: Calibri, sans-serif;">30A</span><span style="font-size: 24px; font-family: 宋体;">，长时间高负荷工作时注意</span><span style="font-size: 24px; font-family: Calibri, sans-serif;">PCB</span><span style="font-size: 24px; font-family: 宋体;">板的发热情况，做好散热。</b></span><span style="font-size: 24px; font-family: 宋体, SimSun;"></span></span>
</p>