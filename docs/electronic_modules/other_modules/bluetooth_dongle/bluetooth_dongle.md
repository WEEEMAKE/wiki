<div align=center>
<h1 class="text-center">蓝牙Dongle</h1>
</div>

## **1-简要介绍**

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;本蓝牙dongle模块用于连接电脑和weeeemake的蓝牙设备，包括主控板上的蓝牙模块和蓝牙手柄。该模块连接稳定，传输距离远，可以用于传输数据和下载程序用。</span>
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;模块外观：</span>
</p>
<p>
    <br/>
</p>

<div align=center>
<img src="docs/electronic_modules/other_modules/bluetooth_dongle/20200306-173037.png">
</div>

## **2-参数介绍**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>项</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压</td><td>DC 5V</td>
</tr>
<tr>
    <td>蓝牙芯片</td><td>CYW20707（双模）</td>
</tr>
<tr>
    <td>USB串口芯片</td><td>CH340</td>
</tr>
<tr>
    <td>默认波特率</td><td>115200</td>
</tr>
<tr>
    <td>工作频率</td><td>2.4G</td>
</tr>
<tr>
    <td>发射功率</td><td>4dBm</td>
</tr>
<tr>
    <td>数据速率-最大值</td><td>3Mbps GFSK</td>
</tr>
<tr>
    <td>调制/协议</td><td>蓝牙2.1, SPP/蓝牙低功耗, BLE4.1</td>
</tr>
<tr>
    <td>灵敏度</td><td>-98dB</td>
</tr>
<tr>
    <td>调制/协议</td><td>蓝牙2.1, SPP/蓝牙低功耗, BLE4.1</td>
</tr>
<tr>
    <td>灵敏度</td><td>-98dB</td>
</tr>
<tr>
    <td>工作温度范围</td><td>-20℃~+70℃</td>
</tr>
<tr>
    <td>存储温度</td><td>-40℃~+125℃</td>
</tr>
<tr>
    <td>传输距离</td><td>0~40m（空旷地带）</td>
</tr>
</table>

## **3-使用指南**

<ul class=" list-paddingleft-2" style="list-style-type: disc;">
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;">模块插上电脑的USB接口后，一般会自动安装CH340的驱动，如果安装不成功，也可以手动安装。</span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;">打开串口助手后，波特率设置为115200，数据位8，校验无，停止位1。</span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;">当模块通电后，模块上有个蓝色LED灯会闪烁，当蓝牙连接成功后，会常亮。</span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;">如果之前没有连接过蓝牙，可以按压模块上闪灯部位配对按钮，此时蓝色led灯快闪，模块进入配对模式，把weeemake的蓝牙模块靠近此dongle，会自动连接。连接成功后常亮。</span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;">如果需要重新连接，按照上一步的方法，连接即可。每次上电，dongle会记住上一次配对的蓝牙，只要此蓝牙处于未连接状态，就会自动连接，不需要重新配对。</span>
        </p>
    </li>
</ul>