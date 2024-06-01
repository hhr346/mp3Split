# MP3分割与识别

当你下载了一个长长的歌曲合集的时候，你就会想将其分割成很多部分文件，可以按照以下方法进行操作：

主要操作借鉴了：[ffmpeg - How to split an mp3 file by detecting silent parts? - Ask Ubuntu](https://askubuntu.com/questions/1264779/how-to-split-an-mp3-file-by-detecting-silent-parts) 

## 时间点分割

首先是利用ffmpeg工具进行时间点的分割。

```
ffmpeg -i input.mp3 -af silencedetect=d=2 -f null -
```

`silencedetect=d=2` 2为间隔的秒数，可以按照需要更改。

该步骤已经整合到脚本当中，会自动输出分割结果到`timestamp.txt`中。



## 文件输出

`timestamp.txt`中的结果类似以下：

```txt
[silencedetect @ 00000242958da740] silence_start: 20627.2
[silencedetect @ 00000242958da740] silence_end: 20630.2 | silence_duration: 3.01819
```

接下来通过Python进行读取`silence_end:`后面的那串数字，并调用ffmpeg进行分割。



## 音乐识别

分开了各个音频之后我们当然还希望进行音频识别，将文件重命名为歌曲名啦。似乎可以考虑使用Shazam的API进行操作：[Shazam API API: How To Use the API with Free API Key | RapidAPI](https://rapidapi.com/diyorbekkanal/api/shazam-api6/details)

有待后续研究。
