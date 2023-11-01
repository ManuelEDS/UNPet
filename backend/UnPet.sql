-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema unpet
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema unpet
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `unpet` DEFAULT CHARACTER SET utf8mb4 ;
USE `unpet` ;

-- -----------------------------------------------------
-- Table `unpet`.`localidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `unpet`.`localidades` (
  `idLocalidades` INT NOT NULL,
  `NOMBRE` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idLocalidades`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `unpet`.`organizacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `unpet`.`organizacion` (
  `idPersona` INT NOT NULL,
  `Contraseña` VARCHAR(45) NOT NULL,
  `DIRECCION` VARCHAR(100) NOT NULL,
  `NIT` INT NOT NULL,
  `DESCRIPCION` VARCHAR(300) NULL DEFAULT NULL,
  `TELEFONO` INT NOT NULL,
  `CORREO` VARCHAR(100) NOT NULL,
  `URLFOTO` VARCHAR(700) NULL DEFAULT NULL,
  `idLocalidades` INT NOT NULL,
  PRIMARY KEY (`idPersona`),
  INDEX `fk_Organizacion_Localidades1_idx` (`idLocalidades` ASC) VISIBLE,
  CONSTRAINT `fk_Organizacion_Localidades1`
    FOREIGN KEY (`idLocalidades`)
    REFERENCES `unpet`.`localidades` (`idLocalidades`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `unpet`.`persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `unpet`.`persona` (
  `idPersona` INT NOT NULL,
  `Contraseña` VARCHAR(45) NOT NULL,
  `esModerador` TINYINT(1) NOT NULL,
  `DOCUMENTO` VARCHAR(5) NOT NULL,
  `No DOCUMENTO` VARCHAR(45) NOT NULL,
  `SEXO` TINYINT(1) NOT NULL,
  `DESCRIPCION` VARCHAR(300) NULL DEFAULT NULL,
  `TELEFONO` INT NOT NULL,
  `CORREO` VARCHAR(100) NOT NULL,
  `URLFOTO` VARCHAR(700) NULL DEFAULT NULL,
  `idLocalidades` INT NOT NULL,
  PRIMARY KEY (`idPersona`),
  INDEX `fk_Persona_Localidades1_idx` (`idLocalidades` ASC) VISIBLE,
  CONSTRAINT `fk_Persona_Localidades1`
    FOREIGN KEY (`idLocalidades`)
    REFERENCES `unpet`.`localidades` (`idLocalidades`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `unpet`.`publicacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `unpet`.`publicacion` (
  `idPublicacion` INT NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  `Titulo` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(45) NOT NULL,
  `FechaPublicacion` VARCHAR(45) NOT NULL,
  `idOrganizacion` INT NULL DEFAULT NULL,
  `idPersona` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idPublicacion`),
  INDEX `fk_Publicacion_Organizacion1_idx` (`idOrganizacion` ASC) VISIBLE,
  INDEX `fk_Publicacion_Persona1_idx` (`idPersona` ASC) VISIBLE,
  CONSTRAINT `fk_Publicacion_Organizacion1`
    FOREIGN KEY (`idOrganizacion`)
    REFERENCES `unpet`.`organizacion` (`idPersona`),
  CONSTRAINT `fk_Publicacion_Persona1`
    FOREIGN KEY (`idPersona`)
    REFERENCES `unpet`.`persona` (`idPersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `unpet`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `unpet`.`comentarios` (
  `idComentarios` INT NOT NULL,
  `Contenido` VARCHAR(300) NOT NULL,
  `Respuesta` VARCHAR(300) NULL DEFAULT NULL,
  `Publicacion_idPublicacion` INT NOT NULL,
  `idComentador` INT NULL DEFAULT NULL,
  `idRespondedor` INT NULL DEFAULT NULL,
  `idComentadorOrg` INT NULL DEFAULT NULL,
  `idRespondedorOrg` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idComentarios`),
  INDEX `fk_Comentarios_Publicacion1_idx` (`Publicacion_idPublicacion` ASC) VISIBLE,
  INDEX `fk_Comentarios_Persona1_idx` (`idComentador` ASC) VISIBLE,
  INDEX `fk_Comentarios_Persona2_idx` (`idRespondedor` ASC) VISIBLE,
  INDEX `fk_Comentarios_Organizacion1_idx` (`idComentadorOrg` ASC) VISIBLE,
  INDEX `fk_Comentarios_Organizacion2_idx` (`idRespondedorOrg` ASC) VISIBLE,
  CONSTRAINT `fk_Comentarios_Organizacion1`
    FOREIGN KEY (`idComentadorOrg`)
    REFERENCES `unpet`.`organizacion` (`idPersona`),
  CONSTRAINT `fk_Comentarios_Organizacion2`
    FOREIGN KEY (`idRespondedorOrg`)
    REFERENCES `unpet`.`organizacion` (`idPersona`),
  CONSTRAINT `fk_Comentarios_Persona1`
    FOREIGN KEY (`idComentador`)
    REFERENCES `unpet`.`persona` (`idPersona`),
  CONSTRAINT `fk_Comentarios_Persona2`
    FOREIGN KEY (`idRespondedor`)
    REFERENCES `unpet`.`persona` (`idPersona`),
  CONSTRAINT `fk_Comentarios_Publicacion1`
    FOREIGN KEY (`Publicacion_idPublicacion`)
    REFERENCES `unpet`.`publicacion` (`idPublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `unpet`.`mascota`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `unpet`.`mascota` (
  `idMascota` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Especie` TINYINT(1) NOT NULL,
  `Raza` VARCHAR(45) NOT NULL,
  `Sexo` TINYINT(1) NOT NULL,
  `FechaNacimiento` DATE NOT NULL,
  `UrlFoto` VARCHAR(700) NULL DEFAULT NULL,
  `idPersona` INT NULL DEFAULT NULL,
  `idOrganizacion` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idMascota`),
  INDEX `fk_Mascota_Persona1_idx` (`idPersona` ASC) VISIBLE,
  INDEX `fk_Mascota_Organizacion1_idx` (`idOrganizacion` ASC) VISIBLE,
  CONSTRAINT `fk_Mascota_Organizacion1`
    FOREIGN KEY (`idOrganizacion`)
    REFERENCES `unpet`.`organizacion` (`idPersona`),
  CONSTRAINT `fk_Mascota_Persona1`
    FOREIGN KEY (`idPersona`)
    REFERENCES `unpet`.`persona` (`idPersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
