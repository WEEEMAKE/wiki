<div align=center>
<h1 class="text-center">大功率编码电机驱动模块</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/rj11/36encoder_motor_driver/img.png">
</div>

<p style="text-indent:28px">
    <span style="font-size: 20px;"><span style="font-family: 宋体;">&nbsp;本模块采用大功率</span>MOS<span style="font-family: 宋体;">管组成的电机驱动电路，能同时驱动</span>2<span style="font-family: 宋体;">路直流电机和编码电机，支持正反转和调速。模块采用</span>WM<span style="font-family: 宋体;">单总线控制，内置</span>MCU<span style="font-family: 宋体;">控制，需要外接电源，支持单个电机持续</span>5A<span style="font-family: 宋体;">，瞬时</span>10A<span style="font-family: 宋体;">的功率，拥有过流保护，电机转动指示灯。编码电机支持</span>AB<span style="font-family: 宋体;">两相检测，能准确的控制正转、反转的速度、方向、位移量，内置</span>PID<span style="font-family: 宋体;">算法，能更稳定的运动到指定位置。</span>PCB<span style="font-family: 宋体;">板采用镀金工艺，使模块更美观耐用<span style="font-family: 宋体;"></span>。</span></span>
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
    <td>电机电压</td><td>DC 6-12V</td>
</tr>
<tr>
    <td>工作电流</td><td>5A</td>
</tr>
<tr>
    <td>保护电流</td><td>10A</td>
</tr>
<tr>
    <td>编码电机接口</td><td>2个</td>
</tr>
<tr>
    <td>直流电机接口</td><td>2个</td>
</tr>
<tr>
    <td>电源接口</td><td>1个</td>
</tr>

<tr>
    <td>运行状态指示灯</td><td>4个</td>
</tr>
<tr>
    <td>模块尺寸</td><td>88mm*40mm(长*宽)</td>
</tr>
</table>

## **3-编程指南**

> [!Tip]
> <font size=4><b>插上RJ11线通电后PWR红色指示灯会亮，这时可以程序发送控制指令，但只有电源接口（XT30）通电后，电机运行指示灯才会亮，电机才会开始转动。</b></font>

### **3.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>脉冲计数清零，注意模块上电时的脉冲计数是为0的。<br>可选参数为模块连接主控板的端口号和电机（M1或M2）。</td><td>（2个参数）端口、接口索引</td><td><img src="docs/electronic_modules/rj11/36encoder_motor_driver/img_1.png"></td>
</tr>
<tr>
    <td>使电机按照一定占空比来运行，范围为-255到255，<br>表现为按直流电机方式运动，不检测速度。</td><td>（3个参数）端口、接口索引、速度</td><td><img src="docs/electronic_modules/rj11/36encoder_motor_driver/img_2.png"></td>
</tr>
<tr>
    <td>每100ms转动多少个脉冲，可以换算成电机按照多少速度运行，<br>模块会检测速度，如果电机阻力大速度低了，<br>模块会加大功率，以保证按指定速度运行。<br>脉冲数可以为正整数也可以为负整数和0（停止）。</td><td>（3个参数）端口、接口索引、速度</td><td><img src="docs/electronic_modules/rj11/36encoder_motor_driver/img_3.png"></td>
</tr>
<tr>
    <td>电机以某个速度转动多少个脉冲，<br>可以换算成电机转动多少角度多少圈，到了位置就停止。<br>脉冲数可以为正整数也可以为负整数。<br>0表示不转动。</td><td>（4个参数）端口、接口索引、脉冲数、速度</td><td><img src="docs/electronic_modules/rj11/36encoder_motor_driver/img_4.png"></td>
</tr>
<tr>
    <td>电机转动到第几个脉冲，相对于原点。<br>可以换算成电机转动到多少角度多少圈，<br>脉冲数可以为正整数也可以为负整数。<br>0表示转动到原点。</td><td>（4个参数）端口、接口索引、脉冲、速度</td><td><img src="docs/electronic_modules/rj11/36encoder_motor_driver/img_5.png"></td>
</tr>
<tr>
    <td>获取当前电机的脉冲数，脉冲数可以为正整数也可以为负整数。0表示原点。</td><td>（2个参数）端口、接口索引</td><td><img src="docs/electronic_modules/rj11/36encoder_motor_driver/img_6.png"></td>
</tr>
</table>

### **3.2-文本代码编程**

## **4-注意事项**

> [!Note]
> <ul class=" list-paddingleft-2" style="list-style-type: disc;">
    <li>
        <p>
            <span style="font-family: 宋体, SimSun;"><strong><span style="font-size: 20px; color: rgb(255, 0, 0);">2组电机接口（M1和M2），一个编码电机接口和一个直流电机接口组成一组，每组内的编码电机和直流电机运动方向和速度是一致的，不能单独控制，2个接口是同时通电的。</span></strong></span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-family: 宋体, SimSun;"><strong><span style="font-family: 宋体, SimSun; font-size: 20px; color: rgb(255, 0, 0);">本模块元器件比较密集，注意要防止螺丝等导电物体掉落其上，导致短路。</span></strong></span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-family: 宋体, SimSun;"><strong><span style="font-family: 宋体, SimSun; font-size: 20px; color: rgb(255, 0, 0);">电机电源的供电功率要大于电机的堵转功率，这样才不会触发电池的过流保护或者损坏电池。</span></strong></span>
        </p>
    </li>
</ul>