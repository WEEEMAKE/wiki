<div align=center>
<h1 class="text-center">ELF K210 AI主控板</h1>
</div>

## **1-初步了解K210**

<div align=center>
<img src="docs\electronic_modules\main_control_board\elf_k210\K210_Introduction\K210.gif" width=50%>
</div>

### **1.1-K210简要概述**

<div class=WordSection1 style='layout-grid:15.6pt'>

<p class=MsoNormal style='text-indent:30.0pt'><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>Kendryte K210 </span><span
style='font-size:15.0pt;color:#495057;background:white'>是集成<span
style='background:yellow'>机器视觉</span>与<span style='background:yellow'>机器听觉</span>能力的系统级芯片<span
lang=EN-US>(SoC)</span>。使用台积电<span lang=EN-US>(TSMC)</span>超低功耗的<span
lang=EN-US style='background:yellow'>28</span><span style='background:yellow'>纳米</span>先进制程，具有<span
style='background:yellow'>双核<span lang=EN-US>64</span>位</span>处理器，拥有较好的功耗性能，稳定性与可靠性。该方案力求零门槛开发，可在最短时效部署于用户的产品中，赋予产品人工智能。</span></p>

<p class=MsoNormal style='text-indent:30.0pt'><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>Kendryte K210 </span><span
style='font-size:15.0pt;color:#495057;background:white'>定位于<span lang=EN-US
style='background:yellow'>AI </span><span style='background:yellow'>与<span
lang=EN-US>IoT</span></span><span lang=EN-US> </span>市场的<span lang=EN-US>SoC</span>，同时是使用非常方便的<span
lang=EN-US>MCU</span>。</span></span></p>

<p class=MsoNormal style='text-indent:30.0pt'><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>Kendryte </span><span
style='font-size:15.0pt;color:#495057;background:white'>中文含义为<span
style='background:yellow'>勘智</span>，而勘智取自勘物探智。这颗芯片主要应用领域为物联网领域，在物联网领域进行开发，因此为勘物；这颗芯片主要提供的是人工智能解决方案，在人工智能领域探索，因此为探智。</span></p>

<p class=MsoListParagraph align=left style='margin-left:63.0pt;text-align:left;
text-indent:-21.0pt;text-autospace:none'><span lang=EN-US style='font-size:
15.0pt;font-family:Wingdings;color:#495057'>l<span style='font:7.0pt "Times New Roman"'>&nbsp;
</span></span><span style='font-size:15.0pt;color:#495057;background:white'>具备机器视觉能力</span></p>

<p class=MsoListParagraph align=left style='margin-left:63.0pt;text-align:left;
text-indent:-21.0pt;text-autospace:none'><span lang=EN-US style='font-size:
15.0pt;font-family:Wingdings;color:#495057'>l<span style='font:7.0pt "Times New Roman"'>&nbsp;
</span></span><span style='font-size:15.0pt;color:#495057;background:white'>具备机器听觉能力</span></p>

<p class=MsoListParagraph align=left style='margin-left:63.0pt;text-align:left;
text-indent:-21.0pt;text-autospace:none'><span lang=EN-US style='font-size:
15.0pt;font-family:Wingdings;color:#495057'>l<span style='font:7.0pt "Times New Roman"'>&nbsp;
</span></span><span style='font-size:15.0pt;color:#495057;background:white'>更好的低功耗视觉处理速度与准确率</span></p>

<p class=MsoListParagraph align=left style='margin-left:63.0pt;text-align:left;
text-indent:-21.0pt;text-autospace:none'><span lang=EN-US style='font-size:
15.0pt;font-family:Wingdings;color:#495057'>l<span style='font:7.0pt "Times New Roman"'>&nbsp;
</span></span><span style='font-size:15.0pt;color:#495057;background:white'>具备卷积人工神经网络硬件加速器<span
lang=EN-US>KPU</span>，可高性能进行卷积人工神经网络运算</span></p>

<p class=MsoListParagraph align=left style='margin-left:63.0pt;text-align:left;
text-indent:-21.0pt;text-autospace:none'><span lang=EN-US style='font-size:
15.0pt;font-family:Wingdings;color:#495057'>l<span style='font:7.0pt "Times New Roman"'>&nbsp;
</span></span><span lang=EN-US style='font-size:15.0pt;color:#495057;
background:white'>TSMC 28nm </span><span style='font-size:15.0pt;color:#495057;
background:white'>先进制程，温度范围<span lang=EN-US>-40</span>°<span lang=EN-US>C </span>到<span
lang=EN-US>125</span>°<span lang=EN-US>C</span>，稳定可靠</span></p>

<p class=MsoListParagraph align=left style='margin-left:63.0pt;text-align:left;
text-indent:-21.0pt;text-autospace:none'><span lang=EN-US style='font-size:
15.0pt;font-family:Wingdings;color:#495057'>l<span style='font:7.0pt "Times New Roman"'>&nbsp;
</span></span><span style='font-size:15.0pt;color:#495057;background:white'>支持固件加密，难以使用普通方法破解</span></p>

<p class=MsoListParagraph align=left style='margin-left:63.0pt;text-align:left;
text-indent:-21.0pt;text-autospace:none'><span lang=EN-US style='font-size:
15.0pt;font-family:Wingdings;color:#495057'>l<span style='font:7.0pt "Times New Roman"'>&nbsp;
</span></span><span style='font-size:15.0pt;color:#495057;background:white'>独特的可编程<span
lang=EN-US>IO </span>阵列，使产品设计更加灵活</span></p>

<p class=MsoListParagraph align=left style='margin-left:63.0pt;text-align:left;
text-indent:-21.0pt;text-autospace:none'><span lang=EN-US style='font-size:
15.0pt;font-family:Wingdings;color:#495057'>l<span style='font:7.0pt "Times New Roman"'>&nbsp;
</span></span><span style='font-size:15.0pt;color:#495057;background:white'>低电压，与相同处理能力的系统相比具有更低功耗</span></p>

