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

## Results

Below is my top 10 ranking of the consensus top 10 freshmen and some words to make sense of the results. I include three interesting comparisons the system found that I believe are somewhat fitting based on similar playing styles. I will give two highly successful comps that appeared, which represent the prospects' ceilings, followed by a realistic comp that appeared.

### My Favorite Four

*1.* **Lonzo Ball** - Jason Kidd, Jason Williams, Deron Williams

The most unique prospect in the dataset. Lonzo’s unprecedented advanced stats caused extremely low similarity scores in the adv set. Curiously enough, all four of TJ McConnell’s college seasons were returned, and TJ’s freshman year at Duquesne was the highest scored season in the intersection set. The comparisons to Jason Kidd are validated with the only Kidd season (the more impressive Sophomore season) appearing in the per40 set. Interestingly, another passing magician makes his lone appearance here, Jason Williams with his Marshall season. Lonzo’s absurd open-court playmaking skills and NBA range are why I give him the slight edge over Fultz.

*2.* **Markelle Fultz** - Russell Westbrook, Sam Cassell, George Hill

Only one NBA legend could match Markelle’s all-around college output of 20/5/5 and 1 block per game (Penny Hardaway). Unfortunately Penny wasn’t returned in any prospect’s top 30 set. Reggie Jackson’s final season at Boston College is the highest scored in the intersection set, showing what Fultz’s floor is. Russell Westbrook’s freshman season makes its lone appearance in the per40 set, but that was mostly due to a vector error. However, their shooting lines are eerily similar (Fultz: 0.476 FG% / 0.502 2P% / 0.413 3P% /0.649 FT% | Westbrook: 0.457 FG% / 0.470 2P% / 0.409 3P% / 0.548 FT%). Also, Sam Cassell’s sophomore FSU season makes its lone appearance here, as well as his freshman season. While Fultz projects to be more of a scorer, Cassell produced a positive VORP in each of his 14 seasons, so it’s nice to see two of his college seasons appearing here. Fultz is going to get buckets in his career, and his long wingspan gives him some interesting, untapped defensive potential.

*3.* **De'Aaron Fox** - Dwyane Wade, John Wall, Marcus Smart

The only prospect to return a Dwyane Wade Marquette season, which was his Sophomore season. Their offensive games are similar (high FT’s, mid 70s FT%, low 3P%, a love for the midrange, and most of all killer speed & quickness). However, he'll need to bulk up more to be a PG version of DWade. Additionally, Fox was one of three guards to return John Wall’s Kentucky season (along with Dennis Smith and Jawun Evans). Interestingly, Fox was the only guard to return a Jeremy Lin Harvard season, and the only guard to return Speedy (pun initiated) Claxton’s freshman Hofstra season. His intersection set isn’t kind to him with the likes of Nate Wolters, Ray McCallum, Tim Frazier, Jordan Clarkson, and Delon Wright. However, those were all upperclassmen seasons, besides Wright’s, to which it was his sophomore year. I slot Fox this high because of his elite speed, potential for ferocious PG defense, as well as his high FT% being a promising indicator of his jumper improving when he gets stronger.

*4.* **Josh Jackson** - Richard Jefferson, Josh Howard, Justise Winslow

He can seemingly do everything on a basketball court besides shoot. There was only one player in his intersection set, and that was Justise Winslow. I think this is one of the more accurate results in the system as they have a lot of the same characteristics, except Jackson might be a better playmaker and is taller. A better playmaking, taller version of Winslow is an extremely intriguing prospect. Here’s to hoping they both find their jumpers. If Jackson solves his shot, I’m not sure there is a hole in his game. I rate him below Fox because I’m not sure he’ll ever be the primary playmaker on a good team, which I think Fox can be. However, Jackson competes like crazy and stuffs the stat sheet enough to be a super role player on a talented team.

### The Wildcards

*5.* **Jonathan Isaac** - Otto Porter, Wilson Chandler, Al-Farouq Aminu

Speaking of super role players, Jon Isaac has the potential to be one of the most ridiculous 3&D creatures the league has ever seen. Al-Farouq Aminu makes his lone appearance here, showing what Isaac’s potential role could be in the NBA; a 3, 4, or small-ball 5. Except, Isaac exceeded Aminu’s 3P% and FT% in college. Isaac might have a higher ceiling than Josh Jackson due to his shooting and extra rim protection, but might have the lowest floor out of all the high lottery prospects. Is he too much of a tweener? Does he have the foot-speed to keep up with NBA guards? Is he ever going to be a playmaker on offense? These questions keep him below Jackson, but his absurd 3&D ceiling at his insane height keep him in the top 5. Adreian Payne’s MSU junior year was the highest scored season in the intersection set, highlighting how much of a question mark Isaac is.

