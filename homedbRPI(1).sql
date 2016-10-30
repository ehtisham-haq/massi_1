-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 01, 2016 at 03:43 PM
-- Server version: 5.5.47-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `homedbRPI`
--

-- --------------------------------------------------------

--
-- Table structure for table `module`
--

CREATE TABLE IF NOT EXISTS `module` (
  `module_id` int(11) NOT NULL AUTO_INCREMENT,
  `module_name` varchar(255) NOT NULL,
  `room_id` int(11) NOT NULL,
  PRIMARY KEY (`module_id`),
  KEY `room_id` (`room_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `module`
--

INSERT INTO `module` (`module_id`, `module_name`, `room_id`) VALUES
(1, 'test_1', 22);

-- --------------------------------------------------------

--
-- Table structure for table `people`
--

CREATE TABLE IF NOT EXISTS `people` (
  `people_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(50) NOT NULL,
  `accounttype` varchar(15) NOT NULL,
  PRIMARY KEY (`people_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `people`
--

INSERT INTO `people` (`people_id`, `name`, `username`, `password`, `accounttype`) VALUES
(6, 'Ahmed', 'mahmed', 'ahmed', 'local'),
(9, 'Ehtisham ul haq', 'ehtisham', 'ehtisham', 'admin'),
(10, 'a', 'a', 'a', 'admin'),
(11, 'l', 'l', 'l', 'local');

-- --------------------------------------------------------

--
-- Table structure for table `peopleroom`
--

CREATE TABLE IF NOT EXISTS `peopleroom` (
  `connect_id` int(11) NOT NULL AUTO_INCREMENT,
  `people_id` int(11) NOT NULL,
  `room_id` int(11) NOT NULL,
  PRIMARY KEY (`connect_id`),
  KEY `room_id` (`room_id`),
  KEY `people_id` (`people_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `peopleroom`
--

INSERT INTO `peopleroom` (`connect_id`, `people_id`, `room_id`) VALUES
(6, 10, 22),
(7, 10, 24),
(8, 11, 25),
(9, 11, 23);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE IF NOT EXISTS `room` (
  `room_id` int(11) NOT NULL AUTO_INCREMENT,
  `room_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`room_id`),
  KEY `room_id` (`room_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=26 ;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_id`, `room_name`) VALUES
(22, 'commonroom'),
(23, 'livingroom'),
(24, 'bedroom1'),
(25, 'bedroom2');

-- --------------------------------------------------------

--
-- Table structure for table `sensors`
--

CREATE TABLE IF NOT EXISTS `sensors` (
  `sensor_id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_name` varchar(255) NOT NULL,
  `power_status` varchar(10) NOT NULL,
  `data_status` varchar(50) NOT NULL,
  `module_id` int(11) NOT NULL,
  PRIMARY KEY (`sensor_id`),
  KEY `module_id` (`module_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `sensors`
--

INSERT INTO `sensors` (`sensor_id`, `sensor_name`, `power_status`, `data_status`, `module_id`) VALUES
(1, 'PIR_1', 'OFF', 'No_Motion_detected', 1);

-- --------------------------------------------------------

--
-- Table structure for table `switches`
--

CREATE TABLE IF NOT EXISTS `switches` (
  `switch_id` int(11) NOT NULL AUTO_INCREMENT,
  `switch_name` varchar(255) NOT NULL,
  `switch_state` varchar(20) NOT NULL,
  `module_id` int(11) NOT NULL,
  PRIMARY KEY (`switch_id`),
  KEY `module_id` (`module_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `switches`
--

INSERT INTO `switches` (`switch_id`, `switch_name`, `switch_state`, `module_id`) VALUES
(3, 'load_1', '0', 1),
(4, 'load_2', '0', 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `module`
--
ALTER TABLE `module`
  ADD CONSTRAINT `module_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`);

--
-- Constraints for table `peopleroom`
--
ALTER TABLE `peopleroom`
  ADD CONSTRAINT `peopleroom_ibfk_1` FOREIGN KEY (`people_id`) REFERENCES `people` (`people_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `peopleroom_ibfk_2` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`);

--
-- Constraints for table `sensors`
--
ALTER TABLE `sensors`
  ADD CONSTRAINT `sensors_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `module` (`module_id`);

--
-- Constraints for table `switches`
--
ALTER TABLE `switches`
  ADD CONSTRAINT `switches_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `module` (`module_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
