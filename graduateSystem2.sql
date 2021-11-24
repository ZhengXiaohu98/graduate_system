/*student table actions*/
drop table if exists student;

create table student(
sid	int primary key auto_increment,
stuName varchar(36) NOT NULL,
username varchar(8) NOT NULL,
pw varchar(12) DEFAULT '123456',
gender varchar(1) DEFAULT 'M',
GPA float,
email varchar(64),
cp_num integer DEFAULT 0,
class_taking integer DEFAULT 0,
class_taken integer DEFAULT 0,
curStatus integer DEFAULT 0
);

insert into student(stuName, username, pw, gender, GPA, email, cp_num, class_taking, class_taken, curStatus)
	values("Xiaohu", "23708726", "123456", "M", 3.5, "xzheng@gmail.com", 0, 3, 2, 1),
		("howard", "23708727", "123456", "M", 4.0, "howard@gmail.com", 0, 2, 2, 1),
        ("yangying", "23508726", "123456", "F", 4.0, "yangying@gmail.com", 0, 3, 3, 1),
        ("Kevin", "20358726", "123456", "M", 3.0, "Kevin@gmail.com", 0, 2, 1, 1),
        ("Alice", "23845726", "123456", "F", 0.75, "Alice@gmail.com", 0, 0, 4, 0),
        ("Jack", "23706526", "123456", "M", 2.6, "Jack@gmail.com", 0, 0, 9, 1),
        ("Jay", "23732726", "123456", "M", 2.5, "JayC@gmail.com", 0, 0, 8, 2),
        ("Victor", "23712726", "123456", "M", 3.7, "Victor@gmail.com", 0, 3, 3, 2),
        ("Zoe", "23701526", "123456", "F", 3.9, "Zoe@gmail.com", 0, 3, 6, 1),
        ("Tommy", "23703226", "123456", "M", 3.3, "Tommy@gmail.com", 0, 2, 4, 1),
        ("Lucy", "23208726", "123456", "M", 2.9, "Lucy@gmail.com", 0, 3, 3, 1),
        ("Wei", "13768826", "123456", "M", 2.8, "wei@gmail.com", 0, 2, 3, 1),
        ("Dido", "51236849", "123456", "M", 2.7, "Dido@gmail.com", 0, 2, 4, 1),
        ("Alex", "12356849", "123456", "F", 3.8, "Alex@gmail.com", 3, 3, 0, 2),
        ("Mike", "65849562", "123456", "M", 3.8, "Mike@gmail.com", 0, 2, 1, 1),
        ("Feng", "95842658", "123456", "F", 2.6, "Feng@gmail.com", 0, 3, 0, 2),
        ("Sophia", "84563259", "123456", "F", 2.7, "Sophia@gmail.com", 1, 4, 0, 1),
        ("Emma", "23154826", "123456", "F", 3.1, "Emma@gmail.com", 2, 3, 3, 1),
        ("Eve", "26485741", "123456", "F", 3.2, "Eve@gmail.com", 0, 3, 4, 0),
        ("Leona", "21548963", "123456", "F", 3.5, "Leona@gmail.com", 2, 4, 3, 1),
        ("janine", "32659845", "123456", "F", 3.9, "janine@gmail.com", 0, 3, 2, 2),
        ("Oven", "96545658", "123456", "M", 3.2, "Oven@gmail.com", 0, 3, 1, 1),
        ("Rio", "12123548", "123456", "M", 2.8, "Rio@gmail.com", 2, 3, 1, 1),
        ("Cole", "85496523", "123456", "M", 2.3, "Cole@gmail.com", 4, 2, 2, 0),
        ("Zion", "12341412", "123456", "M", 2.4, "Zion@gmail.com", 0, 4, 3, 1),
        ("Milo", "32142525", "123456", "M", 2.5, "Milo@gmail.com", 1, 2, 2, 0),
        ("Flynn", "95895956", "123456", "M", 2.9, "Flynn@gmail.com", 0, 4, 4, 2),
        ("Jonas", "75845756", "123456", "M", 2.9, "Jonas@gmail.com", 0, 3, 2, 2);



