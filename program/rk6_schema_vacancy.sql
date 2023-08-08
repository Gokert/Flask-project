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
-- Table structure for table `vacancy`
--

DROP TABLE IF EXISTS `vacancy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacancy` (
  `Vac_id` int NOT NULL AUTO_INCREMENT,
  `Name` text NOT NULL,
  `Open_date` date NOT NULL,
  `Close_date` date DEFAULT NULL,
  `Pos_id` int NOT NULL,
  `txt` text NOT NULL,
  PRIMARY KEY (`Vac_id`,`Pos_id`),
  KEY `fk_vacancy_position_unitcode1001_idx` (`Pos_id`),
  CONSTRAINT `fk_vacancy_position_unitcode1001` FOREIGN KEY (`Pos_id`) REFERENCES `position_unitcode100` (`Pos_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancy`
--

LOCK TABLES `vacancy` WRITE;
/*!40000 ALTER TABLE `vacancy` DISABLE KEYS */;
INSERT INTO `vacancy` VALUES (3,'Frontend разработчик ','2022-01-01',NULL,4,'Необходимые технологии: javascript/html/css '),(4,'Переводчик английского языка ','2022-01-02','2023-01-23',10,'Уровень знания: Upper intermediate '),(5,'Переводчик английского языка ','2022-01-02',NULL,10,'Уровень знания: Upper intermediate '),(6,'Переводчик английского языка ','2022-01-02',NULL,10,'Уровень знания: Upper intermediate '),(7,'Python разработчик ','2022-01-03',NULL,9,'Необходимые технологии: Django '),(20,'Переводчик английского языка','2023-01-22','2023-01-29',48,'+'),(25,'Java епта','2023-01-23','2023-01-23',71,'лул'),(26,'ЧВК12','2023-01-23','2023-01-23',72,'xr1'),(27,'Frontend разработчик','2023-01-23','2023-01-23',4,'вап'),(28,'Frontend разработчик','2023-01-23','2023-01-23',4,'апп');
/*!40000 ALTER TABLE `vacancy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-13 22:09:01
