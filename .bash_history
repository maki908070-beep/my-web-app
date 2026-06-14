pkg update && pkg upgrade
pkg install python
mkdir MyWebIDE
cd MyWebIDE
pip install flask
cd ~
mkdir -p storage/shared/MyWebIDE
cd storage/shared/MyWebIDE
pkg install wget
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz
tar -xvzf ngrok-stable-linux-arm64.tgz
ls
python app.py
cd ~/storage/shared
ls
cd MyWebIDE
ls
termux-setup-storage
