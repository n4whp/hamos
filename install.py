import subprocess
import sys

# List of ham radio packages to install
ham_radio_packages = [
    'fldigi', 'wsjtx', 'xastir', 'chirp', 'cqrlog', 'hamlib-utils', 'qsstv', 
    'direwolf', 'pat', 'ax25-tools', 'ax25-apps', 'soundmodem', 'gqrx-sdr',
    'gnuradio', 'gpredict', 'noaa-apt', 'gr-satellites'
]

# List of lightweight desktop environment packages (XFCE or LXDE)
desktop_environment_packages = [
    'task-xfce-desktop',  # Installs the XFCE desktop environment
    # Uncomment the next line if you prefer LXDE over XFCE
    # 'task-lxde-desktop',  # Installs the LXDE desktop environment
    'lightdm'  # Lightweight display manager
]

def install_packages(package_list):
    """Install a list of packages using apt-get on a Debian-based system."""
    try:
        # Update the package list
        print("Updating package list...")
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)

        # Install each package in the list
        for package in package_list:
            print(f"Installing {package}...")
            subprocess.run(['sudo', 'apt-get', 'install', '-y', package], check=True)

        print("All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing {e.cmd}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Ham Radio Software and Lightweight Desktop Installer")

    # Install the lightweight desktop environment
    print("\nInstalling a lightweight desktop environment...")
    install_packages(desktop_environment_packages)

    # Install the ham radio software
    print("\nInstalling ham radio software...")
    install_packages(ham_radio_packages)

    print("\nInstallation complete. Reboot your system to use the new desktop environment.")
