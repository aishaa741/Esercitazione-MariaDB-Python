/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.14-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ROBOT_DB
-- ------------------------------------------------------
-- Server version	10.11.14-MariaDB-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Robots`
--

DROP TABLE IF EXISTS `Robots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Robots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modello` varchar(100) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `anno_creazione` int(11) DEFAULT NULL,
  `autonomia_ore` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Robots`
--

LOCK TABLES `Robots` WRITE;
/*!40000 ALTER TABLE `Robots` DISABLE KEYS */;
INSERT INTO `Robots` VALUES
(1,'NEX-STRIKE-V1','Combattimento',2024,4500),
(2,'NEX-STRIKE-V2','Combattimento',2025,9200),
(3,'MK1-PHALANX-P','Combattimento',1995,1200),
(4,'SYS-TITAN-CORE','Logistica',2022,15000),
(5,'XG-HERMES-S','Ricognizione',2023,850),
(6,'UNIT-APOLLO-A','Medico',2021,3200),
(7,'NEX-VALKYRIE-S','Combattimento',2026,6000),
(8,'MK0-GOLIATH-H','Logistica',1988,2500),
(9,'NEX-LEVIATHAN-S','Esplorazione',2024,18000),
(10,'SYS-CHRONOS-M','Ricerca',1999,8500),
(11,'DRON-ARTEMIS-H','Combattimento',2022,3400),
(12,'UNIT-HEPHAESTUS','Costruzioni',2020,12500),
(13,'MK2-SPARTAN-G','Combattimento',1998,2100),
(14,'XG-ICARUS-H','Ricognizione',2025,400),
(15,'NEX-ORION-DS','Esplorazione',2023,50000),
(16,'SYS-DEMETER-A','Agricoltura',2019,6500),
(17,'UNIT-ASCLEPIUS','Medico',2026,4800),
(18,'MK1-CENTURION','Combattimento',1992,1500),
(19,'NEX-NEMESIS-H','Combattimento',2025,5500),
(20,'SYS-ATLAS-L','Logistica',2021,9500),
(21,'DRON-ZEPHYR-W','Manutenzione',2020,1200),
(22,'MK0-ALPHA-T','Ricerca',1985,800),
(23,'NEX-ARES-C','Combattimento',2026,7200),
(24,'SYS-POSEIDON-R','Estrazione',2018,24000),
(25,'XG-NYX-S','Combattimento',2024,3100),
(26,'UNIT-HESTIA-C','Manutenzione',2022,14000),
(27,'MK1-PRAETORIAN','Combattimento',1996,1800),
(28,'NEX-HELIOS-S','Energetica',2023,80000),
(29,'SYS-VULCAN-S','Costruzioni',2015,11000),
(30,'DRON-ARGUS-E','Ricognizione',2026,900),
(31,'MK0-BETA-S','Logistica',1989,1600),
(32,'NEX-ODIN-O','Combattimento',2025,8800),
(33,'UNIT-ATHENA-T','Ricerca',2021,6700),
(34,'SYS-HADES-DC','Estrazione',2020,16500),
(35,'XG-ROGUE-I','Combattimento',2023,2800),
(36,'MK1-GLADIATOR','Combattimento',1994,1400),
(37,'NEX-CHIMERA-M','Combattimento',2026,6400),
(38,'SYS-GAIA-T','Esplorazione',2024,45000),
(39,'DRON-HERMES-B','Ricognizione',2010,750),
(40,'MK0-GAMMA-R','Comunicazioni',1982,5000),
(41,'NEX-CERBERUS-G','Combattimento',2022,10500),
(42,'UNIT-PANACEA-M','Emergenza',2025,8200),
(43,'SYS-TALOS-S','Combattimento',2019,9000),
(44,'XG-PHANTOM-G','Combattimento',2026,4100),
(45,'MK1-LEGIONNAIRE','Combattimento',1997,2000),
(46,'NEX-HYPERION-D','Esplorazione',2027,95000),
(47,'SYS-MORPHEUS-D','Ricerca',2005,13000),
(48,'DRON-ECHO-P','Ricognizione',2018,600),
(49,'MK0-DELTA-C','Energetica',1980,20000),
(50,'NEX-TERMINUS-F','Combattimento',2026,12000),
(51,'ARC-SENTINEL-X1','Sicurezza',1995,4500),
(52,'ARC-SENTINEL-X2','Sicurezza',1996,4800),
(53,'ARC-OBSERVER-01','Ricognizione',1984,300),
(54,'ARC-OBSERVER-02','Ricognizione',1985,350),
(55,'NEX-STORM-V1','Combattimento',2024,7800),
(56,'NEX-STORM-V2','Combattimento',2025,11000),
(57,'NEX-STORM-V3','Combattimento',2026,15000),
(58,'NEX-SABRE-A','Combattimento',2023,5500),
(59,'NEX-SABRE-B','Combattimento',2024,5900),
(60,'NEX-SABRE-C','Combattimento',2025,6200),
(61,'UNIT-MED-S1','Medico',2022,4000),
(62,'UNIT-MED-S2','Medico',2023,4100),
(63,'UNIT-MED-S3','Medico',2024,4200),
(64,'SYS-LOAD-T1','Logistica',2015,12000),
(65,'SYS-LOAD-T2','Logistica',2016,12500),
(66,'SYS-LOAD-T3','Logistica',2017,13000),
(67,'DRON-SCAN-X','Ricognizione',2021,500),
(68,'DRON-SCAN-Y','Ricognizione',2022,550),
(69,'DRON-SCAN-Z','Ricognizione',2023,600),
(70,'NEX-RAZOR-01','Combattimento',2025,3200),
(71,'NEX-RAZOR-02','Combattimento',2026,3400),
(72,'SYS-MINE-A1','Estrazione',2020,22000),
(73,'SYS-MINE-A2','Estrazione',2021,23000),
(74,'SYS-MINE-A3','Estrazione',2022,25000),
(75,'ARC-WORKER-P1','Costruzioni',1978,8000),
(76,'ARC-WORKER-P2','Costruzioni',1979,8500),
(77,'ARC-WORKER-P3','Costruzioni',1980,9000),
(78,'NEX-GUARD-01','Sicurezza',2024,10000),
(79,'NEX-GUARD-02','Sicurezza',2025,10500),
(80,'NEX-GUARD-03','Sicurezza',2026,11000),
(81,'UNIT-LAB-X','Ricerca',2018,7000),
(82,'UNIT-LAB-Y','Ricerca',2019,7500),
(83,'UNIT-LAB-Z','Ricerca',2020,8000),
(84,'NEX-BLADE-V1','Combattimento',2024,4500),
(85,'NEX-BLADE-V2','Combattimento',2025,4800),
(86,'NEX-BLADE-V3','Combattimento',2026,5200),
(87,'SYS-AERO-01','Trasporto',2022,35000),
(88,'SYS-AERO-02','Trasporto',2023,38000),
(89,'SYS-AERO-03','Trasporto',2024,42000),
(90,'NEX-VOID-01','Esplorazione',2025,60000),
(91,'NEX-VOID-02','Esplorazione',2026,75000),
(92,'NEX-VOID-03','Esplorazione',2027,120000),
(93,'DRON-FIX-A','Manutenzione',2021,1500),
(94,'DRON-FIX-B','Manutenzione',2022,1600),
(95,'DRON-FIX-C','Manutenzione',2023,1700),
(96,'ARC-GEN-01','Generico',1970,500),
(97,'ARC-GEN-02','Generico',1971,600),
(98,'ARC-GEN-03','Generico',1972,700),
(99,'NEX-ULTRA-Z','Combattimento',2026,18000),
(100,'SYS-OMEGA-CORE','Logistica',2025,25000);
/*!40000 ALTER TABLE `Robots` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-19 14:23:38
