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
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidate`
--

LOCK TABLES `candidate` WRITE;
/*!40000 ALTER TABLE `candidate` DISABLE KEYS */;
INSERT INTO `candidate` VALUES (1,'Andrey Ivanov','Moscow','male','MGU','1999-01-01',NULL,NULL),(2,'Ivan Kolesov','Moscow','male','MGSU','1998-01-01',NULL,NULL),(3,'Ivan Petrenko','Tver','male','MGSU','2001-05-01',NULL,NULL),(26,'Vlad Scripal','Moscow','male','MSTU','2002-01-01',' ',NULL),(27,'Pasha Pashutin','Moscow','male','MGU','2005-01-01',' ',NULL),(28,'Misha Timofeev','Moscow','male','MSTU','2005-01-01','',NULL),(29,'Kasha Kek','Moscow','female','MSTU','2000-01-01','',1),(30,'Andrey Scrip','Moscow','male','MGU','2000-01-01','',NULL),(31,'Masha','Moscow','female','MSTU','2005-01-01','',NULL),(32,'Masha Timof','Moscow','female','MGU','2005-01-01','',1),(33,'Masha Tet','Moscow','female','MSTU','2005-01-01','',1),(34,'Toha','Moscow','male','MSTU','2001-01-01','',1),(35,'Petya','Moscow','male','MGU','2001-01-01','',3),(36,'Petya','Moscow','male','MSTU','2005-01-01','',3),(37,'Masha','Moscow','male','MSTU','2005-01-01','',1),(38,'Anton','Moscow','male','MIREA','1999-01-01','',3),(39,'Vlad Scripalenko','Moscow','male','MGU','2005-01-01','',1),(40,'Vlad Scripalenko214213','Moscow','male','MSTU','2005-01-01','',1),(41,'Masha Kek','Moscow','female','MGU','1111-02-22','',1);
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

-- Dump completed on 2023-08-10 18:29:40
