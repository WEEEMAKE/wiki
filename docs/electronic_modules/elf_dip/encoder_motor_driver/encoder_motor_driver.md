<div align=center>
<h1 class="text-center">编码电机驱动模块</h1>
</div>

## **1-简要概述**

<div align=center>
<img src="docs/electronic_modules/elf_dip/encoder_motor_driver/2E331FC1-D881-4fe6-A058-9245B08761D0.png">
</div>

<p>
    <span style="font-family: 宋体, SimSun; font-size: 24px;">&nbsp; &nbsp;编码/直流电机驱动用于ELF主控板上，可以同时驱动2个直流电机，或者1个编码电机。模块包括了MCU和电机驱动芯片MCU内置PID算法，可以实现对编码电机速度、方向、距离的精确判断，可以用于麦轮小车上也可以用于自平衡小车的驱动。此模块体积小，功能强大，既可以满足普通直流电机驱动的需求也可以满足编码电机驱动的需求。</span>
</p>

## **2-参数规格**

<!-- Table goes in the document BODY -->
<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>项</th><th>值/描述</th>
</tr>
<tr>
    <td>模块工作电压</td><td>DC 5V</td>
</tr>
<tr>
    <td>接口类型</td><td>插针与ELF主控板适配使用</td>
</tr>
<tr>
    <td>通信方式</td><td>WM单总线</td>
</tr>
<tr>
    <td>电机工作电压</td><td>DC 6V~12V</td>
</tr>
<tr>
    <td>电机通道</td><td>1个编码电机或2个直流电机</td>
</tr>
<tr>
    <td>单通道持续输出电流</td><td>2A</td>
</tr>
<tr>
    <td>单通道峰值电流</td><td>4A</td>
</tr>
</table>

## **3-功能特性**

<ul class=" list-paddingleft-2" style="list-style-type: disc;">
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;"></span><span style="background-color: rgb(255, 255, 255); color: rgb(51, 51, 51); font-size: 24px; font-family: 宋体, SimSun;">准确的控制编码电机的位置</span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;"><span style="color: rgb(51, 51, 51); font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; box-sizing: border-box; font-size: 21px;">提供实时的位置和速度反馈</span></span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;"><span style="color: rgb(51, 51, 51); font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; box-sizing: border-box; font-size: 21px;">采用排针排母组合方式，防止反接</span></span>
        </p>
    </li>
    <li>
        <p>
            <span style="font-size: 24px; font-family: 宋体, SimSun;"><span style="color: rgb(51, 51, 51); font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; box-sizing: border-box; font-size: 21px;">模块体积小巧，接插方便</span></span>
        </p>
    </li>
</ul>

## **4-连接方式**

<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 本模块目前只能用于ELF主控板上，可以接插在ELF主控板上的PORT3~PORT6的4个口上，以及2560比赛扩展板的PORT7~PORT9的3个口上。</span>
</p>
<div align=center>
<img src="docs/electronic_modules/elf_dip/encoder_motor_driver/2E331FC1-D881-4fe6-A058-9245B08761D0.png">
</div>
<p>
    <span style="font-size: 24px; font-family: 宋体, SimSun;">&nbsp; 直流电机是接插在ELF主控板的橘红色端子上，编码电机是接插在驱动模块的白色端子上。编码电机和直流电机不可同时插上，这样会造成电流过大且不好控制的问题。</span>
</p>

## **5-编程指南**
### **5.1-图形化编程**

<table class="imagetable" style="display: table; text-align: left;">
<tr>
    <th>模块功能</th><th>需设参数</th><th>图形化编程块举例(其他平台图形化编程块大同小异)</th>
</tr>
<tr>
    <td>设置0点</td><td>(1个参数）端口</td><td><img src="docs/electronic_modules/elf_dip/encoder_motor_driver/img.png"></td>
</tr>
<tr>
    <td>以某速度运行（不检测速度）</td><td>(2个参数）端口、速度（0~255）</td><td><img src="docs/electronic_modules/elf_dip/encoder_motor_driver/img_1.png"></td>
</tr>
<tr>
    <td>以某速度运行（检测速度），注：这个速度是50ms的脉冲数</td><td>(2个参数）端口、速度（0~255）</td><td><img src="docs/electronic_modules/elf_dip/encoder_motor_driver/img_2.png"></td>
</tr>
<tr>
    <td>以150速度在移动某位置（相对位置）</td><td>(2个参数）端口、移动量</td><td><img src="docs/electronic_modules/elf_dip/encoder_motor_driver/img_3.png"></td>
</tr>
<tr>
    <td>以150速度在移动某位置（绝对位置）</td><td>(2个参数）端口、移动量</td><td><img src="docs/electronic_modules/elf_dip/encoder_motor_driver/img_4.png"></td>
</tr>
</table>


