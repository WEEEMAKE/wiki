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
>
> <p>
> <span style="font-family: 宋体; font-size: 24px;"><b>这里所提的编程针对的是具有电调的无刷电机。</b></span>
> </p>

## **4-无刷电机电调介绍**

<div align=center>
<img src="docs/electronic_modules/rj11/brushless_motor_adapter/20221015.jpg" width=40%>
</div>


### 4.1 参数功能

|          |                                                              |
| :------: | :----------------------------------------------------------- |
|   电流   | 持续电流30A，瞬间35A ，40A能持续10秒                         |
| 电压范围 | 4V-16V                                                       |
|   性能   | 转速上限，2极内转高达300000转，12极外转50000转，14极外转42000转<br/>自动油门适应，适合更多遥控设备。<br/>使用BEC，MCU分离电源供应，工作更稳定。 |
| 保护功能 | 安全启动，油门位置不对禁止启动；<br/>温度保护，110度表面温度停机；<br/>失控保护，无信号1秒以后停机。 |
| 外型尺寸 | 32 X 24 X 7 (mm)                                             |

### 4.2 设置方法

第一次使用电调需要识别遥控的最大行程与最小行程，方法如下：

#### 4.2.1 上电现象 

上电后会听到电调发出一段音乐，此后，会有一定频率的嘀声，代表电调正常，等待PWM信号接入。

#### 4.2.2 线路解释

红色正极线：在测试的时候可以接，也可以不接，作用就是给板子供电.<br/>
褐色负极线：所有时候必须都接，因为黄色接收到的PWM信号线需要和同一块板子的地线电压做比较，只有这样电调才能判断信号线的电压.<br/>
黄色信号线：连接板子的定时器PWM输出端口。<br/>

(红色接模块5V 褐色接GND 黄色接SIG）

#### 4.2.3 油门校准

每次上电，电调都需要校准油门。电调频率建议选用500Hz，即占空比下界61%，占空比上界99%的PWM信号。不同的频率上下界需要调整。<br/>
**CCR/ARR=占空比**

#### 4.2.4 校对过程

电调接上电机------电调线接上接收机-----打开遥控器并把油门推到最高点------把电调插上电池-------听声音----音乐(123)-----嘀嘀（油门最高点确认音）----二声过后把油门杆拉到最低点-----听到嘀嘀嘀三声----（油门最低点确认音,2S二声,3S三声）-----OK

> ps: 无刷电调的三条线可以任意接，如果转向不对，把其中的任意两条线对调一下就可以了

## **5-注意事项**

> [!Attention]
> <p style="text-align: justify; text-indent: 0em;">
    <span style="font-size: 24px; color: rgb(255, 0, 0);"><span style="font-size: 24px; font-family: 宋体;"><b>注意电机的功率不能太大，电流最好不要超过</span><span style="font-size: 24px; font-family: Calibri, sans-serif;">30A</span><span style="font-size: 24px; font-family: 宋体;">，长时间高负荷工作时注意</span><span style="font-size: 24px; font-family: Calibri, sans-serif;">PCB</span><span style="font-size: 24px; font-family: 宋体;">板的发热情况，做好散热。</b></span><span style="font-size: 24px; font-family: 宋体, SimSun;"></span></span>
</p>