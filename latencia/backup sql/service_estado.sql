BEGIN TRANSACTION;
DROP TABLE IF EXISTS "service_estado";
CREATE TABLE "service_estado" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "estado" text NOT NULL, "fecha" date NOT NULL, "estacion_id" integer NOT NULL REFERENCES "service_estacion" ("id"));
INSERT INTO "service_estado" VALUES(3631,'ok','2016-08-10 11:20:28',1);
INSERT INTO "service_estado" VALUES(3632,'ok','2016-08-10 11:20:13',3);
INSERT INTO "service_estado" VALUES(3633,'ok','2016-08-10 11:20:20',5);
INSERT INTO "service_estado" VALUES(3634,'ok','2016-08-10 11:20:26',6);
INSERT INTO "service_estado" VALUES(3635,'ok','2016-08-10 11:20:22',7);
INSERT INTO "service_estado" VALUES(3636,'ok','2016-08-10 11:20:19',8);
INSERT INTO "service_estado" VALUES(3637,'ok','2016-08-10 11:20:11',9);
INSERT INTO "service_estado" VALUES(3638,'ok','2016-08-10 11:20:14',10);
INSERT INTO "service_estado" VALUES(3639,'ok','2016-08-10 11:20:15',13);
INSERT INTO "service_estado" VALUES(3640,'ok','2016-08-10 11:19:40',14);
INSERT INTO "service_estado" VALUES(3641,'ok','2016-08-10 11:19:44',16);
INSERT INTO "service_estado" VALUES(3642,'ok','2016-08-10 11:20:24',17);
INSERT INTO "service_estado" VALUES(3643,'ok','2016-08-10 11:20:16',18);
INSERT INTO "service_estado" VALUES(3644,'ok','2016-08-10 11:20:03',19);
INSERT INTO "service_estado" VALUES(3645,'ok','2016-08-10 11:20:07',20);
INSERT INTO "service_estado" VALUES(3646,'ok','2016-08-10 11:20:19',22);
INSERT INTO "service_estado" VALUES(3647,'fuera','2016-08-10 11:20:29',23);
INSERT INTO "service_estado" VALUES(3648,'ok','2016-08-10 11:20:08',24);
INSERT INTO "service_estado" VALUES(3649,'ok','2016-08-10 11:20:24',25);
INSERT INTO "service_estado" VALUES(3650,'fuera','2016-08-10 11:20:29',26);
INSERT INTO "service_estado" VALUES(3651,'ok','2016-08-10 11:20:12',27);
INSERT INTO "service_estado" VALUES(3652,'ok','2016-08-10 11:20:28',28);
INSERT INTO "service_estado" VALUES(3653,'ok','2016-08-10 11:20:21',29);
INSERT INTO "service_estado" VALUES(3654,'ok','2016-08-10 11:20:16',30);
INSERT INTO "service_estado" VALUES(3655,'ok','2016-08-10 11:19:54',31);
INSERT INTO "service_estado" VALUES(3656,'ok','2016-08-10 11:20:20',32);
INSERT INTO "service_estado" VALUES(3657,'ok','2016-08-10 11:20:16',33);
INSERT INTO "service_estado" VALUES(3658,'ok','2016-08-10 11:20:12',34);
INSERT INTO "service_estado" VALUES(3659,'ok','2016-08-10 11:20:19',35);
INSERT INTO "service_estado" VALUES(3660,'ok','2016-08-10 11:20:02',36);
INSERT INTO "service_estado" VALUES(3661,'ok','2016-08-10 11:20:21',37);
INSERT INTO "service_estado" VALUES(3662,'ok','2016-08-10 11:20:23',38);
INSERT INTO "service_estado" VALUES(3663,'ok','2016-08-10 11:20:12',39);
INSERT INTO "service_estado" VALUES(3664,'ok','2016-08-10 11:20:22',40);
INSERT INTO "service_estado" VALUES(3665,'fuera','2016-08-10 11:20:29',41);
INSERT INTO "service_estado" VALUES(3666,'ok','2016-08-10 11:19:40',42);
INSERT INTO "service_estado" VALUES(3667,'ok','2016-08-10 11:20:21',43);
INSERT INTO "service_estado" VALUES(3668,'ok','2016-08-10 11:20:27',44);
INSERT INTO "service_estado" VALUES(3669,'fuera','2016-08-10 11:20:29',45);
INSERT INTO "service_estado" VALUES(3670,'ok','2016-08-10 11:20:23',46);
INSERT INTO "service_estado" VALUES(3671,'ok','2016-08-10 11:20:27',47);
INSERT INTO "service_estado" VALUES(3672,'ok','2016-08-10 11:20:19',48);
INSERT INTO "service_estado" VALUES(3673,'ok','2016-08-10 11:20:16',49);
INSERT INTO "service_estado" VALUES(3674,'ok','2016-08-10 11:20:25',50);
INSERT INTO "service_estado" VALUES(3675,'ok','2016-08-10 11:20:24',51);
INSERT INTO "service_estado" VALUES(3676,'fuera','2016-08-10 11:20:29',52);
INSERT INTO "service_estado" VALUES(3677,'ok','2016-08-10 11:20:05',53);
INSERT INTO "service_estado" VALUES(3678,'ok','2016-08-10 11:20:28',54);
INSERT INTO "service_estado" VALUES(3679,'fuera','2016-08-10 11:20:29',55);
INSERT INTO "service_estado" VALUES(3680,'ok','2016-08-10 11:20:17',58);
INSERT INTO "service_estado" VALUES(3681,'ok','2016-08-10 11:19:54',59);
INSERT INTO "service_estado" VALUES(3682,'ok','2016-08-10 11:20:23',60);
INSERT INTO "service_estado" VALUES(3683,'ok','2016-08-10 11:20:14',63);
INSERT INTO "service_estado" VALUES(3684,'fuera','2016-08-10 11:20:29',65);
INSERT INTO "service_estado" VALUES(3685,'ok','2016-08-10 11:20:16',67);
INSERT INTO "service_estado" VALUES(3686,'ok','2016-08-10 11:20:12',68);
INSERT INTO "service_estado" VALUES(3687,'ok','2016-08-10 11:20:22',69);
INSERT INTO "service_estado" VALUES(3688,'ok','2016-08-10 11:20:28',74);
INSERT INTO "service_estado" VALUES(3689,'ok','2016-08-10 11:19:54',75);
INSERT INTO "service_estado" VALUES(3690,'ok','2016-08-10 11:20:11',76);
INSERT INTO "service_estado" VALUES(3691,'ok','2016-08-10 11:20:25',81);
INSERT INTO "service_estado" VALUES(3692,'fuera','2016-08-10 11:20:29',82);
INSERT INTO "service_estado" VALUES(3693,'ok','2016-08-10 11:19:50',88);
INSERT INTO "service_estado" VALUES(3694,'fuera','2016-08-10 11:20:29',90);
INSERT INTO "service_estado" VALUES(3695,'fuera','2016-08-10 11:20:29',93);
INSERT INTO "service_estado" VALUES(3696,'ok','2016-08-10 11:20:00',94);
INSERT INTO "service_estado" VALUES(3697,'fuera','2016-08-10 11:20:29',95);
INSERT INTO "service_estado" VALUES(3698,'ok','2016-08-10 11:20:27',96);
INSERT INTO "service_estado" VALUES(3699,'ok','2016-08-10 11:19:31',97);
INSERT INTO "service_estado" VALUES(3700,'ok','2016-08-10 11:19:45',98);
INSERT INTO "service_estado" VALUES(3701,'ok','2016-08-10 11:20:22',99);
INSERT INTO "service_estado" VALUES(3702,'ok','2016-08-10 11:20:12',100);
INSERT INTO "service_estado" VALUES(3703,'ok','2016-08-10 11:20:02',101);
INSERT INTO "service_estado" VALUES(3704,'ok','2016-08-10 11:20:26',102);
INSERT INTO "service_estado" VALUES(3705,'ok','2016-08-10 11:19:31',103);
INSERT INTO "service_estado" VALUES(3706,'fuera','2016-08-10 11:20:29',104);
INSERT INTO "service_estado" VALUES(3707,'ok','2016-08-10 11:20:19',105);
INSERT INTO "service_estado" VALUES(3708,'fuera','2016-08-10 11:20:29',106);
INSERT INTO "service_estado" VALUES(3709,'fuera','2016-08-10 11:20:29',107);
INSERT INTO "service_estado" VALUES(3710,'ok','2016-08-10 11:20:12',108);
INSERT INTO "service_estado" VALUES(3711,'ok','2016-08-10 11:20:22',109);
INSERT INTO "service_estado" VALUES(3712,'ok','2016-08-10 11:19:37',110);
INSERT INTO "service_estado" VALUES(3713,'fuera','2016-08-10 11:20:20',111);
INSERT INTO "service_estado" VALUES(3714,'ok','2016-08-10 11:19:37',112);
INSERT INTO "service_estado" VALUES(3715,'ok','2016-08-10 11:20:15',113);
INSERT INTO "service_estado" VALUES(3716,'fuera','2016-08-10 11:20:29',114);
INSERT INTO "service_estado" VALUES(3717,'ok','2016-08-10 11:19:31',115);
INSERT INTO "service_estado" VALUES(3718,'ok','2016-08-10 11:19:42',116);
INSERT INTO "service_estado" VALUES(3719,'fuera','2016-08-10 11:20:29',117);
INSERT INTO "service_estado" VALUES(3720,'ok','2016-08-10 11:20:22',118);
INSERT INTO "service_estado" VALUES(3721,'ok','2016-08-10 11:20:15',119);
INSERT INTO "service_estado" VALUES(3722,'ok','2016-08-10 11:20:10',120);
INSERT INTO "service_estado" VALUES(3723,'ok','2016-08-10 11:20:25',121);
INSERT INTO "service_estado" VALUES(3724,'ok','2016-08-10 11:20:07',122);
INSERT INTO "service_estado" VALUES(3725,'ok','2016-08-10 11:19:55',123);
INSERT INTO "service_estado" VALUES(3726,'ok','2016-08-10 11:19:44',124);
INSERT INTO "service_estado" VALUES(3727,'ok','2016-08-10 11:20:03',125);
INSERT INTO "service_estado" VALUES(3728,'ok','2016-08-10 11:20:20',126);
INSERT INTO "service_estado" VALUES(3729,'ok','2016-08-10 11:20:04',127);
INSERT INTO "service_estado" VALUES(3730,'ok','2016-08-10 11:20:04',128);
INSERT INTO "service_estado" VALUES(3731,'ok','2016-08-10 11:19:56',129);
INSERT INTO "service_estado" VALUES(3732,'ok','2016-08-10 11:19:57',130);
INSERT INTO "service_estado" VALUES(3733,'ok','2016-08-10 11:20:22',131);
INSERT INTO "service_estado" VALUES(3734,'ok','2016-08-10 11:20:26',132);
INSERT INTO "service_estado" VALUES(3735,'ok','2016-08-10 11:19:44',133);
INSERT INTO "service_estado" VALUES(3736,'ok','2016-08-10 11:20:16',134);
INSERT INTO "service_estado" VALUES(3737,'fuera','2016-08-10 11:20:20',135);
INSERT INTO "service_estado" VALUES(3738,'ok','2016-08-10 11:20:22',136);
INSERT INTO "service_estado" VALUES(3739,'ok','2016-08-10 11:19:43',137);
INSERT INTO "service_estado" VALUES(3740,'ok','2016-08-10 11:20:19',138);
INSERT INTO "service_estado" VALUES(3741,'fuera','2016-08-10 11:20:29',139);
INSERT INTO "service_estado" VALUES(3742,'fuera','2016-08-10 11:20:29',140);
INSERT INTO "service_estado" VALUES(3743,'fuera','2016-08-10 11:20:29',141);
INSERT INTO "service_estado" VALUES(3744,'fuera','2016-08-10 11:20:29',142);
INSERT INTO "service_estado" VALUES(3745,'fuera','2016-08-10 11:20:29',143);
INSERT INTO "service_estado" VALUES(3746,'fuera','2016-08-10 11:20:29',144);
INSERT INTO "service_estado" VALUES(3747,'fuera','2016-08-10 11:20:29',145);
INSERT INTO "service_estado" VALUES(3748,'fuera','2016-08-10 11:20:29',146);
INSERT INTO "service_estado" VALUES(3749,'ok','2016-08-10 11:20:08',147);
INSERT INTO "service_estado" VALUES(3750,'fuera','2016-08-10 11:20:18',148);
INSERT INTO "service_estado" VALUES(3751,'fuera','2016-08-10 11:20:29',149);
COMMIT;
