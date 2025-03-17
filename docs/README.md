# Video2Hap 🎬  视频批量转换为 HAP 编码格式

[简体中文](README.md) | [English](README_EN.md)

Video2Hap 🎬  视频批量转换为 HAP 编码格式，支持 Window / macOS。

这是我自用的小工具，希望对你也有帮助。

# 功能
通过 Python 调用 FFmpeg 来实现视频格式的转换，避免使用复杂的图形界面软件或繁琐的设置。

只需提供视频文件夹路径，Video2Hap 会自动识别并转换视频文件为 HAP 格式，含 Alpha 信息的视频会自动识别并转换为 HAP_Alpha 编码。

## 为什么需要 HAP？
HAP 是一种专为高性能实时视频播放设计的编码格式，常用于新媒体艺术、沉浸式投影、舞台表演、VJ、互动装置等场景。

相比 H.264，HAP 具有以下优势：

✅ GPU 解码，播放时更流畅，减少 CPU 负载

✅ 支持 Alpha 通道，适用于透明背景视频

✅ 帧无损压缩，保证高质量画面

✅ 低延迟，适用于实时播放

我主要在 Max/MSP 中同时处理多个视频文件，HAP 编码能显著提升播放性能，让多视频同时运行时更加稳定流畅。此外，多数主流影像类工具（如 TouchDesigner、Resolume、Unreal Engine、Notch、MadMapper 等）都对 HAP 提供了良好的支持，在数字艺术、新媒体艺术、实时视觉领域这种格式是非常好的选择。

## 前置条件
在运行 Video2HAP 之前，请确保你的系统已安装以下软件：

[Python](https://www.python.org/) | [FFmpeg](https://ffmpeg.org/) | [git](https://git-scm.com/)

## 安装
``` 
git clone https://github.com/hendasheng/Video2Hap.git 
```

## 调用
```
cd Video2Hap
cd main
python video2hap.py
```
- 输入目标文件夹路径
- 脚本会自动在目标文件夹中创建 `HAP_Codecs` 文件夹，转码后的文件也会保存在这里。

## 如果你觉得很需要，但这种方式过于陌生
需要一点点前置知识，这些知识并非只针对这一个项目，对探索整个编程世界都有很大帮助：
- 文件路径 [目录，文件和命令行 - soulhacker](https://www.bilibili.com/video/BV1aE41117cN/?spm_id_from=333.1387.upload.video_card.click&vd_source=6c68891752436b0097051bf700e169a9)
- git 和 github [Git 和 GitHub 简明入门 - soulhacker](https://www.bilibili.com/video/BV1LE411a7dY/?spm_id_from=333.1387.upload.video_card.click&vd_source=6c68891752436b0097051bf700e169a9)
- 终端工具 [window](https://www.bilibili.com/video/BV1jE411y7FQ/?spm_id_from=333.1387.collection.video_card.click&vd_source=6c68891752436b0097051bf700e169a9) | [mac](https://www.bilibili.com/video/BV1gt411N7Ez/?spm_id_from=333.1387.collection.video_card.click)

[《欢迎来到编程世界》 - soulhacker](https://space.bilibili.com/760331/lists/353626?type=season)，这份课程可以解决大多数入门问题，并且简洁清晰地讲明编程这件事儿到底在干嘛。