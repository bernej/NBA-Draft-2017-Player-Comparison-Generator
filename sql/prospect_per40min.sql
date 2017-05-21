CREATE TABLE prosp_per40(
   Player VARCHAR(16) NOT NULL PRIMARY KEY
  ,Season VARCHAR(7) NOT NULL
  ,School VARCHAR(20) NOT NULL
  ,Conf   VARCHAR(8) NOT NULL
  ,G      INTEGER  NOT NULL
  ,MP     INTEGER  NOT NULL
  ,FG     NUMERIC(3,1) NOT NULL
  ,FGA    NUMERIC(4,1) NOT NULL
  ,FGP    NUMERIC(4,3) NOT NULL
  ,2P     NUMERIC(3,1) NOT NULL
  ,2PA    NUMERIC(4,1) NOT NULL
  ,2PP    NUMERIC(4,3) NOT NULL
  ,3P     NUMERIC(3,1) NOT NULL
  ,3PA    NUMERIC(3,1) NOT NULL
  ,3PP    NUMERIC(4,3)
  ,FT     NUMERIC(3,1) NOT NULL
  ,FTA    NUMERIC(3,1) NOT NULL
  ,FTP    NUMERIC(4,3) NOT NULL
  ,TRB    NUMERIC(4,1) NOT NULL
  ,AST    NUMERIC(3,1) NOT NULL
  ,STL    NUMERIC(3,1) NOT NULL
  ,BLK    NUMERIC(3,1) NOT NULL
  ,TOV    NUMERIC(3,1) NOT NULL
  ,PF     NUMERIC(3,1) NOT NULL
  ,PTS    NUMERIC(4,1) NOT NULL
);
INSERT INTO prosp_per40 VALUES ('Lonzo Ball','2016-17','UCLA','Pac-12',36,1263,6.0,10.9,.551,3.5,4.7,.732,2.5,6.1,.412,2.1,3.1,.673,6.8,8.7,2.1,0.9,2.8,2.1,16.6);
INSERT INTO prosp_per40 VALUES ('Markelle Fultz','2016-17','Washington','Pac-12',25,892,9.4,19.7,.476,7.0,14.0,.502,2.3,5.7,.413,4.9,7.5,.649,6.4,6.6,1.7,1.3,3.6,2.8,26.0);
INSERT INTO prosp_per40 VALUES ('Josh Jackson','2016-17','Kansas','Big 12',35,1077,8.2,15.9,.513,6.9,12.6,.549,1.3,3.3,.378,3.6,6.4,.566,9.6,3.9,2.2,1.4,3.6,3.9,21.2);
INSERT INTO prosp_per40 VALUES ('Malik Monk','2016-17','Kentucky','SEC',38,1218,8.2,18.3,.450,4.8,9.7,.497,3.4,8.6,.397,4.9,5.9,.822,3.1,2.9,1.2,0.6,2.5,2.4,24.8);
INSERT INTO prosp_per40 VALUES ('DeAaron Fox','2016-17','Kentucky','SEC',36,1064,8.0,16.8,.478,7.4,14.2,.520,0.6,2.6,.246,5.9,7.9,.739,5.3,6.2,2.0,0.3,3.3,3.4,22.6);
INSERT INTO prosp_per40 VALUES ('Jonathan Isaac','2016-17','Florida State','ACC',32,839,6.2,12.2,.508,4.7,8.0,.593,1.5,4.2,.348,4.4,5.6,.780,12.0,1.8,1.8,2.3,2.3,3.3,18.3);
INSERT INTO prosp_per40 VALUES ('Lauri Markkanen','2016-17','Arizona','Pac-12',37,1140,6.5,13.2,.492,4.1,7.5,.545,2.4,5.7,.423,4.8,5.8,.835,9.3,1.1,0.5,0.7,1.4,2.6,20.2);
INSERT INTO prosp_per40 VALUES ('Dennis Smith Jr.','2016-17','North Carolina State','ACC',32,1114,6.9,15.1,.455,4.9,9.6,.509,2.0,5.5,.359,5.1,7.2,.715,5.2,7.1,2.2,0.5,3.9,2.4,20.8);
INSERT INTO prosp_per40 VALUES ('Jayson Tatum','2016-17','Duke','ACC',29,966,6.8,15.1,.452,5.2,10.3,.504,1.7,4.8,.342,4.9,5.8,.849,8.8,2.6,1.6,1.4,3.1,3.6,20.2);
INSERT INTO prosp_per40 VALUES ('Zach Collins','2016-17','Gonzaga','WCC',39,673,8.0,12.3,.652,7.4,11.1,.672,0.6,1.2,.476,6.5,8.8,.743,13.6,1.0,1.1,4.1,3.6,6.2,23.2);
INSERT INTO prosp_per40 VALUES ('Donovan Mitchell', '2016-17', 'Louisville', 'ACC',34,1098,6.6,16.2,.408,3.7,7.9,.463,2.9,8.2,.354,3.2,3.9,.806,6.0,3.4,2.6,0.6,2.0,3.2,19.3);
INSERT INTO prosp_per40 VALUES ('Justin Jackson', '2016-17', 'UNC', 'ACC',40,1281,8.2,18.6,.443,5.0,9.7,.510,3.3,8.9,.370,3.1,4.1,.748,5.8,3.5,1.0,0.3,2.2,1.7,22.8);
INSERT INTO prosp_per40 VALUES ('OG Anunoby', '2016-17', 'Indiana', 'Big Ten',16,402,6.8,12.1,.557,5.4,7.7,.701,1.4,4.5,.311,2.7,4.8,.563,8.7,2.3,2.1,2.1,2.6,3.3,17.6);
INSERT INTO prosp_per40 VALUES ('Ike Anigbogu', '2016-17','UCLA','Pac-12',29,377,6.0,10.7,.564,6.0,10.7,.564,0.0,0.0,.000,2.4,4.6,.535,12.4,0.6,0.5,3.7,2.5,7.6,14.5);
INSERT INTO prosp_per40 VALUES ('Luke Kennard', '2016-17','Duke','ACC',37,1314,7.2,14.7,.490,4.5,8.6,.527,2.7,6.1,.438,4.9,5.7,.856,5.7,2.8,0.9,0.4,1.8,2.5,22.0);
INSERT INTO prosp_per40 VALUES ('Jarrett Allen', '2016-17','Texas','Big 12',33,1061,6.7,11.9,.566,6.7,11.6,.579,0.0,0.3,.000,3.2,5.6,.564,10.5,1.0,0.7,1.9,3.2,2.6,16.7);
INSERT INTO prosp_per40 VALUES ('John Collins', '2016-17','Wake Forest','ACC',33,878,10.7,17.1,.622,10.7,17.1,.624,0.0,0.0,.000,7.5,10.0,.745,14.8,0.8,1.0,2.4,2.7,4.5,28.8);
INSERT INTO prosp_per40 VALUES ('Justin Patton', '2016-17','Creighton','Big East',35,885,9.0,13.4,.676,8.7,12.7,.683,0.4,0.7,.533,2.0,3.9,.517,9.8,1.9,1.4,2.3,2.7,4.3,20.5);
INSERT INTO prosp_per40 VALUES ('Tyler Lydon','2016-17','Syracuse','ACC',34,1227,4.9,10.4,.472,3.3,6.4,.523,1.6,4.1,.392,3.2,3.8,.836,9.6,2.3,1.1,1.6,1.9,2.7,14.6);
INSERT INTO prosp_per40 VALUES ('Ivan Rabb','2016-17','Cal','Pac-12',31,1012,6.0,12.3,.484,5.7,11.5,.490,0.3,0.8,.400,4.9,7.4,.663,12.8,1.9,0.8,1.2,2.6,3.8,17.2);
