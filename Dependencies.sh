############ Run this file as root user ###################


################ install pip ########################
apt-get install python3-pip

################ install PyQt5 ######################
apt-get install python-pyqt5

############## install docker module in python #################
pip install docker

################ Download Kad file and install ##################
wget https://pypi.python.org/packages/e3/09/fada80a946dfb41c470877a0bb5c15e4e43061dfc77d0b622212c13647f6/kad.py-0.5.6-py3-none-any.whl#md5=a378a9feb12d4d51689e24649ab8d10b
pip install kad.py-0.5.6-py3-none-any.whl

######################## Install Docker ##################
apt-get update
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
apt-key fingerprint 0EBFCD88
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
apt-get update
apt-get install docker-ce

############# Proxy setting in Docker  ###################
mkdir -p /etc/systemd/system/docker.service.d
touch /etc/systemd/system/docker.service.d/http-proxy.conf
echo "[Service]
Environment=HTTP_PROXY=http://edcguest:edcguest@172.31.102.29:3128" >> /etc/systemd/system/docker.service.d/http-proxy.conf
echo "[Service]
Environment=HTTPS_PROXY=https://edcguest:edcguest@172.31.102.29:3128" >> /etc/systemd/system/docker.service.d/http-proxy.conf
systemctl daemon-reload
systemctl restart docker


