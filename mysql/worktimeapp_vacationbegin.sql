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
-- Table structure for table `vacationbegin`
--

DROP TABLE IF EXISTS `vacationbegin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacationbegin` (
  `id` int NOT NULL,
  `date_of_last_change` timestamp NULL DEFAULT NULL,
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
INSERT INTO `vacationbegin` VALUES (1,'2022-05-11 09:05:58','2022-05-11 11:05:57','vacationbegin'),(2,'2022-05-11 09:05:59','2022-05-11 11:05:57','vacationbegin'),(3,'2022-05-11 09:06:00','2022-05-11 11:05:57','vacationbegin'),(4,'2022-05-11 09:06:00','2022-05-11 11:05:57','vacationbegin'),(5,'2022-05-11 09:06:01','2022-05-11 11:05:57','vacationbegin'),(6,'2022-05-11 09:06:01','2022-05-11 11:05:57','vacationbegin'),(7,'2022-05-11 09:06:01','2022-05-11 11:05:57','vacationbegin'),(8,'2022-05-11 09:06:02','2022-05-11 11:05:57','vacationbegin'),(9,'2022-05-11 09:06:02','2022-05-11 11:05:57','vacationbegin'),(10,'2022-05-11 09:06:03','2022-05-11 11:05:57','vacationbegin'),(11,'2022-05-11 09:06:03','2022-05-11 11:05:57','vacationbegin'),(12,'2022-05-11 09:11:51','2022-05-11 11:11:50','vacationbegin'),(13,'2022-05-11 09:11:52','2022-05-11 11:11:50','vacationbegin'),(14,'2022-05-11 09:11:53','2022-05-11 11:11:50','vacationbegin'),(15,'2022-05-11 09:11:53','2022-05-11 11:11:50','vacationbegin'),(16,'2022-05-11 09:11:54','2022-05-11 11:11:50','vacationbegin'),(17,'2022-05-11 09:11:55','2022-05-11 11:11:50','vacationbegin'),(18,'2022-05-11 09:11:55','2022-05-11 11:11:50','vacationbegin'),(19,'2022-05-11 09:11:56','2022-05-11 11:11:50','vacationbegin'),(20,'2022-05-11 09:11:56','2022-05-11 11:11:50','vacationbegin'),(21,'2022-05-11 09:11:57','2022-05-11 11:11:50','vacationbegin'),(22,'2022-05-11 09:11:57','2022-05-11 11:11:50','vacationbegin'),(23,'2022-05-28 09:35:18','2022-05-06 20:05:00','vacationbegin'),(24,'2022-05-28 09:35:40','2022-05-06 20:05:00','vacationbegin'),(25,'2022-05-28 09:35:40','2022-05-06 20:05:00','vacationbegin'),(26,'2022-05-28 09:35:41','2022-05-06 20:05:00','vacationbegin'),(27,'2022-05-28 09:35:42','2022-05-06 20:05:00','vacationbegin'),(28,'2022-05-28 09:35:42','2022-05-06 20:05:00','vacationbegin'),(29,'2022-05-28 09:35:43','2022-05-06 20:05:00','vacationbegin'),(30,'2022-05-28 09:35:43','2022-05-06 20:05:00','vacationbegin'),(31,'2022-05-28 09:35:44','2022-05-06 20:05:00','vacationbegin'),(32,'2022-05-28 09:35:44','2022-05-06 20:05:00','vacationbegin'),(33,'2022-05-28 09:35:45','2022-05-06 20:05:00','vacationbegin'),(34,'2022-05-28 09:35:45','2022-05-06 20:05:00','vacationbegin'),(35,'2022-05-28 09:35:46','2022-05-06 20:05:00','vacationbegin'),(36,'2022-05-28 09:35:46','2022-05-06 20:05:00','vacationbegin'),(37,'2022-05-28 09:35:47','2022-05-06 20:05:00','vacationbegin'),(38,'2022-05-28 09:35:47','2022-05-06 20:05:00','vacationbegin'),(39,'2022-05-28 09:35:48','2022-05-06 20:05:00','vacationbegin'),(40,'2022-05-28 09:35:49','2022-05-06 20:05:00','vacationbegin'),(41,'2022-05-28 09:35:49','2022-05-06 20:05:00','vacationbegin'),(42,'2022-05-28 09:35:50','2022-05-06 20:05:00','vacationbegin'),(43,'2022-05-28 09:35:50','2022-05-06 20:05:00','vacationbegin');
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

-- Dump completed on 2022-05-28 22:21:33
