import subprocess
import os
import platform  # 用于判断操作系统

print(' ')
print('- 将文件夹中的视频文件转换为 HAP 编码')
print('- 在下方输入目标文件夹根目录')
print(' ')

# 输入目标文件夹路径，并进行标准化
inputPath = os.path.abspath(input('输入目标文件夹路径：').strip())

# 创建目标文件夹函数
def createFolder():
    subDirectory = "Hap_Codecs"
    savePath = os.path.join(inputPath, subDirectory)
    try:
        os.mkdir(savePath)
        print(f"已创建文件夹: {savePath}")
    except FileExistsError:
        print(f"文件夹已存在: {savePath}")
    return savePath

# 遍历文件夹并处理视频文件
def loopFile(path):
    count = 0
    for root, dirs, files in os.walk(path):
        dirs.clear()  # 不读取子目录
        for i in files:
            if i.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):  # 只读取视频文件
                file_path = os.path.join(root, i)
                file_name = os.path.splitext(i)[0]
                yield file_path, file_name
                count += 1  # 计数正确递增
    print(f"已找到 {count} 个视频文件")

# 主函数
def main():
    savePath = createFolder()
    for index, (file_path, file_name) in enumerate(loopFile(inputPath)):
        outPath = os.path.join(savePath, file_name + "_hap.mov")

        # 构建 ffmpeg 命令
        ffmpeg_cmd = ["ffmpeg", "-i", file_path, "-c:v", "hap", outPath]

        # 使用 ffmpeg 转码
        try:
            print(f"正在转码: {file_name}")
            subprocess.run(ffmpeg_cmd, check=True)
            print(f"转码完成: {file_name}")
        except subprocess.CalledProcessError as e:
            print(f"转码失败: {file_name}, 错误: {e}")
        except FileNotFoundError:
            print("未找到 ffmpeg，请确保已安装 ffmpeg 并添加到环境变量。")

# 程序入口
if __name__ == '__main__':
    main()
