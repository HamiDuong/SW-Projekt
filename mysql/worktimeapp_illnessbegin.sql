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
-- Table structure for table `illnessbegin`
--

DROP TABLE IF EXISTS `illnessbegin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `illnessbegin` (
  `id` int NOT NULL,
  `date_of_last_change` datetime NOT NULL,
  `date` datetime DEFAULT NULL,
  `type` varchar(45) DEFAULT 'illnessbegin',
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `illnessbegin`
--

LOCK TABLES `illnessbegin` WRITE;
/*!40000 ALTER TABLE `illnessbegin` DISABLE KEYS */;
INSERT INTO `illnessbegin` VALUES (1,'2022-05-28 11:35:18','2022-05-06 20:05:00','illnessbegin'),(2,'2022-05-28 11:35:40','2022-05-06 20:05:00','illnessbegin'),(3,'2022-05-28 11:35:41','2022-05-06 20:05:00','illnessbegin'),(4,'2022-05-28 11:35:41','2022-05-06 20:05:00','illnessbegin'),(5,'2022-05-28 11:35:42','2022-05-06 20:05:00','illnessbegin'),(6,'2022-05-28 11:35:42','2022-05-06 20:05:00','illnessbegin'),(7,'2022-05-28 11:35:43','2022-05-06 20:05:00','illnessbegin'),(8,'2022-05-28 11:35:43','2022-05-06 20:05:00','illnessbegin'),(9,'2022-05-28 11:35:44','2022-05-06 20:05:00','illnessbegin'),(10,'2022-05-28 11:35:44','2022-05-06 20:05:00','illnessbegin'),(11,'2022-05-28 11:35:45','2022-05-06 20:05:00','illnessbegin'),(12,'2022-05-28 11:35:45','2022-05-06 20:05:00','illnessbegin'),(13,'2022-05-28 11:35:46','2022-05-06 20:05:00','illnessbegin'),(14,'2022-05-28 11:35:46','2022-05-06 20:05:00','illnessbegin'),(15,'2022-05-28 11:35:47','2022-05-06 20:05:00','illnessbegin'),(16,'2022-05-28 11:35:48','2022-05-06 20:05:00','illnessbegin'),(17,'2022-05-28 11:35:48','2022-05-06 20:05:00','illnessbegin'),(18,'2022-05-28 11:35:49','2022-05-06 20:05:00','illnessbegin'),(19,'2022-05-28 11:35:49','2022-05-06 20:05:00','illnessbegin'),(20,'2022-05-28 11:35:50','2022-05-06 20:05:00','illnessbegin'),(21,'2022-05-28 11:35:50','2022-05-06 20:05:00','illnessbegin'),(22,'2022-05-29 10:21:50','2022-05-17 18:34:00','illnessbegin'),(23,'2022-05-29 10:22:40','2022-05-17 18:34:00','illnessbegin'),(24,'2022-05-29 10:25:26','2022-05-17 18:34:00','illnessbegin'),(25,'2022-05-29 10:27:09','2022-05-17 18:34:00','illnessbegin'),(26,'2022-05-29 10:28:03','2022-05-17 18:34:00','illnessbegin'),(27,'2022-05-29 10:28:26','2022-05-17 18:34:00','illnessbegin');
/*!40000 ALTER TABLE `illnessbegin` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-29 10:55:34
