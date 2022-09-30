<div align=center>
<h1 class="text-center">图像识别传感器V1</h1>
</div>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
  width=799 height=336 id="图片 1" src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-165109.png">



<p class=MsoTitle style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:#222222;background:white'>本图像识别传感器是一款体积小巧，功耗低的初级视觉识别传感器。内置识别程序，所有识别算法都在本地处理，无须联网。具有颜色识别、大小识别、人脸跟踪、形状模糊识别等作用，可以用于跟踪小球、人脸，辨别方位距离，巡线，无人驾驶，自动分拣机等案例。用户可以自由输入想要识别的颜色信息，通过自有的单总线协议，可以和平台任何</span><span
style='font-size:16.0pt;font-family:宋体;color:#222222;background:white'>Arduino<span
lang=ZH-CN>、</span>micro:bit<span lang=ZH-CN>等主控板通讯，可用</span><b>Scratch<span
lang=ZH-CN>、</span>Python<span lang=ZH-CN>、</span>Arduino C++</b><span
lang=ZH-CN>等编程，方便快捷。</span></span></p>

## 2. 参数规格

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>参数</th><th>值/描述</th>
</tr>
<tr>
    <td>工作电压</td><td>DC 5V(内置3.3V电平转换)</td>
</tr>
<tr>
    <td>接口类型</td><td>RJ11</td>
</tr>
    <tr>
    <td>通信方式</td><td>WM单总线</td>
</tr>
    <tr>
    <td>处理器</td><td>STM32高性能处理器,180MHz,ARM Crotex M4内核</td>
</tr>
    <tr>
    <td>摄像头</td><td>30W像素摄像头,视场角66°,最大帧率60fps,具有高灵敏度、镜头失光补偿、饱和度自动调节等功能</td>
</tr>
    <tr>
    <td>状态指示灯</td><td>当摄像头工作时,蓝色LED灯闪烁,识别一次,闪烁一次,不工作时熄灭</td>
</tr>
    <tr>
    <td>复位按键</td><td>当模块工作不正常时，可短按复位处理器</td>
</tr>
    <tr>
    <td>功耗</td><td>120mA~200mA</td>
</tr>
    <tr>
    <td>工作温度</td><td>-20℃~70℃</td>
</tr>
    <tr>
    <td>尺寸大小</td><td>55mm*24mm*18.5mm(长*宽*高)</td>
</tr>
</table>

##  3. 编程指南 

###  3.1. 模块软件功能说明 

<p class=MsoNormal style='margin-left:.5in;text-indent:.5in'><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>本模块内部机器视觉算法，会把处理好的结果反馈回主控，不能传输图片或者视频。有多种输出方式，满足不同应用需求，并支持参数输入和修改。具有自动锁定眼前目标，并跟踪的能力。拥有</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>2<span
lang=ZH-CN>种巡线输出方式，满足不同用户需求。</span></span></p>

<p class=MsoNormal style='margin-left:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;background:white'>颜色识别色域：</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>LAB<span
lang=ZH-CN>空间</span></span></p>

<p class=MsoNormal style='margin-left:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;background:white'>默认预设识别颜色：</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>5<span
lang=ZH-CN>种，分别是</span>1-<span lang=ZH-CN>红，</span>2-<span lang=ZH-CN>黄，</span>3-<span
lang=ZH-CN>蓝，</span>4-<span lang=ZH-CN>草绿，</span>5-<span lang=ZH-CN>深绿</span></span></p>

<p class=MsoNormal style='margin-left:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;background:white'>自定义识别颜色：</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>4<span
lang=ZH-CN>种</span></span></p>

<p class=MsoNormal style='margin-left:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;background:white'>颜色识别速率：最快</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>25ms</span></p>

<p class=MsoNormal style='margin-left:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;background:white'>巡线模式输出：角度模式、坐标模式</span></p>


