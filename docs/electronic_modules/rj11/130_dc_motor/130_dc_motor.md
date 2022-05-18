<div align=center>
<h1 class="text-center">130直流电机模块</h1>
</div>

## **1-模块介绍**
<div align=center>
<img src="docs/electronic_modules/rj11/130_dc_motor/20200313-164954.png" width=30%>
</div>

<font size=4>130直流电机模块板载固定一个130直流电机，模块会附赠一个泡棉软风扇叶片，可用于制作和风扇相关的作品，如智能风扇、灭火机器人、吹泡泡机等。</font>

## **2-模块介绍**

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
    <td>工作温度</td><td>-10℃~+50℃</td>
</tr>
<tr>
    <td>工作湿度</td><td>5%~85% RH</td>
</tr>
<tr>
    <td>空载转速</td><td>16000±10% RPM</td>
</tr>
<tr>
    <td>指示灯</td><td>2个LED指示旋转方向</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-编程指南**

### **3.1-图形化编程**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块(各平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>设置电机转速</td><td>2个参数）端口、转速（-255~255）</td><td><img src="docs/electronic_modules/rj11/130_dc_motor/20200302-110756.png" width=60%></img></td>
</tr>
</table>

### **3.2-文本代码编程**

<!-- tabs:start -->

### **Arduino-IDE编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>头文件</th><td>We130DCMotor.h</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>We130DCMotor</td><td>We130DCMotor dc130_A(PORT_A);</td>
</tr>
<tr>
    <th>设置电机转速</th><td>void run(int16_t speed);</td><td>dc130_A.run(100);</td>
</tr>
</table>

> <font size=4 >详情链接 **→** [130直流电机模块Arduino库-API头文件-We130DCMotor.h](https://github.com/WEEEMAKE/Weeemake_Libraries_for_Arduino/blob/master/Weeemake/src/We130DCMotor.h)</font>

### **Micropython-micro:bit-v1编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from elfshield import *</th><th>调用示例</th>
</tr>
<tr>
    <th>设置电机转速</th><td>dc130motor_speed(port, speed)</td><td>dc130motor_speed(PORT_A, 100)</td>
</tr>
</table>

### **Micropython-micro:bit-v2/ESP32/mPython/K210编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from We130DCMotor import *</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>We130DCMotor</td><td>dc130_A = We130DCMotor(PORT_A)</td>
</tr>
<tr>
    <th>设置电机转速</th><td>run(speed)</td><td>dc130_A.run(100)</td>
</tr>
</table>

> [!NOTE]
> - <b><font size=4>PORT_X的引用需要导入库：</font><font size=5 color=green >from WePort import *</font></b>

<!-- tabs:end -->

### **3.3-模块入手自测**

## **4-注意事项**

> [!Note]
> <font size=4 color=red><b>不能长时间快速正反转，这样会造成电流过大，发热量大，烧毁模块上的驱动芯片。</b></font>