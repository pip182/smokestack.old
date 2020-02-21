# SmokeStack

## Server Setup

### Ubuntu 18.04

1. Run the `./utility/install_requirements.sh` script to set the basic stuff up for you.
2. second
3. third

#### WSL

It's not ideal but sure is handy to use WSL when a full Linux server is not available but there are a few things that you need to take into consideration. Firstly that systemd is not supported and services need to be started manually, you can create a script to start them at boot. Second is that performance is much slower than if it was a native linus server, due to translation layers and whatnot, I'm sure this will be improved in the future.

##### Setting up SSH

    # Need to create the syustem keys since they don't exist.
    sudo ssh-keygen -A
    # Need to edit /etc/ssh/sshd_config
        PasswordAuthentication to yes
    # Start the service
    sudo service ssh start
