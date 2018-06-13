# AuroraCleanData
Aurora4 Clean Data
## 1. 文件夹描述：
* tobesegmented:
需要切割的原始语音文件，包含6000个左右的纯净语音片段 (不一定要全部用上)
* segmentedsamples: 
已经切割好了的样本，我们想要得到的比较典型的例子

## 2. 具体需求：
### 语音片段长度：
* 我们理想的长度是0.5s, 但是手动截取不需要那么精确，精度在 0.5s< 语音片段长度 <=0.52s。
### 具体需要的语音片段类型：
* 一段语音的开头 并且 人发声前有大段空白: **example: segementedsamples/1.wav**
![](
https://user-images.githubusercontent.com/20760190/41382976-5291fe8c-6f23-11e8-9d66-d8a0a278eb34.png)

* 一段语音的结尾 并且 结尾词以后有大段空白： **example: segmentedsamples/13.wav, segmentedsamples/19.wav**
![](https://user-images.githubusercontent.com/20760190/41383171-3d53ddfa-6f24-11e8-9599-686625e9a036.png)
![](https://user-images.githubusercontent.com/20760190/41383170-3d382ca4-6f24-11e8-824d-e2da857cce5a.png)

* 一段语音结尾 +大段空白+ 一段语音开头 **example: segmentedsmaples/2.wav**
![](https://user-images.githubusercontent.com/20760190/41383283-cef45d20-6f24-11e8-9b02-ab2d224ef40c.png)

### 需求数量
800 个 左右的 0.5s 的语音片段。注意不要有重复的~


