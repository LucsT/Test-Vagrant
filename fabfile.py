from fabric.api import run
# Decompresse, compile, deploie nodeJS

def install():
#    run('uname -a')
#    run('sudo apt-get install sl')

# Recuperation de node via le shared folder
    run('cp /vagrant/node-v0.6.18.tar.gz ./node-v0.6.18.tar.gz')
    run('tar zxvf node-v0.6.18.tar.gz')
   
# install d'un compilateur
    run('sudo apt-get install g++')
# build de node
    run('cd node-v0.6.18; ./configure; make; sudo make install')
 
    launch()

def launch():
# lancement hello sur node depuis le shared folder
# Il faut forward le port 8000 depuis la boucle locale sur la VM
# rajouter dans le Vagrantfile 
#      config.vm.forward_port 8000, 8000
    run('node /vagrant/hello.js')


  
