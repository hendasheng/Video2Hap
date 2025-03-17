# Video2Hap 🎬  Batch Convert Videos to HAP Format

[简体中文](README.md) | [English](README_EN.md)

Video2Hap 🎬 is a batch video conversion tool for HAP encoding, supporting Windows and macOS.

This is a personal tool I use, and I hope it helps you as well.

## Features
Video2Hap utilizes Python to call FFmpeg for video format conversion, eliminating the need for complex graphical software or tedious settings.

Simply provide a folder path containing video files, and Video2Hap will automatically detect and convert them into HAP format. Videos containing alpha information will be automatically detected and converted into HAP_Alpha encoding.

## Why HAP?
HAP is a codec specifically designed for high-performance real-time video playback, commonly used in new media art, immersive projection, stage performances, VJing, interactive installations, and more.

Compared to H.264, HAP offers the following advantages:

✅ **GPU decoding** for smoother playback and reduced CPU load  
✅ **Supports Alpha channel**, making it suitable for videos with transparent backgrounds  
✅ **Lossless frame compression** to maintain high-quality visuals  
✅ **Low latency**, ideal for real-time playback  

I primarily use HAP encoding in Max/MSP to handle multiple video files simultaneously. HAP significantly improves playback performance, ensuring smoother and more stable multi-video playback. Moreover, many mainstream video tools (such as TouchDesigner, Resolume, Unreal Engine, Notch, MadMapper, etc.) offer excellent support for HAP, making it an ideal choice for digital art, new media, and real-time visuals.

## Prerequisites
Before running Video2Hap, ensure your system has the following installed:

- [Python](https://www.python.org/)  
- [FFmpeg](https://ffmpeg.org/)  
- [git](https://git-scm.com/)  

## Installation
```sh
git clone https://github.com/hendasheng/Video2Hap.git
cd Video2Hap
cd main
python video2hap.py
```

## If you find this tool useful but unfamiliar with this method

Some basic knowledge is required, which is not only helpful for this project but also beneficial for exploring the world of programming:

- **File Path Basics**: [Directories, Files, and Command Line - soulhacker](https://www.bilibili.com/video/BV1aE41117cN/)  
- **Git & GitHub**: [Git and GitHub Quick Start - soulhacker](https://www.bilibili.com/video/BV1LE411a7dY/)  
- **Terminal Tools**: [Windows](https://www.bilibili.com/video/BV1jE411y7FQ/) | [macOS](https://www.bilibili.com/video/BV1gt411N7Ez/)  
- **Programming Basics**: ["Welcome to the World of Programming" - soulhacker](https://space.bilibili.com/760331/lists/353626?type=season)  

