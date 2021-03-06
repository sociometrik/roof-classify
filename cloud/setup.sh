# Setup essential libraries for Python
cd ~

git clone https://github.com/sociometrik/roof-classify.git

apt update && apt upgrade -y && apt install build-essential -y

apt install libncurses5-dev libgdbm-dev libnss3-dev libsqlite3-dev

apt install libssl-dev libreadline-dev libffi-dev -y 

sudo apt-get install zlib1g-dev libbz2-dev

sudo apt-get install liblzma-dev

apt-get install ca-certificates



# Get Python
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz && tar -xzvf Python-3.7.0.tgz

Python-3.7.0/configure --enable-optimizations && make && make install

update-alternatives --install /usr/bin/python python /root/python 1


# Set up virtual environment
cd ~
    
python -m venv roof-env && cd ~/roof-classify && source ./../roof-env/bin/activate

pip install --upgrade pip && pip install -r ./setup/requirements.txt

mkdir data
