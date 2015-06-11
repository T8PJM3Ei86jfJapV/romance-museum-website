CREATE DATABASE IF NOT EXISTS `romance_museum`;
#GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER ON romance_museum.* TO hack@localhost IDENTIFIED BY 'password';
USE `romance_museum`;

DROP TABLE IF EXISTS `romance_museum`.`user`;
CREATE TABLE  `romance_museum`.`user` (
    `u_id` VARCHAR( 16 ) NOT NULL,
    `u_nickname` VARCHAR( 32 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `u_password` VARCHAR( 16 ) NOT NULL,
    `u_email` VARCHAR( 32 ) NOT NULL,
    `u_qq` VARCHAR( 12 ) NULL,
    PRIMARY KEY (  `u_id` )
) ENGINE = MYISAM DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `romance_museum`.`article`;
CREATE TABLE  `romance_museum`.`article` (
    `a_id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `u_id` VARCHAR( 16 ) NOT NULL,
    `a_title` VARCHAR( 64 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `a_mode` VARCHAR( 16 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `a_content` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
    PRIMARY KEY (  `a_id` ),
    INDEX (  `u_id` )
) ENGINE = MYISAM DEFAULT CHARSET=utf8;