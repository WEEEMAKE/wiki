<div align=center>
<h1 class="text-center">语音识别传感器V1</h1>
</div>

# 1-模块介绍


<p class=MsoTitle align=left style='text-align:left'><span style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>&nbsp;&nbsp;
<span lang=ZH-CN>本模块是一款非特定人声的语音识别模块，即任何人的声音都可以进行识别和判断，不需要用户事先训练和录音，不需要联网，本地就能识别。以无声调汉语拼音的方式进行匹配识别，同时选择一组最接近当前语音关键词进行输出。关键词可以随时修改，以汉语拼音的形式动态编辑，不同于市面上关键词固定的模块，这样操作更灵活、更方便。</span></span></p>


# 2-参数规格

<div align=center>
<img src="docs\electronic_modules\rj11\speech_recognition_v1\20190803-172740.png">
</div>

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
    <td>工作电压</td><td>DC 5V（内置3.3V电平转换）</td>
</tr>
<tr>
    <td>接口类型</td><td>RJ11</td>
</tr>
<tr>
    <td>通信方式</td><td>WM单总线协议</td>
</tr>
<tr>
    <td>控制芯片</td><td>STC11L08XE</td>
</tr>
<tr>
    <td>识别芯片</td><td>LD3320</td>
</tr>
<tr>
    <td>晶振频率</td><td>22.1184MHz</td>
</tr>
<tr>
    <td>状态指示灯</td><td>当模块识别到语音时，蓝灯状态翻转一次</td>
</tr>
<tr>
    <td>启动指示灯</td><td>当模块正常启动时，绿色LED灯常量</td>
</tr>
<tr>
    <td>模块尺寸</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

# 3-使用指南
## 3.1-模块使用说明

<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>（</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>1<span
lang=ZH-CN>）使用本模块前，必须先输入要识别的关键词，添加关键词以拼音方式输入，例如想添加“<b><span style='background:
yellow'>开灯</span></b>”命令，则输入“</span><b><span style='background:yellow'>kai deng</span></b><span
lang=ZH-CN>”，每个汉字间的拼音用空格隔开。</span></span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>（</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>2<span
lang=ZH-CN>）每个关键词对应一个数字号，当识别到这个关键词时，模块返回对应的数字号。</span></span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>（</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>3<span
lang=ZH-CN>）本模块有</span>2<span lang=ZH-CN>种模式，直接模式和口令模式。直接模式是只要识别到关键词就输出对应数字；口令模式是需要先说出口令词，识别后，再说关键词。</span></span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>（</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>4<span
lang=ZH-CN>）识别原理：当模块检测出一段连续的背景噪音后，认为用户已经在说话了，当检测到有连续的</span>600ms<span
lang=ZH-CN>不说话或者没有声波时，才会给出识别结果。所以，从说话结束到有识别结果，至少需要</span>600ms<span lang=ZH-CN>。</span></span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>（</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>5<span
lang=ZH-CN>）最多可以设置</span>20<span lang=ZH-CN>组候选识别句，每个识别句可以是单字，词组或者短句，长度不超过</span>8<span
lang=ZH-CN>个汉字或者</span>40<span lang=ZH-CN>个字节的拼音串。</span></span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>（</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>6<span
lang=ZH-CN>）本模块只支持中文普通话识别。</span></span></p>
</body></html>

## 3.2-功能模块及WeeeCode图形化编程指南

<html><body>
<p class=MsoNormal style='text-indent:21.0pt'><span style='font-size:16.0pt;
font-family:华文楷体;color:#222222;background:white'>&nbsp;&nbsp;&nbsp; </span><span
lang=ZH-CN style='font-size:16.0pt;color:black;background:white'>该模块支持的图形化编程平台目前有</span><span
style='font-size:16.0pt;color:black;background:white'>WeeeCode 3.0<span
lang=ZH-CN>，其图形化编程指南如下：</span></span></p>

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>选择工作模式</td><td>(2个参数）端口、选择模式</td><td><img src="docs\electronic_modules\rj11\speech_recognition_v1\20190807-112424.png"></img></td>
</tr>
<tr>
    <td>设置需要识别的口令语句</td><td>(2个参数）端口、口令语句</td><td><img src="docs\electronic_modules\rj11\speech_recognition_v1\20190807-112459.png"></img></td>
</tr>
<tr>
    <td>设置需要识别的语句及序号</td><td>(3个参数）端口、语句序号、识别拼音语句</td><td><img src="docs\electronic_modules\rj11\speech_recognition_v1\20190807-112601.png"></img></td>
</tr>
<tr>
    <td><p class=MsoNormal align=center style='text-align:center'><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;'>当识别有效的语句后返回相应的序号（</span><span
  lang=ZH-CN style='font-size:14.0pt;font-family:华文楷体;color:red;background:
  yellow'>备注：</span><span lang=ZH-CN style='font-size:14.0pt;font-family:华文楷体;
  color:red;'>需要新建一个变量来储存该返回值</span><span lang=ZH-CN
  style='font-size:14.0pt;font-family:华文楷体;color:black;'>）</span></p></td><td>(1个参数）端口</td><td><img src="docs\electronic_modules\rj11\speech_recognition_v1\20190807-112638.png"></img></td>
</tr>
</table>

> [!Attention]
> <div>
<div align=center>
<img src="docs/electronic_modules/rj11/speech_recognition_v1/img_5.png">
</div>
<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 此语句块只能是V1.0模块在线模式下使用，用于反馈识别到的字符串（拼音）而不是序号。</span>
</p>
</div>

## 3.3-文本代码编程指南

# 4-技巧提高

<html><body>
<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>1<span
lang=ZH-CN>、如果想提高语音识别的准确度和抗干扰性，可以采用口令模式。给模块或者机器人起一个名字，每次喊它的名字后才能输出控制指令。起名字时需要注意</span>2<span
lang=ZH-CN>点：</span>3-6<span lang=ZH-CN>个字；发音平时不常听到。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>2<span
lang=ZH-CN>、不同的关键词可以对应同一个</span>ID</span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>3<span
lang=ZH-CN>、本模块只支持中文普通话识别，如果需要识别一些简单的外文或者方言发音时，可以用拼音标注的方式来实现。比如：</span>one<span
lang=ZH-CN>（英文）——</span>wan<span lang=ZH-CN>（拼音）、</span>two<span lang=ZH-CN>——</span>tu</span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>4<span
lang=ZH-CN>、识别的效果和一下因素有关，用户可以根据这些方面加以改善：</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; a. <span
lang=ZH-CN>周围环境的声音，也就是噪音越小越好</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; b. <span
lang=ZH-CN>关键词是发音响亮的开口音还是不容易发音的闭口音，一般开口音识别效果好，闭口音需要离模块近。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; c. <span
lang=ZH-CN>关键词之间的差别程度，差别越大，误判越小。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; d. <span
lang=ZH-CN>说话人的发音清晰度、快慢、口语、认真程度。吐词要清楚、不宜过快。</span></span></p>
</body></html>


# 5-注意事项

<html><body>
<p class=MsoTitle><span style='font-size:16.0pt'>1<span lang=ZH-CN>、当识别效果差时，在安静环境下放几秒钟，或者断一下电，重启。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt'>2<span lang=ZH-CN>、有些电脑</span>USB<span
lang=ZH-CN>供电可能不足，请尽量使用外部电源供电。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt'>3<span lang=ZH-CN>、最好不要在比较嘈杂的环境中使用。</span></span></p>
</body></html>