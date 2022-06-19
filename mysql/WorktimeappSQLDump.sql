-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: worktimeapp
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activities`
--

DROP TABLE IF EXISTS `activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activities` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `name` varchar(45) NOT NULL,
  `capacity` float NOT NULL,
  `projectId` int DEFAULT NULL,
  `currentCapacity` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `projectId_idx` (`projectId`),
  CONSTRAINT `projectId` FOREIGN KEY (`projectId`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities`
--

LOCK TABLES `activities` WRITE;
/*!40000 ALTER TABLE `activities` DISABLE KEYS */;
INSERT INTO `activities` VALUES (1,'2022-06-11 00:00:00','Test',5,1,12.89);
/*!40000 ALTER TABLE `activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `userId` int NOT NULL,
  `workTimeAccountId` int DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  `timeIntervalBookingId` int DEFAULT NULL,
  `eventBookingId` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `timeIntervalBookingId_idx` (`timeIntervalBookingId`),
  KEY `eventBookingId_idx` (`eventBookingId`),
  KEY `bookingsUserId_idx` (`userId`),
  CONSTRAINT `bookingsUserId` FOREIGN KEY (`userId`) REFERENCES `users` (`id`),
  CONSTRAINT `eventBookingId` FOREIGN KEY (`eventBookingId`) REFERENCES `eventbookings` (`id`),
  CONSTRAINT `timeIntervalBookingId` FOREIGN KEY (`timeIntervalBookingId`) REFERENCES `timeintervalbookings` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (5,'2022-06-15 22:27:14',1,1,'T',5,NULL);
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `breakbegin`
--

DROP TABLE IF EXISTS `breakbegin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breakbegin` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'breakbegin',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breakbegin`
--

LOCK TABLES `breakbegin` WRITE;
/*!40000 ALTER TABLE `breakbegin` DISABLE KEYS */;
/*!40000 ALTER TABLE `breakbegin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `breakend`
--

DROP TABLE IF EXISTS `breakend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breakend` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'breakend',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breakend`
--

LOCK TABLES `breakend` WRITE;
/*!40000 ALTER TABLE `breakend` DISABLE KEYS */;
/*!40000 ALTER TABLE `breakend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `breaks`
--

DROP TABLE IF EXISTS `breaks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breaks` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `startEvent` int DEFAULT NULL,
  `endEvent` int DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `startEvent_idx` (`startEvent`),
  KEY `endEvent_idx` (`endEvent`),
  CONSTRAINT `endEvent` FOREIGN KEY (`endEvent`) REFERENCES `breakend` (`id`),
  CONSTRAINT `startEvent` FOREIGN KEY (`startEvent`) REFERENCES `breakbegin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breaks`
--

LOCK TABLES `breaks` WRITE;
/*!40000 ALTER TABLE `breaks` DISABLE KEYS */;
/*!40000 ALTER TABLE `breaks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coming`
--

DROP TABLE IF EXISTS `coming`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coming` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'coming',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coming`
--

LOCK TABLES `coming` WRITE;
/*!40000 ALTER TABLE `coming` DISABLE KEYS */;
/*!40000 ALTER TABLE `coming` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `type` varchar(45) NOT NULL,
  `coming_id` int DEFAULT NULL,
  `going_id` int DEFAULT NULL,
  `vacation_begin_id` int DEFAULT NULL,
  `vacation_end_id` int DEFAULT NULL,
  `illness_begin_id` int DEFAULT NULL,
  `illness_end_id` int DEFAULT NULL,
  `project_work_begin_id` int DEFAULT NULL,
  `project_work_end_id` int DEFAULT NULL,
  `break_begin_id` int DEFAULT NULL,
  `break_end_id` int DEFAULT NULL,
  `flex_day_start_id` int DEFAULT NULL,
  `flex_day_end_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idevent_UNIQUE` (`id`),
  KEY `id_idx2` (`illness_begin_id`),
  KEY `id_idx3` (`illness_end_id`),
  KEY `id_idx4` (`vacation_begin_id`),
  KEY `id_idx5` (`vacation_end_id`),
  KEY `id_idx6` (`project_work_begin_id`),
  KEY `id_idx7` (`project_work_end_id`),
  KEY `ComingID_idx` (`coming_id`),
  KEY `GoingID_idx` (`going_id`),
  KEY `BreakEndID_idx` (`break_end_id`),
  KEY `BreakBeginID_idx` (`break_begin_id`),
  KEY `FlexDayStartID_idx` (`flex_day_start_id`),
  KEY `FlexDayEndID_idx` (`flex_day_end_id`),
  CONSTRAINT `BreakBeginID` FOREIGN KEY (`break_begin_id`) REFERENCES `breakbegin` (`id`),
  CONSTRAINT `BreakEndID` FOREIGN KEY (`break_end_id`) REFERENCES `breakend` (`id`),
  CONSTRAINT `ComingID` FOREIGN KEY (`coming_id`) REFERENCES `coming` (`id`),
  CONSTRAINT `FlexDayEndID` FOREIGN KEY (`flex_day_end_id`) REFERENCES `flexdayend` (`id`),
  CONSTRAINT `FlexDayStartID` FOREIGN KEY (`flex_day_start_id`) REFERENCES `flexdaystart` (`id`),
  CONSTRAINT `GoingID` FOREIGN KEY (`going_id`) REFERENCES `going` (`id`),
  CONSTRAINT `IllnessBeginID` FOREIGN KEY (`illness_begin_id`) REFERENCES `illnessbegin` (`id`),
  CONSTRAINT `IllnessEndID` FOREIGN KEY (`illness_end_id`) REFERENCES `illnessend` (`id`),
  CONSTRAINT `ProjectWorkBeginID` FOREIGN KEY (`project_work_begin_id`) REFERENCES `projectworkbegin` (`id`),
  CONSTRAINT `ProjectWorkEndID` FOREIGN KEY (`project_work_end_id`) REFERENCES `projectworkend` (`id`),
  CONSTRAINT `VacationBeginID` FOREIGN KEY (`vacation_begin_id`) REFERENCES `vacationbegin` (`id`),
  CONSTRAINT `VacationEndID` FOREIGN KEY (`vacation_end_id`) REFERENCES `vacationend` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (5,'2022-06-15 22:27:12','FlexDayStart',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL),(6,'2022-06-15 22:27:12','FlexDayEnd',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventbookings`
--

DROP TABLE IF EXISTS `eventbookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eventbookings` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `eventId` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `eventId_idx` (`eventId`),
  CONSTRAINT `eventId` FOREIGN KEY (`eventId`) REFERENCES `event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventbookings`
--

LOCK TABLES `eventbookings` WRITE;
/*!40000 ALTER TABLE `eventbookings` DISABLE KEYS */;
INSERT INTO `eventbookings` VALUES (5,'2022-06-15 22:27:12',5),(6,'2022-06-15 22:27:12',6);
/*!40000 ALTER TABLE `eventbookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flexdayend`
--

DROP TABLE IF EXISTS `flexdayend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flexdayend` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'flexdayend',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flexdayend`
--

LOCK TABLES `flexdayend` WRITE;
/*!40000 ALTER TABLE `flexdayend` DISABLE KEYS */;
INSERT INTO `flexdayend` VALUES (1,'2022-06-15 22:27:12','2022-06-15 18:28:52','flexdayend');
/*!40000 ALTER TABLE `flexdayend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flexdays`
--

DROP TABLE IF EXISTS `flexdays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flexdays` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `startEvent` int DEFAULT NULL,
  `endEvent` int DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `startEvent_idx` (`startEvent`),
  KEY `endEvent_idx` (`endEvent`),
  CONSTRAINT `endEventf` FOREIGN KEY (`endEvent`) REFERENCES `flexdayend` (`id`),
  CONSTRAINT `startEventf` FOREIGN KEY (`startEvent`) REFERENCES `flexdaystart` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flexdays`
--

LOCK TABLES `flexdays` WRITE;
/*!40000 ALTER TABLE `flexdays` DISABLE KEYS */;
INSERT INTO `flexdays` VALUES (1,'2022-06-15 22:27:12','2022-06-15 12:02:47','2022-06-15 18:28:52',1,1,'Flexday');
/*!40000 ALTER TABLE `flexdays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flexdaystart`
--

DROP TABLE IF EXISTS `flexdaystart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flexdaystart` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'flexdaystart',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flexdaystart`
--

LOCK TABLES `flexdaystart` WRITE;
/*!40000 ALTER TABLE `flexdaystart` DISABLE KEYS */;
INSERT INTO `flexdaystart` VALUES (1,'2022-06-15 22:27:12','2022-06-15 12:02:47','flexdaystart');
/*!40000 ALTER TABLE `flexdaystart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `going`
--

DROP TABLE IF EXISTS `going`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `going` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` timestamp NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'going',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idcoming_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `going`
--

LOCK TABLES `going` WRITE;
/*!40000 ALTER TABLE `going` DISABLE KEYS */;
/*!40000 ALTER TABLE `going` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `illnessbegin`
--

DROP TABLE IF EXISTS `illnessbegin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `illnessbegin` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'illnessbegin',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `illnessbegin`
--

LOCK TABLES `illnessbegin` WRITE;
/*!40000 ALTER TABLE `illnessbegin` DISABLE KEYS */;
/*!40000 ALTER TABLE `illnessbegin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `illnessend`
--

DROP TABLE IF EXISTS `illnessend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `illnessend` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'illnessend',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `illnessend`
--

LOCK TABLES `illnessend` WRITE;
/*!40000 ALTER TABLE `illnessend` DISABLE KEYS */;
/*!40000 ALTER TABLE `illnessend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `illnesses`
--

DROP TABLE IF EXISTS `illnesses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `illnesses` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `startEvent` int DEFAULT NULL,
  `endEvent` int DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `startEventil_idx` (`startEvent`),
  KEY `endEventil_idx` (`endEvent`),
  CONSTRAINT `endEventil` FOREIGN KEY (`endEvent`) REFERENCES `illnessend` (`id`),
  CONSTRAINT `startEventil` FOREIGN KEY (`startEvent`) REFERENCES `illnessbegin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `illnesses`
--

LOCK TABLES `illnesses` WRITE;
/*!40000 ALTER TABLE `illnesses` DISABLE KEYS */;
/*!40000 ALTER TABLE `illnesses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectdurations`
--

DROP TABLE IF EXISTS `projectdurations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projectdurations` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `startEvent` int DEFAULT NULL,
  `endEvent` int DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  `projectId` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `projectIdp_idx` (`projectId`),
  CONSTRAINT `projectIdp` FOREIGN KEY (`projectId`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectdurations`
--

LOCK TABLES `projectdurations` WRITE;
/*!40000 ALTER TABLE `projectdurations` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectdurations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `id` int NOT NULL,
  `dateOfLastChange` date NOT NULL,
  `name` varchar(45) NOT NULL,
  `commissioner` varchar(45) NOT NULL,
  `userId` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES (1,'2022-05-06','Test','Test',1);
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectusers`
--

DROP TABLE IF EXISTS `projectusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projectusers` (
  `id` int NOT NULL,
  `dateOfLastChange` date NOT NULL,
  `projectId` int NOT NULL,
  `userId` int NOT NULL,
  `capacity` float NOT NULL,
  `currentCapacity` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `projectIdpu_idx` (`projectId`),
  KEY `userIdpu_idx` (`userId`),
  CONSTRAINT `projectIdpu` FOREIGN KEY (`projectId`) REFERENCES `projects` (`id`),
  CONSTRAINT `userIdpu` FOREIGN KEY (`userId`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectusers`
--

LOCK TABLES `projectusers` WRITE;
/*!40000 ALTER TABLE `projectusers` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectusers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectworkbegin`
--

DROP TABLE IF EXISTS `projectworkbegin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projectworkbegin` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'projectworkbegin',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectworkbegin`
--

LOCK TABLES `projectworkbegin` WRITE;
/*!40000 ALTER TABLE `projectworkbegin` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectworkbegin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectworkend`
--

DROP TABLE IF EXISTS `projectworkend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projectworkend` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'projectworkend',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectworkend`
--

LOCK TABLES `projectworkend` WRITE;
/*!40000 ALTER TABLE `projectworkend` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectworkend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectworks`
--

DROP TABLE IF EXISTS `projectworks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projectworks` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `startEvent` int DEFAULT NULL,
  `endEvent` int DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  `activityId` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `startEventpw_idx` (`startEvent`),
  KEY `endEventpw_idx` (`endEvent`),
  KEY `activityIdpw_idx` (`activityId`),
  CONSTRAINT `activityIdpw` FOREIGN KEY (`activityId`) REFERENCES `activities` (`id`),
  CONSTRAINT `endEventpw` FOREIGN KEY (`endEvent`) REFERENCES `projectworkend` (`id`),
  CONSTRAINT `startEventpw` FOREIGN KEY (`startEvent`) REFERENCES `projectworkbegin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectworks`
--

LOCK TABLES `projectworks` WRITE;
/*!40000 ALTER TABLE `projectworks` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectworks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timeintervalbookings`
--

DROP TABLE IF EXISTS `timeintervalbookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timeintervalbookings` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `timeIntervalId` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `timeintervalidtb_idx` (`timeIntervalId`),
  CONSTRAINT `timeintervalidtb` FOREIGN KEY (`timeIntervalId`) REFERENCES `timeintervals` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timeintervalbookings`
--

LOCK TABLES `timeintervalbookings` WRITE;
/*!40000 ALTER TABLE `timeintervalbookings` DISABLE KEYS */;
INSERT INTO `timeintervalbookings` VALUES (5,'2022-06-15 22:27:12',5);
/*!40000 ALTER TABLE `timeintervalbookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timeintervals`
--

DROP TABLE IF EXISTS `timeintervals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timeintervals` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `type` varchar(45) NOT NULL,
  `breakId` int DEFAULT NULL,
  `illnessId` int DEFAULT NULL,
  `projectDurationId` int DEFAULT NULL,
  `projectWorkId` int DEFAULT NULL,
  `vacationId` int DEFAULT NULL,
  `workId` int DEFAULT NULL,
  `flexDayId` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `breakId_idx` (`breakId`),
  KEY `illnessId_idx` (`illnessId`),
  KEY `vacationId_idx` (`vacationId`),
  KEY `workId_idx` (`workId`),
  KEY `flexDayId_idx` (`flexDayId`),
  KEY `projectDurationId_idx` (`projectDurationId`),
  KEY `projectWorkId_idx` (`projectWorkId`),
  CONSTRAINT `breakId` FOREIGN KEY (`breakId`) REFERENCES `breaks` (`id`),
  CONSTRAINT `flexDayId` FOREIGN KEY (`flexDayId`) REFERENCES `flexdays` (`id`),
  CONSTRAINT `illnessId` FOREIGN KEY (`illnessId`) REFERENCES `illnesses` (`id`),
  CONSTRAINT `projectDurationId` FOREIGN KEY (`projectDurationId`) REFERENCES `projectdurations` (`id`),
  CONSTRAINT `projectWorkId` FOREIGN KEY (`projectWorkId`) REFERENCES `projectworks` (`id`),
  CONSTRAINT `vacationId` FOREIGN KEY (`vacationId`) REFERENCES `vacations` (`id`),
  CONSTRAINT `workId` FOREIGN KEY (`workId`) REFERENCES `works` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timeintervals`
--

LOCK TABLES `timeintervals` WRITE;
/*!40000 ALTER TABLE `timeintervals` DISABLE KEYS */;
INSERT INTO `timeintervals` VALUES (5,'2022-06-15 22:27:12','flexday',NULL,NULL,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `timeintervals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `mailAdress` varchar(45) NOT NULL,
  `googleUserId` varchar(70) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'2022-06-15 22:27:17','Mihriban','Dogan','mihrid5@gmail.com','xIQBzuOYQCOwdXGdG417RUFgIzo2');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacationbegin`
--

DROP TABLE IF EXISTS `vacationbegin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacationbegin` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'vacationbegin',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacationbegin`
--

LOCK TABLES `vacationbegin` WRITE;
/*!40000 ALTER TABLE `vacationbegin` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacationbegin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacationend`
--

DROP TABLE IF EXISTS `vacationend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacationend` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime NOT NULL,
  `type` varchar(45) NOT NULL DEFAULT 'vacationend',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacationend`
--

LOCK TABLES `vacationend` WRITE;
/*!40000 ALTER TABLE `vacationend` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacationend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacations`
--

DROP TABLE IF EXISTS `vacations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacations` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `startEvent` int DEFAULT NULL,
  `endEvent` int DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `endEventv_idx` (`endEvent`),
  KEY `startEventv` (`startEvent`),
  CONSTRAINT `endEventv` FOREIGN KEY (`endEvent`) REFERENCES `vacationend` (`id`),
  CONSTRAINT `startEventv` FOREIGN KEY (`startEvent`) REFERENCES `vacationbegin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacations`
--

LOCK TABLES `vacations` WRITE;
/*!40000 ALTER TABLE `vacations` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works`
--

DROP TABLE IF EXISTS `works`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `startEvent` int DEFAULT NULL,
  `endEvent` int DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `startEventwo_idx` (`startEvent`),
  KEY `endEventwo_idx` (`endEvent`),
  CONSTRAINT `endEventwo` FOREIGN KEY (`endEvent`) REFERENCES `going` (`id`),
  CONSTRAINT `startEventwo` FOREIGN KEY (`startEvent`) REFERENCES `coming` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works`
--

LOCK TABLES `works` WRITE;
/*!40000 ALTER TABLE `works` DISABLE KEYS */;
/*!40000 ALTER TABLE `works` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `worktimeaccounts`
--

DROP TABLE IF EXISTS `worktimeaccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `worktimeaccounts` (
  `id` int NOT NULL,
  `dateOfLastChange` datetime NOT NULL,
  `userId` int NOT NULL,
  `contractTime` float NOT NULL,
  `overTime` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userID_idx` (`userId`),
  CONSTRAINT `userID` FOREIGN KEY (`userId`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `worktimeaccounts`
--

LOCK TABLES `worktimeaccounts` WRITE;
/*!40000 ALTER TABLE `worktimeaccounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `worktimeaccounts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-15 22:29:34
