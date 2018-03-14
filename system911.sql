-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cnberdynedb
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `casetable`
--

DROP TABLE IF EXISTS `casetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `casetable` (
  `caseId` int(3) NOT NULL AUTO_INCREMENT,
  `summary` text NOT NULL,
  `reportId` varchar(45) NOT NULL,
  `caseName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`caseId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `casetable`
--

LOCK TABLES `casetable` WRITE;
/*!40000 ALTER TABLE `casetable` DISABLE KEYS */;
INSERT INTO `casetable` VALUES (8,'testing','3,2','testing t'),(9,'','1',NULL);
/*!40000 ALTER TABLE `casetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `report` (
  `incident` varchar(55) NOT NULL,
  `caseNumber` int(3) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `callerName` varchar(45) NOT NULL,
  `callerContact` int(8) NOT NULL,
  `location` varchar(150) NOT NULL,
  `whathappen` text NOT NULL,
  `casualities` varchar(45) NOT NULL,
  `dangers` text NOT NULL,
  `involvement` varchar(45) NOT NULL,
  `typeOfEmergency` varchar(45) NOT NULL,
  `severity` int(1) NOT NULL,
  `addToCase` varchar(45) NOT NULL DEFAULT 'n',
  PRIMARY KEY (`caseNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` VALUES ('traffic accident',1,'2018-03-04','14:14:00','caller name 1',12345678,'asd','this is what happened 3','asd','asd asd','asd','ad',2,'n'),('test',2,'2018-03-04','17:10:00','test tester',84840972,'test','this is what happened 1','asd','asd asd','asd','ddd',0,'y'),('fire ',3,'2018-03-07','18:18:00','eugene yeo',84840972,'ntu','this is what happened','100','none none','student','test',0,'y');
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `username` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `role` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('c1','p1','CallCT'),('co1','p1','CallOp'),('o1','p1','officer'),('s1','p1','sup');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-14 11:27:29