<p class=MsoListParagraph style='margin-left:63.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:15.0pt;font-family:Wingdings;color:#495057'>l<span
style='font:7.0pt "Times New Roman"'>&nbsp; </span></span><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>3.3V/1.8V </span><span
style='font-size:15.0pt;color:#495057;background:white'>双电压支持，无需电平转换，节约成本</span></p>

<p class=MsoNormal style='text-indent:30.0pt'><span style='font-size:15.0pt;
color:#495057;background:white'>更多介绍可前往官网查看：<b><span lang=EN-US><a
href="https://canaan-creative.com/product/kendryteai" target="_blank"><span lang=EN-US><span
lang=EN-US>勘智K210</span></span></a></span></b></span></p>

</div>

### **1.2-K210系统架构**

<div align=center>
<img src="docs\electronic_modules\main_control_board\elf_k210\K210_Introduction\K210_Architecture.png" width=50%>
</div>

<p class=MsoNormal style='text-indent:30.0pt'><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>K210 </span><span
style='font-size:15.0pt;color:#495057;background:white'>包含<span lang=EN-US>RISC-V
64 </span>位双核<span lang=EN-US>CPU</span>，每个核心内置独立<span lang=EN-US>FPU. K210 </span>的核心功能是机器视觉与听觉，其包含用于计算卷积人工神经网络的<span
lang=EN-US>KPU </span>与用于处理麦克风阵列输入的<span lang=EN-US>APU. </span>同时<span
lang=EN-US>K210 </span>具备快速傅里叶变换加速器，可以进行高性能复数<span lang=EN-US>FFT </span>计算。因此对于大多数机器学习算法，<span
lang=EN-US>K210 </span>具备高性能处理能力。</span></p>

<p class=MsoNormal style='text-indent:30.0pt'><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>K210 </span><span
style='font-size:15.0pt;color:#495057;background:white'>内嵌<span lang=EN-US>AES </span>与<span
lang=EN-US>SHA256 </span>算法加速器，为用户提供基本安全功能。</span></p>

<p class=MsoNormal style='text-indent:30.0pt'><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>K210 </span><span
style='font-size:15.0pt;color:#495057;background:white'>拥有高性能、低功耗的<span
lang=EN-US>SRAM</span>，以及功能强大的<span lang=EN-US>DMA</span>，在数据吞吐能力方面性能优异。</span></p>

<p class=MsoNormal style='text-indent:30.0pt'><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>K210 </span><span
style='font-size:15.0pt;color:#495057;background:white'>具备丰富的外设单元，分别是：<span
lang=EN-US>DVP</span>、<span lang=EN-US>JTAG</span>、<span lang=EN-US>OTP</span>、<span
lang=EN-US>FPIOA</span>、<span lang=EN-US>GPIO</span>、<span lang=EN-US>UART</span>、<span
lang=EN-US>SPI</span>、<span lang=EN-US>RTC</span>、<span lang=EN-US>I</span>&sup2;<span
lang=EN-US>S</span>、<span lang=EN-US>I</span>&sup2;<span lang=EN-US>C</span>、</span></p>

<p class=MsoNormal style='text-indent:30.0pt'><span lang=EN-US
style='font-size:15.0pt;color:#495057;background:white'>WDT</span><span
style='font-size:15.0pt;color:#495057;background:white'>、<span lang=EN-US>Timer
</span>与<span lang=EN-US>PWM</span>，可满足海量应用场景。</span></p>

<div align=center>
<img src="docs\electronic_modules\main_control_board\elf_k210\K210_Introduction\K210.jpg" width="80%">
</div>

### **1.3-芯片手册**

<embed class="pdfobject" src="docs\electronic_modules\main_control_board\elf_k210\K210_Introduction\kendryte_datasheet_20180919020633.pdf" style="overflow: auto; width: 100%; height: 40rem;">

---
## **2-ELF K210 AI主控板**

### **2.1-简要概述** 

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>ELF K210 AI</span><span
style='font-size:16.0pt;font-family:宋体'>主控板是<span lang=EN-US>WEEEMAKE</span>开发的一款针对人工智能领域的全功能开发板套件。主控采用双核心设计，以<span
lang=EN-US>K210</span>为主，<span lang=EN-US>ESP32</span>为辅，既可以实现机器视觉，机器听觉，同时也实现<span
lang=EN-US>wifi</span>物联网功能。板上提供了丰富的接口，方便接入各种传感器模块，方便二次开发和学习，降低了学习<span
lang=EN-US>AI</span>视觉的门槛。</span></p>

<div align=center>
<img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image001.png">
</div>

### **2.2-主控芯片介绍**

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体;color:#0070C0'>①</span></b><b><span
lang=EN-US style='font-size:16.0pt;font-family:宋体'>K210</span></b><b><span
style='font-size:16.0pt;font-family:宋体'>芯片</span></b><span style='font-size:
16.0pt;font-family:宋体'>。勘智<span lang=EN-US>K210</span>是集成机器视觉与机器听觉能力的系统级芯片，它使用了超低功耗的<span
lang=EN-US>28</span>纳米先进制程，具有<span lang=EN-US>64</span>位处理器，总算力可达<span
lang=EN-US>1TOPS</span>，内置多种硬件加速单元（<span lang=EN-US>KUP</span>、<span
lang=EN-US>FPU</span>、<span lang=EN-US>FFT</span>等），主频<span lang=EN-US>400MHz</span>。<span
lang=EN-US>K210</span>模组内置<span lang=EN-US>8M</span>的<span lang=EN-US>SRAM</span>。</span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体;color:#0070C0'>②</span></b><b><span
lang=EN-US style='font-size:16.0pt;font-family:宋体'>ESP32</span></b><b><span
style='font-size:16.0pt;font-family:宋体'>模组</span></b><span style='font-size:
16.0pt;font-family:宋体'>。本主控采用了<span lang=EN-US>ESP32-WROOM-32D</span>通用型<span
lang=EN-US>WiFi+BT+BLE MCU</span>模组。模组集成了传统蓝牙、低功耗蓝牙和<span lang=EN-US>WIFI</span>，时钟频率可以在<span
lang=EN-US>80MHz</span>到<span lang=EN-US>240MHz</span>之间调节。</span></p>


