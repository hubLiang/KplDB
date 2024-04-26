--1.表创建
/*
Player(Pid#,Pname,Page,Psex,Plocation)Pname非空、Plocation（对抗路、中路、打野、发育路、游走）
PT(Pid#,Tid,Psalary,Pcaptain)  外码Tid，Pcaptain:0或1
Hero(Hid#,Hname,Hrole)
Team(Tid#,Tname,Tcity,Mid)   外码Mid 
Coach(Cid#,Cname,Cage,Csex)
CT(Cid#,Tid,Csalary)         外码Tid
Manager(Mid#,Mname,Mage,Msex)
League(Lid#,Lname,Llevel,Lrule)
Skilled(Pid#,Hid#,Sdegree) 
Attend(Tid#,Lid#,Tpoints)
*/
-- Player表
CREATE TABLE Player(
    Pid CHAR(5) NOT NULL UNIQUE, 
    Pname VARCHAR(6) NOT NULL,                   
    Page INT,                      
    Psex CHAR(2), 
    Plocation VARCHAR(6)
);
--PT表
CREATE TABLE PT(
    Pid CHAR(5) PRIMARY KEY, 
    Tid CHAR(5) NOT NULL,                   
    Psalary INT,                      
    Pcaptain INT
);
--Hero表
CREATE TABLE Hero(
    Hid CHAR(5) NOT NULL UNIQUE, 
    Hname VARCHAR(8) NOT NULL,                   
    Hrole CHAR(4)                   
);
--Team表
CREATE TABLE Team(
    Tid CHAR(5) NOT NULL UNIQUE, 
    Tname VARCHAR(12) NOT NULL,                   
    Tcity CHAR(4),                      
    Mid CHAR(5)
);
--Coach表
CREATE TABLE Coach(
    Cid CHAR(5) NOT NULL UNIQUE, 
    Cname VARCHAR(6) NOT NULL,                   
    Cage INT,                      
    Csex CHAR(2)
);
--CT表
CREATE TABLE CT(
    Cid CHAR(5) NOT NULL UNIQUE, 
    Tid CHAR(5) NOT NULL,                   
    Csalary INT                     
);
--Manager表
CREATE TABLE Manager(
    Mid CHAR(5) NOT NULL UNIQUE, 
    Mname VARCHAR(6) NOT NULL,                   
    Mage INT,   
    Msex  CHAR(2)
);
--League表
CREATE TABLE League(
    Lid CHAR(5) NOT NULL UNIQUE, 
    Lname VARCHAR(12) NOT NULL,                   
    Llevel CHAR(4),   
    Lrule  VARCHAR(20)
);
--Skilled表
CREATE TABLE Skilled(
    Pid CHAR(5) NOT NULL, 
    Hid CHAR(5) NOT NULL,                   
    Sdegree VARCHAR(8),
    PRIMARY KEY (Pid,Hid)
);
--Attend表
CREATE TABLE Attend(
    Tid CHAR(5) NOT NULL,
    Lid CHAR(5) NOT NULL,                   
    Tpoints INT,
    PRIMARY KEY (Tid,Lid)
);

--Team
DROP TABLE Player;
DROP TABLE PT;
DROP TABLE Hero;
DROP TABLE Team;
DROP TABLE Coach;
DROP TABLE CT;
DROP TABLE Manager;
DROP TABLE League;
DROP TABLE Skilled;
DROP TABLE Attend;


--数据插入
insert into PT(Hid,Hname,Hrole) values('92001','亚瑟','坦克');

select*from Player;
select*from Coach;
select*from Manager;
select*from PT;
select*from CT;
select*from Hero;
select* from Team;
select* from Attend;
select* from LEAGUE;
select Team.*from Team;

select Player.Pid,Psalary,Pcaptain,Tname 
from Player,PT,Team 
where Player.Pid=PT.Pid and PT.Tid=Team.Tid;


select Coach.* ,Csalary,Tname from Coach,CT,Team where Coach.Cid=CT.Cid and CT.Tid = Team.Tid  order by Cage;
                  
delete from player where Pid='21009';


--创建用户表
CREATE TABLE USERS(
    Uname VARCHAR(10) PRIMARY KEY,  
    Upassword VARCHAR(6)NOT NULL
);

 

DROP TABLE USERS;
