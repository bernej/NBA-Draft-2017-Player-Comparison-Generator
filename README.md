# 2017 NBA Draft Player Generator

How well did the top NBA prospects perform in the NCAA relative to NBA players in the past? This project aims answer that question.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Please note that this setup is for users with OS X and may require extra installation for users with Windows. This setup is the same as the EECS 485 development environment at University of Michigan, and the installation steps are taken from the first discussion.

### Prerequisites

Things you must install on your computer before you fork and clone the repo:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - So you can have an Ubuntu Linux virtual machine.

* [Vagrant](https://www.vagrantup.com/downloads.html) - So the files in the git repo between this Ubuntu vm and your local machine are mapped.

### Setup

Now that VirtualBox and Vagrant are installed, the repo can be forked and cloned. To fork, in the top-right corner of this page click Fork. You now will have an original copy of this repo on your account. On GitHub, navigate to your fork of this repo under the 'Repositories' section on your profile page and click on it. Under the repository name, click Clone or download. In the Clone with HTTPs section, click to copy the clone URL for the repository. It should be in the format:

```
https://github.com/YOUR-USERNAME/NBA-Draft-2017-Player-Comparison-Generator
```

Open Terminal, and type in the following commands:

```
git clone https://github.com/YOUR-USERNAME/NBA-Draft-2017-Player-Comparison-Generator
cd NBA-Draft-2017-Player-Comparison-Generator
vagrant up
```

Now, you are installing the Ubuntu Linux vm on your machine. Once installed, the 'vagrant up' command simply starts the machine. Instead of accessing the vm through VirtualBox we will are accessing the vm through Terminal.

```
vagrant ssh
```

SSH into the vm using ssh keys. You are now accessing your vm through Terminal.

```
cd /vagrant
```

Access the folder that is mapped (which in this case is the git repo).  The vm and your local machine can both read and write files here. You are now in the git repo folder on the vm. Now that the virtual machine is set up, the virtual environment needs to be set up:

```
virtualenv venv
source venv/bin/activate
```

This creates an isolated Python environment. The reason for this is to run in a newer version of Python and so dependencies are isolated from each other.

```
pip install -r requirements.txt
```

Installs PyMySQL, which is the database connector I chose for this project.

## Create the Database of Players

Once the setup is complete, you can now setup the database.

```
mysql -u root -p
root
```

You are now accessing the MySQL server on your vm. Time to create the database:

```
CREATE DATABASE NBA_DRAFT17;
```

You have now created the database that will contain all of the players along with their data.

```
show tables;
```

As you can see, there is no data associated with the NBA_DRAFT17 db as it was just created. Now it's time to insert the data:

```
\. add_comps.sql
\. insert_prospect.sql
```

Both of these SQL scripts insert both the NBA players and prospects' per 40 minute and advanced NCAA data. Now we have all the data we need to run the program.

## Running the program

After exiting out of the MySQL server (type 'exit' or 'quit'), we now have everything needed to run the program.

```
python main.py
```

This will compute similarity scores across all the NBA players inserted into the database to the prospects in the database. The results are split by position, written to 'guards.txt', 'wings.txt', and 'bigs.txt'; 'unique.txt' will contain mappings between prospects and NBA players' NCAA seasons that only appear once in a top 30 per 40 minute or advanced set.

To close the ssh connection to the vm, press CONTROL + D (^D). To shut the vm down, type:

```
vagrant halt
```

If you don't shut the vm down, your CPU usage will go up and slow your computer down.

## Recap

Now that the vm and environment is setup on your local machine, you can run the program in less mandatory steps:

```
vagrant up
vagrant ssh
cd /vagrant
source venv/bin/activate
python main.py
```

## Acknowledgments

* EECS 485 at University of Michigan for the development environment.