### **2.3-开发板介绍**

<div align=center>
<img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image002.png">
</div>

<p class=MsoNormal align=center style='text-align:center'><b><span
style='font-size:18.0pt;font-family:宋体'>（开发板正面）</span></b></p>


<div align=center>
<img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image003.png">
</div>

<p class=MsoNormal align=center style='text-align:center'><b><span
style='font-size:18.0pt;font-family:宋体'>（开发板背面）</span></b></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>主控板硬件特点：</span></b></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
lang=EN-US style='font-size:16.0pt;font-family:宋体'>RJ11</span><span
style='font-size:16.0pt;font-family:宋体'>座：<span lang=EN-US>4</span>个</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体'>电机接口：<span lang=EN-US>4</span>个</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体'>功能按键：<span lang=EN-US>1</span>个</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体'>复位按键：<span lang=EN-US>1</span>个</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体'>电源开关：<span lang=EN-US>1</span>个</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
lang=EN-US style='font-size:16.0pt;font-family:宋体'>BOOT</span><span
style='font-size:16.0pt;font-family:宋体'>按键：<span lang=EN-US>1</span>个</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
lang=EN-US style='font-size:16.0pt;font-family:宋体'>MEMS</span><span
style='font-size:16.0pt;font-family:宋体'>麦克风：<span lang=EN-US>1</span>个</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
lang=EN-US style='font-size:16.0pt;font-family:宋体'>TF</span><span
style='font-size:16.0pt;font-family:宋体'>卡槽：<span lang=EN-US>1</span>个（<span
lang=EN-US>max128G</span>）</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体'>显示屏：<span lang=EN-US>1</span>个（<span
lang=EN-US>2.4</span>英寸<span lang=EN-US>TFT</span>，<span lang=EN-US>240*320</span>）</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体'>摄像头：<span lang=EN-US>1</span>个（<span
lang=EN-US>OV2640</span>像素<span lang=EN-US>200W</span>）</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体'>喇叭：<span lang=EN-US>1</span>个（<span
lang=EN-US>8R1W</span>）</span></p>

<p class=MsoListParagraph style='margin-left:21.0pt;text-indent:-21.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:Wingdings'>l</span><span
lang=EN-US style='font-size:7.0pt;font-family:"Times New Roman",serif'>&nbsp; </span><span
style='font-size:16.0pt;font-family:宋体'>排母座：<span lang=EN-US>20</span>组<span
lang=EN-US>IO</span>引脚<span lang=EN-US>+2</span>组<span lang=EN-US>I2C</span>引脚</span></p>

<p class=MsoNormal><span style='font-size:16.0pt;font-family:宋体'>其中电源输入电压在<span
lang=EN-US>DC6-12V</span>之间，<span lang=EN-US>4</span>路电机接口可以直接驱动电机，最大输出电源电压，每路最大电流<span
lang=EN-US>2A</span>。<span lang=EN-US>4</span>个<span lang=EN-US>RJ11</span>接口，可以连接<span
lang=EN-US>weeemake</span>大量丰富的传感器模块，接口电压<span lang=EN-US>DC5V</span>，输出电流<span
lang=EN-US>3A</span>。</span></p>

<img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image004.png">

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>22</span><span style='font-size:16.0pt;
font-family:宋体'>组排母座与<span lang=EN-US>arduino uno</span>的针脚类似，<span lang=EN-US>0-13</span>为数字管脚，<span
lang=EN-US>0</span>、<span lang=EN-US>1</span>同时为串口，加上<span lang=EN-US>I2C</span>管脚，共<span
lang=EN-US>16</span>排管脚，这些管脚从<span lang=EN-US>K210</span>模组中引出，电源电压可以在<span
lang=EN-US>3.3V</span>和<span lang=EN-US>5V</span>之间切换。此外还有<span lang=EN-US>A0-A5</span>这<span
lang=EN-US>6</span>个模拟口，这些端口从<span lang=EN-US>ESP32</span>中引出，电源固定<span
lang=EN-US>3.3V</span>。电机、按键和<span lang=EN-US>PORT</span>口的<span lang=EN-US>IO</span>控制管脚均来自<span
lang=EN-US>K210</span>，和排母上的<span lang=EN-US>IO</span>复用。</span></p>

<p class=MsoNormal align=center style='text-align:center'><b><span
style='font-size:18.0pt;font-family:宋体'>功能模块对应<span lang=EN-US>IO</span>管脚</span></b></p>

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

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th width=300>功能</th><th>具体模块</th><th>Arduino</th><th>K210</th>
</tr>
<tr>
  <td rowspan=4>电机</td>
  <td >M1</td><td >D12/D13</td><td>IO10/IO3</td>
</tr>
<tr>
  <td >M2</td><td >D10/D11</td><td>IO12/IO11</td>
</tr>
<tr>
  <td >M3</td><td >D8/D9</td><td>IO14/IO13</td>
</tr>
<tr>
  <td >M4</td><td >D6/D7</td><td>IO32/IO15</td>
</tr>
<tr>
  <td rowspan=4>PORT口</td>
  <td >PORT_A</td><td >D5</td><td>IO24</td>
</tr>
<tr>
  <td >PORT_B</td><td >D2</td><td>IO21</td>
</tr>
<tr>
  <td >PORT_C</td><td >D3</td><td>IO22</td>
</tr>
<tr>
  <td >PORT_D</td><td >D4</td><td>IO23</td>
</tr>
<tr>
  <td >板载按键</td><td >---</td><td >D6</td><td>IO32</td>
</tr>
<tr>
  <td >BOOT按键</td><td >---</td><td >---</td><td>IO6</td>
</tr>
<tr>
  <td >板载RGB灯（新版新增）</td><td >---</td><td >---</td><td>IO25</td>
