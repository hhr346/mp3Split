import re
import os
import subprocess

def extract_audio_segment(input_file, start_time, end_time, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-ss', str(start_time),
        '-to', str(end_time),
        '-c', 'copy',
        output_file
    ]
    subprocess.run(command, check=True)

# 调用示例
name = "xxoo"
input_file = name + ".mp3"  # 输入音频文件路径
output_folder = "./" + name + "/"  # 输出片段文件夹路径

# Create the timestamp file
# 要执行的命令
command = "ffmpeg -i " + input_file + " -af silencedetect=d=1 -f null -"

# 打开一个文件来保存命令输出
with open("timestamp.txt", "w") as output_file:
    # 调用命令并将输出重定向到文件
    print(f"Running command: {command}")
    process = subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

# First read the timestamp file
with open('timestamp.txt', 'r', encoding='utf-8') as file:
    content = file.read()
# 使用正则表达式提取 silence_end 后面的数字
pattern = r'silence_end: ([0-9]+\.[0-9]+)'
silence_end_numbers = re.findall(pattern, content)

# 转换提取的数字为浮点数列表
silence_end_numbers = [float(num) for num in silence_end_numbers]
print(silence_end_numbers)

# Cut the original file
# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)
startpoint = 0
for i, endpoint in enumerate(silence_end_numbers):
    output_file = output_folder + name + f'{i:02d}' + '.mp3'
    print(f"Processing {output_file}, {i}/{len(silence_end_numbers)}")
    if i == 0:
        continue
    extract_audio_segment(input_file, startpoint, endpoint, output_file)
    startpoint = endpoint
