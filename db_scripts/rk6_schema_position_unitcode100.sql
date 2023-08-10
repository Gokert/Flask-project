-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: rk6_schema
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `position_unitcode100`
--

DROP TABLE IF EXISTS `position_unitcode100`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `position_unitcode100` (
  `Pos_id` int NOT NULL AUTO_INCREMENT,
  `Name_pos` varchar(64) NOT NULL,
  `Min_salary` int NOT NULL,
  `Max_salary` int NOT NULL,
  PRIMARY KEY (`Pos_id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position_unitcode100`
--

LOCK TABLES `position_unitcode100` WRITE;
/*!40000 ALTER TABLE `position_unitcode100` DISABLE KEYS */;
INSERT INTO `position_unitcode100` VALUES (2,'Director',90000,11500),(3,'Head of HR Department',70000,90000),(4,'frontend developer',70000,90000),(5,'Java developer',70000,90000),(6,'C# developer',60000,90000),(7,'Java developer',40000,60000),(8,'SQL developer',44000,64000),(9,'Python developer',43000,64000),(10,'English Translator',50000,75000),(34,'Cook',10000,30000),(35,'Accountant',30000,40000),(37,'C++ developer',50000,70000),(44,'Plumber',10010,30010),(48,'English Translator',110000,130000),(71,'Java ',60079,80079),(72,'Machinist',60079,80079),(74,'Teacher',30000,30000);
/*!40000 ALTER TABLE `position_unitcode100` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-10 18:29:40