</tr>
<tr>
  <td >板载红外接收器（新版新增）</td><td >---</td><td >---</td><td>IO2</td>
</tr>
</table>

<p class=MsoNormal style='text-indent:32.15pt'><b><span style='font-size:16.0pt;
font-family:宋体;color:red'>注：由于按键和电机<span lang=EN-US>M4</span>公用一个<span
lang=EN-US>IO</span>管脚，所以当按下按键时会对<span lang=EN-US>M4</span>造成干扰，尽量避免同时使用这<span
lang=EN-US>2</span>个功能。</span></b></p>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>RST</span><span style='font-size:16.0pt;
font-family:宋体'>和<span lang=EN-US>BOOT</span>按键用于控制<span lang=EN-US>K210</span>复位，串口指示灯也是用于指示电脑和<span
lang=EN-US>K210</span>的通信情况。<span lang=EN-US>K210</span>和<span lang=EN-US>ESP32</span>通过串口相连，两者都通过<span
lang=EN-US>SPI</span>连接<span lang=EN-US>SD</span>卡槽。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>主控板会固定在一块亚力克上，这样方便固定安装和保护主板。另外还有一个旋转摄像头支架，摄像头既可以固定在主控板上，也可以配合延长线固定在旋转支架上，这样就可以随意转动摄像头（<span
lang=EN-US>0-180</span>°）到需要的角度。摄像头和屏幕都采用<span lang=EN-US>FPC</span>座连接，这样方便更换不同的摄像头和屏幕。</span></p>

<div align=center>
<img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image005.png">
</div>

<p class=MsoNormal><span style='font-size:16.0pt;font-family:宋体'>由于主控板上有<span
lang=EN-US>2</span>块主控芯片，所有连接电脑串口时，也会出现<span lang=EN-US>2</span>个挨着的<span
lang=EN-US>com</span>口，一般来说第一个（数字小的比如<span lang=EN-US>com2</span>）是<span
lang=EN-US>K210</span>芯片的<span lang=EN-US>com</span>口，第二个（数字大的比如<span
lang=EN-US>com3</span>）是<span lang=EN-US>ESP32</span>芯片的<span lang=EN-US>com</span>口。这<span
lang=EN-US>2</span>个<span lang=EN-US>com</span>口可以分别对<span lang=EN-US>K210</span>和<span
lang=EN-US>ESP32</span>下载程序和打印串口信息。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;font-family:宋体'>TF</span><span
style='font-size:16.0pt;font-family:宋体'>卡槽可以插小于<span lang=EN-US>128G</span>的<span
lang=EN-US>TF</span>卡，这个卡主要用于存放算法模型和音视频文件，稍微复杂一点的人工智能算法必须插入<span lang=EN-US>TF</span>卡，才能正常使用。</span></p>

### **2.4-功能介绍**

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>本主控板定义为人工智能开发板，重点在于离线的快速运算能力，用户自己开发挖掘的潜力大，快速实现人工智能应用。本主控并不适合算法模型训练，那需要更高的硬件条件，但可以加载算法和模型，使用机器视觉和听觉得到的结果，再加上丰富的输入输出传感器设备，可以做出丰富的案例和场景。现介绍几个常用的功能：</span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>①颜色识别</span></b><span
style='font-size:16.0pt;font-family:宋体'>——用于寻找指定颜色，用户指定一个颜色区间，主控就会反馈视野中符合要求颜色的大小、方位等信息，通过大小就可以判定远近（需要事先知道需要找的物体实际大小），就可以实现抓取特定物体的功能。同时也可以反馈指定区域内颜色情况。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
width=149 height=134 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image006.png"></span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>②巡线追踪</span></b><span
style='font-size:16.0pt;font-family:宋体'>——可以追踪指定颜色的线条，做路径预测。用机器视觉相比巡线传感器。可以获取线条在画面中的位置偏移、方向角度等更多数据，实现平滑的巡线。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'><img width=152 height=127
src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image007.png"></span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>③标签识别</span></b><span
style='font-size:16.0pt;font-family:宋体'>——可以识别<span lang=EN-US>AprilTag</span>标签、二维码、条形码。特别是<span
lang=EN-US>AprilTag</span>标签，可以反馈标签的位置信息及三位变换数据，实现空间定位，其它<span lang=EN-US>2</span>种可以获取内容和位置信息。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'><img width=133 height=122
src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image008.png"></span></p>


<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>④人脸识别和追踪</span></b><span
style='font-size:16.0pt;font-family:宋体'>——可以分辨视野中是否有人脸，并获取人脸在画面中的位置、大小等数据实现人脸追踪，还可以分别是谁的脸，实现人脸识别。</span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>⑤图像识别</span></b><span
style='font-size:16.0pt;font-family:宋体'>——可以学习不同物体的多张照片，然后使用特定的机器学习算法进行训练，训练完成后就可以识别训练过的图标，同一物体的照片越多，学的越多，识别越好。可以实现垃圾分类，交通卡片识别等应用。</span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>⑥物体分类</span></b><span
style='font-size:16.0pt;font-family:宋体'>——已有现成的识别模型，可以识别大约<span lang=EN-US>20</span>种不同的物体，包括：飞机、自行车、鸟、猫、狗、盆栽等，可以输出位置、大小等数据。</span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>⑦语音识别</span></b><span
style='font-size:16.0pt;font-family:宋体'>——加载特定的固件和模型，就可以通过汉语拼音来识别语音。</span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>⑧<span
lang=EN-US>wifi</span>物联网</span></b><span style='font-size:16.0pt;font-family:
宋体'>——通过和<span lang=EN-US>ESP32</span>通信，可以访问互联网，或者自己组建网络来传递图片、控制指令等信息，实现远程监控。</span></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;font-family:宋体'>⑨音视频播放</span></b><span
style='font-size:16.0pt;font-family:宋体'>——板载有<span lang=EN-US>1W</span>的喇叭，可以播放程序里或者<span
lang=EN-US>SD</span>卡上的音视频。</span></p>

