#!/bin/bash
echo "update system"
sudo apt update && sudo apt upgrade -y
echo "install john"
sudo apt install john -y
echo "john test"
john --test
echo "get essentials"
sudo apt install build-essential libssl-dev -y
echo "get extras"
sudo apt install yasm libgmp-dev libpcap-dev libnss3-dev libkrb5-dev pkg-config libbz2-dev zlib1g-dev -y
echo "make and goto installation dir"
mkdir ~/src
cd /src
git clone git://github.com/magnumripper/JohnTheRipper -b bleeding-jumbo john
cd ~/src/john/src
echo "build"
./configure && make -s clean && make -sj4
echo "test"
../run/john --test
