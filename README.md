# System Info Widget
<p align='center'><img src="https://i.imgur.com/UuOD5q9.png"></p>

**System Info Widget** is a widget on your desktop. 
It displays information about:
- CPU load
- CPU temperature
- GPU load
- GPU temperature
- GPU memory usage
- System memory usage
- Battery charge

**Important!** GPU monitoring only works with NVIDIA graphics cards. The application must be run as an ***administrator*** to track CPU metrics. If you see *"not work"* on any of the metrics, it means you haven't launched the application as an administrator or your computer doesn't support one or more of the metrics.

### Installation
Download the application from the [releases](https://github.com/Anton-Euro/system-info-widget/releases/tag/release) or
```bash
git clone https://github.com/Anton-Euro/system-info-widget.git
cd system-info-widget
pip install PySide6 psutil wmi
python main.py
```

## Usage
You can modify the color, positioning, and displayed metrics in the `config.ini` file.

- In the `[main]` section, the `color` variable can be changed using either a hex color code or a [color in CSS format](https://www.w3.org/wiki/CSS/Properties/color/keywords), the `x` and `y` variables adjust the positioning in pixels relative to the top left corner of the screen.

- In the `[widget_config]` section, all variables accept values of `true` or `false`, indicating whether to display a metric or not.

To add or remove a task to start the application with Windows using the Task Scheduler, you can navigate to the *autorun directory* and run *auto_tool.exe* as an administrator or 
```bash
python autorun\auto_tool.py
```