#!/usr/bin/env bash

# Update apt first (system package installer)
sudo apt update

# Install the only editors you'll ever need.
# Protip: vim is better than emacs
sudo apt install vim emacs --yes

# Version control!
sudo apt install git --yes

# Install python3, pip (python's package manager), and virutal environment for python
sudo apt install python3 python3-pip --yes
pip3 install virtualenv

# By default, while installing MySQL, there will be a blocking prompt asking you to enter the password
# Next two lines set the default password of root so there is no prompt during installation
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'

# Install MySQL server with the default argument --yes
sudo apt install mysql-server --yes
sudo apt install build-essential python-dev libmysqlclient-dev --yes

