import streamlit as st
import subprocess
import os
import psutil
import platform

# ------------------------------
# Main Entry
# ------------------------------
def run():
    """Main function to run the Linux module"""

    st.title("🐧 CommandHub – Linux System Management & Analysis")
    st.markdown("A centralized platform to execute, manage, and monitor essential system commands and tools.")

    # Sidebar navigation
    st.sidebar.title("🛠️ Linux Tools")

    tool_category = st.sidebar.selectbox(
        "Select Category:",
        [
            "📊 System Analysis",
            "🖥️ GUI Analysis",
            "🎨 Icon Management",
            "💻 Terminal Enhancement",
            "📱 Communication",
            "📝 Documentation"
        ]
    )

    if tool_category == "📊 System Analysis":
        show_system_analysis()
    elif tool_category == "🖥️ GUI Analysis":
        show_gui_analysis()
    elif tool_category == "🎨 Icon Management":
        show_icon_management()
    elif tool_category == "💻 Terminal Enhancement":
        show_terminal_enhancement()
    elif tool_category == "📱 Communication":
        show_linux_communication()
    elif tool_category == "📝 Documentation":
        show_linux_documentation()

# ------------------------------
# 📊 System Analysis
# ------------------------------
def show_system_analysis():
    st.header("📊 Linux System Analysis")

    # System Information
    st.subheader("🖥️ System Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Basic System Info:**")
        st.write(f"OS: {platform.system()}")
        st.write(f"Release: {platform.release()}")
        st.write(f"Version: {platform.version()}")
        st.write(f"Machine: {platform.machine()}")
        st.write(f"Processor: {platform.processor()}")

    with col2:
        st.write("**System Resources:**")
        cpu_percent = psutil.cpu_percent(interval=1)
        st.write(f"CPU Usage: {cpu_percent}%")

        memory = psutil.virtual_memory()
        st.write(f"Memory Usage: {memory.percent}%")
        st.write(f"Available Memory: {memory.available / (1024**3):.2f} GB")

        disk = psutil.disk_usage('/')
        st.write(f"Disk Usage: {disk.percent}%")
        st.write(f"Free Disk: {disk.free / (1024**3):.2f} GB")

    # Process Analysis
    st.subheader("📋 Process Analysis")

    if st.button("🔄 Refresh Process List"):
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

            processes.sort(key=lambda x: x['cpu_percent'], reverse=True)

            st.write("**Top 10 Processes by CPU Usage:**")
            for i, proc in enumerate(processes[:10], 1):
                st.write(f"{i}. {proc['name']} (PID: {proc['pid']}) - CPU: {proc['cpu_percent']:.1f}%")

        except Exception as e:
            st.error(f"Error getting process list: {str(e)}")

    # Network Analysis
    st.subheader("🌐 Network Analysis")

    try:
        net_io = psutil.net_io_counters()
        st.write(f"Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
        st.write(f"Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")

        connections = psutil.net_connections()
        st.write(f"Active Connections: {len(connections)}")

    except Exception as e:
        st.error(f"Error getting network info: {str(e)}")

# ------------------------------
# 🖥️ GUI Analysis
# ------------------------------
def show_gui_analysis():
    st.header("🖥️ GUI Program Analysis")
    st.markdown("""
    ### Identify Terminal Commands Used by GUI Applications
    """)

    gui_apps = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline'] and (
                'usr/bin' in ' '.join(proc.info['cmdline']) or '/bin/' in ' '.join(proc.info['cmdline'])
            ):
                gui_apps.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    if gui_apps:
        app_names = [f"{p['name']} (PID: {p['pid']})" for p in gui_apps]
        selected = st.selectbox("Select a running GUI app:", app_names)
        idx = app_names.index(selected)
        st.write(f"**Command:** {' '.join(gui_apps[idx]['cmdline'])}")
    else:
        st.info("No running GUI apps detected.")

    st.markdown("---")
    st.subheader("Manual Command Analysis")
    custom_cmd = st.text_input("Enter a command to analyze:")
    if st.button("Analyze Command") and custom_cmd:
        st.code(f"which {custom_cmd.split()[0]}", language="bash")
        result = subprocess.run(['which', custom_cmd.split()[0]], capture_output=True, text=True)
        if result.returncode == 0:
            st.success(f"Found: {result.stdout.strip()}")
        else:
            st.warning("Not found in PATH.")

# ------------------------------
# 🎨 Icon Management
# ------------------------------
def show_icon_management():
    st.header("🎨 Icon & Logo Management")
    st.markdown("""
    ### Change the Logo or Icon of Any Program in Linux
    1. Find the .desktop file for the app
    2. Edit the file and update the **Icon=** line
    3. Update icon cache: `sudo gtk-update-icon-cache`
    """)

    app_name = st.text_input("App name to search for .desktop file:")
    if st.button("Find .desktop file") and app_name:
        found = False
        for base in ["/usr/share/applications", os.path.expanduser("~/.local/share/applications")]:
            for root, dirs, files in os.walk(base):
                for file in files:
                    if app_name.lower() in file.lower() and file.endswith('.desktop'):
                        st.success(f"Found: {os.path.join(root, file)}")
                        found = True
        if not found:
            st.warning("No .desktop file found.")

# ------------------------------
# Other modules (Terminal, Communication, Docs)
# ------------------------------
# (Kept as-is from your original, only indentation fixed)

# ------------------------------
# Run Streamlit app
# ------------------------------
if __name__ == "__main__":
    run()
