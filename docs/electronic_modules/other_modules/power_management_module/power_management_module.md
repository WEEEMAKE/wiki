<div align=center>
<h1 class="text-center">电源管理模块</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/other_modules/power_management_module/power_management_module.png" width=30%>
</div>

<p>
    <span style="font-family: 宋体, SimSun; font-size: 20px;">&nbsp; &nbsp;本模块为比赛专用模块，用于电源控制。模块把锂电池的电分成几个部分，用于给主控、电机驱动模块等电路板供电。另外模块上集成mcu，用于计时和检测击打情况，当被击打或者比赛时间结束时，自动关闭给主控、电机等的供电，实现比赛自动停止。</span>
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
    <td>电源输出电压</td><td>DC 6-12V</td>
</tr>
<tr>
    <td>拨动开关</td><td>1个</td>
</tr>
<tr>
    <td>电源指示灯</td><td>3个</td>
</tr>
<tr>
    <td>RGB灯</td><td>1个</td>
</tr>
<tr>
    <td>2位数码管</td><td>1个</td>
</tr>
<tr>
    <td>XT60接口</td><td>1个</td>
</tr>
<tr>
    <td>XT30接口</td><td>4个</td>
</tr>
<tr>
    <td>DC-007B接口</td><td>2个</td>
</tr>
<tr>
    <td>KF2510接口</td><td>4个</td>
</tr>
<tr>
    <td>功能按键</td><td>2个</td>
</tr>
<tr>
    <td>模块尺寸</td><td>100mm*68mm(长*宽)</td>
</tr>
</table>

## **3-使用指南**

<div align=center>
<img src="docs/electronic_modules/other_modules/power_management_module/img.png" width="60%">
</div>

<p dir="ltr">
    <span style="font-size: 20px; font-family: 宋体, SimSun;"><span style="font-size: 20px;"><span style="font-family: 宋体, SimSun; font-size: 20px;">&nbsp;&nbsp;</span>当给模块最左侧的</span>XT60<span style="font-size: 20px;">接口处插上电池后，拨动开关拨至</span>ON<span style="font-size: 20px;">处，此时模块</span>5V<span style="font-size: 20px;">控制端通电，右侧电源指示灯亮。</span></span>
</p>
<p dir="ltr">
    <span style="font-size: 20px;"><font face="宋体, SimSun">&nbsp;&nbsp;</font></span><span style="font-size: 20px; font-family: 宋体;">板上有</span><span style="font-family: 宋体, SimSun; font-size: 20px;">2</span><span style="font-size: 20px; font-family: 宋体;">个按键，一个是控制自动赛一个是控制手动赛，按下任意按键后电源接口通电，左侧上下</span><span style="font-family: 宋体, SimSun; font-size: 20px;">2</span><span style="font-size: 20px; font-family: 宋体;">个电源指示灯亮，同时数码管显示剩余时间，</span><span style="font-family: 宋体, SimSun; font-size: 20px;">RGB</span><span style="font-size: 20px; font-family: 宋体;">灯变绿色。同时按下</span><span style="font-family: 宋体, SimSun; font-size: 20px;">2</span><span style="font-size: 20px; font-family: 宋体;">个按键为调试模块，不受时间和击打模块影响。(<strong><span style="font-size: 20px; font-family: 宋体; background-color: rgb(255, 255, 0);">这里按键按下持续时间为0.5秒以上</span></strong>)</span>
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 20px;"><span style="font-family: 宋体, SimSun;"><span style="font-family: 宋体, SimSun; font-size: 20px;">&nbsp;&nbsp;</span>4</span><span style="font-family: 宋体;">个黄色的</span><span style="font-family: 宋体, SimSun;">XT30</span><span style="font-family: 宋体;">接口主要给</span><span style="font-family: 宋体, SimSun;">36</span><span style="font-family: 宋体;">编码电机驱动模块供电，</span><span style="font-family: 宋体, SimSun;">2</span><span style="font-family: 宋体;">个金属的</span><span style="font-family: 宋体, SimSun;">DC007B</span><span style="font-family: 宋体;">接口主要给主控板以及舵机驱动板供电。这几个供电接口插上任意一个都可以，没有区别，这</span><span style="font-family: 宋体, SimSun;">6</span><span style="font-family: 宋体;">个接口上的电压基本等同于电池电压。</span></span>
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 20px;"><span style="font-family: 宋体;"><span style="font-family: 宋体, SimSun; font-size: 20px;">&nbsp;&nbsp;</span>模块有</span><span style="font-family: 宋体, SimSun;">4</span><span style="font-family: 宋体;">个击打模块接口，为白色的</span><span style="font-family: 宋体, SimSun;">KF2510</span><span style="font-family: 宋体;">接口，这几个接口可以任意接击打模块（任意几个都可以），只要其中一个击打模块受到击打，即可触发（<strong style="font-family: 宋体; font-size: 20px; white-space: normal;"><span style="background-color: rgb(255, 255, 0);">当为手动模式时才会被触发</span></strong>）。接口电压为</span><span style="font-family: 宋体, SimSun;">DC5V</span><span style="font-family: 宋体;">。</span></span>
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 20px;"><span style="font-family: 宋体, SimSun;"><span style="font-family: 宋体, SimSun; font-size: 20px;">&nbsp;&nbsp;</span>RJ11</span><span style="font-family: 宋体;">座子为</span><span style="font-family: 宋体, SimSun;">DC5V</span><span style="font-family: 宋体;">的供电接口，没有通讯功能，可以用于对外输出电流，主要为主控板提供额外的</span><span style="font-family: 宋体, SimSun;">5V</span><span style="font-family: 宋体;">供电，目的是被击打或者部分比赛结束时主控不掉电（此时只是电机断电了），避免主控、蓝牙重启出错，影响比赛。通过</span><span style="font-family: 宋体, SimSun;">RJ11</span><span style="font-family: 宋体;">电话线连接主控板上任意一个</span><span style="font-family: 宋体, SimSun;">RJ11</span><span style="font-family: 宋体;">座即可供电。</span></span>
</p>

> [!Tip]
> <p dir="ltr">
    <span style="font-family: 宋体; font-size: 20px;">本模块无需编程。</span>
</p>

## **4-注意事项**

> [!Note]
> <p dir="ltr">
    <strong><span style="font-family: 宋体; font-size: 20px;"><span style="font-family: 宋体;">&nbsp;&nbsp;由于导通电流较大，本模块没有过流保护，通电情况下，注意接口<span style="font-family: 宋体; color: red;">不要短路</span>，特别是</span><span style="font-family: Calibri, sans-serif;">XT30</span><span style="font-family: 宋体;">接口和</span><span style="font-family: Calibri, sans-serif;">KF2510</span><span style="font-family: 宋体;">接口，针脚均暴露在外，要防止螺丝等导电物体掉落。</span></span></strong>
</p>