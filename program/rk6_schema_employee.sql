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
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `Emp_id` int NOT NULL AUTO_INCREMENT,
  `Name` text NOT NULL,
  `Birthday` date NOT NULL,
  `Adress` text NOT NULL,
  `education` text NOT NULL,
  `Enroll_date` date DEFAULT NULL,
  `Dismiss_date` date DEFAULT NULL,
  `Salary` int NOT NULL,
  `Pos_id` int NOT NULL,
  PRIMARY KEY (`Emp_id`),
  KEY `fk_employee_position_unitcode100_idx` (`Pos_id`),
  CONSTRAINT `fk_employee_position_unitcode100` FOREIGN KEY (`Pos_id`) REFERENCES `position_unitcode100` (`Pos_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (3,'Andrey Myshlyaev','2002-05-20','','MSTU Bauman','2020-02-04',NULL,100000,2),(7,'Aleksander Davidov','2002-03-21','','MSTU Bauman','2021-10-10',NULL,85000,3),(9,'aaa','2003-03-24','','MSTU Bauman','2022-01-01','2023-02-18',80000,5),(51,'Vlad Scripalenko','2000-01-01','Moscow','MGU','2020-01-01','2023-01-23',60000,37),(52,'Misha Timof','2000-01-01','Moscow','mgtu','2021-01-01','2023-02-18',60000,35),(53,'Vlad Scripalenko','2000-01-01','Moscow','mgtu','2020-01-01','2023-01-23',60000,10),(54,'Vlad Scripalenko214213','2000-01-01','Moscow','mgtu','2021-01-01','2023-02-18',60000,2);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
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
