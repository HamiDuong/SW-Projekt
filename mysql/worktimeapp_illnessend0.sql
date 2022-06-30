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
-- Table structure for table `illnessend`
--

DROP TABLE IF EXISTS `illnessend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `illnessend` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime DEFAULT NULL,
  `type` varchar(45) DEFAULT 'illnessend',
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `illnessend`
--

LOCK TABLES `illnessend` WRITE;
/*!40000 ALTER TABLE `illnessend` DISABLE KEYS */;
INSERT INTO `illnessend` VALUES (1,'2022-05-28 11:35:18','2022-05-06 20:05:00','illnessend'),(2,'2022-05-28 11:35:40','2022-05-06 20:05:00','illnessend'),(3,'2022-05-28 11:35:41','2022-05-06 20:05:00','illnessend'),(4,'2022-05-28 11:35:41','2022-05-06 20:05:00','illnessend'),(5,'2022-05-28 11:35:42','2022-05-06 20:05:00','illnessend'),(6,'2022-05-28 11:35:42','2022-05-06 20:05:00','illnessend'),(7,'2022-05-28 11:35:43','2022-05-06 20:05:00','illnessend'),(8,'2022-05-28 11:35:43','2022-05-06 20:05:00','illnessend'),(9,'2022-05-28 11:35:44','2022-05-06 20:05:00','illnessend'),(10,'2022-05-28 11:35:44','2022-05-06 20:05:00','illnessend'),(11,'2022-05-28 11:35:45','2022-05-06 20:05:00','illnessend'),(12,'2022-05-28 11:35:45','2022-05-06 20:05:00','illnessend'),(13,'2022-05-28 11:35:46','2022-05-06 20:05:00','illnessend'),(14,'2022-05-28 11:35:47','2022-05-06 20:05:00','illnessend'),(15,'2022-05-28 11:35:47','2022-05-06 20:05:00','illnessend'),(16,'2022-05-28 11:35:48','2022-05-06 20:05:00','illnessend'),(17,'2022-05-28 11:35:48','2022-05-06 20:05:00','illnessend'),(18,'2022-05-28 11:35:49','2022-05-06 20:05:00','illnessend'),(19,'2022-05-28 11:35:49','2022-05-06 20:05:00','illnessend'),(20,'2022-05-28 11:35:50','2022-05-06 20:05:00','illnessend'),(21,'2022-05-28 11:35:50','2022-05-06 20:05:00','illnessend'),(22,'2022-05-29 10:21:51','2022-05-17 18:34:00','illnessend'),(23,'2022-05-29 10:22:41','2022-05-17 18:34:00','illnessend'),(24,'2022-05-29 10:25:27','2022-05-17 18:34:00','illnessend'),(25,'2022-05-29 10:27:10','2022-05-17 18:34:00','illnessend'),(26,'2022-05-29 10:28:04','2022-05-17 18:34:00','illnessend'),(27,'2022-05-29 10:28:27','2022-05-17 18:34:00','illnessend');
/*!40000 ALTER TABLE `illnessend` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-15 11:52:25
