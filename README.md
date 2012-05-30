Test Vagrant
====

Sur l'hote 

Installation des outils et téléchargement de la VM ubuntu server
> $ sudo apt-get install vagrant
> $ sudo apt-get install fabric
> $ vagrant box add ubuntu-server http://timhuegdon.com/vagrant-boxes/ubuntu-11.10.box

$ cd test_vagrant

//Creation du Vagrantfile permettant la config de la VM
$ vagrant init ubuntu-server


//Modifier le Vagrantfile ainsi créé en ajoutant la ligne
//  config.vm.forward_port 8000, 8000
//Elle forward le port sur la VM
$ echo  config.vm.forward_port 8000, 8000  >>  Vagrantfile 

//Lancement de la VM
$ vagrant up

//Lancement du script
//Si le port 22 est bien routé sur le port 2200
$ fab -H vagrant@localhost:2200 install
//   mot de passe : vagrant