*6.* **Dennis Smith Jr.** - Isaiah Thomas, Derrick Rose, Eric Bledsoe

Wildcard of the draft. He could be an uber-athletic, scoring PG in the mold of Derrick Rose, whose Memphis season appears here. But will he create enough for others? Will he compete defensively? Smith’s athleticism is undeniable, he has a solid handle, and appears to have shooting ability, giving him decent offensive potential. He probably has more defensive potential as well. He seems to have a high ceiling but a low floor, which makes him the wildcard of the guards, much like Isaac is the wildcard of the forwards. Isaiah Thomas’ final season at Washington was the highest scored season in the intersection set, showing that he has the tools to be a dynamic scoring guard. Bob Sura’s senior season at FSU makes its lone appearance here. Bob Sura was a decent role player for 10 years and made a dunk contest appearance, which I think encapsulates a realistic outcome for Dennis Smith.

### The Safe Bets to be Good Role Players

*7.* **Jayson Tatum** - Kevin Durant, Michael Redd, Tobias Harris

Tatum seems to be able to do pretty much everything on the court, just not in an elite manner (besides FT shooting). Tim Thomas’ only season at Villanova makes its only appearance here for Tatum. He is an interesting comp, selected 7th overall in ’97. He was a combo-forward, role player with decent scoring ability for 13 years who racked up 35.2 win shares over his career. I don’t see Tatum as being the go to guy or having the elite role player skills that Jackson and Isaac do, but he could easily become the best scorer of the forwards. I could be underrating him, but I see Jackson and Isaac having more of an impact in other facets of the game and Dennis Smith Jr. having a higher ceiling. Quincy Miller’s lone season at Baylor is the highest scored in the intersection set, which I don’t know what to make out of.

*8.* **Lauri Markkanen** - Ryan Anderson, Keith Van Horn, Jon Leuer

Both of Ryan Anderson's Cal seasons ranked first and third in Markkanen's per40 set. Seven footers that can shoot an elite clip (42% on 5.7 3PA for Markkanen) are valuable commodities; 7 footers that can’t protect the rim, however aren’t. Much like Ryan Anderson, Markkanen can’t protect the rim (0.7 blocks per 40 minutes). Yet, Ryan Anderson just shot 40% from three on 7 attempts per game. That is valuable. I see Markkanen having a long career and having a positive offensive contribution to a team. Defensively, I’m not sure what he is yet. Pair him with a rim protecting center and have him be a stretch 4 for now. If he’s the 5 in a lineup, I don’t know how good the team's defense will be, unless he becomes a better rim protector.

### The Could-be Busts or Good Role Players

*9.* **Malik Monk** - JJ Redick, Devin Booker, Arron Afflalo

Monk unfortunately appears to be a SG in a PG body. A lot of great college shooters who are defensive liabilities have flamed out in the NBA, even while being lottery picks. Case in point: Jimmer Fredette’s AP POY season at BYU makes its lone appearance in the system in Monk's per40 set. Shawn Respert is the scariest comp here. His final two MSU seasons appear here and he was quite lethal from 3 those years (45% on 6.4 3PA and 47% on 9.0 3PA). Here’s the catch though: Respert was a 6-1 SG who was selected 8th overall in the ’95 Draft; Respert played 4 seasons and never lived up to his draft slot. Isaiah Canaan is another SG in a PG body that makes an appearance here. It’s tough seeing Monk as a starter unless he improves his playmaking, defense, and PG skills. Lindsey Hunter is a realistic outcome here, a 6-2 combo guard who was a solid role player for 16 years. Seth Curry’s final year at Duke was the highest scored season in the intersection set, and he just had a solid year for Dallas.

*10.* **Zach Collins** - Chris Bosh, Kevin Love, Richaun Holmes

Richaun Holmes’ final two Bowling Green seasons are Zach Collins’ top two similar seasons in the intersection set. If Collins can encapsulate what Holmes brings to the table (energy, shot blocking, and not being a black-hole on offense), then he will be a servicaeble backup big with the potential to eventually start. He's got to stop fouling so much, though.

Feel free to check out all of the results in the [guards.txt](https://github.com/bernej/NBA-Draft-2017-Player-Comparison-Generator/blob/master/guards.txt), [wings.txt](https://github.com/bernej/NBA-Draft-2017-Player-Comparison-Generator/blob/master/wings.txt), and [bigs.txt](https://github.com/bernej/NBA-Draft-2017-Player-Comparison-Generator/blob/master/bigs.txt) files!

## Acknowledgments

* [sports-reference](http://www.sports-reference.com/cbb/) for the NCAA data.

* [basketball-reference](http://www.basketball-reference.com/) for the NBA data.

* EECS 485 at University of Michigan for the development environment.