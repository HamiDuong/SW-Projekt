-- MySQL dump 10.13  Distrib 8.0.20, for macos10.15 (x86_64)
--
-- Host: localhost    Database: worktimeapp
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `vacationbegin`
--

DROP TABLE IF EXISTS `vacationbegin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacationbegin` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime DEFAULT NULL,
  `type` varchar(45) DEFAULT 'vacationbegin',
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacationbegin`
--

LOCK TABLES `vacationbegin` WRITE;
/*!40000 ALTER TABLE `vacationbegin` DISABLE KEYS */;
INSERT INTO `vacationbegin` VALUES (1,'2022-05-29 10:21:50','2022-05-17 18:34:00','vacationbegin'),(2,'2022-05-29 10:22:40','2022-05-17 18:34:00','vacationbegin'),(3,'2022-05-29 10:25:26','2022-05-17 18:34:00','vacationbegin'),(4,'2022-05-29 10:27:09','2022-05-17 18:34:00','vacationbegin'),(5,'2022-05-29 10:28:03','2022-05-17 18:34:00','vacationbegin'),(6,'2022-05-29 10:28:26','2022-05-17 18:34:00','vacationbegin'),(7,'2022-06-11 22:19:14','2022-06-15 23:22:36','vacationbegin'),(8,'2022-06-11 22:20:46','2022-06-15 23:22:36','vacationbegin'),(9,'2022-06-11 22:29:22','2022-08-06 00:00:00','vacationbegin');
/*!40000 ALTER TABLE `vacationbegin` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-15 11:52:30