<p class=MsoNormal><span style='font-size:16.0pt;font-family:宋体'>此外还可以实现游戏模拟器等功能。</span></p>

### **2.5-编程软件介绍**

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>主控板目前支持图形化、<span lang=EN-US>Python</span>、<span lang=EN-US>C/C++</span>编程。图形化编程使用<span
lang=EN-US>weeecode</span>软件，<span lang=EN-US>Python</span>编程使用<span
lang=EN-US>weeecode</span>软件中内嵌的<span lang=EN-US>MaixPy IDE</span>，<span
lang=EN-US>C/C++</span>编程使用<span lang=EN-US>arduino IDE</span>。其中功能最全的是<span
lang=EN-US>Python</span>编程，其次是<span lang=EN-US>weeecode</span>图形化软件和<span
lang=EN-US>arduino IDE</span>编程。入门和体验可以从图形化开始，深入学习图像处理和语音处理建议使用<span
lang=EN-US>Python</span>编程。</span></p>

<!-- tabs:start -->

### **2.5.1-WEEECODE软件界面介绍**

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>在<span lang=EN-US>WEEEMAKE</span>官网上下载最新的<span lang=EN-US>WeeeCode</span>软件，打开后界面如下：</span></p>


<div align=center>
<img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image009.png" width="100%">
</div>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;font-family:宋体'><b>1-</b></span><span
style='font-size:16.0pt;font-family:宋体'>号区域第一个是选择主控板，此时应该选择<span lang=EN-US>WEEEMAKE
K210</span>；第二个位置是否打开对应图形化的<span lang=EN-US>Python</span>代码，默认不打开，为舞台界面，打开后才能看到<span
lang=EN-US><b>2</b></span>号和<span lang=EN-US><b>3</b></span>号界面；第三个为恢复固件，目前没有使用。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;font-family:宋体'><b>2-</b></span><span
style='font-size:16.0pt;font-family:宋体'>号区域用于显示<span lang=EN-US>Python</span>代码，其中点击“用<span
lang=EN-US>IDE</span>打开”，就会跳转到<span lang=EN-US>MaixPy IDE</span>软件中，此按键可以使<span
lang=EN-US>MaixPy IDE</span>软件中的<span lang=EN-US>Python</span>代码跟图形化语句同步。目前只能图形化转<span
lang=EN-US>Python</span>。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;font-family:宋体'><b>3-</b></span><span
style='font-size:16.0pt;font-family:宋体'>号区域是程序下载和串口信息，点击第一个串口图标，软件会自动连接主控板上的<span
lang=EN-US>K210COM</span>口，后面的“调试”相当于在线运行，“上传”是下载当前的程序，相当于离线，“中断”用于停止在线运行，“复位”用于复位主控板，“清空”是清空下面窗口的打印信息。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;font-family:宋体'><b>4-</b></span><span
style='font-size:16.0pt;font-family:宋体'>号区域是积木块区，选择不同的主控板，界面左下角“机器人”项目里的积木块会自动变化。</span></p>

<p class=MsoNormal><span lang=EN-US style='font-size:16.0pt;font-family:宋体'><b>5-</b></span><span
style='font-size:16.0pt;font-family:宋体'>号区域是图形化编程区。</span></p>

### **2.5.2-WEEECODE软件相关积木块介绍**

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>由于人工智能内容非常丰富，所以涉及的积木块也特别多。相比于之前的编程，<span lang=EN-US>K210</span>人工智能积木块具有种类多、参数多、不容易理解等特点。这里只做一个简单的介绍，详细的请参考相关教程。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>点击机器人大类选项后，旁边一栏顶端会变成如下：</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:32.15pt'><span
lang=EN-US><img width=310 height=153 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image010.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>点击其中的积木块选择器，会出现一个菜单。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
width=308 height=1001 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image011.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这个菜单主要是用于选取需要用到的<span lang=EN-US>weeemake</span>的传感器模块，<span
lang=EN-US>K210</span>主控板资源及人工智能模块，一些<span lang=EN-US>Python</span>语言的选择（一些复杂的程序需要用到<span
lang=EN-US>Python</span>语言）。只有选取了对应的功能后，才会出现相应的积木块。这个功能主要是解决积木块过多，难以寻找的问题。</span></p>

### **2.5.3-一个简单的示例程序**

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>拖出如下的积木块，这个程序的作用是把摄像头拍摄的图像实时的显示在主板的屏上。不用修改积木块中参数，直接就可以使用（参数的具体作用我们有配套的教材可以使用），这个程序一般是用来检测主控板的摄像头和屏还有串口是否正常工作。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'><img width=553 height=197
src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image012.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>编好程序后，连接串口，然后再点击调试，此时<span lang=EN-US>3</span>号窗口会打印相关信息，几秒后，主控上的屏幕就会显示拍摄的画面了。</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:32.0pt'><span
lang=EN-US><img width=553 height=815 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image013.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>如果显示的画面翻转了或者不对应，可以参考以下几个积木块，自行调整。</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:32.0pt'><span
lang=EN-US><img width=298 height=72 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image014.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这个是调整摄像头拍摄画面的，在电源的下拉框中可以选取水平镜像和垂直翻转。</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:32.0pt'><span
lang=EN-US><img width=336 height=232 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image015.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这<span lang=EN-US>2</span>个是调试<span lang=EN-US>LCD</span>显示屏画面的，如果需要对拍摄图片做处理，优先使用摄像头调整。</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:32.0pt'><span
lang=EN-US><img width=573 height=67 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image016.png"></span></p>

### **2.5.4-Maixpy软件介绍**

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'>WeeeCode</span><span style='font-size:
16.0pt;font-family:宋体'>软件里面集成完整的<span lang=EN-US>maixpy</span>软件，这个软件的优点是可以<span
lang=EN-US>python</span>编程，较完整的<span lang=EN-US>API</span>接口，可视化图片阈值分析、完成各种生成器等。想要深入学习机器视觉的用户，可以直接使用这个软件。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image017.png"></span></p>


<!-- tabs:end -->

