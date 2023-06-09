<div align=center>
<h1 class="text-center">语音识别传感器V2</h1>
</div>
## **1-简要介绍**

<div align=center>
<img src="docs/electronic_modules/rj11/speech_recognition_v2/img_1.png" width=30%>
</div>
<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 本模块为语音识别传感器V1.0的升级版，和之前版本一样不需要事先训练和录音，不需要联网。不同之处是，V2.0语音识别更加准确，灵敏度更高，并可在轻度嘈杂的环境中很好识别，同时识别后还可以发声，但此版本不支持用户修改识别指令。</span>
</p>
## **2-参数规格**

<div align=center>
<img src="docs/electronic_modules/rj11/speech_recognition_v2/img_2.png">
</div>

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
    <td>识别芯片</td><td>US516</td>
</tr>
<tr>
    <td>拾音器</td><td>咪头1个</td>
</tr>
<tr>
    <td>喇叭接口</td><td>1个(标配8欧0.5W喇叭一个)</td>
</tr>
<tr>
    <td>状态指示灯</td><td>当模块识别到语音时，蓝灯状态翻转一次</td>
</tr>
<tr>
    <td>模块尺寸</td><td>48mm*24mm(长*宽)</td>
</tr>
</table>

## **3-使用指南**

<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 本模块有一个喇叭接口，可以接一个最大4欧2.9W或者8欧1.8W的喇叭，模块上电后和识别到命令词后会有语音提示，当然不接喇叭语音识别也是可以正常工作的。</span>
</p>
<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 模块必须先唤醒后才能识别命令词，唤醒词包括：<b>小美小美|你好小美|叮当象</b>，这3个中的任意一个。唤醒后，可以连续识别命令词，当识别到唤醒词或命令词后15秒内，没有识别到任何命令词，则模块进入睡眠模式，需要重新唤醒。</span>
</p>
<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 图形化编程不同于之前版本，V2.0只有一个语句块，此语句块用于返回识别到的命令词序号。</span>
</p>

<div align=center>
<img src="docs/electronic_modules/rj11/speech_recognition_v2/img_3.png">
</div>

<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 指令表解析：</span>
</p>
<div align=center>
<img src="docs/electronic_modules/rj11/speech_recognition_v2/img_4.png">
</div>

<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 指令对应编码如下：</span>
</p>

<embed class="pdfobject" src="docs/electronic_modules/rj11/speech_recognition_v2/命令词.pdf" style="overflow: auto; width: 100%; height: 40rem;">

<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 这些命令词里面大部分是有喇叭反馈的，有少数没有反馈如：现在温度、现在湿度、土壤湿度、测量距离、检测颜色、检测环境等，这是为了搭配语音合成或者mp3模块来用时避免混音。 另外“增大音量|加大音量”和“减小音量|音量减小”可以控制喇叭的音量。</span>
</p>
<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 以后会用语音识别V2.0来替换V1.0模块，这样会造成一些教材和示例程序会不一样，原理上使用上V2.0会更简单，用户可稍作修改，去除V1.0的设置命令词相关程序，直接用文档中固定的命令词即可。</span>
</p>

## **4-注意事项**

> [!Note]
>
> <div>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; 本模块使用SU-03T语音识别方案，如果用户知道如何生成语音文件及下载，可以用模块上的排母自行更新下载，下载串口采用的是B6和B7，通讯口也是这2个。</span>
</p>
<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; 如果用户没有过这种操作经验，不建议尝试，过程比较麻烦，如果有定制唤醒词和命令词需求的可以找我们。</span>
</p>
</div>