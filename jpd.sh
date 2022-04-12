#!/usr/bin/env bash


git clone https://github.com/ProdEngAcademyAdmin/jpd.git
cd jpd
if [ ! -d ~/jpd/ ]; then
  mkdir ~/jpd
fi 
cp ./config.yaml ~/jpd/


for commandname in python3 pip virtualenv
do
if ! command -v $commandname &> /dev/null
then
    echo "$commandname could not be found"
    echo "Install the $commandname that is misssing"
    exit 1 
fi
done 

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

echo "Please fill the details in the config.yaml file in ~/jpd/ folder"
echo "to run the cli write jpd"