### **2.6-基础实验例程**

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>本例程只列举一些常用的基础程序，以及这些程序运行的简单介绍，至于每个积木块内参数的意义，如何使用请参考我们出的对应教材。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>以下示例程序相关资料下载：<b><span lang=EN-US><a
href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">k210_samples.rar</a></span></b></span></p>

<!-- tabs:start -->

#### **2.6.1-放音乐**

<p class=MsoNormal align=center style='text-align:center;text-indent:32.0pt'><span
lang=EN-US><img border=0 width=418 height=320 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image018.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这个程序是从<span lang=EN-US>SD</span>卡中读取文件名为<span lang=EN-US>1</span>的音频进行播放。需要先在<span
lang=EN-US>sd</span>卡中下载对应的文件，注意目前主控板只支持<span lang=EN-US>WAV</span>格式的音频文件。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:16.0pt;font-family:宋体'><a href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">下载程序</a></span></p>

#### **2.6.2-寻找色块**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image019.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这个程序是寻找视野中颜色从（<span lang=EN-US>0</span>，<span lang=EN-US>-70</span>，<span
lang=EN-US>0</span>）到（<span lang=EN-US>80</span>，<span lang=EN-US>-10</span>，<span
lang=EN-US>30</span>）区间的物体。注意颜色体系是<span lang=EN-US>LAB</span>，不是<span
lang=EN-US>RGB</span>，示例程序中的数值范围是寻找深绿色物体，当有深绿色物体出现时，会在<span lang=EN-US>LCD</span>显示屏上框出来，并用十字标明中心点。除了程序中的可以获取中心位置外，还可以获取像素量，面积等很多参数，适用于寻找特点颜色物体的方位大小等。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:16.0pt;font-family:宋体'><a href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">下载程序</a></span></p>

#### **2.6.3-标签识别**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image020.png"></span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:16.0pt;font-family:宋体'><a href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">下载程序</a></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这个程序是识别<span lang=EN-US>AprilTag</span>标记。<span lang=EN-US>AprilTag</span>是一个视觉基准系统，通过<span
lang=EN-US>AprilTag</span>标签可以计算出精确的<span lang=EN-US>3D</span>位置、反向和<span
lang=EN-US>ID</span>。<span lang=EN-US>AprilTag</span>有很多种，目前本开发板只支持<span
lang=EN-US>TAG36H11</span>这个类型。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'><img border=0 width=197 height=215
src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image021.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>用户可以自己寻找相应网址打印<span lang=EN-US>TAG36H11</span>，关于<span
lang=EN-US>AprilTag</span>标记详细的介绍可以参考如下网址。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span lang=EN-US
style='font-size:16.0pt;font-family:宋体'><a
href="https://book.openmv.cc/image/apriltag.html">https://book.openmv.cc/image/apriltag.html</a></span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:16.0pt;font-family:宋体'><a href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">下载程序</a></span></p>

#### **2.6.4-视觉巡线**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image022.png"></span></p>
<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image023.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这是一个小车视觉巡线程序，程序分为<span lang=EN-US>4</span>段，分别是巡线初始化、图像读取和分析、电机设定和主程序。这个巡线程序总的思想是，将拍摄的图片分成<span
lang=EN-US>5</span>份（主程序最上面的几条指令），在每个区间内寻找黑线块的中心位置，由近到远再乘以权重因子，最后得出小车运动方向。程序中设定<span
lang=EN-US>M1</span>为右轮，<span lang=EN-US>M2</span>为左轮，<span lang=EN-US>LAB</span>（<span
lang=EN-US>0</span>，<span lang=EN-US>50</span>，<span lang=EN-US>0</span>，<span
lang=EN-US>0</span>，<span lang=EN-US>0</span>，<span lang=EN-US>0</span>）为线的颜色范围。注意，本程序只是基本的视觉巡线程序，只能寻单条线，弯度不能太大，线条不能交叉。需要更好巡线效果，可以在此基础上修改。</span></p>

<p class=MsoNormal><span style='font-size:16.0pt;font-family:宋体'>巡线原理可以参考：<b><span
lang=EN-US><a
href="https://book.openmv.cc/example/10-Color-Tracking/black-grayscale-line-following.html">https://book.openmv.cc/example/10-Color-Tracking/black-grayscale-line-following.html</a></span></b></span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:16.0pt;font-family:宋体'><a href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">下载程序</a></span></p>

#### **2.6.5-人脸追踪**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image024.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>有别于人脸识别，人脸追踪只能分别是不是人脸，并把人脸的坐标等信息反馈回来，并不能分辨是谁的脸。此程序运行前需要加载人脸追踪模型“<span
lang=EN-US>facedetect.kmodel</span>”（模型下载地址），将模型下载早<span lang=EN-US>SD</span>卡中，然后插入主控板中再运行程序。此程序的结果是，在<span
lang=EN-US>LCD</span>屏幕上显示拍摄的图片，并用方框表示识别到的人脸。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:16.0pt;font-family:宋体'><a href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">下载程序</a></span></p>

#### **2.6.6-语音识别**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image025.png"></span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:16.0pt;font-family:宋体'><a href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">下载程序</a></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这是一个语音识别的示例程序，使用的是汉语拼音的形式识别，程序内部已经集成了识别算法，用户可以任意添加改动关键词。这个只能识别汉语普通话，如果是其他语言或者方言，可以使用进阶例程中的自学习语音识别。此程序运行的结果是，当说“前进”时，打印<span
lang=EN-US>1</span>，当说“右转”时，打样<span lang=EN-US>2</span>。关键词后面数字<span
lang=EN-US>0.3</span>是判别阈值，值越高，识别率越低，但错误率也越低。</span></p>

<p class=MsoNormal style='text-indent:32.15pt'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;background:yellow'>注意：需要将语音识别声学模型烧录在<span
lang=EN-US>flash</span>里面，示例中，该模型烧录在地址<span lang=EN-US>0x500000</span>。</span></b></p>

