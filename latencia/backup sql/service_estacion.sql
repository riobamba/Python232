BEGIN TRANSACTION;
DROP TABLE IF EXISTS "service_estacion";
CREATE TABLE "service_estacion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "estacion" text NOT NULL, "red" text NOT NULL, "localizador" text NOT NULL, "latitud" text NOT NULL, "longitud" text NOT NULL, "administrador" text NOT NULL, "canal" text NOT NULL);
INSERT INTO "service_estacion" VALUES(1,'ARGC','CM','00','9.86','-74.25','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(3,'BBAC','CM','00','2.02','-77.25','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(5,'BRR','CM','00','7.11','-73.71','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(6,'CAP2','CM','00','8.65','-77.36','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(7,'CBOC','CM','00','5.86','-76.01','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(8,'CHI','CM','00','4.64','-73.73','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(9,'CRJC','CM','00','11.02','-72.88','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(10,'CRU','CM','20','1.57','-76.95','RSNC','EHZ');
INSERT INTO "service_estacion" VALUES(13,'FLO2','CM','00','1.58','-75.65','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(14,'GARC','CM','00','2.19','-75.49','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(16,'GUA','CM','20','2.54','-72.63','RSNC','EHZ');
INSERT INTO "service_estacion" VALUES(17,'GUY2C','CM','00','5.22','-75.36','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(18,'HEL','CM','00','6.19','-75.53','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(19,'LCBC','CM','00','8.86','-76.37','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(20,'MACC','CM','00','2.15','-73.85','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(22,'MAP','CM','00','4','-81.61','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(23,'MON','CM','00','8.78','-75.67','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(24,'NOR','CM','00','5.56','-74.87','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(25,'OCA','CM','00','8.24','-73.32','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(26,'ORTC','CM','00','3.91','-75.25','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(27,'PAL','CM','00','4.91','-76.28','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(28,'PAM','CM','20','7.34','-72.7','RSNC','EHZ');
INSERT INTO "service_estacion" VALUES(29,'PIZC','CM','00','4.97','-77.36','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(30,'POP2','CM','00','2.54','-76.68','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(31,'PRA','CM','00','3.71','-74.89','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(32,'PRV','CM','00','13.38','-81.36','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(33,'PTA','CM','00','7.15','-77.81','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(34,'PTB','CM','00','6.54','-74.46','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(35,'PTGC','CM','00','4.2','-72.13','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(36,'PTLC','CM','00','0.17','-74.8','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(37,'ROSC','CM','','4.84','-74.32','RSNC','BHZ');
INSERT INTO "service_estacion" VALUES(38,'RUS','CM','00','5.89','-73.08','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(39,'SJC','CM','00','9.9','-75.18','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(40,'SMAR','CM','00','11.16','-74.22','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(41,'SML','CM','00','8.8','-74.07','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(42,'SOL','CM','20','6.23','-77.41','RSNC','EHZ');
INSERT INTO "service_estacion" VALUES(43,'SPBC','CM','00','5.65','-74.07','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(44,'TAM','CM','00','6.44','-71.79','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(45,'TOLC','CM','00','4.58','-75.32','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(46,'TUM','CM','00','1.82','-78.73','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(47,'URE','CM','00','7.75','-75.53','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(48,'URI','CM','00','11.7','-71.99','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(49,'VIL','CM','20','4.11','-73.69','RSNC','EHZ');
INSERT INTO "service_estacion" VALUES(50,'YOT','CM','00','3.98','-76.34','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(51,'ZAR','CM','00','7.49','-74.86','RSNC','HHZ');
INSERT INTO "service_estacion" VALUES(52,'ARMEC','CM','10','4.56','-75.66','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(53,'BAR2','CM','10','6.59','-73.18','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(54,'BET','CM','10','2.72','-75.42','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(55,'BOG','CM','10','4.64','-74.08','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(58,'CUFI','CM','10','1.23','-77.34','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(59,'CUM','CM','10','0.94','-77.83','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(60,'DBB','CM','10','7.02','-76.21','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(63,'GR1C','CM','10','3','-78.17','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(65,'IBA1C','CM','10','4.45','-75.23','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(67,'MAL','CM','10','4.01','-77.33','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(68,'MAN1C','CM','10','5.07','-75.52','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(69,'NIZA','CM','10','5.06','-75.47','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(74,'PAM','CM','10','7.34','-72.7','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(75,'PAS1','CM','10','1.19','-77.33','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(76,'PAS2','CM','10','1.22','-77.25','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(81,'RAC2C','CM','10','3.37','-76.53','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(82,'RECRC','CM','10','4.96','-75.35','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(88,'TUM3C','CM','10','1.82','-78.75','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(90,'VALLC','CM','10','10.51','-73.26','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(93,'REAC','CM','10','4.64','-74.09','RNAC','HNZ');
INSERT INTO "service_estacion" VALUES(94,'ANIL','OM','','4.49','-75.4','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(95,'AUA1','PR','','12.51','-70.01','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(96,'AZU','RP','','7.79','-80.27','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(97,'BCIP','CU','00','9.17','-79.84','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(98,'BOAV','BR','','2.4','-60.52','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(99,'BRU2','PA','','8.79','-82.69','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(100,'CACAO','RP','','7.33','-80.85','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(101,'CUSE','EC','','0.31','-78.4','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(102,'DABV','VE','','10.92','-70.64','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(103,'ELA','OM','','4.86','-75.4','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(104,'ELOV','VE','','7','-69.48','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(105,'GCUF','OP','','1.23','-77.34','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(106,'GMAL','RP','','7.8','-81.25','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(107,'GTBY','CU','00','19.93','-75.11','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(108,'LPAZ','GT','00','-16.29','-68.13','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(109,'MTDJ','CU','00','18.23','-77.53','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(110,'OTAV','IU','00','0.24','-78.45','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(111,'PAC1','EC','','0.27','-78.79','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(112,'PAYG','IU','00','-0.67','-90.29','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(113,'PNME','RP','','8.49','-80.33','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(114,'PTP','RP','','8.2','-82.87','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(115,'SDDR','CU','00','18.98','-71.29','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(116,'SOCV','VE','','8.28','-70.86','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(117,'TBTG','BR','','-4.19','-69.91','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(118,'TGUH','CU','00','14.06','-87.27','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(119,'TULM','EC','','0.72','-77.79','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(120,'UPA','RP','','8.98','-79.53','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(121,'UPD2','RP','','8.55','-78.01','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(122,'CONO','CM','00','2.33','-76.4','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(123,'MARO','CM','00','2.84','-75.95','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(124,'SOTO','CM','00','2.13','-76.61','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(125,'LL1C','CM','00','9.54','-73.56','SUB','HHZ');
INSERT INTO "service_estacion" VALUES(126,'LL5C','CM','00','9.75','-73.72','SUB','HHZ');
INSERT INTO "service_estacion" VALUES(127,'LL6C','CM','00','9.74','-73.27','SUB','HHZ');
INSERT INTO "service_estacion" VALUES(128,'ACON','NU','','11.968','-85.174','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(129,'ANWB','CU','00','17.66853','-61.78557','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(130,'BBGH','CU','20','13.1434','-59.5588','INTER','LN2');
INSERT INTO "service_estacion" VALUES(131,'BONI','EC','','0.4528','-77.5297','INTER','HHN');
INSERT INTO "service_estacion" VALUES(132,'CNGN','NU','','12.5','-86.6985','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(133,'COHC','EC','','-2.4661','-79.2574','INTER','HHN');
INSERT INTO "service_estacion" VALUES(134,'CRIN','NU','','12.696167','-87.0315','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(135,'FLF1','EC','','-0.35743','-79.84268','INTER','HHN');
INSERT INTO "service_estacion" VALUES(136,'GRGR','CU','00','12.1324','-61.654','INTER','BH1');
INSERT INTO "service_estacion" VALUES(137,'GRTK','CU','00','21.51149','-71.1327','INTER','BH2');
INSERT INTO "service_estacion" VALUES(138,'PPLP','EC','','-1.5451','-80.775','INTER','HHZ');
INSERT INTO "service_estacion" VALUES(139,'MASN','NU','','12.00283','-86.01491','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(140,'SDV','IU','00','8.8839','-70.634','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(141,'SJG','IU','00','18.1091','-66.15','INTER','BHZ');
INSERT INTO "service_estacion" VALUES(142,'SAML','IU','00','-8.9489','-63.1831','INTER','BH1');
INSERT INTO "service_estacion" VALUES(143,'PTGA','IU','00','-0.7308','-59.9666','INTER','BH1');
INSERT INTO "service_estacion" VALUES(144,'JTS','II','00','10.2908','-84.9525','INTER','BH1');
INSERT INTO "service_estacion" VALUES(145,'NNA','II','10','-11.9875','-76.8422','INTER','BH2');
INSERT INTO "service_estacion" VALUES(146,'AUCA','EC','','-0.55','-76.9','INTER','HHE');
INSERT INTO "service_estacion" VALUES(147,'PTGL','EC','01','0.78153','-80.03037','INTER','HHE');
INSERT INTO "service_estacion" VALUES(148,'MCRA','EC','','-4.3697','-79.9544','INTER','HHE');
INSERT INTO "service_estacion" VALUES(149,'PIAT','EC','','-0.9771','-78.2616','INTER','BLE');
COMMIT;
