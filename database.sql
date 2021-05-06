/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - agro
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`agro` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `agro`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Comp_id` int(11) NOT NULL AUTO_INCREMENT,
  `Complaint` varchar(200) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Reply` varchar(50) DEFAULT NULL,
  `User_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`Comp_id`,`Complaint`,`Date`,`Status`,`Reply`,`User_id`) values (1,'Not good','23/12/2020','Replied','ok',1),(2,'vcvv','2021-05-06','pending','pending',1);

/*Table structure for table `crop` */

DROP TABLE IF EXISTS `crop`;

CREATE TABLE `crop` (
  `crpid` int(20) NOT NULL AUTO_INCREMENT,
  `Photo` varchar(200) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Description` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`crpid`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `crop` */

insert  into `crop`(`crpid`,`Photo`,`Name`,`Description`) values (27,'/static/crop/wheat.jpg',' Wheat','Wheat is a grass widely cultivated for its seed, a cereal grain which is a worldwide staple food. The many species of wheat together make up the genus Triticum; the most widely grown is common wheat (T. aestivum).'),(29,'/static/crop/oat.jpg','Oats','The oat, sometimes called the common oat, is a species of cereal grain grown for its seed, which is known by the same name. While oats are suitable for human consumption as oatmeal and rolled oats, one of the most common uses is as livestock feed'),(30,'/static/crop/Maize.jpg','Maize','Maize, also known as corn, is a cereal grain first domesticated by indigenous peoples in southern Mexico about 10,000 years ago. The leafy stalk of the plant produces pollen inflorescences and separate ovuliferous inflorescences called ears that yield kernels or seeds, which are fruits.'),(31,'/static/crop/Finger millet.jpg','Finger millet','Eleusine coracana, or finger millet, is an annual herbaceous plant widely grown as a cereal crop in the arid and semiarid areas in Africa and Asia. It is a tetraploid and self-pollinating species probably evolved from its wild relative Eleusine africana. Finger millet is native to the Ethiopian and Ugandan highlands.'),(32,'/static/crop/Triticale.jpg','Triticale  ','Triticale is a hybrid of wheat and rye first bred in laboratories during the late 19th century in Scotland and Germany. Commercially available triticale is almost always a second-generation hybrid, i.e., a cross between two kinds of primary triticales.'),(33,'/static/crop/Alfalfa Meal.jpg','inj','ddd');

/*Table structure for table `fert` */

DROP TABLE IF EXISTS `fert`;

CREATE TABLE `fert` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Photo` varchar(2000) DEFAULT NULL,
  `fdes` varchar(1000) DEFAULT NULL,
  `fuse` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `fert` */

insert  into `fert`(`fid`,`Name`,`Photo`,`fdes`,`fuse`) values (17,'Alfalfa Meal','/static/fertiliser/Alfalfa Meal.jpg','NPK Ratio: 3-2-2\r\nAlfalfa is commonly used as part of livestock feed. However, alfalfa meal is simply ground up so that it breaks down faster. This particular fertilizer has low amounts of nitrogen, phosphorus, and potassium. As a result, alfalfa meal works at moderate rate of speed. ','The best use for this fertilizer is as a soil conditioner in the early spring prior to planting crops.'),(18,'Cottonseed Meal','/static/fertiliser/cottenseed meal.jpg','NPK Ratio: 6-1-1\r\nThis fertilizer has plenty of nitrogen, but it also contains fair amounts of phosphorus and potassium. The downsides to cottonseed meal are that it works slowly and that it is available primarily in cotton growing areas. However, this fertilizer is particularly useful for conditioning gardens in the fall before cover crops are planted or before mulch is applied. ','This gives the cotton seed meal time to break down fully so that the nitrogen present is readily available in the spring.'),(19,'Corn Gluten Meal','/static/fertiliser/corn-gluten-meal.jpg','NPK Ratio: 0.5-0.5-1\r\nCorn gluten meal contains trace amounts of nitrogen, phosphorous, and potassium. It is also good soil stabilizer but it works slowly.','you should add it in the fall so that it has time to break down over the winter.'),(20,'Rock Phosphate','/static/fertiliser/rock-phosphate-powder.jpg','NPK Ratio: 0-5-0\r\nThis fertilizer is made from rocks that have been ground up. It contains large amounts of phosphate as well as other essential nutrients. The main benefit of using rock phosphate is that the elements it contains don’t dissolve in water.','they hang around in the soil until they’re used by the plants that are growing there.'),(21,'Cow Manure','/static/fertiliser/cow-manure.jpg','NPK Ratio: 2.5-1-1.5\r\nManure in general has a high mass to nutrients ratio. It nonetheless contains respectable amounts of nitrogen, phosphorus, and potassium. Cow manure also works on gardens at a moderate rate of speed. These elements all help to make it an excellent compost additive. However, some weed seeds may survive being digested by the cows in question and this can cause obvious problems. You should also avoid manure leftover from industrial operations because it contains lots of salt. ','regular manure can end up burning plants if too much is used or if it’s used too often.'),(22,'Earthworm Castings','/static/fertiliser/worm-castings.jpg','NPK Ratio: 2-1-1\r\nEarthworm castings contain decent amounts of all three vital nutrients. ','this type of fertilizer is considered a great addition to flower and vegetable gardens.');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`type`) values ('admin','admin','admin'),('shijo@gmail.com','a','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `Nid` int(20) NOT NULL AUTO_INCREMENT,
  `Notifications` varchar(5000) DEFAULT NULL,
  `NotificationDate` datetime DEFAULT NULL,
  PRIMARY KEY (`Nid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`Nid`,`Notifications`,`NotificationDate`) values (10,'Distribution,Sales and USe of pesticides- Guidelines for quality cotrol','2019-03-04 00:00:00'),(11,'We haven seen you in a while check back for new products.','2019-03-04 00:00:00'),(12,'HI','2019-03-04 00:00:00'),(13,'Version 1.2.0.3 will be release on 12/03/2019','2019-03-04 00:00:00');

