![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
![Gluten Status](https://img.shields.io/badge/Gluten-Free-green.svg)
![Eco Status](https://img.shields.io/badge/ECO-Friendly-green.svg)

# PC_Unluck_Song

_website design project_

<br>

## 🌟 About

This project is for educational porpuses only. Pull request are welcome, but priority for project authors! Thank you for your cooperation!

Site published at: 

Song: [Iron Men Jarvis](https://www.youtube.com/watch?v=5Vt7QvMdsNA)

## 🎯 Project features/goals

-   Github pages
-   desktop only

## 🧰 Getting Started

### 💻 Prerequisites

Python - _download and install_

```
https://www.python.org/downloads
```

### 🏃 Run locally

Would like to run this project locally? Open terminal and follow these steps:

1. Clone the repo
    ```sh
    git clone https://github.com/AntiusDragon/pc_unluck_song
    ```
2. Install pygame
    ```sh
    pip install pygame
    ```

### 🧪 Running tests

1. Open Command Prompt or PowerShell and navigate to the folder where your pc_unluck_song.pyw ​​script is located
    ```sh
    cd C:\Users\Name\Documents\pc_unluck_song
    ```
2. Then run the script with the full path
    ```
    C:\Users\Name\AppData\Local\Programs\Python\Python313\python.exe pc_unluck_song.pyw
    ```
3. Use the Windows **Task Scheduler** to play a song when the computer is unlocked
    * In general
        * Open **Task Scheduler**
        * On the left side, select **Task Scheduler Library**
        * On the right side, click **Create Task...**
    * Create a new **Trigger**
        * Enter a name
        * Go to the **Triggers** tab
        * Press **New...**
        * Select "On workstation unlock" and click "OK"
    * Set **Action**
        * Go to the **Actions** tab.
        * Press **New...**.
        * Select **Start a program**.
        * In the **Program/scripts** field, enter
            ```
            C:\Users\Name\AppData\Local\Programs\Python\Python313\python.exe
            ```
        * Add arguments (path to your script)
            ```
            C:\Users\Name\Documents\python\win11-startup\pc_unluck_song.pyw
            ```

## 🎅 Authors

Antanas: [Github](https://github.com/AntiusDragon)

## ⚠️ License

Distributed under the MIT License. See LICENSE.txt for more information.

## 🔗 Other resources

No other resouces.