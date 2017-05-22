CREATE TABLE prosp_per40(
   Player VARCHAR(19) NOT NULL
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
INSERT INTO prosp_per40 VALUES ('TJ Leaf', '2016-17','UCLA','Pac-12',35,1048,9.0,14.5,.617,7.9,12.3,.644,1.0,2.2,.466,2.7,4.0,.679,11.0,3.2,0.8,1.5,2.0,3.4,21.7);
INSERT INTO prosp_per40 VALUES ('Jawun Evans','2016-17','Oklahoma State','Big 12',32,936,9.0,20.6,.438,7.5,16.5,.452,1.5,4.1,.379,6.6,8.2,.812,4.7,8.7,2.4,0.2,3.8,3.2,26.2);
INSERT INTO prosp_per40 VALUES ('Semi Ojeleye','2016-17','SMU','AAC',35,1195,7.0,14.3,.488,4.6,8.6,.531,2.4,5.8,.424,5.8,7.3,.785,8.0,1.8,0.5,0.5,1.7,2.1,22.2);
INSERT INTO prosp_per40 VALUES ('DJ Wilson','2016-17','Michigan','Big Ten',38,1155,5.7,10.6,.538,4.3,6.8,.631,1.4,3.8,.373,1.7,2.1,.833,7.0,1.7,0.7,2.0,1.5,2.5,14.5);
INSERT INTO prosp_per40 VALUES ('Justin Jackson','2016-17','Maryland','Big Ten',33,919,5.1,11.6,.438,3.1,7.1,.438,2.0,4.6,.438,2.9,4.2,.698,8.7,1.3,1.3,1.1,2.4,3.1,15.1);
INSERT INTO prosp_per40 VALUES ('Derrick White','2016-17','Colorado','Pac-12',34,1116,7.3,14.5,.507,5.3,9.3,.569,2.0,5.2,.396,5.3,6.5,.813,5.0,5.3,1.5,1.8,2.9,2.6,22.0);
INSERT INTO prosp_per40 VALUES ('Jordan Bell','2016-17','Oregon','Pac-12',39,1124,6.1,9.6,.636,6.0,9.1,.659,0.1,0.5,.214,2.9,4.2,.701,12.2,2.5,1.7,3.1,2.7,2.5,15.2);
INSERT INTO prosp_per40 VALUES ('Harry Giles','2016-17','Duke','ACC',26,300,6.0,10.4,.577,6.0,10.4,.577,0.0,0.0,.000,1.6,3.2,.500,13.3,1.2,1.2,2.3,2.4,7.7,13.6);
INSERT INTO prosp_per40 VALUES ('Caleb Swanigan','2016-17','Purdue','Big Ten',35,1139,7.8,14.8,.527,6.5,11.8,.548,1.3,3.0,.447,5.8,7.4,.781,15.3,3.7,0.5,1.0,4.1,3.4,22.7);
INSERT INTO prosp_per40 VALUES ('Alec Peters','2016-17','Valparaiso','Horizon',29,1019,8.6,18.4,.466,6.3,12.1,.519,2.3,6.3,.363,6.8,7.6,.887,11.5,2.5,0.9,0.4,2.8,2.5,26.1);
INSERT INTO prosp_per40 VALUES ('Edrice Adebayo','2016-17','Kentucky','SEC',38,1145,5.9,9.9,.599,5.9,9.9,.601,0.0,0.0,.000,5.4,8.2,.653,10.6,1.1,0.9,2.0,2.2,3.5,17.3);
INSERT INTO prosp_per40 VALUES ('Thomas Bryant','2016-17','Indiana','Big Ten',34,954,6.2,11.9,.519,5.2,9.4,.556,1.0,2.5,.383,4.5,6.2,.730,9.5,2.1,1.1,2.2,3.3,4.4,17.9);
INSERT INTO prosp_per40 VALUES ('Johnathan Motley','2016-17','Baylor','Big 12',34,1036,8.7,16.7,.522,8.4,15.5,.541,0.3,1.2,.281,4.9,7.1,.699,12.9,3.1,0.5,1.4,3.9,4.0,22.7);
INSERT INTO prosp_per40 VALUES ('Tony Bradley','2016-17','UNC','ACC',38,553,7.4,12.9,.573,7.4,12.9,.573,0.0,0.0,.000,4.7,7.6,.619,14.1,1.7,0.7,1.6,1.8,5.0,19.5);
INSERT INTO prosp_per40 VALUES ('Frank Jackson','2016-17','Duke','ACC',36,895,5.9,12.6,.473,3.7,6.7,.543,2.3,5.8,.392,3.4,4.6,.755,4.1,2.7,0.9,0.1,2.2,3.8,17.6);
INSERT INTO prosp_per40 VALUES ('Kyle Kuzma','2016-17','Utah','Pac-12',29,894,8.1,16.2,.504,6.9,12.4,.560,1.2,3.8,.321,3.8,5.7,.669,12.1,3.2,0.8,0.6,2.8,2.1,21.3);
INSERT INTO prosp_per40 VALUES ('Frank Mason','2016-17','Kansas','Big 12',36,1301,7.4,15.1,.490,4.9,9.8,.500,2.5,5.3,.471,5.8,7.3,.794,4.6,5.7,1.4,0.1,2.6,2.2,23.2);
INSERT INTO prosp_per40 VALUES ('LJ Peak','2016-17','Georgetown','Big East',32,1051,6.4,13.2,.480,5.1,9.4,.543,1.3,3.8,.327,5.8,7.3,.796,4.6,4.2,1.3,0.5,3.3,3.3,19.8);
INSERT INTO prosp_per40 VALUES ('Tyler Dorsey','2016-17','Oregon','Pac-12',39,1169,6.5,13.9,.467,3.5,6.7,.513,3.0,7.1,.423,3.6,4.8,.755,4.6,2.3,1.0,0.1,2.0,2.0,19.5);
INSERT INTO prosp_per40 VALUES ('Devin Robinson','2016-17','Florida','SEC',36,952,6.0,12.6,.475,4.2,7.9,.524,1.8,4.6,.391,3.1,4.2,.723,9.2,1.0,1.3,1.2,1.6,3.4,16.8);
INSERT INTO prosp_per40 VALUES ('Josh Hart','2016-17','Villanova','Big East',36,1193,7.9,15.5,.510,5.4,9.4,.579,2.5,6.1,.404,4.3,5.7,.747,7.7,3.6,1.8,0.3,2.4,2.7,22.6);
INSERT INTO prosp_per40 VALUES ('Sindarius Thornwell','2016-17','South Carolina','SEC',31,1051,7.4,16.7,.445,5.2,11.1,.471,2.2,5.6,.395,8.2,9.9,.830,8.4,3.3,2.5,1.1,2.9,2.7,25.2);
INSERT INTO prosp_per40 VALUES ('Nigel Williams-Goss','2016-17','Gonzaga','WCC',38,1248,7.1,14.5,.486,5.7,10.8,.527,1.4,3.8,.368,5.0,5.8,.867,7.3,5.7,2.1,0.1,2.6,1.9,20.5);
INSERT INTO prosp_per40 VALUES ('Monte Morris','2016-17','Iowa State','Big 12',35,1237,7.0,15.0,.465,5.2,10.4,.503,1.7,4.6,.378,2.9,3.6,.802,5.5,7.0,1.7,0.3,1.4,1.6,18.6);
INSERT INTO prosp_per40 VALUES ('Nigel Hayes','2016-17','Wisconsin','Big Ten',37,1190,6.1,13.2,.457,5.3,10.9,.488,0.7,2.4,.314,4.5,7.7,.587,8.2,3.4,0.9,0.5,2.1,2.3,17.4);
INSERT INTO prosp_per40 VALUES ('Moe Wagner','2016-17','Michigan','Big Ten',38,908,7.4,13.2,.560,5.4,8.2,.661,2.0,5.0,.395,3.4,4.7,.726,7.0,0.9,1.7,0.6,2.4,4.5,20.2);
INSERT INTO prosp_per40 VALUES ('Isaiah Briscoe','2016-17','Kentucky','SEC',36,1095,6.0,12.7,.470,5.3,10.5,.507,0.6,2.2,.288,3.4,5.4,.635,7.1,5.6,1.1,0.3,3.3,3.4,16.0);
INSERT INTO prosp_per40 VALUES ('Dwayne Bacon','2016-17','Florida State','ACC',35,1008,8.8,19.4,.452,6.5,12.6,.516,2.3,6.8,.333,4.1,5.5,.754,5.8,2.4,1.4,0.2,2.8,2.2,23.9);