#### **2.6.7-物体分类**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image026.png"></span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:16.0pt;font-family:宋体'><a href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">下载程序</a></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>此程序为物体分类识别，可以分别<span lang=EN-US>20</span>种不同的物体，分别是飞机、自行车、鸟、船、瓶子、公交、汽车、猫、椅子、奶牛、餐桌、狗、马、摩托车、人、盆栽植物、羊、沙发、火车、显示器。此程序运行前需要加载20种物体识别模型“<span
lang=EN-US>20class.kmodel</span>”，将模型下载早<span lang=EN-US>SD</span>卡根目录中，然后插入主控板中再运行程序。此程序的结果是，在<span
lang=EN-US>LCD</span>屏幕上显示拍摄的图片，并用方框表示到的物体，并把名称显示在旁边。</span></p>

<p class=MsoNormal style='text-indent:32.15pt'><b><span style='font-size:16.0pt;
font-family:宋体;color:black;background:yellow'>注：当在<span lang=EN-US>weeecode</span>软件中点击调试、上传、中断、复位时，没有信息反馈或者反馈一直是错误时，需要手动硬件复位，复位按钮（<span
lang=EN-US>RST</span>）在主控板的<span lang=EN-US>LCD</span>屏和摄像头接口旁边。复位后，<span
lang=EN-US>weeecode</span>软件里会出现复位信息，前提是串口一直保持连接。</span></b></p>

<!-- tabs:end -->

### **2.7-进阶实验介绍**

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>由于<span lang=EN-US>K210</span>内存有限，人工智能的内容很多，一个固件不能放下所有的功能，所以以下功能需要重新刷固件。刷固件的方法及固件地址参考论坛：<b><span
lang=EN-US><a
href="https://www.weeemake.com.cn/bbs/forum.php?mod=viewthread&amp;tid=94" target="_blank"><span
lang=EN-US><span lang=EN-US>【K210</span></span><span lang=EN-US><span
lang=EN-US>固件烧录】kflash_gui</span></span><span lang=EN-US><span lang=EN-US>的使用</span></span></a></span></b></span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span><span style='font-size:16.0pt;font-family:宋体'>以下示例程序相关资料下载：<b><span
lang=EN-US><a
href="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\k210_samples.rar">k210_samples.rar</a></span></b></span></p>

<!-- tabs:start -->

#### **2.7.1-自学习语音识别**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image027.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这是一个自学习语音识别，有别于之前的语音识别，这个识别程序需要先录入语音，要识别几个关键词，就需要录入几条语音，每条语音只录一遍。示例程序中需要识别<span
lang=EN-US>3</span>个关键词，关键词名称（例如红色、蓝色、绿色）可以和录入的语音无关，录入的语音可以是各种语言（如汉语、英语、俄语等等）、方言等，算法只负责对比录入的语音和现场的语音。开始运行示例程序后，软件会打印如下信息：</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:21.0pt'><span
lang=EN-US><img border=0 width=557 height=284 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image028.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>此时靠近麦克风说一段语音，主控板会自动监测，当检测到有说话时，会自动录入并进入下一段语音的检测，不过在检测前需要按一下主控板上的按键，以防止录入错误。注意每次录入语音时最好保持周围环境安静，否则录入的语音可能是无效的语音。当录入完成后会自动进入识别状态，并将识别到的关键词打印出来。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>第一次录入语音需要完整的执行示例代码，当录入完成后，可以修改程序，去掉以下这条语句，其它不变。</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:21.0pt'><span
lang=EN-US><img border=0 width=884 height=60 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image029.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这样就可以不需要每次开机都要录入语音了，因为语音信息已经保存到<span lang=EN-US>SD</span>卡中。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>注意这个自学习的语音识别相比于汉语拼音语音识别，错误率会高一点。</span></p>

#### **2.7.2-人脸识别**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image030.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>此程序为人脸识别程序，在识别前需要录入人脸，流程会比人脸追踪复杂一些。具体流程如下：需要先将程序中的<span
lang=EN-US>3</span>个<span lang=EN-US>.smodel</span>文件下载到<span lang=EN-US>SD</span>卡的根目录中，运行程序后，会打印如下信息。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img
border=0 width=504 height=214 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image031.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>同时，<span lang=EN-US>LCD</span>显示实时拍摄的画面，当识别到人脸时，会框出并用<span
lang=EN-US>5</span>个小点代表眼睛、鼻子、嘴巴。旋转摄像头，找到能稳定识别人脸的方位，按下主控板上的按键，此时第一个人脸录入完成，接下来录第二个人脸，方法相同。当第二个人脸录入完成后，程序自动进入识别状态，并把识别到的信息反馈到电脑和<span
lang=EN-US>LCD</span>屏上。最后一条语句<span lang=EN-US>70</span>为识别阈值，当超过<span
lang=EN-US>70%</span>的相似度时才会反馈结果到电脑，可以跟进情况适当调整。</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:21.0pt'><span
lang=EN-US><img border=0 width=370 height=74 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image032.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这条语句为需要录入的人脸名称，需要录入几人，就添加几条。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>第一次录入人脸需要执行训练模型的积木，示例代码，当录入完成后，可以修改程序，去掉以下这条语句，其它不变。</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:21.0pt'><span
lang=EN-US><img border=0 width=817 height=71 src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image033.png"></span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>这样就可以不需要每次开机都要录入人脸了，因为人脸信息已经保存到<span lang=EN-US>SD</span>卡中。</span></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:32.0pt'><span
lang=EN-US style='font-size:16.0pt;font-family:宋体'>&nbsp;</span></p>

#### **2.7.3-特征学习**

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image034.png"></span></p>

