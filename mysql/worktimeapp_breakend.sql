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
-- Table structure for table `breakend`
--

DROP TABLE IF EXISTS `breakend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breakend` (
  `id` int NOT NULL,
  `date_of_last_change` date NOT NULL,
  `date` datetime DEFAULT NULL,
  `type` varchar(45) DEFAULT 'breakend',
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breakend`
--

LOCK TABLES `breakend` WRITE;
/*!40000 ALTER TABLE `breakend` DISABLE KEYS */;
INSERT INTO `breakend` VALUES (1,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(2,'2022-05-28','2022-05-06 20:05:00','breakend'),(3,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(4,'2022-05-28','2022-05-06 20:05:00','breakend'),(5,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(6,'2022-05-28','2022-05-06 20:05:00','breakend'),(7,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(8,'2022-05-28','2022-05-06 20:05:00','breakend'),(9,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(10,'2022-05-28','2022-05-06 20:05:00','breakend'),(11,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(12,'2022-05-28','2022-05-06 20:05:00','breakend'),(13,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(14,'2022-05-28','2022-05-06 20:05:00','breakend'),(15,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(16,'2022-05-28','2022-05-06 20:05:00','breakend'),(17,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(18,'2022-05-28','2022-05-06 20:05:00','breakend'),(19,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(20,'2022-05-28','2022-05-06 20:05:00','breakend'),(21,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(22,'2022-05-28','2022-05-06 20:05:00','breakend'),(23,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(24,'2022-05-28','2022-05-06 20:05:00','breakend'),(25,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(26,'2022-05-28','2022-05-06 20:05:00','breakend'),(27,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(28,'2022-05-28','2022-05-06 20:05:00','breakend'),(29,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(30,'2022-05-28','2022-05-06 20:05:00','breakend'),(31,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(32,'2022-05-28','2022-05-06 20:05:00','breakend'),(33,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(34,'2022-05-28','2022-05-06 20:05:00','breakend'),(35,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(36,'2022-05-28','2022-05-06 20:05:00','breakend'),(37,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(38,'2022-05-28','2022-05-06 20:05:00','breakend'),(39,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(40,'2022-05-28','2022-05-06 20:05:00','breakend'),(41,'2022-05-28','2022-05-06 20:05:00','breakbegin'),(42,'2022-05-28','2022-05-06 20:05:00','breakend');
/*!40000 ALTER TABLE `breakend` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-28 22:21:35
