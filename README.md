# githubUserDataFetch

This is a simple GUI app written using Python and Flet that displays github information about a username that is input.

## Dependencies

Works on Windows and MacOS without any dependencies outside of Python and the requirements.txt

On Linux or WSL you may need to install GStreamer libraries if not already installed:

- On Ubuntu:

  ```bash
  sudo apt-get update && sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
  ```

- For other distrubutions visit [here](https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c) for further help installing GStreamer

### For all OSes:

- Clone this repo
  ```
  git clone https://github.com/JZXHanta/githubUserDataFetch.git
  ```
- Install Python Dependencies
  ```bash
  pip install -r requirements.txt
  ```
  or on MacOS:
  ```bash
  pip3 install -r requirements.txt
  ```

## Run the app

- ```
  python main.py
  ```
  or
  ```
  python3 main.py
  ```
