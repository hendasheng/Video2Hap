import subprocess
import os
import platform

print('\n- 将文件夹中的视频文件转换为 HAP 编码')
print('- 在下方输入目标文件夹根目录\n')

# 识别操作系统
is_windows = platform.system() == "Windows"

# 处理输入路径（去除可能的双引号）
inputPath = os.path.abspath(input('输入目标文件夹路径：').strip().strip('"'))

# 创建存放 HAP 文件的文件夹
def createFolder():
    subDirectory = "Hap_Codecs"
    savePath = os.path.join(inputPath, subDirectory)
    os.makedirs(savePath, exist_ok=True)
    print(f"目标文件夹: {savePath}")
    return savePath

# 检测视频是否包含 Alpha 通道
def hasAlphaChannel(file_path):
    ffprobe_cmd = [
        "ffprobe", "-i", file_path,
        "-show_streams", "-select_streams", "v", "-loglevel", "error"
    ]

    try:
        # Windows 需要 shell=True
        result = subprocess.run(ffprobe_cmd, capture_output=True, text=True, shell=is_windows)
        return any(fmt in result.stdout for fmt in ["pix_fmt=rgba", "pix_fmt=argb", "pix_fmt=yuva"])
    except FileNotFoundError:
        print("⚠️ 未找到 ffprobe，请确保已安装 ffmpeg 并正确配置环境变量！")
        return False

# 遍历文件夹，筛选视频文件
def loopFile(path):
    count = 0
    for root, dirs, files in os.walk(path):
        dirs.clear()  # 不遍历子目录
        for i in files:
            if i.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):  # 筛选视频文件
                file_path = os.path.join(root, i)
                file_name = os.path.splitext(i)[0]
                yield file_path, file_name
                count += 1
    print(f"已找到 {count} 个视频文件")

# 处理视频文件
def main():
    savePath = createFolder()
    
    for file_path, file_name in loopFile(inputPath):
        # 判断是否有 Alpha 通道
        if hasAlphaChannel(file_path):
            codec = "hap_alpha"
            suffix = "_hap_alpha"
        else:
            codec = "hap"
            suffix = "_hap"

        outPath = os.path.join(savePath, file_name + suffix + ".mov")

        # 构建 ffmpeg 转码命令
        ffmpeg_cmd = ["ffmpeg", "-i", file_path, "-c:v", codec, outPath]

        try:
            print(f"🎬 正在转码: {file_name} ({codec})")
            subprocess.run(ffmpeg_cmd, check=True, shell=is_windows)
            print(f"✅ 转码完成: {file_name}{suffix}")
        except subprocess.CalledProcessError as e:
            print(f"❌ 转码失败: {file_name}, 错误: {e}")
        except FileNotFoundError:
            print("⚠️ 未找到 ffmpeg，请确保已安装 ffmpeg 并添加到环境变量。")

# 运行程序
if __name__ == '__main__':
    main()