/*instructor table actions*/
drop table if exists instructor;

create table instructor(
iid	int NOT NULL primary key auto_increment,
insName varchar(36) NOT NULL,
username varchar(8) NOT NULL,
pw varchar(12) DEFAULT '123456',
gender varchar(1) DEFAULT 'M',
email varchar(64),
cp_num int DEFAULT 0,
class_teaching int DEFAULT 0,
curStatus int DEFAULT 0
);

insert into instructor(insName, username, pw, gender, email, cp_num, curStatus)
	values("Michale", "ins16352", "123456", "M", "Michale@gmail.com", 3, 1),
		("Bonner", "ins16552", "123456", "M", "Bonner@gmail.com", 2, 1),
        ("Karen", "ins16952", "123456", "M", "Karen@gmail.com", 3, 1),
        ("Helen", "ins32252", "123456", "F", "Helen@gmail.com", 1, 1),
        ("Hinds", "ins15261", "123456", "F", "Hinds@gmail.com", 0, 1),
        ("Ria", "ins18595", "123456", "F", "Ria@gmail.com", 0, 0),
        ("Frank", "ins16584", "123456", "M", "Frank@gmail.com", 0, 1),
        ("Dan", "ins11535", "123456", "F", "Dan@gmail.com", 2, 1),
        ("Jin", "ins85946", "123456", "M", "Jin@gmail.com", 2, 1),
        ("Andrew", "ins77668", "123456", "M", "Andrew@gmail.com", 1, 0),
        ("Liss", "ins66845", "123456", "F", "Liss@gmail.com", 3, 0),
        ("Jeff", "ins34857", "123456", "M", "Jeff@gmail.com", 2, 1),
        ("David", "ins48595", "123456", "M", "David@gmail.com", 0, 0);

/*adminManagement table actions*/
drop table if exists adminManagement;

create table adminManagement(
username varchar(8) primary key,
pw varchar(12) DEFAULT '123456',
adminName varchar(36) NOT NULL
);

insert into adminManagement(username, pw, adminName) value('admin', 'admin', 'administrator');


/*course table actions*/
drop table if exists course;

create table course(
cid int  primary key auto_increment,
className varchar(36) NOT NULL,
pre_req int, /* 0 : no pre requirement */
department varchar(36) NOT NULL);

INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('1', 'Precalculus', 0,  'Math');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('2', 'Calculus 1', 0, 'Math');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('3', 'Calculus 2', 2, 'Math');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('4', 'Calculus 3', 3, 'Math');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('5', 'Writing 1', 0 , 'English');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('6', 'Writing 2', 5,'English');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('7', 'Writing 3', 6,'English');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('8', 'Chemistry 1', 0, 'Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('9', 'Chemistry 2', 8,'Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('10', 'Physic 1', 0, 'Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('11', 'Physic 2', 10, 'Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('12', 'Art 1', 0, 'Art');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`, `department`) VALUES ('13', 'Art 2', 12, 'Art');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('14', 'Art 3', 13, 'Art');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('15', 'History 1', 0, 'History');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('16', 'History 2', 15, 'History');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('17', 'History 3', 16, 'History');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('18', 'Programming', 0, 'Computer Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('19', 'Data Structure', 0, 'Computer Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('20', 'Algorithms', 18,'Computer Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('21', 'Software Design', 19,'Computer Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('22', 'Operating System', 18,'Computer Science');
INSERT INTO `graduatesystem`.`course` (`cid`, `className`, `pre_req`,`department`) VALUES ('23', 'Database', 19,'Computer Science');


/*course table actions*/
drop table if exists schedules;

create table schedules(
sectionNum int primary key auto_increment,
className varchar(36) NOT NULL,
year int NOT NULL,
semester varchar(36) NOT NULL,
iid int,
days varchar(10),
start_time varchar(20),
max_limit smallint DEFAULT 10,
current_enroll smallint DEFAULT 0,
wait_list smallint DEFAULT 0,
status varchar(10) DEFAULT "Close",
rating float
);

INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('1', 'Precalculus', '2015', 'Fall', '1', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('2', 'Writing 1', '2015', 'Fall', '3', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('3', 'Chemistry 1', '2015', 'Fall', '4', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('4', 'Physic 1', '2015', 'Fall', '5', 'MoWe', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('5', 'Art 1', '2015', 'Fall', '6', 'TuTh', '14:00 -15:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('6', 'History 1', '2015', 'Fall', '10', 'FriSat', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('7', 'Programming', '2015', 'Fall', '8', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('8', 'Calculus 1', '2016', 'Spring', '1', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('9', 'Writing 2', '2016', 'Spring', '3', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('10', 'Chemistry 2', '2016', 'Spring', '4', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('11', 'Physic 2', '2016', 'Spring', '5', 'TuTh', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('12', 'Art 2', '2016', 'Spring', '6', 'FriSat', '14:00 -15:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('13', 'History 2', '2016', 'Spring', '10', 'MoWe', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('14', 'Data Structure', '2016', 'Spring', '8', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('15', 'Art 3', '2016', 'Summer', '7', 'MoWe', '14:00 -15:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('16', 'History 3', '2016', 'Summer', '10', 'TuTh', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('17', 'Calculus 2', '2016', 'Summer', '2', 'FriSat', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('18', 'Precalculus', '2016', 'Fall', '1', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('19', 'Calculus 2', '2016', 'Fall', '2', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('20', 'Writing 1', '2016', 'Fall', '3', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('21', 'Writing 3', '2016', 'Fall', '12', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('22', 'Chemistry 1', '2016', 'Fall', '4', 'TuTh', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('23', 'Physic 1', '2016', 'Fall', '5', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('24', 'Art 1', '2016', 'Fall', '6', 'FriSat', '16:00 - 17:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('25', 'Art 3', '2016', 'Fall', '7', 'TuTh', '16:00 - 17:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('26', 'Programming', '2016', 'Fall', '8', 'MoWe', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('27', 'Algorithms', '2016', 'Fall', '9', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('28', 'Precalculus', '2017', 'Spring', '1', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('29', 'Calculus 3', '2017', 'Spring', '2', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('30', 'Writing 2', '2017', 'Spring', '3', 'TuTh', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('31', 'Chemistry 2', '2017', 'Spring', '4', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('32', 'Physic 2', '2017', 'Spring', '5', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('33', 'Art 2', '2017', 'Spring', '6', 'FriSat', '16:00 - 17:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('34', 'Data Structure', '2017', 'Spring', '8', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('35', 'Database', '2017', 'Spring', '9', 'FriSat', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('36', 'Calculus 1', '2017', 'Spring', '1', 'MoWe', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('37', 'Writing 3', '2017', 'Summer', '12', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('38', 'History 1', '2017', 'Summer', '11', 'TuTh', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('39', 'Art 3', '2017', 'Summer', '7', 'FriSat', '11:00 -12:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('40', 'Calculus 1', '2017', 'Fall', '1', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('41', 'Calculus 3', '2017', 'Fall', '2', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('42', 'Writing 1', '2017', 'Fall', '3', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('43', 'Chemistry 1', '2017', 'Fall', '4', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('44', 'Physic 1', '2017', 'Fall', '5', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('45', 'Art 1', '2017', 'Fall', '7', 'TuTh', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('46', 'History 1', '2017', 'Fall', '11', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('47', 'Programming', '2017', 'Fall', '8', 'MoWe', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('48', 'Algorithms', '2017', 'Fall', '9', 'TuTh', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('49', 'Operating System', '2017', 'Fall', '13', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('50', 'Calculus 1', '2018', 'Spring', '1', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('51', 'Calculus 3', '2018', 'Spring', '2', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('52', 'Writing 2', '2018', 'Spring', '3', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('53', 'Chemistry 2', '2018', 'Spring', '4', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('54', 'Physic 2', '2018', 'Spring', '5', 'TuTh', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('55', 'Art 2', '2018', 'Spring', '7', 'MoWe', '16:00 - 17:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('56', 'History 2', '2018', 'Spring', '11', 'FriSat', '14:00 -15:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('57', 'Data Structure', '2018', 'Spring', '8', 'TuTh', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('58', 'Algorithms', '2018', 'Spring', '9', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('59', 'Database', '2018', 'Spring', '9', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('60', 'Software Design', '2018', 'Spring', '13', 'FriSat', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('61', 'Art 3', '2018', 'Summer', '7', 'TuTh', '09:30 - 10:45', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('62', 'Writing 3', '2018', 'Summer', '12', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('63', 'History 3', '2018', 'Summer', '11', 'MoWe', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('64', 'Precalculus', '2018', 'Fall', '1', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('65', 'Calculus 2', '2018', 'Fall', '2', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('66', 'Writing 1', '2018', 'Fall', '3', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('67', 'Chemistry 1', '2018', 'Fall', '4', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('68', 'Physic 1', '2018', 'Fall', '5', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('69', 'Art 1', '2018', 'Fall', '7', 'TuTh', '14:00 -15:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('70', 'History 1', '2018', 'Fall', '12', 'MoWe', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('71', 'Programming', '2018', 'Fall', '8', 'FriSat', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('72', 'Algorithms', '2018', 'Fall', '9', 'TuTh', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('73', 'Operating System', '2018', 'Fall', '13', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('74', 'Software Design', '2018', 'Fall', '13', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('75', 'Calculus 1', '2019', 'Spring', '1', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('76', 'Calculus 3', '2019', 'Spring', '2', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('77', 'Writing 2', '2019', 'Spring', '3', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('78', 'Chemistry 2', '2019', 'Spring', '4', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('79', 'physic 2', '2019', 'Spring', '5', 'TuTh', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('80', 'Art 2', '2019', 'Spring', '7', 'MoWe', '16:00 - 17:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('81', 'History 2', '2019', 'Spring', '11', 'FriSat', '14:00 -15:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('82', 'Data Structure', '2019', 'Spring', '8', 'TuTh', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('83', 'Algorithms', '2019', 'Spring', '9', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('84', 'Database', '2019', 'Spring', '9', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('85', 'Software Design', '2019', 'Spring', '13', 'FriSat', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('86', 'Art 3', '2019', 'Summer', '7', 'TuTh', '09:30 - 10:45', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('87', 'Writing 3', '2019', 'Summer', '12', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('88', 'History 3', '2019', 'Summer', '11', 'MoWe', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('89', 'Precalculus', '2019', 'Fall', '1', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('90', 'Calculus 2', '2019', 'Fall', '2', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('91', 'Writing 1', '2019', 'Fall', '3', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('92', 'Chemistry 1', '2019', 'Fall', '4', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('93', 'Physic 1', '2019', 'Fall', '5', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('94', 'Art 1', '2019', 'Fall', '7', 'TuTh', '14:00 -15:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('95', 'History 1', '2019', 'Fall', '12', 'MoWe', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('96', 'Programming', '2019', 'Fall', '8', 'FriSat', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('97', 'Algorithms', '2019', 'Fall', '9', 'TuTh', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('98', 'Operating System', '2019', 'Fall', '13', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('99', 'Software Design', '2019', 'Fall', '13', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('100', 'Calculus 1', '2020', 'Spring', '1', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('101', 'Calculus 3', '2020', 'Spring', '2', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('102', 'Writing 2', '2020', 'Spring', '3', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('103', 'Chemistry 2', '2020', 'Spring', '4', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('104', 'Physic 2', '2020', 'Spring', '5', 'TuTh', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('105', 'Art 2', '2020', 'Spring', '7', 'MoWe', '16:00 - 17:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('106', 'History 2', '2020', 'Spring', '11', 'FriSat', '14:00 -15:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('107', 'Data Structure', '2020', 'Spring', '8', 'TuTh', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('108', 'Algorithms', '2020', 'Spring', '9', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('109', 'Database', '2020', 'Spring', '9', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('110', 'Software Design', '2020', 'Spring', '13', 'FriSat', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('111', 'Art 3', '2020', 'Summer', '7', 'TuTh', '09:30 - 10:45', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('112', 'Writing 3', '2020', 'Summer', '12', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('113', 'History 3', '2020', 'Summer', '11', 'MoWe', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('114', 'Precalculus', '2020', 'Fall', '1', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('115', 'Calculus 2', '2020', 'Fall', '2', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('116', 'Writing 1', '2020', 'Fall', '3', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('117', 'Chemistry 1', '2020', 'Fall', '4', 'MoWe', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('118', 'Physic 1', '2020', 'Fall', '5', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('119', 'Art 1', '2020', 'Fall', '7', 'TuTh', '14:00 -15:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('120', 'History 1', '2020', 'Fall', '12', 'MoWe', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('121', 'Programming', '2020', 'Fall', '8', 'FriSat', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('122', 'Algorithms', '2020', 'Fall', '9', 'TuTh', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('123', 'Operating System', '2020', 'Fall', '13', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('124', 'Software Design', '2020', 'Fall', '13', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('125', 'Calculus 1', '2021', 'Spring', '1', 'FriSat', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('126', 'Calculus 3', '2021', 'Spring', '2', 'MoWe', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('127', 'Writing 2', '2021', 'Spring', '3', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('128', 'Chemistry 2', '2021', 'Spring', '4', 'TuTh', '09:30 - 10:45', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('129', 'Physic 2', '2021', 'Spring', '5', 'TuTh', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('130', 'Art 2', '2021', 'Spring', '7', 'MoWe', '16:00 - 17:15', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('131', 'History 2', '2021', 'Spring', '11', 'FriSat', '14:00 -15:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('132', 'Data Structure', '2021', 'Spring', '8', 'TuTh', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('133', 'Algorithms', '2021', 'Spring', '9', 'MoWe', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('134', 'Database', '2021', 'Spring', '9', 'TuTh', '11:00 -12:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('135', 'Software Design', '2021', 'Spring', '13', 'FriSat', '16:00 - 17:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('136', 'Art 3', '2021', 'Summer', '7', 'TuTh', '09:30 - 10:45', '15');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('137', 'Writing 3', '2021', 'Summer', '12', 'FriSat', '14:00 -15:15', '20');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`) VALUES ('138', 'History 3', '2021', 'Summer', '11', 'MoWe', '16:00 - 17:15', '10');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('139', 'Precalculus', '2021', 'Fall', '1', 'FriSat', '09:30 - 10:45', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('140', 'Calculus 2', '2021', 'Fall', '2', 'TuTh', '09:30 - 10:45', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('141', 'Writing 1', '2021', 'Fall', '3', 'MoWe', '09:30 - 10:45', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('142', 'Chemistry 1', '2021', 'Fall', '4', 'MoWe', '14:00 -15:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('143', 'Physic 1', '2021', 'Fall', '5', 'FriSat', '14:00 -15:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('144', 'Art 1', '2021', 'Fall', '7', 'TuTh', '14:00 -15:15', '15','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('145', 'History 1', '2021', 'Fall', '12', 'MoWe', '16:00 - 17:15', '10','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('146', 'Programming', '2021', 'Fall', '8', 'FriSat', '16:00 - 17:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('147', 'Algorithms', '2021', 'Fall', '9', 'TuTh', '16:00 - 17:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('148', 'Operating System', '2021', 'Fall', '13', 'MoWe', '11:00 -12:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('149', 'Software Design', '2021', 'Fall', '13', 'TuTh', '11:00 -12:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('150', 'Calculus 1', '2022', 'Spring', '1', 'FriSat', '09:30 - 10:45', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('151', 'Calculus 3', '2022', 'Spring', '2', 'MoWe', '09:30 - 10:45', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('152', 'Writing 2', '2022', 'Spring', '3', 'FriSat', '14:00 -15:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('153', 'Chemistry 2', '2022', 'Spring', '4', 'TuTh', '09:30 - 10:45', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('154', 'Physic 2', '2022', 'Spring', '5', 'TuTh', '14:00 -15:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('155', 'Art 2', '2022', 'Spring', '7', 'MoWe', '16:00 - 17:15', '15','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('156', 'History 2', '2022', 'Spring', '11', 'FriSat', '14:00 -15:15', '10','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('157', 'Data Structure', '2022', 'Spring', '8', 'TuTh', '16:00 - 17:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('158', 'Algorithms', '2022', 'Spring', '9', 'TuTh', '14:00 -15:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('159', 'Precalculus', '2022', 'Spring', '1', 'FriSat', '16:00 - 17:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`,`current_enroll`) VALUES ('160', 'Calculus 1', '2022', 'Spring', '1', 'FriSat', '14:00 -15:15', '20','open',20);
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('161', 'Writing 2', '2022', 'Spring', '3', 'MoWe', '16:00 - 17:15', '20','open');
INSERT INTO `graduatesystem`.`schedules` (`sectionNum`, `className`, `year`, `semester`, `iid`, `days`, `start_time`, `max_limit`,`status`) VALUES ('162', 'Chemistry 2', '2022', 'Spring', '4', 'TuTh', '16:00 - 17:15', '20','open');
/*stuCourse table actions*/
drop table if exists stuCourse;

create table stuCourse(
id int primary key auto_increment,
sid int NOT NULL,
cid varchar(10) NOT NULL,
sectionNum int NOT NULL,
year int NOT NULL,
semester varchar(36) NOT NULL,
grade varchar(1),
curStatus int /* 0:fail, 1:pass 2:in progress*/
);

INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('1', '1', '114', '2020', 'Fall', 'B', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('1', '2', '125', '2021', 'Spring', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('1', '5', '141', '2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('1', '3', '140', '2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('1', '10', '143', '2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('2', '18', '121', '2020', 'Fall', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('2', '19', '132', '2021', 'Spring', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('2', '10', '143','2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('2', '1', '139','2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('3', '21', '149', '2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('3', '12', '144', '2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('3', '10', '143', '2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('3', '9', '128', '2021', 'Spring', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('3', '8', '117', '2020', 'Fall', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('3', '18', '121', '2020', 'Fall', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('4', '5', '116', '2020', 'Fall', 'B', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('4', '10', '143', '2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `curStatus`) VALUES ('4', '18', '146', '2021', 'Fall', '2');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('5', '16', '106', '2020', 'Spring', 'F', '0');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('5', '5', '116', '2020', 'Fall', 'F', '0');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('5', '15', '95', '2019', 'Fall', 'B', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('5', '16', '131', '2021', 'Spring', 'F', '0');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '5', '2', '2015', 'Fall', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '6', '9', '2016', 'Spring', 'C', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '1', '18', '2016', 'Fall', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '2', '36', '2017', 'Spring', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '15', '46', '2017', 'Fall', 'C', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '16', '56', '2018', 'Spring', 'B', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '3', '65', '2018', 'Fall', 'D', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '4', '76', '2019', 'Spring', 'C', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('6', '8', '67', '2018', 'Fall', 'F', '0');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('7', '5', '2', '2015', 'Fall', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('7', '6', '9', '2016', 'Spring', 'A', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('7', '1', '18', '2016', 'Fall', 'B', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('7', '2', '36', '2017', 'Spring', 'C', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('7', '15', '46', '2017', 'Fall', 'B', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('7', '16', '56', '2018', 'Spring', 'C', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('7', '3', '65', '2018', 'Fall', 'B', '1');
INSERT INTO `graduatesystem`.`stucourse` (`sid`, `cid`, `sectionNum`, `year`, `semester`, `grade`, `curStatus`) VALUES ('7', '4', '76', '2019', 'Spring', 'A', '1');



/* Check insert value of stucourse table
Select sid, cid ,(SELECT className From schedules WHERE schedules.sectionNum = stuCourse.sectionNum) As "className"
FROM stucourse;
*/


/* waitlist */
drop table if exists waitList;

create table waitList(
id int primary key auto_increment,
sid int,
year int,
semester varchar(36),
sectionNum int NOT NULL,
position int NOT NULL
);	



/*stuMsg table actions*/
drop table if exists stuMsg;

create table stuMsg(
nid int primary key auto_increment,
receiverID int,
sender varchar(36),
title varchar(36),
content varchar(256),
getTime datetime,
status int DEFAULT 0  /*  0: UNREAD 1: READ */
);

INSERT INTO `graduatesystem`.`stumsg` (`nid`, `receiverID`, `sender`, `title`, `content`, `getTime`, `status`) 
 VALUES ('1', '3', 'Instructor', 'Chemistry 1 Grade', 'Grade for Class Chemistry 1 have been posted', '2020-12-25 14:57:32', '1'),
		('2', '3', 'Instructor', 'Programming Grade', 'Grade for Class Programming have been posted', '2020-12-27 10:13:02', '1'),
		('3', '3', 'Instructor', 'Chemistry 1 Grade', 'Grade for Class Chemistry 2 have been posted', '2021-05-27 19:17:46', '1'),
		('4', '5', 'Registar', 'Warning', 'This is third time you recieved a warning. Your current status has been change to SUSPENDED. You must pay the fine in order to register for following semester.', '2021-05-29 19:17:46', '0');
/*insMsg table actions*/
drop table if exists insMsg;

create table insMsg(
nid int primary key auto_increment,
receiverID int,
title varchar(36),
content varchar(256),
getTime datetime,
status int DEFAULT 0  /*  0: UNREAD 1: READ */
);


/*complainMsg table actions*/
drop table if exists complainMsg;

create table complainMsg(
id int primary key auto_increment,
sendType varchar(36),
fromId int,
fromName varchar(36),
receiveType varchar(36),
receiveId int,
receiveName varchar(36),
description varchar(1000),
curStatus int, /* 0:pending 1:checked by registar */
createdTime datetime
);


/*student application table actions*/
drop table if exists stuApplication;

create table stuApplication(
stateid int primary key,
stuName varchar(36),
gender varchar(1),
GPA float,
email varchar(36),
curStatus smallint default 0,
info varchar(36) default "None",
feedback varchar(36) default "None"
);

insert into stuApplication(stateid, stuName, gender, GPA, email, curStatus, info) 
						values(214562, "Percy", "M", 3.5, "percy@gmail.com", 0, "I love CCNY"),
								(958467, "Lucy", "F", 3.2, "Lucy@gmail.com", 0, "I love CCNY"),
                                (482751, "Hadis", "F", 3.6, "Hadis@gmail.com", 0, "I love CCNY"),
                                (968435, "Nami", "F", 3.7, "Nami@gmail.com", 0, "I love CCNY"),
                                (123854, "Jennifer", "F", 2.6, "Jennifer@gmail.com", 0, "I love CCNY"),
                                (967485, "Kale", "M", 2.8, "Kale@gmail.com", 0, "I love CCNY"),
                                (777845, "Leo", "M", 3.3, "Leo@gmail.com", 0, "I love CCNY"),
                                (646253, "Linda", "F", 3.9, "Linda@gmail.com", 0, "I love CCNY"),
                                (818957, "Kris", "M", 3.7, "Kris@gmail.com", 0, "I love CCNY"),
                                (455468, "Laila", "F", 4.0, "Laila@gmail.com", 0, "I love CCNY"),
                                (748152, "Chris", "M", 3.0, "Chris@gmail.com", 0, "I love CCNY"),
                                (242431, "Zlien", "M", 2.9, "Zlien@gmail.com", 0, "I love CCNY"),
                                (968596, "Sandy", "F", 3.4, "Sandy@gmail.com", 0, "I love CCNY");
                                
                                
/*student application table actions*/
drop table if exists insApplication;

create table insApplication(
stateid int primary key,
insName varchar(36),
gender varchar(1),
email varchar(36),
curStatus smallint default 0,
info varchar(36) default "None",
feedback varchar(36) default "None"
);

insert into insApplication(stateid, insName, gender, email, curStatus, info) 
						values(958426, "Rick", "M", "Rick@gmail.com", 0, "I love CCNY"),
								(845745, "Hui", "F", "Hui@gmail.com", 0, "I love CCNY"),
                                (114578, "Sindy", "F", "Sindy@gmail.com", 0, "I love CCNY"),
                                (232394, "Iona", "F", "Iona@gmail.com", 0, "I love CCNY"),
                                (948548, "Anna", "F", "Anna@gmail.com", 0, "I love CCNY"),
                                (754845, "Tin", "M", "Tin@gmail.com", 0, "I love CCNY"),
                                (453451, "Eric", "M", "Eric@gmail.com", 0, "I love CCNY"),
                                (975414, "Rita", "F", "Rita@gmail.com", 0, "I love CCNY"),
                                (545715, "Peng", "M", "Peng@gmail.com", 0, "I love CCNY"),
                                (452536, "Vayne", "F", "Vayne@gmail.com", 0, "I love CCNY"),
                                (886947, "Jimmy", "M", "Jimmy@gmail.com", 0, "I love CCNY"),
                                (358487, "Mulisa", "F", "Mulisa@gmail.com", 0, "I love CCNY");
                                
                                
/*Period Table actions*/
drop table if exists period;

create table period(
pid int primary key auto_increment,
term varchar(12),
curPeriod int default 0,
curStatus int default 0
);

/*curPeriod: 0 waiting.  1 setup. 2 class registration. 3 special registration time. 4 running period. 5 grading period.*/
/*curStatus: -1 passed. 0 future term. 1 upcoming term. 2 current term*/
insert into period(pid, term, curPeriod, curStatus) 
				values(1, "2015 Fall", 0, -1),
                    (2, "2016 Spring", 0, -1),
					(3, "2016 Summer", 0, -1),
					(4, "2016 Fall", 0, -1),
                    (5, "2017 Spring", 0, -1),
					(6, "2017 Summer", 0, -1),
					(7, "2017 Fall", 0, -1),
					(8, "2018 Spring", 0, -1),
					(9, "2018 Summer", 0, -1),
					(10, "2018 Fall", 0, -1),
					(11, "2019 Spring", 0, -1),
					(12, "2019 Summer", 0, -1),
					(13, "2019 Fall", 0, -1),
					(14, "2020 Spring", 0, -1),
					(15, "2020 Summer", 0, -1),
                    (16, "2020 Fall", 0, -1),
                    (17, "2021 Spring", 0, -1),
                    (18, "2021 Summer", 5, 2),
                    (19, "2021 Fall", 2, 1),
                    (20, "2022 Spring", 0, 0),
                    (21, "2022 Summer", 0, 0),
                    (22, "2022 Fall", 0, 0);
                    
/*Student review table*/
drop table if exists review;

create table review(
rid int primary key auto_increment,
sid int,
sectionNum int NOT NULL,
rating int,
content VARCHAR(256),
createdTime datetime
);

/*Student review table*/
drop table if exists payFine;

create table payFine(
fid int primary key auto_increment,
sid int,
amount float NOT NULL,
paid float DEFAULT 0,
status int DEFAULT 0, /* 0: wait for student to pay fine 1: paid full amount and wait for registar to unsuspend 3. accepted */
updateTime datetime
);

insert into payFine(sid, amount, updateTime) values(5, 100.00, '2021-05-29 19:17:46');


