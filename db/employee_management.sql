-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 22, 2024 at 06:42 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `employee_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `addemployee`
--

CREATE TABLE IF NOT EXISTS `addemployee` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `ename` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `mbl` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `job` varchar(50) NOT NULL,
  `desin` varchar(50) NOT NULL,
  `psw` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `addemployee`
--

INSERT INTO `addemployee` (`id`, `ename`, `addr`, `mbl`, `dob`, `email`, `job`, `desin`, `psw`) VALUES
(1, 'rs', 'coimbatore', '9078764534', '23/08/2001', 'rs@gmail.com', 'bcom', 'accountant', '12345'),
(2, 'rindhi', 'coimbatore', '9078764534', '2024-05-07', 'rindhiyamanickam23@gmail.com', 'BE', 'Electric Worker', '1234'),
(3, 'sakshi', 'coimbatore', '9078764534', '23/08/2001', 'risibindhu@gmail.com', 'BE', 'Engineer', '1234'),
(4, 'Ravi', 'coimbatore', '9078764578', '25/06/1998', 'ravi@gmail.com', 'BCom', 'Finance', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE IF NOT EXISTS `adminlogin` (
  `user` varchar(50) NOT NULL,
  `psw` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`user`, `psw`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE IF NOT EXISTS `attendance` (
  `aid` int(50) NOT NULL AUTO_INCREMENT,
  `dat` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `reason` varchar(50) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`aid`, `dat`, `status`, `reason`) VALUES
(2, '2024-05-20', 'Present', 'present today');

-- --------------------------------------------------------

--
-- Table structure for table `leave_applications`
--

CREATE TABLE IF NOT EXISTS `leave_applications` (
  `emp_id` varchar(50) NOT NULL,
  `start_date` varchar(100) NOT NULL,
  `end_date` varchar(50) NOT NULL,
  `reason` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `leave_applications`
--

INSERT INTO `leave_applications` (`emp_id`, `start_date`, `end_date`, `reason`, `status`) VALUES
('2', '2024-05-22', '2024-05-25', 'sick leave', 'pending'),
('3', '2024-05-14', '2024-05-14', 'for foreign trip', 'rejected');

-- --------------------------------------------------------

--
-- Table structure for table `salary`
--

CREATE TABLE IF NOT EXISTS `salary` (
  `sid` int(50) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `sdat` varchar(50) NOT NULL,
  `ename` varchar(50) NOT NULL,
  `bs` varchar(50) NOT NULL,
  `bonus` varchar(50) NOT NULL,
  `pf` varchar(50) NOT NULL,
  `hra` varchar(50) NOT NULL,
  `lic` varchar(50) NOT NULL,
  `noofdays` varchar(50) NOT NULL,
  `total` varchar(50) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `salary`
--

INSERT INTO `salary` (`sid`, `email`, `sdat`, `ename`, `bs`, `bonus`, `pf`, `hra`, `lic`, `noofdays`, `total`) VALUES
(1, 'risibindhu@gmail.com', '2024-05-20', 'sakshi', '4000', '46', '647', '45', '54', '13', '3300'),
(2, 'rindhiyamanickam23@gmail.com', '2024-05-07', 'rindhi', '10000', '2500', '200', '65', '35', '23', '12200');
