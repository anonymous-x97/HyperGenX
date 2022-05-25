outt() {
    { "$@" || return $?; } | while read -r line; do
        :
    done
}

welcome(){
echo -e "
The process will take 200-300mb to download files
and will take around 900mb of storage after unpack.
"
}

update(){
echo -e "1.Updating local packages"
yes|outt pkg upgrade
echo -e "Done"
}

install(){
echo -e "2.Installing Requirements,
  This may take upto 5 minutes depending on your 
  internet speed."
outt "$(
pkg install -y git python3
pip3 install python-dotenv
pip3 install wheel
pip3 install pyrogram==1.4.7
pkg update -y python3
pip3 install tgcrypto
pip3 install poetry-core==1.0.7
pip3 install wget
pip install --upgrade pip)"
echo -e "Done"
}

clone(){
echo -e "3.Clonning String Repo"
outt rm -rf string
outt git clone -q https://github.com/anonymous-x97/HyperGenX string
echo -e "Done
"
}

start(){
echo -e"4.Starting Generator
"
cd string
bash gen
}

welcome
update 2> /dev/null
install 2> /dev/null
clone
start
