<div align=center>
<h1 class="text-center">蓝牙手柄</h1>
</div>

## **1-简要介绍**

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;本手柄采用蓝牙连接，传输数据稳定可靠，不易断开，并采用游戏手柄设计，上手更容易，体验更好。此手柄是主从一体设计，既可以连接weeemake的蓝牙模块，控制小车机器人运动，也可以和weeemake蓝牙dongle相连，与电脑通讯，用于scratch编程和学习。内置锂电池包，无需频繁更换干电池，电量指示灯和蓝牙指示灯，方便用户查看电量情况和连接情况。</span>
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;手柄外观及按位介绍：</span>
</p>
<p>
    <br/>
</p>

<div align=center>
<img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-153848.png"><br>
<img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-154500.png">
</div>

## **2-参数介绍**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压</td><td>DC 3.7V(内置锂电池包 550mAh)</td>
</tr>
<tr>
    <td>充电电压</td><td>USB 标准5V</td>
</tr>
<tr>
    <td>工作电流</td><td>小于40mA</td>
</tr>
<tr>
    <td>蓝牙版本</td><td>4.1</td>
</tr>
<tr>
    <td>蓝牙连接指示灯</td><td>蓝色LED</td>
</tr>
<tr>
    <td>电量指示灯</td><td>红色LED灯*3</td>
</tr>
<tr>
    <td>收发距离</td><td>20米(空旷)</td>
</tr>
<tr>
    <td>摇杆数量</td><td>2个</td>
</tr>
<tr>
    <td>按键数量</td><td>18个</td>
</tr>
</table>

## **3-使用指南**

### **3.1-手柄连接说明**

<!-- tabs:start -->

#### **蓝牙手柄+蓝牙模块**

<div align=center>
<img src="docs/electronic_modules/other_modules/bluetooth_controller/490466B7-6C6C-43e7-BAB9-AD69E70940D4.png">
</div>

> [!Note]
> <p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;"><b>蓝牙手柄连接蓝牙模块，蓝牙手柄为主机，蓝牙模块为从机。</b></span>
</p>

#### **蓝牙手柄+蓝牙Dongle（蓝牙适配器）**

<div align=center>
<img src="docs/electronic_modules/other_modules/bluetooth_controller/8DD5A9B2-F89B-4ed6-9CFF-47A811074BD4.png">
</div>

> [!Note]
> <p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;"><b>蓝牙模块连接蓝牙Dongle时，蓝牙手柄为从机，蓝牙Dongle为主机。</b></span>
</p>

<!-- tabs:end -->

### **3.2-手柄使用说明**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>项</th><th>值/描述</th>
</tr>
<tr>
    <td rowspan="2" colspan="1">开机/关机</td><td>按住 <img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-164119.png">(HOME) 键5秒钟，手柄开机。红色电量指示灯亮起，蓝色蓝牙状态灯闪烁。若要关机，亦是长按HOME键5秒钟。</td>
</tr>
<tr>
    <td align="">手柄在开机后，存在两种自动关机的情况：(1)蓝牙未连接状态下，手柄无操作，50秒后自动关机;(2)蓝牙连接状态下，手柄无操作，5分钟后自动关机。</td>
</tr>
<tr>
    <td>连接蓝牙</td><td>手柄开机后默认进入主机状态，会自动搜索并连接上一次连接过的蓝牙模块。如果需要连接新的蓝牙模块，需要同时按住<img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-164119.png">+<img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-164141.png">后3秒，手柄进入搜索新蓝牙模式，会自动连接当时信号最强的蓝牙模块。所以最好把手柄靠近想要连接的蓝牙模块，防止连接错误。</td>
</tr>
<tr>
    <td>连接Dongle</td><td>开机后，同时按住<img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-164119.png">+<img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-164155.png">后3秒，手柄进入从机模式，等待Dongle连接。此时dongle也需要进入配对模式（按住dongle上的按键），把手柄靠近dongle，几秒后会自动连接。此时，通过电脑串口软件就可以看到手柄发送的原始数据。连接一次后，Dongle会记住手柄的信息，下次连接这个手柄时，不需要再按键，但手柄每次开机都需要按键进入从机模式。</td>
