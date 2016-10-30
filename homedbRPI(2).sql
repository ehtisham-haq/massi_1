-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 07, 2016 at 02:47 AM
-- Server version: 5.5.52-0+deb8u1
-- PHP Version: 5.6.24-0+deb8u1

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
`module_id` int(11) NOT NULL,
  `module_name` varchar(255) NOT NULL,
  `room_id` int(11) NOT NULL,
  `module_type` varchar(50) NOT NULL,
  `module_version` varchar(10) NOT NULL,
  `IP_address` varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `module`
--

INSERT INTO `module` (`module_id`, `module_name`, `room_id`, `module_type`, `module_version`, `IP_address`) VALUES
(1, 'Server', 23, 'master, physical', 'v1.0', '192.168.0.202'),
(2, 'client_1', 22, 'physical', 'v1.4', '192.168.0.200');

-- --------------------------------------------------------

--
-- Table structure for table `people`
--

CREATE TABLE IF NOT EXISTS `people` (
`people_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(50) NOT NULL,
  `accounttype` varchar(15) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

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
`connect_id` int(11) NOT NULL,
  `people_id` int(11) NOT NULL,
  `room_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE IF NOT EXISTS `room` (
`room_id` int(11) NOT NULL,
  `room_name` varchar(45) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

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
`sensor_id` int(11) NOT NULL,
  `sensor_name` varchar(255) NOT NULL,
  `power_status` varchar(10) NOT NULL,
  `data_status` varchar(50) NOT NULL,
  `module_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `switches`
--

CREATE TABLE IF NOT EXISTS `switches` (
`switch_id` int(11) NOT NULL,
  `switch_name` varchar(255) NOT NULL,
  `switch_state` varchar(20) NOT NULL,
  `module_id` int(11) NOT NULL,
  `module_switch` varchar(10) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `switches`
--

INSERT INTO `switches` (`switch_id`, `switch_name`, `switch_state`, `module_id`, `module_switch`) VALUES
(1, 'Light', 'ON', 2, 'A'),
(9, 'Out Lamp', 'ON', 2, 'D'),
(11, 'DSA', 'ON', 2, 'C'),
(12, 'qqwe', 'OFF', 2, 'B');

-- --------------------------------------------------------

--
-- Table structure for table `switch_time`
--

CREATE TABLE IF NOT EXISTS `switch_time` (
`time_id` int(11) NOT NULL,
  `switch_id` int(11) NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `state` varchar(5) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `switch_time`
--

INSERT INTO `switch_time` (`time_id`, `switch_id`, `start_time`, `end_time`, `state`) VALUES
(1, 1, '03:35:15', '06:00:00', 'ON');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `module`
--
ALTER TABLE `module`
 ADD PRIMARY KEY (`module_id`), ADD KEY `room_id` (`room_id`);

--
-- Indexes for table `people`
--
ALTER TABLE `people`
 ADD PRIMARY KEY (`people_id`), ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `peopleroom`
--
ALTER TABLE `peopleroom`
 ADD PRIMARY KEY (`connect_id`), ADD KEY `room_id` (`room_id`), ADD KEY `people_id` (`people_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
 ADD PRIMARY KEY (`room_id`), ADD KEY `room_id` (`room_id`);

--
-- Indexes for table `sensors`
--
ALTER TABLE `sensors`
 ADD PRIMARY KEY (`sensor_id`), ADD KEY `module_id` (`module_id`);

--
-- Indexes for table `switches`
--
ALTER TABLE `switches`
 ADD PRIMARY KEY (`switch_id`), ADD KEY `module_id` (`module_id`);

--
-- Indexes for table `switch_time`
--
ALTER TABLE `switch_time`
 ADD PRIMARY KEY (`time_id`), ADD UNIQUE KEY `link_with_switch_id` (`switch_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `module`
--
ALTER TABLE `module`
MODIFY `module_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `people`
--
ALTER TABLE `people`
MODIFY `people_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `peopleroom`
--
ALTER TABLE `peopleroom`
MODIFY `connect_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
MODIFY `room_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `sensors`
--
ALTER TABLE `sensors`
MODIFY `sensor_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `switches`
--
ALTER TABLE `switches`
MODIFY `switch_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `switch_time`
--
ALTER TABLE `switch_time`
MODIFY `time_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
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

--
-- Constraints for table `switch_time`
--
ALTER TABLE `switch_time`
ADD CONSTRAINT `switch_time_ibfk_1` FOREIGN KEY (`switch_id`) REFERENCES `switches` (`switch_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
