-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: worktimeapp
-- ------------------------------------------------------
-- Server version	8.0.25

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
  CONSTRAINT `breakId` FOREIGN KEY (`id`) REFERENCES `breaks` (`id`),
  CONSTRAINT `illnessId` FOREIGN KEY (`id`) REFERENCES `illnesses` (`id`),
  CONSTRAINT `projectDurationId` FOREIGN KEY (`id`) REFERENCES `projectdurations` (`id`),
  CONSTRAINT `projectWorkId` FOREIGN KEY (`id`) REFERENCES `projectworks` (`id`),
  CONSTRAINT `vacationId` FOREIGN KEY (`id`) REFERENCES `vacations` (`id`),
  CONSTRAINT `workId` FOREIGN KEY (`id`) REFERENCES `works` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-30 17:30:54
