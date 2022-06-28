<div align=center>
<h1 class="text-center">6路舵机驱动模块</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/rj11/six_servo_driver_module/six_servo_driver_module.png" width=50%>
</div>

<p style="white-space: normal;">
    <span style="font-size: 20px; font-family: 宋体, SimSun;">&nbsp; &nbsp;6路舵机驱动模块内置<strong><span style="background-color: rgb(255, 255, 0);">大功率DCDC降压模组</span></strong>，可以实现<span style="background-color: rgb(255, 255, 0);"><strong>10A</strong></span>电流输出，可以同时带动6个PWM舵机，或者少数功率更大的PWM舵机。内置MCU，通过1个PORT口即可控制，同时也能控制WS2812RGB灯条，实现最多6条各30个灯的灯条一起点亮，也可以只点亮任意数量的灯。</span>
</p>
<p style="white-space: normal;">
    <span style="font-size: 20px; font-family: 宋体, SimSun;">&nbsp; &nbsp;灯条和舵机混合控制也是可以的，模块需要单独供电。</span>
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
    <td>工作电压</td><td>DC 5V</td>
</tr>
<tr>
    <td>接口类型</td><td>RJ11</td>
</tr>
<tr>
    <td>通信方式</td><td>WM单总线</td>
</tr>
<tr>
    <td>输入电压</td><td>DC 6-12V</td>
</tr>
<tr>
    <td>输出电压</td><td>5V</td>
</tr>
<tr>
    <td>输出电流</td><td>Max 10A</td>
</tr>
<tr>
    <td>通道个数</td><td>6个</td>
</tr>
<tr>
    <td>可控设备</td><td>舵机、RGB灯条</td>
</tr>
<tr>
    <td>拨动开关</td><td>1个</td>
</tr>
<tr>
    <td>电源指示灯</td><td>2个</td>
</tr>
<tr>
    <td>模块尺寸</td><td>88mm*40mm(长*宽)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>控制舵机转动角度，角度范围是0-180度。<br>其它可选参数为模块连接主控板的端口号和模块上第几个舵机。</td><td>（3个参数）端口、索引、角度</td><td><img src="docs/electronic_modules/rj11/six_servo_driver_module/img_1.png"></td>
</tr>
<tr>
    <td>控制灯条的颜色，2个语句块效果一样，只是一个填RGB值，一个直接选颜色。<br>当索引为0时表示整个灯条都颜色同一个颜色，1-30代表具体哪个灯。</td><td>（4个参数）端口、接口索引、灯索引、颜色组合</td><td><img src="docs/electronic_modules/rj11/six_servo_driver_module/img_2.png"></td>
</tr>
</table>

### **3.2-文本代码编程**

## **4-注意事项**

> [!Note]
> <ul class=" list-paddingleft-2" style="list-style-type: disc;">
    <li>
        <p>
            <strong><span style="font-size: 20px; color: rgb(255, 0, 0);"><span style="font-size: 20px; font-family: 宋体;">模块需要单独供电，控制端和电机端的电是隔离的，拨动开关只能控制外接电源，不能关闭</span>RJ11<span style="font-size: 20px; font-family: 宋体;">控制端的电源。</span></span></strong>
        </p>
    </li>
    <li>
        <p>
            <strong><span style="font-family: 宋体; font-size: 20px; color: rgb(255, 0, 0);">本模块元器件比较密集，注意要防止螺丝等导电物体掉落其上，导致短路。</span></strong>
        </p>
    </li>
    <li>
        <p>
            <strong><span style="font-family: 宋体; font-size: 20px; color: rgb(255, 0, 0);">电源的供电功率要大于用电功率的总数（舵机按堵转功率算），这样才不会触发电池的过流保护或者损坏电池。</span></strong>
        </p>
    </li>
</ul>