</tr>
<tr>
    <td>指示灯</td><td>手柄上共有4个LED灯，1个蓝牙状态指示灯-蓝色，3个电量指示灯-红色。当手柄处于主机未连接时，1Hz慢速闪烁；当处于主动搜索蓝牙时，10Hz快闪；当处于从机被dongle连时，5Hz中速闪烁。只要连接成功，常亮。3个电量指示灯，显示电量多少，以及充电状态。</td>
</tr>
<tr>
    <td>充电说明</td><td>充电说明：当手柄需要充电时，插上microUSB线就可以充电，此microUSB只能用于充电功能，不能数据通讯。注意及时充电，最好当指示灯只有2格电时及时补充，当下降到1格电时电池有可能会进入到过放保护。</td>
</tr>
<tr>
    <td>摇杆出厂校验</td><td>当摇杆使用值出现异常时，有可能是摇杆未做出厂校验，可使用以下方法校验：<br>

同时按住<img src="docs/electronic_modules/other_modules/bluetooth_controller/20200617-155749.png">+<img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-164155.png">+<img src="docs/electronic_modules/other_modules/bluetooth_controller/20190807-164119.png">进入校验模式，蓝灯快闪，此时最大摇动摇杆，蓝灯再次慢闪时，结束校验。</td>
</tr>
</table>

### **3.3-按键/摇杆编程宏定义**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>宏定义名</th><th>值</th><th>图形化编程表示</th><th>描述</th>
</tr>
<tr>
    <td>WeJOYSTICK_LY</td><td>1</td><td>——</td><td>左摇杆Y轴</td>
</tr>
<tr>
    <td>WeJOYSTICK_LX</td><td>2</td><td>——</td><td>左摇杆X轴</td>
</tr>
<tr>
    <td>WeJOYSTICK_RY</td><td>3</td><td>——</td><td>右摇杆Y轴</td>
</tr>
<tr>
    <td>WeJOYSTICK_RX</td><td>4</td><td>——</td><td>右摇杆X轴</td>
</tr>
<tr>
    <td>WeBUTTON_ZR</td><td>5</td><td>ZR</td><td>按键ZR</td>
</tr>
<tr>
    <td>WeBUTTON_R</td><td>6</td><td>R</td><td>按键R</td>
</tr>
<tr>
    <td>WeBUTTON_ZL</td><td>7</td><td>ZL</td><td>按键ZL</td>
</tr>
<tr>
    <td>WeBUTTON_L</td><td>8</td><td>L</td><td>按键L</td>
</tr>
<tr>
    <td>WeBUTTON_HOME</td><td>9</td><td>HOME</td><td>按键HOME</td>
</tr>
<tr>
    <td>WeBUTTON_BL</td><td>10</td><td>BL</td><td>左摇杆按键</td>
</tr>
<tr>
    <td>WeBUTTON_Y</td><td>11</td><td>Y</td><td>按键Y</td>
</tr>
<tr>
    <td>WeBUTTON_B</td><td>12</td><td>B</td><td>按键B</td>
</tr>
<tr>
    <td>WeBUTTON_A</td><td>13</td><td>A</td><td>按键A</td>
</tr>
<tr>
    <td>WeBUTTON_X</td><td>14</td><td>X</td><td>按键X</td>
</tr>
<tr>
    <td>WeBUTTON_PLUS</td><td>15</td><td>PLUS</td><td>按键+</td>
</tr>
<tr>
    <td>WeBUTTON_MODE</td><td>16</td><td>MODE</td><td>按键MODE</td>
</tr>
<tr>
    <td>WeBUTTON_UP</td><td>17</td><td>UP</td><td>十字按键 ↑</td>
</tr>
<tr>
    <td>WeBUTTON_DOWN</td><td>18</td><td>DOWN</td><td>十字按键 ↓</td>
</tr>
<tr>
    <td>WeBUTTON_LEFT</td><td>19</td><td>LEFT</td><td>十字按键 ←</td>
</tr>
<tr>
    <td>WeBUTTON_RIGHT</td><td>20</td><td>RIGHT</td><td>十字按键 →</td>
</tr>
<tr>
    <td>WeBUTTON_MINUS</td><td>21</td><td>MINUS</td><td>按键-</td>
</tr>
<tr>
    <td>WeBUTTON_BR</td><td>22</td><td>BR</td><td>右摇杆按键</td>
</tr>
</table>