/*Table structure for table `pesticides` */

DROP TABLE IF EXISTS `pesticides`;

CREATE TABLE `pesticides` (
  `Pid` int(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) DEFAULT NULL,
  `Photo` varchar(200) DEFAULT NULL,
  `Details` varchar(1000) DEFAULT NULL,
  `Puse` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`Pid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `pesticides` */

insert  into `pesticides`(`Pid`,`Name`,`Photo`,`Details`,`Puse`) values (15,'Insecticide','/static/pesticide/insecticides.jpg','Insecticides are substances used to kill insects. They include ovicides and larvicides used against insect eggs and larvae, respectively. ','Insecticides are used in agriculture, medicine, industry and by consumers.'),(16,'Herbicide','/static/pesticide/Herbicides.jpg','A herbicide is a pesticide used to kill unwanted plants. ','Selective herbicides kill certain targets while leaving the desired crop relatively unharmed. '),(17,'Rodenticides','/static/pesticide/Rodenticides.jpg','Rodenticides are pesticides that kill rodents. ','Rodents include not only rats and mice, but also squirrels, woodchucks, chipmunks, porcupines, nutria, and beavers. Although rodents play important roles in nature, they may sometimes require control.'),(18,'Bactericides ','/static/pesticide/bactericides.jpg','A bactericide or bacteriocide, sometimes abbreviated Bcidal, is a substance that kills bacteria.','Bactericides are disinfectants, antiseptics, or antibiotics.'),(19,'Fungicides','/static/pesticide/fungicides.jpg','Fungicides are biocidal chemical compounds or biological organisms used to kill parasitic fungi or their spores.','A fungistatic inhibits their growth. Fungi can cause serious damage in agriculture, resulting in critical losses of yield, quality, and profit.'),(20,'Larvicides','/static/pesticide/larvivides.jpg','A larvicide (alternatively larvacide) is an insecticide that is specifically targeted against the larval life stage of an insect. Their most common use is against mosquitoes.','Larvicides may be contact poisons, stomach poisons, growth regulators, or (increasingly) biological control agents.\r\n');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `farmerid` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) DEFAULT NULL,
  `Place` varchar(100) DEFAULT NULL,
  `City` varchar(100) DEFAULT NULL,
  `Pin` int(10) DEFAULT NULL,
  `Post` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Phone` bigint(15) DEFAULT NULL,
  PRIMARY KEY (`farmerid`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`farmerid`,`Name`,`Place`,`City`,`Pin`,`Post`,`Email`,`Phone`) values (1,'Shijo','kakkad','MAlappuram',673007,'Kakkad','shijo@gmail.com',9809980989);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
