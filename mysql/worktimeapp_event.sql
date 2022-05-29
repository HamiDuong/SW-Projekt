-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: worktimeapp
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
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `id` int NOT NULL,
  `date_of_last_change` date DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
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
INSERT INTO `event` VALUES (1,'2022-05-26','going',NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'2022-05-26','coming',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'2022-06-05','vacationbegin',NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,NULL,'vacationend',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'2022-05-26','going',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-28 22:21:31
