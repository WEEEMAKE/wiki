#  USB HOST模块

## 1 概述简介

<p class=MsoTitle align=left style='text-align:left;text-indent:36.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:宋体;color:#222222;background:
white'>USB Host</span><span style='font-size:16.0pt;font-family:宋体;color:#222222;
background:white'>模块主要是作为<span lang=EN-US>2.4G</span>手柄的接收器，用于接收<span
lang=EN-US>2.4G</span>无线手柄的信号。此模块目前只能用于<span lang=EN-US>ELF</span>主控板上，有了这个模块就可以用手柄控制机器人了。<span
lang=EN-US><o:p></o:p></span></span></p>


## 2 模块外观

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压</td><td>DC 5V</td>
</tr>
<tr>
    <td>接口类型</td><td>模块插针与ELF主控板适配使用、模块上USB接口用于2.4G手柄接收器</td>
</tr>
<tr>
    <td>通信芯片</td><td>CH375B</td>
</tr>
<tr>
    <td>通信方式</td><td>串口</td>
</tr>
</table>

## 3 接口布局

## 4 使用说明

本模块只能连接在ELF主控板的port5和port6口（占用2个口），或者2560比赛扩展板上的USB host专用接口上。

（此处配图）

插上模块正常通电后，模块上的红色指示灯会亮起。插上2.4G遥控手柄的接收器（USB端）后，运行程序，如果通讯正常，模块上的绿色指示灯会亮起。当绿色指示灯亮起，此时就可以接收手柄信号了。