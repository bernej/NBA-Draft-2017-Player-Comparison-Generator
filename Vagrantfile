Vagrant.configure(2) do |config|
  # Install hashicorp/precise32 as the base OS (this is Ubuntu)
  # There is a directory of vagrant boxes you can choose from here:
  # https://atlas.hashicorp.com/boxes/search

  config.vm.box = "bento/ubuntu-16.04"

  # Forward the 3000 port from the VM to your local machine so you can use your
  # local browser while running the dev environment on your VM
  config.vm.network "forwarded_port", guest: 3000, host: 3000

  # Name your virtual machine
  config.vm.provider "virtualbox" do |v|
    v.name = "eecs485_dev_box"
  end

  # Run vagrant.sh the first time a VM is set up
  # If you halt the machine and come back to it, this won't run again but if you
  # destroy the VM and come back to it, this will run again

  config.vm.provision :shell, path: "vagrant.sh"
end
