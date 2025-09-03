# CommandHub – Linux Automation & System Management Platform

CommandHub is a **menu-driven Streamlit application** that allows Linux users to execute, monitor, and manage essential system commands and tools from a single web interface.

---

## Features

1. 📊 **System Analysis**
   - CPU, Memory, Disk, and Process monitoring
   - Active network connections overview

2. 🖥️ **GUI Analysis**
   - Identify underlying terminal commands of running GUI apps
   - Manual command exploration

3. 🎨 **Icon & Logo Management**
   - Locate application icons
   - Change logos/icons via .desktop files

4. 💻 **Terminal Enhancement**
   - Add multiple terminal interfaces (tmux, screen, guake, terminator, etc.)
   - Customize shells: bash, zsh, fish

5. 📱 **Communication Tools**
   - Send Email, WhatsApp, Tweet, and SMS (mock/demo implementations)

6. 📝 **Documentation & Signal Handling**
   - Ctrl+C (SIGINT) and Ctrl+Z (SIGTSTP) learning
   - Generate blogs and technical documentation

---

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/<your-username>/CommandHub-Linux-Automation.git
   cd CommandHub-Linux-Automation

2. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install --upgrade pip
   pip install streamlit psutil requests

---

## Run the Application

Launch the app using Streamlit:

streamlit run commandhub.py

Open a browser and navigate to: http://localhost:8501

---

## Notes

- System analysis features work on Linux and Windows, but **GUI & icon management is Linux-specific**.
- Communication tools are **demo/mocked**. Real API integration requires credentials.
- Extendable: You can integrate Twilio, Twitter API v2, Instagram Graph API, etc.

---

## Learning Outcomes

- Understand Linux system monitoring & process management
- Learn how GUI apps interact with the terminal
- Automate and centralize command-line operations in Python
- Get hands-on experience with Streamlit for building interactive web apps
# CommandHub_system_python
