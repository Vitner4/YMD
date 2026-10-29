<p align="center">
    <img src="src/assets/logo.png" width="300" alt="YMD Logo">
</p>

<h1 align="center">YMD</h1>

<p align="center">
Downloads videos and converts audio to MP3.
</p>

---

[🇷🇺 Русская версия](README_RU.md)

---

## 📌 About

**YMD** is a command-line tool for downloading videos and extracting their audio into MP3 files. Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp), it supports media from a wide range of platforms.

## ✨ Features

- Download videos and extract audio as MP3.
- Convert audio using the best available source quality.
- Download playlists.
- Set a custom download directory.
- View the current download directory.
- View the configuration file path.
- Install and uninstall using Python scripts.

## ⚙️ Requirements

YMD supports:

- Linux
- Android via [Termux](https://termux.dev/)

Required software:

- **Python** — runs YMD and its installation scripts.
- **FFmpeg** — extracts audio and converts it to MP3.
- **Git** — clones the YMD repository and its submodules.

Python dependencies (`yt-dlp` and `platformdirs`) are installed automatically during setup.

### Install dependencies

**Linux — Debian / Ubuntu:**

```bash
sudo apt install git python3 ffmpeg
```

**Linux — Fedora:**

```bash
sudo dnf install git python3 ffmpeg
```

**Android — Termux:**

```bash
pkg update
pkg install git python ffmpeg
```

## 📥 Download the source code

Clone the repository, including its MicroLog submodule:

```bash
git clone --recurse-submodules https://github.com/Vitner4/YMD.git
cd YMD
```

If you have already cloned the repository without its submodules, initialize them with:

```bash
git submodule update --init --recursive
```

## 🚀 Installation

1. Install Python and FFmpeg.
2. Open a terminal in the YMD project directory, where `install.py` is located.
3. Run the installer:

```bash
python install.py
```

On some Linux systems, use `python3 install.py`.

The installer creates a dedicated virtual environment, installs YMD and its dependencies, and makes the `ymd` command available in the terminal.

Verify the installation:

```bash
ymd --help
```

If `~/.local/bin` is not in your `PATH`, add it to your shell configuration.

## 📱 Android Installation (Termux)

Follow these steps to install YMD on Android.

### 1. Install Termux

Install Termux from [F-Droid](https://f-droid.org/packages/com.termux/) or its [official GitHub repository](https://github.com/termux/termux-app).

### 2. Update packages and install dependencies

Open Termux and run:

```bash
pkg update && pkg upgrade
pkg install git python ffmpeg
```

### 3. Allow access to Android storage

Run:

```bash
termux-setup-storage
```

Grant storage permission when Android prompts you.

### 4. Download YMD

Clone the repository and its submodules:

```bash
git clone --recurse-submodules https://github.com/Vitner4/YMD.git
cd YMD
```

### 5. Install YMD

Run the installer from the project directory:

```bash
python install.py
```

### 6. Verify the installation

```bash
ymd --help
```

### 7. Choose where to save downloaded media

To save downloads to the Android Downloads folder:

```bash
ymd --path "$HOME/storage/downloads"
```

You can find downloaded files in the **Downloads** folder using your Android file manager.

To check the configured download directory at any time, run:

```bash
ymd --get_path
```

**Note:** Keep the YMD project directory if you want to run `uninstall.py` later.

## 🕹️ Usage

### Download a video and extract audio as MP3

```bash
ymd "VIDEO_URL"
```

### Download a playlist

```bash
ymd --playlist "PLAYLIST_URL"
```

Short option:

```bash
ymd -p "PLAYLIST_URL"
```

### Set the download directory

```bash
ymd --path "/path/to/downloads"
```

### Show the current download directory

```bash
ymd --get_path
```

### Show the configuration file path

```bash
ymd --config
```

## 🗑️ Uninstallation

Open a terminal in the project directory and run:

```bash
python uninstall.py
```

Use `python3 uninstall.py` if required by your system.

The uninstaller removes the installed command and YMD's dedicated virtual environment. Configuration data may also be removed by the uninstaller. The project source code and downloaded media files are not removed.

## 🧩 How it works

YMD uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to retrieve media and [FFmpeg](https://ffmpeg.org/) to extract and convert audio to MP3. Available formats and quality depend on the source.

## ⚠️ Notes

- An internet connection is required.
- Platform support may change over time.
- Only download content when you have the right to do so and the platform's terms permit it.