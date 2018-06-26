-- MySQL Script generated by MySQL Workbench
-- mar. 05 juin 2018 19:10:55 CEST
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema CDFgeo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema CDFgeo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `CDFgeo` DEFAULT CHARACTER SET utf8 ;
USE `CDFgeo` ;

-- -----------------------------------------------------
-- Table `CDFgeo`.`chaire`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CDFgeo`.`chaire` ;

CREATE TABLE IF NOT EXISTS `CDFgeo`.`chaire` (
  `chaire_id` SMALLINT NOT NULL,
  `chaire_intitule` TINYTEXT NOT NULL,
  `chaire_type` TINYTEXT NOT NULL,
  `chaire_debut` VARCHAR(4) NOT NULL,
  `chaire_fin` VARCHAR(4) NOT NULL,
  `chaire_precision` TEXT NULL,
  PRIMARY KEY (`chaire_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CDFgeo`.`personne`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CDFgeo`.`personne` ;

CREATE TABLE IF NOT EXISTS `CDFgeo`.`personne` (
  `personne_id` SMALLINT NOT NULL,
  `personne_prenom` TINYTEXT NOT NULL,
  `personne_nom` TINYTEXT NOT NULL,
  `personne_statut` TINYTEXT NOT NULL,
  `personne_naissance` VARCHAR(4) NULL,
  `personne_deces` VARCHAR(4) NULL,
  `personne_precision` TEXT NULL,
  `personne_liensexternes` TINYTEXT NULL,
  `chaire_chaire_id` SMALLINT NULL,
  PRIMARY KEY (`personne_id`),
  INDEX `fk_personne_chaire_idx` (`chaire_chaire_id` ASC),
  CONSTRAINT `fk_personne_chaire`
    FOREIGN KEY (`chaire_chaire_id`)
    REFERENCES `CDFgeo`.`chaire` (`chaire_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CDFgeo`.`ville`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CDFgeo`.`ville` ;

CREATE TABLE IF NOT EXISTS `CDFgeo`.`ville` (
  `ville_id` SMALLINT NOT NULL,
  `ville_intitule` TINYTEXT NULL,
  `ville_lat` FLOAT NULL,
  `ville_long` FLOAT NULL,
  PRIMARY KEY (`ville_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CDFgeo`.`mission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CDFgeo`.`mission` ;

CREATE TABLE IF NOT EXISTS `CDFgeo`.`mission` (
  `mission_id` SMALLINT NOT NULL,
  `mission_intitule` TINYTEXT NOT NULL,
  `mission_type` TINYTEXT NULL,
  `mission_institution` TINYTEXT NULL,
  `mission_date_debut` VARCHAR(10) NULL,
  `mission_date_fin` VARCHAR(10) NULL,
  `mission_dates` TINYTEXT NULL,
  `mission_precision` TEXT NULL,
  PRIMARY KEY (`mission_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CDFgeo`.`personne_mission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CDFgeo`.`personne_mission` ;

CREATE TABLE IF NOT EXISTS `CDFgeo`.`personne_mission` (
  `personne_mission_id` SMALLINT NOT NULL AUTO_INCREMENT,
  `personne_mission_personne_id` SMALLINT NOT NULL,
  `personne_mission_mission_id` SMALLINT NOT NULL,
  PRIMARY KEY (`personne_mission_id`),
  INDEX `fk_personne_mission_mission1_idx` (`personne_mission_mission_id` ASC),
  INDEX `fk_personne_mission_personne1_idx` (`personne_mission_personne_id` ASC),
  CONSTRAINT `fk_personne_mission_personne1`
    FOREIGN KEY (`personne_mission_personne_id`)
    REFERENCES `CDFgeo`.`personne` (`personne_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_personne_mission_mission1`
    FOREIGN KEY (`personne_mission_mission_id`)
    REFERENCES `CDFgeo`.`mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CDFgeo`.`pays`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CDFgeo`.`pays` ;

CREATE TABLE IF NOT EXISTS `CDFgeo`.`pays` (
  `pays_id` SMALLINT NOT NULL,
  `pays_intitule` TINYTEXT NOT NULL,
  `pays_lat` FLOAT NOT NULL,
  `pays_long` FLOAT NOT NULL,
  PRIMARY KEY (`pays_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CDFgeo`.`mission_lieu`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CDFgeo`.`mission_lieu` ;

CREATE TABLE IF NOT EXISTS `CDFgeo`.`mission_lieu` (
  `mission_lieu_id` SMALLINT NOT NULL AUTO_INCREMENT,
  `mission_lieu_mission_id` SMALLINT NOT NULL,
  `mission_lieu_ville_id` SMALLINT NULL,
  `mission_lieu_pays_id` SMALLINT NOT NULL,
  PRIMARY KEY (`mission_lieu_id`),
  INDEX `fk_mission_lieu_ville1_idx` (`mission_lieu_ville_id` ASC),
  INDEX `fk_mission_lieu_mission1_idx` (`mission_lieu_mission_id` ASC),
  INDEX `fk_mission_lieu_pays1_idx` (`mission_lieu_pays_id` ASC),
  CONSTRAINT `fk_mission_lieu_mission`
    FOREIGN KEY (`mission_lieu_mission_id`)
    REFERENCES `CDFgeo`.`mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mission_ville`
    FOREIGN KEY (`mission_lieu_ville_id`)
    REFERENCES `CDFgeo`.`ville` (`ville_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mission_pays`
    FOREIGN KEY (`mission_lieu_pays_id`)
    REFERENCES `CDFgeo`.`pays` (`pays_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

DROP USER IF EXISTS cdfgeo_user;
CREATE USER 'cdfgeo_user' IDENTIFIED BY 'password';
GRANT INSERT, SELECT, UPDATE, DELETE ON `CDFgeo`.* TO 'cdfgeo_user';
