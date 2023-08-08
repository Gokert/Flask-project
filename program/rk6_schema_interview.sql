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
-- Table structure for table `interview`
--

DROP TABLE IF EXISTS `interview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interview` (
  `Int_id` int NOT NULL AUTO_INCREMENT,
  `Int_date` date DEFAULT NULL,
  `Result` varchar(45) DEFAULT NULL,
  `Real_sal` int DEFAULT NULL,
  `Emp_id` int DEFAULT NULL,
  `Cand_id` int DEFAULT NULL,
  `Vac_id` int DEFAULT NULL,
  `Scores` int DEFAULT NULL,
  PRIMARY KEY (`Int_id`),
  KEY `fk_interview_candidate1_idx` (`Cand_id`),
  KEY `fk_interview_vacancy1_idx` (`Vac_id`),
  KEY `fk_interview_employee1_idx` (`Emp_id`),
  CONSTRAINT `Cand_id` FOREIGN KEY (`Cand_id`) REFERENCES `candidate` (`Cand_id`),
  CONSTRAINT `Emp_id` FOREIGN KEY (`Emp_id`) REFERENCES `employee` (`Emp_id`),
  CONSTRAINT `Vac_id` FOREIGN KEY (`Vac_id`) REFERENCES `vacancy` (`Vac_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interview`
--

LOCK TABLES `interview` WRITE;
/*!40000 ALTER TABLE `interview` DISABLE KEYS */;
INSERT INTO `interview` VALUES (4,'2021-01-01','no',50000,3,1,3,4),(5,'2021-01-01','no',60000,9,2,4,7),(9,'2021-05-01','yes',65000,9,2,7,10),(10,'2022-01-01','no',55000,7,3,6,6),(21,'2022-01-01','yes',NULL,9,27,3,9),(22,'2022-01-01','yes',NULL,9,28,4,9),(23,'2022-01-01','yes',NULL,7,29,4,9),(24,'2022-01-01','no',NULL,7,30,6,3),(25,'2022-01-01','yes',NULL,3,31,4,10),(27,'2022-01-01','no',NULL,9,33,3,1),(28,'2023-01-01','yes',NULL,3,34,20,10),(29,'2023-01-01','yes',NULL,3,35,25,9),(30,'2021-01-01','no',NULL,3,36,25,9),(31,'2022-01-01','yes',NULL,3,31,27,9),(32,'2022-01-01','1',NULL,7,38,26,9),(33,'2022-01-01','yes',NULL,7,39,3,10),(34,NULL,NULL,NULL,NULL,40,3,NULL);
/*!40000 ALTER TABLE `interview` ENABLE KEYS */;
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