### 3.2. 功能模块及WeeeCode图形化编程指南

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需传参数</th><th>图形化编程块举例</th>
</tr>
<tr>
    <td>选择工作模式</td><td>(2<span lang=ZH-CN>个参数）端口、选择模式</td><td><p class=MsoNormal align=center style='text-align:center'><img width=520
  height=122 id="图片 8" src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-181503.png"></p></td>
</tr>
<tr>
    <td>判断工作模式是否更新数据成功（布尔值）</td><td>(2<span lang=ZH-CN>个参数）端口、选择模式</td><td> <p class=MsoNormal align=center style='text-align:center'><img width=640
  height=126 id="图片 9" src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-181512.png"></p></td>
</tr>
<tr>
    <td>适用于巡线模式，当巡线模式更新数据成功后，获取到巡线角度偏差值</td><td>(1<span lang=ZH-CN>个参数）端口</td><td> <p class=MsoNormal align=center style='text-align:center'><img width=456
  height=50 id="图片 10" src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-181526.png"></p></td>
</tr>
<tr>
    <td>判断选择需要追踪的颜色块是否更新数据成功</td><td>(2<span lang=ZH-CN>个参数）端口、设置要追踪颜色</td><td> <p class=MsoNormal align=center style='text-align:center'><img width=636
  height=199 id="图片 11" src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-181539.png"></p></td>
</tr>
<tr>
    <td>适用于自动跟随模式及颜色追踪，更新数据成功后，可获取所追踪物块像素数量、中心点X坐标、中心点Y坐标</td><td>(2<span lang=ZH-CN>个参数）端口、选择要获取的返回值</td><td> <p class=MsoNormal align=center style='text-align:center'><img width=510
  height=153 id="图片 12" src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-181553.png"></p></td>
</tr>
</table>

### 3.3. 文本代码编程指南 

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:#222222'>直接使用文本代码编程，就涉及到相关编程</span><span style='font-size:
16.0pt;font-family:宋体;color:#222222'>API:</span></p>


<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:#222222'>Arduino <span lang=ZH-CN>函数库介绍：</span></span></b></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool getLab(void)</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——反馈摄像头前面的</span><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>LAB<span
lang=ZH-CN>值。更新后数据为</span>minL, maxL, minA, maxA, minB, maxB<span lang=ZH-CN>，分别为</span>3<span
lang=ZH-CN>个分量的最大和最小值。此模式具有自动捕捉功能，只有当摄像头中心区域内物体颜色基本一致时，才会锁定输出。用户可以根据反馈的</span>LAB<span
lang=ZH-CN>范围做适当修改，以满足不同环境下的识别。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>void
setAutoTrackingMode(void)</span></b><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——设置自动获取模式。此模式为先寻找摄像头前中心区域目标物体信息，当目标中心区域颜色基本一致时，锁定，随后跟踪此物体。此模式类似于小狗拾物的方式，先在眼前放置物体，然后寻找，程序简单，控制方便。</span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool
getAutoPosition(void)</span></b><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——获取自动模式下的物体信息。此函数需在</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>setAutoTrackingMode<span lang=ZH-CN>模式下运行，用于获取目标物体在摄像头前的</span>X<span
lang=ZH-CN>、</span>Y<span lang=ZH-CN>坐标位置以及像素大小。当摄像头捕捉到目标物体后返回</span>1<span
lang=ZH-CN>，没有捕捉到返回</span>0<span lang=ZH-CN>。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool
getColorPosition(uint8_t mun)</span></b><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——获取内置颜色</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>mun<span lang=ZH-CN>的物体信息。此函数是捕捉内置</span>5<span lang=ZH-CN>种颜色中的一种，是否出现在摄像头前。</span>Mun<span
lang=ZH-CN>填写</span>1-5<span lang=ZH-CN>，分别对应</span>1-<span lang=ZH-CN>红、</span>2-<span
lang=ZH-CN>黄、</span>3-<span lang=ZH-CN>蓝、</span>4-<span lang=ZH-CN>草绿、</span>5-<span
lang=ZH-CN>深绿。当摄像头捕捉到目标物体后返回</span>1<span lang=ZH-CN>，没有捕捉到返回</span>0<span
lang=ZH-CN>。当返回</span>1<span lang=ZH-CN>时，会更新物体的</span>X<span lang=ZH-CN>、</span>Y<span
lang=ZH-CN>坐标位置以及像素大小。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>void setLabColor1(int8_t
minL, int8_t maxL, int8_t minA, int8_t maxA, int8_t minB, int8_t maxB)</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——设置用户指定的颜色信息。采用</span><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>LAB<span
lang=ZH-CN>色域，</span>6<span lang=ZH-CN>个值代表一个范围。范围越宽，越容易识别，环境适应性越好，但误判的可能性也提高了。此函数为设置编号</span>1<span
lang=ZH-CN>的颜色信息，同理，有</span>setLabColor2<span lang=ZH-CN>、</span>setLabColor3<span
lang=ZH-CN>、</span>setLabColor4<span lang=ZH-CN>分 别对应</span>2<span lang=ZH-CN>、</span>3<span
lang=ZH-CN>、</span>4<span lang=ZH-CN>的颜色信息。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool getAppColorPosition(uint8_t
mun)</span></b><span lang=ZH-CN style='font-size:16.0pt;font-family:宋体;
color:black;letter-spacing:-.5pt;background:white'>——获取用户指定颜色</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>mun<span lang=ZH-CN>的物体信息。此函数是捕捉用户自定义的颜色，</span>Mun<span
lang=ZH-CN>填写</span>1-4<span lang=ZH-CN>，对应</span>setLabColorX<span lang=ZH-CN>中的</span>X<span
lang=ZH-CN>序号。当摄像头捕捉到目标物体后返回</span>1<span lang=ZH-CN>，没有捕捉到返回</span>0<span
lang=ZH-CN>。当返回</span>1<span lang=ZH-CN>时，会更新物体的</span>X<span lang=ZH-CN>、</span>
Y<span lang=ZH-CN>坐标位置以及像素大小。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>void
setLineFollowerMode(void)</span></b><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——设置巡线模式。此模式下，摄像头会获取</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>160*120<span lang=ZH-CN>像素大小灰度信息，用于分别黑线还白线。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>void setLineFollowerThreshold(uint8_t
min,uint8_t max)</span></b><span lang=ZH-CN style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>——设置需要捕捉线条的灰度阈值。如果背景是白色，线是黑色，一般取值</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>[0<span lang=ZH-CN>，</span>100]<span lang=ZH-CN>，取值最小为</span>0<span
lang=ZH-CN>，最大为</span>255<span lang=ZH-CN>，纯黑为</span>0<span lang=ZH-CN>，纯白为</span>255<span
lang=ZH-CN>。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool
getLineFollowerAngle(void)</span></b><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——获取巡线角度信息。获取的角度信息是一个正负角度值，根据这个值控制小车左右转，这个值在±</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>53<span lang=ZH-CN>°以内。当摄像头捕捉到线条后返回</span>1<span lang=ZH-CN>，没有捕捉到返回</span>0<span
lang=ZH-CN>。注意此函数需要在</span>setLineFollowerMode<span lang=ZH-CN>函数下使用。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool
getLineFollowerAxis(void)</span></b><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——获取巡线区域信息。此函数会更新</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>5<span lang=ZH-CN>个值，代表摄像头前从远到近依次排列的</span>5<span lang=ZH-CN>个区域的中心</span>X<span
lang=ZH-CN>坐标值，这</span>5<span lang=ZH-CN>个区域代表黑线线条区域。当摄像头捕捉到线条后返回</span>1<span
lang=ZH-CN>，没有捕捉到返回</span>0<span lang=ZH-CN>。注意此函数需要在</span>setLineFollowerMode<span
lang=ZH-CN>函数下使用。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>void
setPixelsThreshold(uint8_t mun)</span></b><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——设置识别物体最小像素数。当识别物体的像素数量超过</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>mun<span lang=ZH-CN>时，才会收到反馈信息，否则就当没有识别。此函数可以用于过滤干扰，或者识别较大物体。默认为</span>10<span
lang=ZH-CN>。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool
getColorAllPosition(uint8_t mun)</span></b><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——获取内置颜色</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>mun<span lang=ZH-CN>物体的所有信息。与</span>getColorPosition<span
lang=ZH-CN>类似，但信息更多，共包括</span>centerX<span lang=ZH-CN>、</span>centerY<span
lang=ZH-CN>、</span>pixels<span lang=ZH-CN>、</span>frameX<span lang=ZH-CN>、</span>frameY<span
lang=ZH-CN>、</span> high<span lang=ZH-CN>、</span>width<span lang=ZH-CN>、</span>rotation<span
lang=ZH-CN>等</span>8<span lang=ZH-CN>个信息，分别代表物体中心</span>X<span lang=ZH-CN>坐标、中心</span>Y<span
lang=ZH-CN>坐标、像素个数、物体边框</span>X<span lang=ZH-CN>坐标、边框</span>Y<span lang=ZH-CN>坐标、边框高度、边框宽度、物体旋转角度。由于数据较多，所有识别速率较</span>getColorPosition<span
lang=ZH-CN>慢。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool
getAppColorAllPosition(uint8_t mun)</span></b><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>——获取用户指定颜色</span><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>mun<span lang=ZH-CN>物体的所有信息。与</span>getAppColorPosition<span
lang=ZH-CN>类似，但信息更多，共包括</span>centerX<span lang=ZH-CN>、</span>centerY<span
lang=ZH-CN>、</span>pixels<span lang=ZH-CN>、</span>frameX<span lang=ZH-CN>、</span>frameY<span
lang=ZH-CN>、</span>high<span lang=ZH-CN>、</span>width<span lang=ZH-CN>、</span>rotation<span
lang=ZH-CN>等</span>8<span lang=ZH-CN>个信息，分别代表物体中心</span>X<span lang=ZH-CN>坐标、中心</span>Y<span
lang=ZH-CN>坐标、像素个数、物体边框</span>X<span lang=ZH-CN>坐标、边框</span>Y<span lang=ZH-CN>坐标、边框高度、边框宽度、物体旋转角
度。由于数据较多，所有识别速率较</span>getAppColorPosition<span lang=ZH-CN>慢。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>void
resetColorMode(uint8_t time)</span></b><span lang=ZH-CN style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>——重新初始化物体识别（非巡线）。参数</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>time<span lang=ZH-CN>为曝光时间，时间越短，拾取图像越黑，适合高亮度环境，时间越长，拾取图像越亮，适合较暗的环境。</span>Time<span
lang=ZH-CN>单位为毫秒，默认</span>2000<span lang=ZH-CN>，适合较暗的环境。</span></span></p>

<p class=MsoNormal align=left style='margin-bottom:7.9pt;text-align:left;
text-indent:.5in;background:white'><b><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>bool getFacePositon(void)</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——获取人脸位置信息。当摄像头捕捉到人脸后返回</span><span style='font-size:
16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>1<span
lang=ZH-CN>，没有捕捉到返回</span>0<span lang=ZH-CN>。当返回</span>1<span lang=ZH-CN>时，会更新人脸中心点的</span>X<span
lang=ZH-CN>、</span>Y<span lang=ZH-CN>坐标值。</span></span></p>
## 4. 背景知识介绍 

###  4.1. LAB颜色空间

<p class=MsoTitle style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;background:white'>根据人眼的视觉效果，可以通过</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>RGB<span
lang=ZH-CN>，</span>CMYK<span lang=ZH-CN>，</span>HSB<span lang=ZH-CN>，</span>LAB<span
lang=ZH-CN>色域，来将可见光的颜色描述出来。</span>Lab<span lang=ZH-CN>颜色模型弥补了</span><a
href="https://baike.baidu.com/item/RGB/342517"
target="https://baike.baidu.com/item/Lab%E9%A2%9C%E8%89%B2%E6%A8%A1%E5%9E%8B/_blank"><span
style='color:black;text-decoration:none'>RGB</span></a><span lang=ZH-CN>和</span>CMYK<span
lang=ZH-CN>两种色彩模式的不足。它是一种设备无关的颜色模型，也是一种基于生理特征的颜色模型。</span>&nbsp;Lab<span
lang=ZH-CN>颜色模型由三个要素组成，一个要素是亮度（</span>L<span lang=ZH-CN>），</span>a <span
lang=ZH-CN>和</span>b<span lang=ZH-CN>是两个</span><a
href="https://baike.baidu.com/item/%E9%A2%9C%E8%89%B2%E9%80%9A%E9%81%93/5706858"
target="https://baike.baidu.com/item/Lab%E9%A2%9C%E8%89%B2%E6%A8%A1%E5%9E%8B/_blank"><span
lang=ZH-CN style='color:black;text-decoration:none'>颜色通道</span></a><span
lang=ZH-CN>。</span>a<span lang=ZH-CN>包括的颜色是从</span><a
href="https://baike.baidu.com/item/%E6%B7%B1%E7%BB%BF%E8%89%B2/2192808"
target="https://baike.baidu.com/item/Lab%E9%A2%9C%E8%89%B2%E6%A8%A1%E5%9E%8B/_blank"><span
lang=ZH-CN style='color:black;text-decoration:none'>绿色</span></a><span
lang=ZH-CN>（负数）到灰色（中值）再到红色（正数）；</span>b<span lang=ZH-CN>是从蓝色（负数）到灰色（中值）再到黄色（正数）。</span>Lab<span
lang=ZH-CN>颜色被设计来接近人类视觉。因此</span>L<span lang=ZH-CN>分量可以调整亮度对，修改</span>a<span
lang=ZH-CN>和</span>b<span lang=ZH-CN>分量的输出色阶来做精确的颜色平衡。</span><b>L<span
lang=ZH-CN>取值为</span>[0<span lang=ZH-CN>，</span>100]<span lang=ZH-CN>，</span>A<span
lang=ZH-CN>取值为</span>[-128<span lang=ZH-CN>，</span>+128]<span lang=ZH-CN>，</span>B<span
lang=ZH-CN>取值为</span>[-128<span lang=ZH-CN>，</span>+128]</b><span lang=ZH-CN>。</span></span></p>

### 4.2. 曝光时间

<p class=MsoTitle style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;background:white'>下面是在同一环境中不同曝光时间后的画面，可以看出在</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>time=1000<span
lang=ZH-CN>时比</span>2000<span lang=ZH-CN>时暗不少。图</span>1<span lang=ZH-CN>、图</span>2<span
lang=ZH-CN>是在室内夜间拍摄，图</span>3<span lang=ZH-CN>是在白天室内拍摄。可以看出不同条件下，曝光时间对识别的效果影响还是很大的。注意调整曝光时间，能更好的识别目标。</span></span></p>
<p class=MsoTitle align=center style='text-align:center;text-indent:.5in'><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>&nbsp;&nbsp;
</span><img border=0 width=156 height=115 id="图片 13"
src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-185321.png"><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><img
border=0 width=154 height=115 id="图片 14"
src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-185331.png"><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><img
border=0 width=153 height=115 id="图片 15"
src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-185338.png"></p>


<p class=MsoTitle align=center style='text-align:center;text-indent:.5in'><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>&nbsp;&nbsp;&nbsp;</span><b><span
lang=ZH-CN style='font-size:14.0pt;font-family:宋体;color:black;background:white'>图</span></b><b><span
style='font-size:14.0pt;font-family:宋体;color:black;background:white'>1&nbsp;
Time=2000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span lang=ZH-CN>图</span>2&nbsp;
Time=1000&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span lang=ZH-CN>图</span>3&nbsp;
Time=2000</span></b></p>

<p class=MsoTitle style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;background:white'>图</span><span
style='font-size:16.0pt;font-family:宋体;color:black;background:white'>1<span
lang=ZH-CN>红色小球位置的</span>LAB<span lang=ZH-CN>数值</span><b>[60,72,54,66,-20,-8]</b><span
lang=ZH-CN>，图</span>2<span lang=ZH-CN>的</span>LAB<span lang=ZH-CN>数值</span><b>[45,58,66,74,-24,0]</b><span
lang=ZH-CN>，图</span>3<span lang=ZH-CN>的</span>LAB<span lang=ZH-CN>数值</span><b>[71,95,8,60,-37,-7]</b><span
lang=ZH-CN>，可以看出不同环境下的</span>LAB<span lang=ZH-CN>值差别还是比较大的。</span></span></p>
### 4.3. 颜色反馈值的含义

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>如下图为识别到一个橘红色圆</span></p>

<p class=MsoNormal align=center style='text-align:center'><img border=0
width=700 height=352 id="图片 16"
src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-185429.png"></p>


<p class=MsoNormal style='text-indent:.5in'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>centerX</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——识别色块中心点的</span><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>X<span
lang=ZH-CN>坐标，这个中心点不一定是外框的二分之一处，当识别到的物体不是圆时，这个点就会偏重心方向。</span></span></p>

<p class=MsoNormal style='text-indent:.5in'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>centerY</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——识别色块中心点的</span><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>Y<span
lang=ZH-CN>坐标。</span></span></p>

<p class=MsoNormal style='text-indent:.5in'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>Pixels</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——色块像素点数量，也就是这个橘红色的圆占了多少个像素。</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>&nbsp;&nbsp;&nbsp;&nbsp; </span></p>

<p class=MsoNormal style='text-indent:.5in'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>frameX</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——外框的</span><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>X<span lang=ZH-CN>坐标，这个外框会包含这个色块所有的像素。如果这个圆有一个角，那么这个外框也将包含这个角。</span></span></p>

<p class=MsoNormal style='text-indent:.5in'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>frameY</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——外框的</span><span style='font-size:16.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>Y<span lang=ZH-CN>坐标。</span></span></p>

<p class=MsoNormal style='text-indent:.5in'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>High</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——外框的高度</span></p>

<p class=MsoNormal style='text-indent:.5in'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>Width</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——外框的宽度</span></p>

<p class=MsoNormal style='margin-left:.5in'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>Rotation</span></b><span
lang=ZH-CN style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:
-.5pt;background:white'>——物体旋转角度，此值是色块的旋转（<b>单位：弧度</b>）。如果色块类似铅笔或钢笔，那么这个值就是介于</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>0-180<span lang=ZH-CN>之间的唯一值。 如果这个色块圆的，那么这个值就没有效用。如果这个色块完全不具有对称性，您只能由此得到</span>0-360<span
lang=ZH-CN>度的旋转。范围</span>X[0,320]<span lang=ZH-CN>，</span>Y[0,240]</span></p>
</body></html>

### 4.4. 巡线

<html><body>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>本模块有</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>2<span lang=ZH-CN>种巡线方式，第一种直接给出角度值，范围从</span>-53<span
lang=ZH-CN>°到</span>53<span lang=ZH-CN>°，用户可以根据这个角度来控制小车转动。第二种是给出</span>5<span
lang=ZH-CN>个值，如下图所示，在灰度图上，等分</span>5<span lang=ZH-CN>个区域，每个区域会寻找黑线的中心点，返回这</span>5<span
lang=ZH-CN>个中心点的</span>X<span lang=ZH-CN>坐标值，从</span>linex1<span lang=ZH-CN>到</span>linex5<span
lang=ZH-CN>分别代表从上到下的</span>5<span lang=ZH-CN>个点，也就是从远到近。根据这些值就可以判断地图上是直线还是曲线，车的姿态是否一致，可以写一个加权公式，来判断是否需要转弯，转弯大小如何。通过设置</span>setLineFollowerThreshold<span
lang=ZH-CN>函数里阈值的大小，就可以改变黑线的识别灰度值，满足不同颜色的巡线地图需求。范围</span></span><b><span
style='font-size:16.0pt;font-family:宋体;color:red;letter-spacing:-.5pt;
background:white'>X[0,160]<span lang=ZH-CN>，</span>Y[0,120]</span></b></p>
<p class=MsoNormal align=center style='text-align:center'><img border=0
width=159 height=120 id="图片 17"
src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-185459.png"><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><img
border=0 width=159 height=119 id="图片 18"
src="\docs\electronic_modules\rj11\imagerecognition_sensor\20190717-185507.png"></p>


<p class=MsoNormal align=center style='text-align:center'><b><span lang=ZH-CN
style='font-size:14.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>图</span></b><b><span style='font-size:14.0pt;font-family:
宋体;color:black;letter-spacing:-.5pt;background:white'>1 <span lang=ZH-CN>直线</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;<span lang=ZH-CN>图</span>2 <span lang=ZH-CN>左转弯</span></span></b></p>

<p class=MsoNormal style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;background:white'>本模式下可以制作视觉识别巡线小车或者模拟无人驾驶小车，需要注意的是，图像识别用于巡线的速度是不快的，最快</span><span
style='font-size:16.0pt;font-family:宋体;color:black;letter-spacing:-.5pt;
background:white'>50ms<span lang=ZH-CN>判断一次，所以和传统的巡线传感器相比，在速度上不具有优势。根据地图适当调整摄像头与地面的夹角以及和地面的高度，能更好的巡线。</span></span></p>
</body></html>

##  5. 技巧提升 

<html><body>
<p class=MsoTitle style='margin-left:0in;text-indent:0in'><b><span
style='font-size:16.0pt;font-family:宋体'>1、</span></b><b><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体'>标定视野范围</span></b></p>

<p class=MsoTitle style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体'>由于本模块不具有输出图像和视频的功能，所有在实际应用时，不知道摄像头的视野范围，不方便调试，这时需要对视野进行测定。测定的方法可以是用预定颜色的小球，从</span><span
style='font-size:16.0pt;font-family:宋体'>4<span lang=ZH-CN>个角落慢慢靠近中心，当在边缘位置小球被捕获，有数据输出后，即为视界边界。调整好合适的视野后，固定摄像头，这样就方便以后进一步的调试了。</span></span></p>

<p class=MsoTitle style='margin-left:0in;text-indent:0in'><b><span
style='font-size:16.0pt;font-family:宋体'>2、</span></b><b><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体'>同种颜色最多识别</span></b><b><span
style='font-size:16.0pt;font-family:宋体'>2<span lang=ZH-CN>个</span></span></b></p>

<p class=MsoTitle style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体'>在摄像头范围内，同种颜色同时识别最多</span><span style='font-size:16.0pt;
font-family:宋体'>2<span lang=ZH-CN>个物体。如果有背景有很多零碎的颜色干扰，可以设置</span>setPixelsThreshold<span
lang=ZH-CN>识别物体最小像素数，这样就可以直接滤除一些小的色块干扰。</span></span></p>

<p class=MsoTitle style='margin-left:0in;text-indent:0in'><b><span
style='font-size:16.0pt;font-family:宋体'>3、</span></b><b><span lang=ZH-CN
style='font-size:16.0pt;font-family:宋体'>人脸识别</span></b></p>

<p class=MsoTitle style='text-indent:.5in'><span lang=ZH-CN style='font-size:
16.0pt;font-family:宋体'>人脸识别采用的是</span><span style='font-size:16.0pt;font-family:
宋体'>240*160<span lang=ZH-CN>大小的灰度图，所以人脸距离摄像头</span>20cm<span lang=ZH-CN>以上跟踪效果比较好。模块能只能同时识别</span>1<span
lang=ZH-CN>张人脸，人脸需要正对摄像头，侧着脸，或者歪着头都会影响识别效果，本算法仅支持整张脸的识别，不支持半张或者部分脸的识别。识别最快</span>70ms<span
lang=ZH-CN>一次。</span></span></p>


</body></html>

##  6. 注意事项 

<html><body>
<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>1<span
lang=ZH-CN>、环境的变化对图像检测的结果将产生不同影响，使用时应尽量注意：</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; a<span
lang=ZH-CN>、避免在过暗、过亮、强逆光的环境下使用； </span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; b<span
lang=ZH-CN>、避免让灯光或强烈阳光直射目标物体，避免造成物体反光； </span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; c<span
lang=ZH-CN>、避免在彩色灯光或可变换的灯光下使用，稳定均匀的白色是最好的光源； </span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; d<span
lang=ZH-CN>、避免正对光源使用； </span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>&nbsp; e<span
lang=ZH-CN>、尽量避免在背景图案复杂的情况下使用，或者目标物体和背景颜色相近； </span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>2<span
lang=ZH-CN>、开机时间。本模块从上电到开始接收指令是需要一定时间的，这个时间大概是</span>3s<span lang=ZH-CN>左右，所以主程序上电设置摄像头参数时需要延迟</span>3s<span
lang=ZH-CN>以上，确保摄像头模块进入工作状态，或者上电后复位主控芯片。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>3<span
lang=ZH-CN>、图像识别模块一般为持续不断调用的，也就是不停的工作状态下使用，如果是隔比较久的一段时间再判断，可能数据缓存中会记录上一次未调取的数据，而直接反馈回来，所以在这种情况下使用，最好判断</span>2<span
lang=ZH-CN>次以上，排除残留干扰。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>4<span
lang=ZH-CN>、如果开启了人脸识别程序、或者巡线识别程序后，想开启寻找颜色的程序，需要调用</span>resetColorMode<span
lang=ZH-CN>（）函数，把摄像头由灰度模式返回为彩色模式，当然也可以重启摄像头模块。</span></span></p>

<p class=MsoTitle><span style='font-size:16.0pt;font-family:宋体'>5<span
lang=ZH-CN>、如果环境不是特别亮（如在太阳底下），建议模块在较暗处上电，然后再正常使用，这样识别效果更好，同一场景下识别的像素点更多。</span></span></p>
</body></html>