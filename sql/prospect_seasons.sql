CREATE TABLE prosp_szns(
   Name    VARCHAR(16) NOT NULL
  ,Height  VARCHAR(5) NOT NULL
  ,Weight  INTEGER  NOT NULL
  ,Age     INTEGER  NOT NULL
  ,Season  VARCHAR(7) NOT NULL
  ,School  VARCHAR(24) NOT NULL
  ,Conf    VARCHAR(24) NOT NULL
  ,G       VARCHAR(8) NOT NULL
  ,MP      INTEGER  NOT NULL
  ,FG      NUMERIC(4,1) NOT NULL
  ,FGA     NUMERIC(3,1) NOT NULL
  ,FGP     NUMERIC(4,1) NOT NULL
  ,2P      NUMERIC(4,3) NOT NULL
  ,2PA     NUMERIC(3,1) NOT NULL
  ,2PP     NUMERIC(4,1) NOT NULL
  ,3P      NUMERIC(4,3) NOT NULL
  ,3PA     NUMERIC(3,1) NOT NULL
  ,3PP     NUMERIC(3,1)
  ,FT      NUMERIC(4,3)
  ,FTA     NUMERIC(3,1) NOT NULL
  ,FTP     NUMERIC(3,1) NOT NULL
  ,TRB     NUMERIC(3,1) NOT NULL
  ,AST     NUMERIC(4,1) NOT NULL
  ,STL     NUMERIC(3,1) NOT NULL
  ,BLK     NUMERIC(3,1) NOT NULL
  ,TOV     NUMERIC(3,1) NOT NULL
  ,PF      NUMERIC(3,1) NOT NULL
  ,PTS     NUMERIC(3,1) NOT NULL
);
INSERT INTO prosp_szns VALUES ('Lonzo Ball','6-6',190,19,'2016-17','UCLA','Pac-12',36,35.1,5.3,9.5,.551,3.0,4.1,.732,2.2,5.4,.412,1.8,2.7,.673,6.0,7.6,1.8,0.8,2.5,1.8,14.6);
INSERT INTO prosp_szns VALUES ('Markelle Fultz','6-4',195,18.5,'2016-17','Washington','Pac-12',25,35.7,8.4,17.6,.476,6.3,12.5,.502,2.1,5.0,.413,4.4,6.7,.649,5.7,5.9,1.6,1.2,3.2,2.5,23.2);
INSERT INTO prosp_szns VALUES ('Josh Jackson','6-8',207,19.5,'2016-17','Kansas','Big 12',35,30.8,6.3,12.3,.513,5.3,9.7,.549,1.0,2.6,.378,2.8,4.9,.566,7.4,3.0,1.7,1.1,2.8,3.0,16.3);
INSERT INTO prosp_szns VALUES ('Malik Monk','6-3',200,18.75,'2016-17','Kentucky','SEC',38,32.1,6.6,14.7,.450,3.9,7.8,.497,2.7,6.9,.397,3.9,4.7,.822,2.5,2.3,0.9,0.5,2.0,1.9,19.8);
INSERT INTO prosp_szns VALUES ('DeAaron Fox','6-3',187,19,'2016-17','Kentucky','SEC',36,29.6,5.9,12.4,.478,5.5,10.5,.520,0.5,1.9,.246,4.3,5.9,.739,3.9,4.6,1.5,0.2,2.4,2.5,16.7);
INSERT INTO prosp_szns VALUES ('Jonathan Isaac','6-10',210,19,'2016-17','Florida State','ACC',32,26.2,4.1,8.0,.508,3.1,5.2,.593,1.0,2.8,.348,2.9,3.7,.780,7.8,1.2,1.2,1.5,1.5,2.2,12.0);
INSERT INTO prosp_szns VALUES ('Lauri Markannen','7-0',230,18.75,'2016-17','Arizona','Pac-12',37,30.8,5.0,10.2,.492,3.1,5.8,.545,1.9,4.4,.423,3.7,4.4,.835,7.2,0.9,0.4,0.5,1.1,2.0,15.6);
INSERT INTO prosp_szns VALUES ('Dennis Smith Jr','6-3',195,19,'2016-17','North Carolina State','ACC',32,34.8,6.0,13.1,.455,4.3,8.3,.509,1.7,4.8,.359,4.5,6.3,.715,4.6,6.2,1.9,0.4,3.4,2.1,18.1);
INSERT INTO prosp_szns VALUES ('Jayson Tatum','6-8',205,18.75,'2016-17','Duke','ACC',29,33.3,5.7,12.6,.452,4.3,8.6,.504,1.4,4.0,.342,4.1,4.8,.849,7.3,2.1,1.3,1.1,2.6,3.0,16.8);
INSERT INTO prosp_szns VALUES ('Zach Collins','7-0',230,19,'2016-17','Gonzaga','WCC',39,17.3,3.5,5.3,.652,3.2,4.8,.672,0.3,0.5,.476,2.8,3.8,.743,5.9,0.4,0.5,1.8,1.5,2.7,10.0);
INSERT INTO prosp_szns VALUES ('Harry Giles','6-10',240,18.5,'2016-17','Duke','ACC',26,11.5,1.7,3.0,.577,1.7,3.0,.577,0.0,0.0,NULL,0.5,0.9,.500,3.8,0.3,0.3,0.7,0.7,2.2,3.9);
INSERT INTO prosp_szns VALUES ('OG Anunoby','6-8',215,18.5,'2015-16','Indiana','Big Ten',34,13.7,1.9,3.4,.569,1.6,2.6,.609,0.4,0.9,.448,0.6,1.2,.476,2.6,0.5,0.8,0.8,0.8,1.5,4.9);
INSERT INTO prosp_szns VALUES ('OG Anunoby','6-8',215,19.5,'2016-17','Indiana','Big Ten',16,25.1,4.3,7.6,.557,3.4,4.8,.701,0.9,2.8,.311,1.7,3.0,.563,5.4,1.4,1.3,1.3,1.6,2.1,11.1);
INSERT INTO prosp_szns VALUES ('Jarrett Allen','6-11',235,18.5,'2016-17','Texas','Big 12',33,32.2,5.4,9.6,.566,5.4,9.4,.579,0.0,0.2,.000,2.5,4.5,.564,8.5,0.8,0.6,1.5,2.5,2.1,13.4);
INSERT INTO prosp_szns VALUES ('Luke Kennard','6-5',180,19.5,'2015-16','Duke','ACC',36,26.7,3.9,9.3,.420,2.4,4.5,.528,1.5,4.8,.318,2.4,2.8,.889,3.6,1.5,0.9,0.2,0.8,1.9,11.8);
INSERT INTO prosp_szns VALUES ('Luke Kennard','6-5',180,20.5,'2016-17','Duke','ACC',37,35.5,6.4,13.1,.490,4.0,7.6,.527,2.4,5.4,.438,4.3,5.1,.856,5.1,2.5,0.8,0.4,1.6,2.2,19.5);
INSERT INTO prosp_szns VALUES ('TJ Leaf','6-10',225,19.5,'2016-17','UCLA','Pac-12',35,29.9,6.7,10.9,.617,5.9,9.2,.644,0.8,1.7,.466,2.1,3.0,.679,8.2,2.4,0.6,1.1,1.5,2.5,16.3);
INSERT INTO prosp_szns VALUES ('Ike Anigbogu','6-10',250,18,'2016-17','UCLA','Pac-12',29,13.0,2.0,3.5,.564,2.0,3.5,.564,0.0,0.0,NULL,0.8,1.5,.535,4.0,0.2,0.2,1.2,0.8,2.5,4.7);
INSERT INTO prosp_szns VALUES ('Justin Patton','6-11',215,19.5,'2016-17','Creighton','Big East',35,25.3,5.7,8.5,.676,5.5,8.0,.683,0.2,0.4,.533,1.3,2.5,.517,6.2,1.2,0.9,1.4,1.7,2.7,12.9);
INSERT INTO prosp_szns VALUES ('Tony Bradley','6-10',240,19,'2016-17','UNC','ACC',38,14.6,2.7,4.7,.573,2.7,4.7,.573,0.0,0.0,NULL,1.7,2.8,.619,5.1,0.6,0.3,0.6,0.7,1.8,7.1);
INSERT INTO prosp_szns VALUES ('John Collins','6-10',218,18,'2015-16','Wake Forest','ACC',31,14.4,2.6,4.8,.547,2.6,4.8,.547,0.0,0.0,NULL,2.1,3.0,.691,3.9,0.2,0.3,0.7,1.0,2.6,7.3);
INSERT INTO prosp_szns VALUES ('John Collins','6-10',218,19,'2016-17','Wake Forest','ACC',33,26.6,7.1,11.4,.622,7.1,11.4,.624,0.0,0.0,.000,5.0,6.7,.745,9.8,0.5,0.6,1.6,1.8,3.0,19.2);
INSERT INTO prosp_szns VALUES ('Donovan Mitchell','6-3',210,19,'2015-16','Louisville','ACC',31,19.1,2.7,6.1,.442,2.1,3.8,.559,0.6,2.3,.250,1.4,1.8,.754,3.4,1.7,0.8,0.1,1.0,2.5,7.4);
INSERT INTO prosp_szns VALUES ('Donovan Mitchell','6-3',210,20,'2016-17','Louisville','ACC',34,32.3,5.3,13.1,.408,3.0,6.4,.463,2.4,6.6,.354,2.6,3.2,.806,4.9,2.7,2.1,0.5,1.6,2.6,15.6);
INSERT INTO prosp_szns VALUES ('Edrice Adebayo','6-10',260,19.5,'2016-17','Kentucky','SEC',38,30.1,4.5,7.5,.599,4.5,7.4,.601,0.0,0.0,.000,4.1,6.2,.653,8.0,0.8,0.7,1.5,1.7,2.6,13.0);
INSERT INTO prosp_szns VALUES ('Ivan Rabb','6-11',220,19,'2015-16','University of California','Pac-12',34,28.7,4.7,7.7,.615,4.7,7.6,.615,0.0,0.1,.500,3.0,4.5,.669,8.5,0.9,0.5,1.2,1.5,3.1,12.5);
INSERT INTO prosp_szns VALUES ('Ivan Rabb','6-11',220,20,'2016-17','University of California','Pac-12',31,32.6,4.9,10.1,.484,4.6,9.4,.490,0.3,0.6,.400,4.0,6.0,.663,10.5,1.5,0.7,1.0,2.2,3.1,14.0);
INSERT INTO prosp_szns VALUES ('Justin Jackson','6-8',193,20,'2014-15','UNC','ACC',38,26.7,4.1,8.7,.477,3.4,6.2,.544,0.7,2.4,.304,1.7,2.4,.710,3.7,2.3,0.5,0.5,1.4,1.4,10.7);
INSERT INTO prosp_szns VALUES ('Justin Jackson','6-8',193,21,'2015-16','UNC','ACC',40,28.4,4.9,10.4,.466,4.0,7.4,.537,0.9,3.0,.292,1.6,2.4,.667,3.9,2.8,0.6,0.4,1.1,1.7,12.2);
INSERT INTO prosp_szns VALUES ('Justin Jackson','6-8',193,22,'2016-17','UNC','ACC',40,32.0,6.6,14.9,.443,4.0,7.8,.510,2.6,7.1,.370,2.5,3.3,.748,4.7,2.8,0.8,0.2,1.7,1.4,18.3);
INSERT INTO prosp_szns VALUES ('Moe Wagner','6-10',210,19,'2015-16','Michigan','Big Ten',30,8.6,1.2,2.0,.607,1.2,1.6,.714,0.1,0.4,.167,0.3,0.6,.556,1.6,0.1,0.2,0.2,0.5,1.6,2.9);
INSERT INTO prosp_szns VALUES ('Moe Wagner','6-10',210,20,'2016-17','Michigan','Big Ten',38,23.9,4.4,7.9,.560,3.2,4.9,.661,1.2,3.0,.395,2.0,2.8,.726,4.2,0.5,1.0,0.4,1.4,2.7,12.1);
INSERT INTO prosp_szns VALUES ('DJ Wilson','6-9',220,20,'2015-16','Michigan','Big Ten',26,6.1,1.0,2.2,.474,0.7,1.3,.576,0.3,0.9,.333,0.3,0.4,.727,0.7,0.3,0.2,0.4,0.3,0.8,2.7);
INSERT INTO prosp_szns VALUES ('DJ Wilson','6-9',220,21,'2016-17','Michigan','Big Ten',38,30.4,4.3,8.0,.538,3.2,5.1,.631,1.1,2.9,.373,1.3,1.6,.833,5.3,1.3,0.5,1.5,1.1,1.9,11.0);
INSERT INTO prosp_szns VALUES ('Jawun Evans','6-0',175,19.5,'2015-16','Oklahoma State','Big 12',22,28.9,4.4,9.4,.471,3.5,7.5,.470,0.9,1.8,.475,3.2,3.8,.833,4.4,4.9,1.1,0.2,2.5,2.5,12.9);
INSERT INTO prosp_szns VALUES ('Jawun Evans','6-0',175,20.5,'2016-17','Oklahoma State','Big 12',32,29.3,6.6,15.1,.438,5.5,12.1,.452,1.1,3.0,.379,4.8,6.0,.812,3.4,6.4,1.8,0.1,2.8,2.3,19.2);
INSERT INTO prosp_szns VALUES ('Andrew Jones','6-4',190,19,'2016-17','Texas','Big 12',33,27.9,3.8,8.8,.425,2.5,4.9,.503,1.3,4.0,.328,2.6,3.4,.775,3.9,3.5,1.2,0.4,2.5,2.2,11.4);
INSERT INTO prosp_szns VALUES ('Caleb Swanigan','6-9',260,19,'2015-16','Purdue','Big Ten',34,25.7,3.8,8.3,.461,3.2,6.2,.519,0.6,2.1,.292,2.0,2.8,.713,8.3,1.8,0.4,0.2,2.6,2.2,10.2);
INSERT INTO prosp_szns VALUES ('Caleb Swanigan','6-9',260,20,'2016-17','Purdue','Big Ten',35,32.5,6.3,12.0,.527,5.3,9.6,.548,1.1,2.4,.447,4.7,6.0,.781,12.5,3.0,0.4,0.8,3.4,2.8,18.5);
INSERT INTO prosp_szns VALUES ('Tyler Lydon','6-8',205,20,'2015-16','Syracuse','ACC',37,30.3,3.4,7.2,.479,2.1,3.9,.542,1.3,3.3,.405,1.9,2.5,.774,6.3,1.1,1.1,1.8,1.3,2.7,10.1);
INSERT INTO prosp_szns VALUES ('Tyler Lydon','6-8',205,21,'2016-17','Syracuse','ACC',34,36.1,4.4,9.4,.472,3.0,5.7,.523,1.4,3.7,.392,2.9,3.4,.836,8.6,2.1,1.0,1.4,1.7,2.5,13.2);
