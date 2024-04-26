class FilePath:
    file1="C:\\Users\yj250\Desktop\kplDB\KplSystem\photos\login.png"
    file2="C:\\Users\yj250\Desktop\kplDB\KplSystem\photos\information.png"
    file3="C:\\Users\yj250\Desktop\kplDB\KplSystem\photos\系统管理.png"

#1.表创建
"""
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
    Pcaptain INT);#1:队长，0:不是队长
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
"""
#2.数据录入
"""
"""
#1
insert_Player_sql="insert into Player(Pid,Pname,Page,Psex,Plocation)values(:Pid,:Pname,:Page,:Psex,:Plocation)"
sql="insert into Player(Pid,Pname,Page,Psex,Plocation)values('21006','子阳',24,'男','游走')"
Player_list=[
('21001','Fly',25,'男','对抗路'),
('21002','小胖',20,'男','打野'),
('21003','向鱼',21,'男','中路'),
('21004','妖刀',20,'男','发育路'),
('21005','一笙',10,'男','游走')]

data1 = [
    ["21012", "羲和", 20,'男', "游走"],
    ["21013", "酷偕", 21, '男',"对抗路"],
    ["21014", "灵梦", 22, '男',"中路"],
    ["21015", "秀豆", 23, '男',"发育路"],
    ["21016", "九月", 19, '男',"打野"],
    ["21017", "一门", 25, '男',"游走"],
    ["21018", "清清", 24, '男',"对抗路"],
    ["21019", "不然", 23, '男',"打野"],
    ["21020", "风箫", 21, '男',"发育路"],
    ["21021", "帆帆", 22, '男',"游走"],
    ["21022", "紫幻", 23, '男',"中路"]
]


#2.
insert_PT_sql="insert into PT(Pid,Tid,Psalary,Pcaptain) values(:Pid,:Tid,:Psalary,:Pcaptain)"
PT_list=[
('21001','41001',1000000,1),
('21002','41001',2000000,0),
('21003','41001',500000,0),
('21004','41001',500000,0),
('21005','41001',400000,0)
]
#3
insert_Hero_sql="insert into Hero(Hid,Hname,Hrole) values(:Hid,:Hname,:Hrole)"
Hero_list=[
('92001','亚瑟','坦克'),
('92002','项羽','坦克'),
('92003','庄周','辅助'),
('92004','鲁班七号','射手'),
('92005','貂蝉','法师')
]
#4
insert_Team_sql="insert into Team(Tid,Tname,Tcity,Mid) values(:Hid,:Tname,:Tcity,:Mid)"
Team_list=[
('41001','重庆狼队','上海','31001'),#周东泽
('41002','武汉EstPro','武汉','31002'),#何猷君
('41003','广州TTG','广州','31003')#肖剑鹏
]

#5
insert_Coach_sql="insert into Coach(Cid,Cname,Cage,Csex) values(:Cid,:Cname,:Cage,:Csex)"
Coach_list=[
('31001','老林','35','男'),
('31002','黎落','32','男'),
('31003','姚遥','30','女'),
('31004','久哲','31','男'),
('31005','张角','33','男')
]

#6
insert_Manager_sql='insert into Manager(Mid,Mname,Mage,Msex) values(:Mid,:Mname,:Mage,:Msex)'
Manager_list=[
('51001','周东泽','40','男'),
('51002','何猷君','30','男'),
('51003','肖剑鹏','38','女'),
('51004','赵邓起','37','男'),
('51005','言豫津','35','男')
]

users_sql="""
    CREATE TABLE USERS(
    Uname VARCHAR(10) PRIMARY KEY,  
    Upassword VARCHAR(6)NOT NULL
)
    """
insert_users_sql="insert into user_table('Uname','Upassword') values(:Uname,:Upassword)"
users_list=[('zhl','123456')]

from dsa.database import OracleDB
if __name__ == "__main__":
    sql_id = "select*from Player where Pid=:Pid"
    try:
        db = OracleDB()
        db.connect()
        #db.executemany(insert_Player_sql,Player_list)
        #db.executemany(insert_PT_sql,PT_list)
        #db.executemany(insert_Hero_sql,Hero_list)
        #db.executemany(insert_Team_sql,Team_list)
        #db.executemany(insert_Coach_sql,Coach_list)
        #db.executemany(insert_Manager_sql,Manager_list)
        # db.executemany(insert_users_sql,users_list)
        db.executemany(insert_Player_sql, data1)
        #查看
        # print(result)
        # print(len(result))
        # r=db.query("select*from player")
        # print(r)
        # db.close()
    except Exception as e:
        # 发生错误时回滚事务
        db.conn.rollback()
        print(f"Error: {e}")
    finally:
        db.close()






