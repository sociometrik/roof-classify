
    apt update && apt upgrade -y

    apt install build-essential -y

    apt install libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev -y        

    sudo apt-get install zlib1g-dev

    wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

    tar -xzvf Python-3.7.0.tgz

    Python-3.7.0/configure --enable-optimizations

    make

    make install

    update-alternatives --install /usr/bin/python python /root/python 1

    cd ~

    git clone https://github.com/sociometrik/roof-classify.git
    
    python -m venv roof-env

    cd ~/roof-classify

    source ./../roof-env/bin/activate