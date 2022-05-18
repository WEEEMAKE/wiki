<div align=center>
<h1 class="text-center">MP3模块</h1>
</div>

## **1-模块介绍**

<div align=center>
<img src="docs/electronic_modules/rj11/mp3_module/20190511-165917.png">
</div>

<font size=4pt>MP3模块是一个用于控制播放MP3文件的音频播放模块。模块板载了一个0.1W的喇叭，可以直接播放音乐，不需要另外再接喇叭。同时也可以通过插针接口，外接功率更大的喇叭。模块内置4M内存，可以存放少量音频文件，同时也支持TF卡，用户可以存入更多更大的音频文件。</font>

## **2-模块参数**

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
    <td>工作温度</td><td>-40℃~+80℃</td>
</tr>
<tr>
    <td>语音IC</td><td>KT603C</td>
</tr>
<tr>
    <td>板载Flash</td><td>4M</td>
</tr>
<tr>
    <td>USB接口</td><td>USB2.0标准</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

## **3-模块使用**

### **3.1-存入文件**

<font size=4>模块上有一个microUSB接口，通过USB 连接电脑，电脑上会以U盘的形式读出，此时直接往里面放入MP3格式的音频文件就好了。注意，内置的flash卡只有4M大小。更大的文件需要存入TF卡，然后插入模块上面的TF卡槽中去。</font>

### **3.2-测试播放**

<font size=4>用RJ11线连接主控板通电后，模块上L1的指示灯会常亮，此时可以按下模块上的白色按键，如果模块上已经有文件，不需要编程就会立刻播放文件，同时L1的指示灯会闪烁，当播放停止时，常亮。</font>

## **4-编程指南**

### **4.1-图形化编程**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块(各平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>选择MP3文件播放来源：板载FLASH或TF卡</td><td>（1个参数）端口</td><td><img src="docs/electronic_modules/rj11/mp3_module/20190510-122341.png"></img></td>
</tr>
<tr>
    <td>设置播放音量</td><td>2个参数）端口、播放音量值（0~25）</td><td><img src="docs/electronic_modules/rj11/mp3_module/20190510-122433.png"></img></td>
</tr>
<tr>
    <td>指定播放第几首</td><td>（2个参数）端口、播放音量值（1~3000）</td><td><img src="docs/electronic_modules/rj11/mp3_module/20190510-122547.png"></img></td>
</tr>
<tr>
    <td>恢复播放</td><td>（1个参数）端口</td><td><img src="docs/electronic_modules/rj11/mp3_module/20190510-122625.png"></img></td>
</tr>
<tr>
    <td>暂停播放</td><td>（1个参数）端口</td><td><img src="docs/electronic_modules/rj11/mp3_module/20190510-122653.png"></img></td>
</tr>
<tr>
    <td>上一首</td><td>（1个参数）端口</td><td><img src="docs/electronic_modules/rj11/mp3_module/20190510-122719.png"></img></td>
</tr>
<tr>
    <td>下一首</td><td>（1个参数）端口</td><td><img src="docs/electronic_modules/rj11/mp3_module/20190510-122845.png"></img></td>
</tr>
<tr>
    <td>判断当前曲目是否播放完毕</td><td>（1个参数）端口</td><td><img src="docs/electronic_modules/rj11/mp3_module/20190510-122927.png"></img></td>
</tr>
</table>

### **4.2-文本代码编程**

<!-- tabs:start -->

### **Arduino-IDE编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>头文件</th><td>WeMP3.h</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeMP3</td><td>WeMP3 mp3_A(PORT_A);</td>
</tr>
<tr>
    <th>选择MP3文件播放来源：板载FLASH或TF卡</th><td>void appointDevice(uint8_t devtype);  //2-TF; 4-FLASH</td><td>mp3_A.appointDevice(4);</td>
</tr>
<tr>
    <th>设置播放音量</th><td>void appointVolume(uint8_t num); // 0~22</td><td>mp3_A.appointVolume(22);</td>
</tr>
<tr>
    <th>指定播放第几首</th><td>void appointMusic(uint16_t num);</td><td>mp3_A.appointMusic(1);</td>
</tr>
<tr>
    <th>恢复播放</th><td>void play(void);</td><td>mp3_A.play();</td>
</tr>
<tr>
    <th>暂停播放</th><td>void pause(void);</td><td>mp3_A.pause();</td>
</tr>
<tr>
    <th>上一首</th><td>void prevMusic(void);</td><td>mp3_A.prevMusic();</td>
</tr>
<tr>
    <th>下一首</th><td>void nextMusic(void);</td><td>mp3_A.nextMusic();</td>
</tr>
<tr>
    <th>判断当前曲目是否播放完毕</th><td>uint8_t isOver(void);</td><td>mp3_A.isOver();</td>
</tr>
</table>

