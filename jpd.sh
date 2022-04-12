#!/usr/bin/env bash
git clone https://github.com/ProdEngAcademyAdmin/jpd.git
cd jpd
if [ ! -d ~/jpd/ ]; then
  mkdir ~/jpd
fi 
cp ./config.yaml ~/jpd/


for commandname in python3 virtualenv pip3 
do
if ! command -v $commandname &> /dev/null
then
    echo "$commandname could not be found"
    echo "Install the $commandname that is misssing"
    exit 1 
fi
done 

if [ -f /usr/local/bin/jpd ]; then

    echo "I found that you have jpd binary under /usr/local/bin/, I'm backing it up "
    mv /usr/local/bin/jpd /usr/local/bin/jpdbackup
fi 

if [ -d "/venv-jpd" ]; then
  # Virtualenv Exists
  source venv-jpd/bin/activate
  pip install -r requirements.txt
  python3 setup.py develop

else
  # Virtualenv created
  virtualenv --python=python3. venv-jpd
  sleep 1
  source venv-jpd/bin/activate
  pip install -r requirements.txt
  python3 setup.py develop
fi


jpd

cat <<INSTRUCTIONS

Please fill the details in the config.yaml file under ~/jpd/ folder


Please run the following command  $ source jpd/venv-jpd/bin/activate


INSTRUCTIONS
