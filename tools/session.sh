#!/usr/bin/env bash
# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

clear
printLogo() {
    printLine
    echo '
                 XXXXXXX       XXXXXXX                
                 X:::::X       X:::::X                
                 X:::::X       X:::::X                
                 X::::::X     X::::::X                
                 XXX:::::X   X:::::XXX                
                    X:::::X X:::::X                   
                     X:::::X:::::X                    
 ---------------      X:::::::::X      ---------------
 -:::::::::::::-      X:::::::::X      -:::::::::::::-
 ---------------     X:::::X:::::X     ---------------
                    X:::::X X:::::X                   
                 XXX:::::X   X:::::XXX                
                 X::::::X     X::::::X                
                 X:::::X       X:::::X                
                 X:::::X       X:::::X                
                 XXXXXXX       XXXXXXX                
'
    printLine
}

sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
pkg install pip3
wget https://raw.githubusercontent.com/NotShroudX97/HyperGenX/mai/tools/genx.py
pip3 install pyrogram
pip3 install tgcrypto
clear
python3 genx.py