<p class=MsoNormal style='text-indent:21.0pt'><span lang=EN-US>&nbsp;</span><span
style='font-size:16.0pt;font-family:宋体'>此程序为特征学习部分，程序可以学习用户指定的物体，实现自动辨认。流程是用户先从不同角度拍摄需要识别的物体，拍摄的图片数量由用户自己确定，一般是拍摄越多识别效果越好，需要有物体的不同侧面和远近，这样就可以做到多角度的识别。注意：特征学习过程是学习整张图片，并不能分辨图中的物体，所以物体的大小和背景都会影响识别效果。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>此程序运行前需要加载特征学习模型“<span lang=EN-US>Feature_learning.kmodel</span>”，将模型下载早<span
lang=EN-US>SD</span>卡根目录中，然后插入主控板中再运行程序。程序识别<span lang=EN-US>2</span>个物体“<span
lang=EN-US>f1</span>”和“<span lang=EN-US>f2</span>”（名称可以自行定义），学习次数为每个物体<span
lang=EN-US>5</span>次。当程序开始运行后，电脑串口端和<span lang=EN-US>LCD</span>屏上都会提示开始采样图片，先从“<span
lang=EN-US>f1</span>”开始，模型照片<span lang=EN-US>+</span>训练照片一共是<span lang=EN-US>6</span>张，每次拍照都需要按一次主板上的按键。等<span
lang=EN-US>2</span>个模型共<span lang=EN-US>12</span>张照片拍摄完毕后，程序会自动训练，学习模型的特征点。训练过程一般很快，<span
lang=EN-US>12</span>张照片会在<span lang=EN-US>1</span>秒内训练完成。训练完成后会在<span
lang=EN-US>LCD</span>屏上显示“<span lang=EN-US>Train end!</span>”。</span></p>

<p class=MsoNormal align=center style='text-align:center'><span lang=EN-US><img src="docs\electronic_modules\main_control_board\elf_k210\K210_AI_MainControlBoard\image035.png"></span></p>

<p class=MsoNormal style='text-indent:21.0pt'><b><span lang=EN-US>&nbsp;</span></b><span
style='font-size:16.0pt;font-family:宋体'>此程序为特征学习后对比物体相似度的代码。执行代码后，<span
lang=EN-US>LCD</span>屏上会显示拍摄的图片，同时左上角会显示对比最相近的物体名称，如“<span lang=EN-US>f1</span>”或“<span
lang=EN-US>f2</span>”，并在后面显示相似度。</span></p>

<p class=MsoNormal style='text-indent:32.0pt'><span style='font-size:16.0pt;
font-family:宋体'>注：此特征学习可以用于物体分类或卡片识别等，但不能输出识别物体的方位信息，不能用于定位功能。</span></p>

</div>

<!-- tabs:end -->

### **2.8-目前固件说明**

<p>
    <span style="font-family: 宋体, SimSun; font-size: 20px;"><span style="font-family: 宋体, SimSun; color: rgb(52, 73, 94); word-spacing: 0.8px;">&nbsp; 目前发布两个固件</span><span style="font-family: 宋体, SimSun; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600; word-spacing: 0.8px;">Basic</span><span style="font-family: 宋体, SimSun; color: rgb(52, 73, 94); word-spacing: 0.8px;">和</span><span style="font-family: 宋体, SimSun; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600; word-spacing: 0.8px;">Advance</span><span style="font-family: 宋体, SimSun; color: rgb(52, 73, 94); word-spacing: 0.8px;">，因为K210本身内存有限，不可能将所有的功能集于一个固件之内，所以分为两个固件，两个固件的区别：</span></span>
</p>
<p>
    <span style="color: rgb(52, 73, 94); word-spacing: 0.8px; font-family: 宋体, SimSun; font-size: 20px;"></span>
</p>
<ul style="-webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; font-size: 15px; line-height: 1.6rem; word-spacing: 0.05rem; padding-left: 1.5rem; color: rgb(52, 73, 94); font-family: &quot;Source Sans Pro&quot;, &quot;Helvetica Neue&quot;, Arial, sans-serif; white-space: normal;" class=" list-paddingleft-2">
    <li>
        <p>
            <span style="font-family: 宋体, SimSun; font-size: 20px;"><span style="font-family: 宋体, SimSun; font-size: 24px; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600;">Basic</span>固件支持的固件功能比较多，仅<span style="font-family: 宋体, SimSun; font-size: 24px; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600;">OpenMV</span>的功能就占用比较大的一部分空间，所以<span style="font-family: 宋体, SimSun; font-size: 24px; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600;">Basic</span>固件如果需要调用<span style="font-family: 宋体, SimSun; font-size: 24px; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600;">KPU</span>，模型文件需要相当小才能正常使用；</span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-family: 宋体, SimSun; font-size: 20px;"><span style="font-family: 宋体, SimSun; font-size: 24px; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600;">Advance</span>固件去掉<span style="font-family: 宋体, SimSun; font-size: 24px; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600;">OpenMV</span>功能和<span style="font-family: 宋体, SimSun; font-size: 24px; -webkit-font-smoothing: antialiased; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-size-adjust: none; box-sizing: border-box; color: rgb(44, 62, 80); font-weight: 600;">Video</span>的功能，以便能调用稍微大一点的模型文件。</span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-family: 宋体, SimSun; font-size: 20px;">常用功能对比见下表：</span>
        </p>
    </li>
</ul>

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th width=300>功能</th><th>Basic</th><th>Advance</th>
</tr>
<tr>
  <td >Maixpy IDE</td><td >√</td><td>√</td>
</tr>
<tr>
  <td >_thread</td><td >×</td><td>×</td>
</tr>
<tr>
  <td >NES</td><td >×</td><td>×</td>
</tr>
<tr>
  <td >Video</td><td >√</td><td>×</td>
</tr>
<tr>
  <td >OpenMV</td><td >√</td><td>×</td>
</tr>
<tr>
  <td >Little LVGL</td><td >×</td><td>×</td>
</tr>
<tr>
  <td >Mic Array</td><td >×</td><td>×</td>
</tr>
<tr>
  <td >WS2812</td><td >√</td><td>√</td>
</tr>
<tr>
  <td >Speech Recognizer</td><td >√</td><td >√</td>
</tr>
<tr>
  <td >Https SSL</td><td >√</td><td >√</td>
</tr>
<tr>
  <td >Weeemake Module</td><td >√</td><td >√</td>
</tr>
</table>