> <font size=4 >详情链接 **→** [MP3模块Arduino库-API头文件-WeMP3.h](https://github.com/WEEEMAKE/Weeemake_Libraries_for_Arduino/blob/master/Weeemake/src/WeMP3.h)</font>

### **Micropython-micro:bit-v1编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from elfshield import *</th><th>调用示例</th>
</tr>
<tr>
    <th>选择MP3文件播放来源：板载FLASH或TF卡</th><td>mp3_setDevice(port, index)</td><td>mp3_setDevice(PORT_A, 4)</td>
</tr>
<tr>
    <th>设置播放音量</th><td>mp3_setVolume(port, volume)</td><td>mp3_setVolume(PORT_A, 22)</td>
</tr>
<tr>
    <th>指定播放第几首</th><td>mp3_playMusic(port, index)</td><td>mp3_playMusic(PORT_A, 1)</td>
</tr>
<tr>
    <th>恢复播放</th><td>mp3_play(port)</td><td>mp3_play(PORT_A)</td>
</tr>
<tr>
    <th>暂停播放</th><td>mp3_pause(port)</td><td>mp3_pause(PORT_A)</td>
</tr>
<tr>
    <th>上一首</th><td>mp3_prevMusic(port)</td><td>mp3_prevMusic(PORT_A)</td>
</tr>
<tr>
    <th>下一首</th><td>mp3_nextMusic(port)</td><td>mp3_nextMusic(PORT_A)</td>
</tr>
<tr>
    <th>判断当前曲目是否播放完毕</th><td>mp3_isOver(port)</td><td>mp3_isOver(PORT_A)</td>
</tr>
</table>

### **Micropython-micro:bit-v2/ESP32/mPython/K210编程API**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>导入库</th><td>from WeMP3 import *</th><th>调用示例</th>
</tr>
<tr>
    <th>对象类</th><td>WeMP3</td><td>mp3_A = WeMP3(PORT_A)</td>
</tr>
<tr>
    <th>选择MP3文件播放来源：板载FLASH或TF卡</th><td>appointDevice(index)</td><td>mp3_A.appointDevice(4)</td>
</tr>
<tr>
    <th>设置播放音量</th><td>appointVolume(volume)</td><td>mp3_A.appointVolume(22)</td>
</tr>
<tr>
    <th>指定播放第几首</th><td>appointMusic(index)</td><td>mp3_A.appointMusic(1)</td>
</tr>
<tr>
    <th>恢复播放</th><td>play()</td><td>mp3_A.play()</td>
</tr>
<tr>
    <th>暂停播放</th><td>pause()</td><td>mp3_A.pause()</td>
</tr>
<tr>
    <th>上一首</th><td>prevMusic()</td><td>mp3_A.prevMusic()</td>
</tr>
<tr>
    <th>下一首</th><td>nextMusic()</td><td>mp3_A.nextMusic()</td>
</tr>
<tr>
    <th>判断当前曲目是否播放完毕</th><td>isOver()</td><td>mp3_A.isOver()</td>
</tr>
</table>

> [!NOTE]
> - <font size=5 >PORT_X的引用需要导入库：</font><font size=5 color=green >from WePort import *</font>

<!-- tabs:end -->

### **4.3-模块入手自测**

<font size=4 >模块上手使用，遇到问题时，可用WeeeCode编程测试，测试代码如下：</font>

<div align=center>
<img src=""></img>
</div>

> <font size=4 >代码下载 **→** <a href = "docs\electronic_modules\rj11\touch_sensor\单路触摸传感器测试代码.sb3">MP3模块测试代码.sb3</a></font>

<!-- tabs:start -->

### **使用Arduino-C/C++编程的主控**

<font size=5>MP3模块支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

### **使用Micropython编程的主控**

<font size=5>MP3模块支持在线调试，可使用<font size=5 color=red>在线调试方式</font>测试该模块，测试现象如下：</font>

<!-- tabs:end -->

## **5-外接喇叭**

<font size=4>如果板载喇叭的音量和声音品质不能满足要求，可以通过按键旁边的2Pin插针来扩展喇叭，建议接入3W以内的喇叭。工作时外接喇叭和板载喇叭会同时响。</font>

> [!Note]
> <font size=4><b>只有老版V1.0预留了外接喇叭的2Pin插针，之后的新版V1.1已去掉该接口。</b></font>

## **6-注意事项**
<b>

> [!Note]
> - <font size=4 color=red>模块只支持MP3格式;</font>
> - <font size=4>曲目排序会按照存入Flash或TF卡先后顺序排列的，即最先存入的曲目为第1首，按照存入先后顺序依次往后排序；</font>
> - <font size=4>编程时，注意循环条件中极短时间内重复调用播放歌曲指令，这样会导致歌曲播放不出，最好加入播放歌曲时间长度的延迟；</font>
> - <font size=4>外接喇叭时，要注意模块散热，不能使模块过热；</font>
> - <font size=4>模块不要经常处于最大音量，以防减少喇叭寿命；</font>
> - <font size=4 color=red>该模块属于较耗电模块，使用时最好外接电源。</font>

</b>
