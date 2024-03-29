-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: mydiscord
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `channel` (
  `channelID` int NOT NULL AUTO_INCREMENT,
  `channel_name` varchar(255) DEFAULT NULL,
  `channel_type` varchar(255) DEFAULT NULL,
  `serverID` int DEFAULT NULL,
  PRIMARY KEY (`channelID`),
  KEY `serverID` (`serverID`),
  CONSTRAINT `channel_ibfk_1` FOREIGN KEY (`serverID`) REFERENCES `server` (`serverID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
INSERT INTO `channel` VALUES (2,'laplateforme','textual',1);
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `messageID` int NOT NULL AUTO_INCREMENT,
  `content` BLOB DEFAULT NULL,
  `date_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `userID` int DEFAULT NULL,
  `type` int DEFAULT NULL,
  `channelID` int DEFAULT NULL,
  PRIMARY KEY (`messageID`),
  KEY `userID` (`userID`),
  KEY `channelID` (`channelID`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`userID`),
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`channelID`) REFERENCES `channel` (`channelID`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (5,'coucou',NULL,1,2),(6,'je suis un test',NULL,1,2),(7,'hello test de thread',NULL,1,2),(10,'je suis groot',NULL,2,2),(11,'Harmony >>>> Discord   (ÔÖ½)',NULL,1,2),(12,'­ƒñúÔÇï­ƒÿéÔÇï­ƒñúÔÇï­ƒÿéÔÇï­ƒñúÔÇï­ƒÿéÔÇï',NULL,1,2),(13,'­ƒÉ▒ÔÇï',NULL,1,2),(14,'',NULL,1,2),(15,'Un Chat d\'AFK',NULL,1,2),(16,'test',NULL,1,2),(17,'hello',NULL,3,2),(20,'test update message',NULL,1,2),(21,'test 2 ',NULL,1,2),(22,'test',NULL,1,2),(23,'a',NULL,1,2),(24,'test echange message local',NULL,1,2),(25,'',NULL,78,2),(26,'dfdfdf­ƒÿè',NULL,79,2),(27,'hello ­ƒÿÄ',NULL,79,2),(28,'',NULL,79,2),(29,'hi ­ƒÿÄ',NULL,79,2),(30,'coucou ­ƒÿÄ',NULL,79,2),(31,'dnfgbvdqsdrt;j,hngdn',NULL,1,2),(32,'',NULL,79,2),(33,'',NULL,79,2),(34,'­ƒÿè',NULL,79,2),(35,'',NULL,79,2),(36,'­ƒÿìhi',NULL,79,2),(59,'test',NULL,1,2),(60,'hello world ! ­ƒÿè',NULL,79,2);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reaction`
--

DROP TABLE IF EXISTS `reaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reaction` (
  `reactionID` int NOT NULL AUTO_INCREMENT,
  `emoji` varchar(255) DEFAULT NULL,
  `messageID` int DEFAULT NULL,
  `userID` int DEFAULT NULL,
  PRIMARY KEY (`reactionID`),
  KEY `messageID` (`messageID`),
  KEY `userID` (`userID`),
  CONSTRAINT `reaction_ibfk_1` FOREIGN KEY (`messageID`) REFERENCES `message` (`messageID`),
  CONSTRAINT `reaction_ibfk_2` FOREIGN KEY (`userID`) REFERENCES `user` (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reaction`
--

LOCK TABLES `reaction` WRITE;
/*!40000 ALTER TABLE `reaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `reaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `server` (
  `serverID` int NOT NULL AUTO_INCREMENT,
  `server_name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `owner` int DEFAULT NULL,
  `server_image` blob,
  `creation_name` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`serverID`),
  KEY `owner` (`owner`),
  CONSTRAINT `server_ibfk_1` FOREIGN KEY (`owner`) REFERENCES `user` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (1,'laplateforme','Description of laplateforme server',1,NULL,'2024-02-22 08:41:00');
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server_member`
--

DROP TABLE IF EXISTS `server_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `server_member` (
  `membershipID` int NOT NULL AUTO_INCREMENT,
  `userID` int DEFAULT NULL,
  `serverID` int DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`membershipID`),
  KEY `userID` (`userID`),
  KEY `serverID` (`serverID`),
  CONSTRAINT `server_member_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`userID`),
  CONSTRAINT `server_member_ibfk_2` FOREIGN KEY (`serverID`) REFERENCES `server` (`serverID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server_member`
--

LOCK TABLES `server_member` WRITE;
/*!40000 ALTER TABLE `server_member` DISABLE KEYS */;
/*!40000 ALTER TABLE `server_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `userID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `auth_token` varchar(255) DEFAULT NULL,
  `creation_name` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Hamici','Lyes','12345','lyes.hamici@laplateforme.io','NULL','2024-02-12 13:09:29'),(2,'Lemelle','Thanh','147852','thanh-son.lemelle@laplateforme.io','NULL','2024-02-12 13:11:51'),(3,'Lakhezoum','Kheira','12369','kheira.lakhezoum@laplateforme.io','NULL','2024-02-12 13:13:29'),(78,'John','Doe','0123','john.doe@laplateforme.io','NULL','2024-02-23 15:00:30'),(79,'a','a','123','a@a','NULL','2024-02-26 13:33:20');
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

-- Dump completed on 2024-02-27 11:17:37
