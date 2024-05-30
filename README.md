# MP3分割与识别

当你下载了一个长长的歌曲合集的时候，你就会想将其分割成很多部分文件，可以按照以下方法进行操作：

## 时间点分割

首先是利用ffmpeg工具进行时间点的分割。

[ffmpeg - How to split an mp3 file by detecting silent parts? - Ask Ubuntu](https://askubuntu.com/questions/1264779/how-to-split-an-mp3-file-by-detecting-silent-parts)

```
ffmpeg -i input.mp3 -af silencedetect=d=2 -f null -
```

`silencedetect=d=2` 2为间隔的秒数，可以按照需要更改。



## 文件输出

当输出了各个时间戳之后，将输出的结果复制粘贴到`timestamp.txt`的文件中，注意一下有没有奇怪的东西混进来。保持好格式，每个暂停点输出两行。

```txt
[silencedetect @ 00000242958da740] silence_start: 20627.2
[silencedetect @ 00000242958da740] silence_end: 20630.2 | silence_duration: 3.01819
```

接下来呢通过Python进行读取`silence_end:`后面的那串数字，并调用ffmpeg进行分割。



### `-ss` and `-t` or `-to`

Using these options will omit the silent segments but is more work to make the commands:

```
ffmpeg -i input.mp3 -to 1.20837 -c copy output_01.mp3
ffmpeg -i input.mp3 -ss 1.92546 -to 3.51778 -c copy output_02.mp3
```

…and so on.

Or do it in one command:

```
ffmpeg -i input.mp3 -to 1.20837 -c copy output_01.mp3 -ss 1.92546 -to 3.51778 -c copy output_02.mp3
```

As in the segment muxer command this also uses stream copy.



## 音乐识别

分开了各个音频之后我们当然还希望进行音频识别，将文件重命名为歌曲名啦。

