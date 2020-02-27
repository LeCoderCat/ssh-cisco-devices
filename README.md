[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/LeCoderCat/SSHCiscoDevices)

# ssh-cisco-devices
Example code to SSH and perform CLI commands on Cisco Devices.
The files included on this repository contain examples on loging in using paramiko package to SSH on DNA Center and Prime infrastructure and execute command(s). After the commands are executed, the output of the result shows on the CLI of the device that is running the script.

## How to run
All the scripts should be run on the terminal on a device that has python 2 and the required python packages installed.
You can find the packages needed listed on the file requirement.txt

### Setting Up to Run the script
Clone and Prep the Environment
    Clone the code repo
    git clone https://github.com/LeCoderCat/ssh-cisco-devices.git
    cd ssh-cisco-devices
   
### Setup Python Virtual Environment.
    1. MacOS or Linux
    python3.6 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
        > Note: If on Linux, you will need to install the Python3.6 development files. On CentOS this is done with yum install -y python36u-devel
    2. Windows - recommendation to use git-bash terminal
    py -3 -m venv venv
    source venv/Scripts/activate
    pip install -r requirements-win.txt
        > Note: Creation and activation of a venv in Windows is slightly different.
