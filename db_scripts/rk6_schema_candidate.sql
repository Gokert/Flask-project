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
-- Table structure for table `candidate`
--

DROP TABLE IF EXISTS `candidate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `candidate` (
  `Cand_id` int NOT NULL AUTO_INCREMENT,
  `Name` text NOT NULL,
  `Address` text NOT NULL,
  `Gender` text NOT NULL,
  `education` text NOT NULL,
  `birthday` date NOT NULL,
  `resume` text,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`Cand_id`),
  KEY `external_user_id` (`user_id`),
  CONSTRAINT `external_user_id` FOREIGN KEY (`user_id`) REFERENCES `external_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidate`
--

LOCK TABLES `candidate` WRITE;
/*!40000 ALTER TABLE `candidate` DISABLE KEYS */;
INSERT INTO `candidate` VALUES (1,'Andrey Ivanov','Moscow','M','MGU','1999-01-01',NULL,NULL),(2,'Ivan Kolesov','Moscow','M','MGSU','1998-01-01',NULL,NULL),(3,'Ivan Petrenko','Tver','M','MGSU','2001-05-01',NULL,NULL),(26,'Vlad Scripal','Moscow','M','MSTU','2002-01-01','Python Django',NULL),(27,'Pasha Pashutin','Moscow','M','MGU','2005-01-01','fghj',NULL),(28,'Misha Timofeev','Moscow','M','MSTU','2005-01-01','кпфукп',NULL),(29,'Маша','Moscow','Ж','MSTU','2000-01-01','B+',1),(30,'Andrey Scrip','Moscow','M','MGU','2000-01-01','U+',NULL),(31,'Masha','Moscow','M','MSTU','2005-01-01','U++',NULL),(32,'Masha Timof','Moscow','M','MGU','2005-01-01','u+++',1),(33,'m','Moscow','Ж','MSTU','2005-01-01','g',1),(34,'Toha','Moscow','M','MSTU','2001-01-01','хочу оч',1),(35,'Petya','Moscow','M','MGU','2001-01-01','хочуу',3),(36,'Petya','Moscow','M','MSTU','2005-01-01','ggg',3),(37,'Masha','Moscow','M','MSTU','2005-01-01','Училась в MSTU на отл , знаю js/css/html',1),(38,'Антон','Moscow','M','MIREA','1999-01-01','Окончил МИРЭА с отличием. Знаю js/css/html',3),(39,'Vlad Scripalenko','Moscow','M','MGU','2005-01-01','asrgeht',1),(40,'Vlad Scripalenko214213','Moscow','M','MSTU','2005-01-01','сптатпь',1);
/*!40000 ALTER TABLE `candidate` ENABLE KEYS */;
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
