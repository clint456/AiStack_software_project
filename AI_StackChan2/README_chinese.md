# AI_StackChan2
如何使用AI_StackChan2
<br><br>

![画像1](images/image1.png)<br><br>

AI Stack Chan 2 的特点<br>

* 使用网页版VOICEVOX进行语音合成。
* 您可以选择“Google Cloud STT”或“OpenAI Whisper”进行语音识别。
<br>

对于 Google Cloud STT，我参考了“MhageGH”的  [esp32_CloudSpeech](https://github.com/MhageGH/esp32_CloudSpeech/ "Title") 。非常感谢。<br> 我要感谢“Inaba”和“kobatan”在使“OpenAI Whisper”可用方面提供的宝贵建议。<br> 对于唤醒词，我使用了“MechaUma”的 [SimpleVox](https://github.com/MechaUma/SimpleVox/ "Title")库。

---


### 制作 M5GoBottom 版本 Stack Chan 主体需要什么以及如何制作 。 ###
看这里。<br>
* [Stackchan M5GoBottom 版本组装套件](https://raspberrypi.mongonta.com/about-products-stackchan-m5gobottom-version/ "Title")<br>

### 构建程序需要什么 ###
* [M5Stack Core2](http://www.m5stack.com/ "Title")<br>
* VSCode<br>
* PlatformIO<br>

使用的库等请参考“platformio.ini”。<br>

~~[截至 5 月 31 日，由于 M5Unified 的问题，它无法与 CoreS3 配合使用。 ]~~<br>

---

* ### 使用伺服电机设置 GPIO 编号

* 在main.cpp第46行左右设置使用伺服电机的GPIO编号。


### 用法 ###

看这里。<br>	

* [AI_StackChan2_README](README_procedure.md)<br>
<br>
<br>
<br>
