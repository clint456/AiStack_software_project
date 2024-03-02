# AI_StackChan2_README
AI Stack Chan 2 的特点<br>

* 使用网页版VOICEVOX进行语音合成。
* 您可以选择“Google Cloud STT”或“OpenAI Whisper”进行语音识别。
  <br>

对于 Google Cloud STT，我参考了“MhageGH”的  [esp32_CloudSpeech](https://github.com/MhageGH/esp32_CloudSpeech/ "Title") 。非常感谢。<br> 我要感谢“Inaba”和“kobatan”在使“OpenAI Whisper”可用方面提供的宝贵建议。<br> 对于唤醒词，我使用了“MechaUma”的 [SimpleVox](https://github.com/MechaUma/SimpleVox/ "Title")库。


---

### 获取 ChatGPT 的 API 密钥 ###

ChatGPT的API key获取方法如下。 （有关详细信息，请参阅本页底部的链接。）

* 访问 [OpenAI](https://openai.com/ "Title") 网站并创建一个帐户。需要电子邮件地址和手机号码。
* 创建帐户后，将颁发 API 密钥。 API 密钥是付费的，但有免费期和积分。<br>

### 获取网页版VOICEVOX API key ###

* 请参阅本页底部（[ttsQuestV3Voicevox](https://github.com/ts-klassen/ttsQuestV3Voicevox/ "Title")）了解如何获取 VOICEVOX 网页版的 API 密钥。 ）<br>

  获取VOICEVOX的API密钥后，不要忘记注册“VOICEVOX的API使用注册”。否则，语音合成速度不够快，语音会断断续续。

### 获取 Google Cloud Speech to Text 的 API 密钥（使用 Whisper 进行语音识别时不需要） ###

如何获取 Google Cloud Speech to Text 的 API 密钥如下。 （有关详细信息，请参阅本页底部的链接。）

* 访问 [Google Cloud Platform](https://cloud.google.com/?hl=ja/ "Title") 网站并创建一个帐户。需要电子邮件地址和手机号码。需要卡注册，但有免费试用和免费限制。
* 创建帐户后，您将获得 API 密钥。 <br>不要忘记在 API 密钥中启用语音转文本。<br>

---


### 设置方法 ###

* 使用前必须在SD卡根目录下创建以下两个文件。<br>
  确认正常工作后，请务必取出用于设置的SD卡。

1. wifi.txt文件：文件名为 "wifi.txt"，内容如下：<br>
YOUR_WIFI_SSID<br>
YOUR_WIFI_PASS<br>

2. apikey.txt文件：文件名为 "apikey.txt"，内容如下<br>
YOUR_OPENAI_APIKEY<br>
YOUR_VOICEVOX_APIKEY<br>
YOUR_STT_APIKEY<br>

* 【注意】<br>对于“YOUR_STT_APIKEY”，设置“Google Cloud STT API 密钥”或与“YOUR_OPENAI_APIKEY”相同。 <br>

  如果您将“YOUR_STT_APIKEY”设置为与“YOUR_OPENAI_APIKEY”相同，则 OpenAI Whisper 将用于语音识别。


* 如果M5Stack之前连接过Wifi，它将自动连接Wifi，无需SD卡。<br>
在这种情况下，您可以通过在浏览器中访问“http://XXX.XXX.XXX.XXX/apikey”来设置API密钥。 
* （xxxx.xxxx.xxxx.xxxx为启动AI Stack Chan时显示的IP地址。）<br>


### 如何使用唤醒词（仅适用于Core2） ###

1. 唤醒词设置<br>
按住按钮 B 2 秒钟。<br>
当显示屏显示 "Start wake word registration"（开始唤醒词登记）时，说出要登记的唤醒词。<br>
如果注册成功，将播放注册的唤醒词。<br>
播放声音较小，但没有问题。<br>
如果不成功，请再试一次。<br>

2. 操作检查<br>
单击按钮A激活唤醒词。<br>
尝试说出已注册的唤醒词。<br>
如果唤醒词被成功识别，系统将等待语音输入。<br>
如果多次尝试后仍无效，请从步骤1重新开始。<br>

3. 提示<br>
・接通电源后，唤醒词功能被禁用。如有必要，请使用按钮 A 激活该功能。<br>
・触摸液晶屏左侧边缘中央，切换至独白模式。<br>

### 如何使用其他功能  ###

* 当您触摸 Stack Chan 的额头时，麦克风将开始录音，您将能够通过语音识别进行交谈。 录音时间约为7秒。<br>

* 您可以设置默认声音（扬声器）。<br>
  示例：http://http://172.20.10.3/setting?speaker=1 <br>

  值为0到60 <br>

  可以在底部的发言者编号列表中找到值列表。<br>

  对于临时语音更改，您可以指定语音参数。<br>

*  可以在底部的发言者编号列表中找到值列表。 <br>

* 例如：<br><br>
http://192.168.11.20/chat?voice=4&text=こんにちは<br>
<br>

* 您可以通过浏览器访问“http://xxxx.xxxx.xxxx.xxxx/role”来设置角色。<br>
（xxxx.xxxx.xxxx.xxxx为启动AI Stack Chan时显示的IP地址。） <br>未在文本区域中输入任何内容的情况下提交将删除之前设置的角色。<br><br>
角色信息自动保存在 spiffs 中。<br>

* 在浏览器中访问“http://xxxx.xxxx.xxxx.xxxx/role_get”即可获取当前设置的角色。<br>

* 您可以调节扬声器音量<br><br>
示例：http://xxxx.xxxx.xxxx.xxxx/setting?volume=180<br> 音量的值是0到255<br>

* 添加独白模式。<br>以随机的时间间隔随机说话。 <br>与情感表达功能结合起来很有趣。 如果触摸液晶屏左边缘中央附近，可以打开/关闭独白模式。<br> 即使在独白模式下，您也可以像以前一样通过智能手机交谈。<br>
<br>

* 如果触摸M5Stack Core2屏幕中央附近，可以停止Stack chan的摆动。<br>

* 您可以通过按 M5Stack Core2 上的按钮 C 来测试语音合成。<br>

以上就是AI Stack Chan的使用方法。<br><br>
### 请注意，如果您使用 M5Burner 编写农场，请不要忘记再次从 SD 设置 API 密钥。 ###
<br>

---

### 获取 ChatGPT API 密钥的参考链接 ###

* [ChatGPT API利用方法の簡単解説](https://qiita.com/mikito/items/b69f38c54b362c20e9e6/ "Title")<br>

### 获取网页版VOICEVOX API key

* Web版 VOICEVOX のAPIキーの取得方法は、このページ（[ttsQuestV3Voicevox](https://github.com/ts-klassen/ttsQuestV3Voicevox/ "Title")）の一番下の方を参照してください。)<br>

### 用于获取 Google Cloud Speech to Text 的 API 密钥的参考链接 ###

* [Speech-to-Text APIキーの取得／登録方法について](https://nicecamera.kidsplates.jp/help/feature/transcription/apikey/ "Title")<br>

### ChatGPT字符设置参考链接 ###

* [ChatGPTのAPIでキャラクター設定を試してみた](https://note.com/it_navi/n/nf5f702b36a75#8e42f887-fb07-4367-9f3f-ab7f119eb064/ "Title")<br>
<br>

### VoiceVoxの話者番号 ###

- VoiceVox 扬声器编号

  VoiceVox扬声器号码列表
  0: Shikoku Métan (阿玛玛)
  1: Zundamon (甜甜蜜蜜)
  2:Shikoku Metan (正常)
  3:Zundamon（正常）
  4: 四国美达 (性感)
  5: 尊达蒙（性感）
  6:四国美坦（啸啸）
  7:尊达蒙（啸啸）
  8:春日部嬬(普通)
  9:那明律（普通）
  10:あめはるは(普通)
  11:源野武弘（普通）
  12:白上虎太郎（普通）
  13:青山龙生（普通）
  14:妃魅明日香（普通）
  15:九州索拉（阿玛阿玛）
  16: 九州索拉 (普通)
  17: 九州索拉 (性感)
  18: 九州索拉 (啸啸)
  19: 九州索拉（耳语）
  20:Mochiko（cv朝霞Yomogi）
  21:剑崎姬夫（正常）
  22:尊达蒙（耳语）
  23:WhiteCUL(普通)
  24:WhiteCUL(撩人)
  25:WhiteCUL(悲伤)
  26:白色CUL (比恩)
  27:Gogo Oni (人类版)
  28:Go-oni (毛绒玩具版)
  29:7号(正常)
  30:7号(广播)
  31:7号(大声朗读)
  32:白上虎太郎(哭泣)
  33:白上虎太郎(大叫)
  34:白上寅太郎(兴奋)
  35:白上虎太郎（哔哔声）
  36:Shikoku Metan (窃窃私语)
  37:Shikoku Metan (窃窃私语)
  38:尊达蒙（低语）
  39:源野武弘（喜悦）
  40:源野武弘 (抽搐)
  41:源野武弘（悲伤）
  42:敷井千叶 (正常)
  43:上田美子樱(正常)
  44:上田樱美子（第二形态）
  45:樱上美子（洛丽塔）
  46:沙耶/SAYO(普通)
  47:护士机器人_Type T (普通)
  48:护士机器人_Type T (简单)
  49:机器人护士T型(恐惧)
  50:护士机器人_类型T（保密谈话）
  51:†神圣骑士红樱花† (普通)
  52:桜松修二（普通）
  53:桐岛馨（普通）
  54:春香奈奈 (普通)
  55:霓裳爱尔 (普通)
  56:霓裳爱尔（冷静）
  57:霓裳羽衣阿露 (乌衣乌衣)
  58:关使蜂（普通）
  59: 梦使蜂 (冷静)
  60: 霓裳使蜂 (害羞)
