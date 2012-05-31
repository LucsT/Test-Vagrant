Test Vagrant
====

Sur l'hote  


Récupération de l'archive  
> $ git clone git@github.com:LucsT/Test-Vagrant.git

Installation des outils et téléchargement de la VM ubuntu server
> $ sudo apt-get install vagrant  
> $ sudo apt-get install fabric  
> $ vagrant box add ubuntu-server http://timhuegdon.com/vagrant-boxes/ubuntu-11.10.box  


> $ cd Test-Vagrant

Creation du Vagrantfile permettant la config de la VM
> $ vagrant init ubuntu-server


Modifier le Vagrantfile ainsi créé en ajoutant la ligne  
	 config.vm.forward_port 8000, 8000  
Elle forward le port sur la VM  
> $ echo  config.vm.forward_port 8000, 8000  >>  Vagrantfile 

Lancement de la VM
> $ vagrant up

Lancement du script  
Si le port 22 est bien routé sur le port 2200
Possibilité de rerouter sur le port de votre choix manuellement sinon cf shell de pendant le lancement de la VM
> $ fab -H vagrant@localhost:2200 install  

mot de passe : vagrant

Le Hello World devrait donc être affichable depuis l'hôte à l'adresse http://localhost:8000


