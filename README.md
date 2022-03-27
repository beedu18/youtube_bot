<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="assets/youtube.webp" alt="Logo" height="80">

  <h3 align="center">Youtube Bot</h3>

  <p align="center">
    <a href="https://github.com/beedu18/youtube_bot"><strong>Explore the docs »</strong></a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#selenium">Selenium</a></li>
        <li><a href="#chromedriver">ChromeDriver</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#video-tutorial">Video Tutorial</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![image](assets/output.gif)

This project uses the Selenium Library and ChromeDriver to automate watching youtube videos. Add your video link in `config.py`, configure the watch time (either fixed or variable) and run the script.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.9](https://www.python.org/)
* [Selenium](https://www.selenium.dev/documentation/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Lets get started

### Clone Repository

Clone this repository using
```sh
git clone https://github.com/beedu18/youtube_bot.git
```

Go to project root
```sh
cd youtube_bot
```

### Selenium

Get selenium using pip.
```sh
pip install -r requirements.txt
```

### ChromeDriver

_Follow the steps below to get ChromeDriver. And add it in `config.py`_

1. Check your Chrome version by going into settings
2. Go [here](https://chromedriver.chromium.org/downloads) and get the suitable chromedriver file
3. Add the executable in the root of the project and check if the name matches with `driver_file` in `config.py`

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the `main.py` file
  ```sh
  python main.py
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- REFERENCE -->
## Video Tutorial

[NoobDev EP02 | Making a YouTube Viewbot | Web Automation using Selenium and Python](https://www.youtube.com/watch?v=Qa30VmcLwGg)

Project Link: [https://github.com/beedu18/youtube_bot](https://github.com/beedu18/youtube_bot)

<p align="right">(<a href="#top">back to top</a>)</p>