# AuroraCleanData
Aurora4 Clean Data
## 1. 文件夹描述：
* tobesegmented:
需要切割的原始语音文件，包含6000个左右的纯净语音片段 (不一定要全部用上)
* segmentedsamples: 
已经切割好了的样本，我们想要得到的比较典型的例子

## 2. 具体需求：
### 语音片段长度：
* 我们理想的长度是0.5s, 但是手动截取不需要那么精确，可以截取到[0.5,0.52)这个区间内就可以 （注意区间是左闭右开）。
### 具体需要的语音片段类型：
* 一段语音的开头 并且 人发声前有大段空白: **example: segementedsamples/1.wav**
![](
https://user-images.githubusercontent.com/20760190/41382976-5291fe8c-6f23-11e8-9d66-d8a0a278eb34.png)

* 一段语音的结尾 并且 结尾词以后有大段空白： **example: segmentedsamples/13.wav, segmentedsamples/19.wav**
![](https://user-images.githubusercontent.com/20760190/41383171-3d53ddfa-6f24-11e8-9599-686625e9a036.png)




