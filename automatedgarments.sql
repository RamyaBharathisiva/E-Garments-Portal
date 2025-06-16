-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 16, 2025 at 04:34 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `automatedgarments`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(100) NOT NULL,
  `employeeid` int(5) DEFAULT NULL,
  `employeename` varchar(20) DEFAULT NULL,
  `dept` varchar(15) DEFAULT NULL,
  `emailid` varchar(30) DEFAULT NULL,
  `gender` varchar(7) DEFAULT NULL,
  `phno` bigint(10) NOT NULL,
  `dob` date DEFAULT NULL,
  `photo` varchar(20) DEFAULT NULL,
  `idproof` varchar(20) DEFAULT NULL,
  `qualification` varchar(10) DEFAULT NULL,
  `experience` varchar(10) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  `reg_date` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `employeeid`, `employeename`, `dept`, `emailid`, `gender`, `phno`, `dob`, `photo`, `idproof`, `qualification`, `experience`, `password`, `reg_date`) VALUES
(1, 455, 'ramya', 'delivery dept', '455', 'female', 908778909, '2024-03-01', 'download.jpg', 'download.jpg', 'bsc', '0', '', '2024-03-05 05:53:52.232198'),
(2, 103, 'ramya', 'service dept', '103', 'female', 9876543456, '2024-03-07', 'circle.png', 'k1.jpg', 'bsc', 'bsc', 'doe000S2', '2024-03-05 05:54:05.665334');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(100) NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `quality` varchar(20) DEFAULT NULL,
  `fit` varchar(20) DEFAULT NULL,
  `deliveryissues` varchar(10) DEFAULT NULL,
  `comments` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `username`, `email`, `quality`, `fit`, `deliveryissues`, `comments`) VALUES
(1, 'RamyaBharathi S', 'ramyabharathi.242002@gmail.com', 'very-satisfied', 'excellent', 'yes', 'sdfghjkl'),
(2, 'RamyaBharathi S', 'ramyabharathi.242002@gmail.com', 'very-satisfied', 'excellent', 'yes', 'dfghjkl');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(200) NOT NULL,
  `productid` int(10) DEFAULT NULL,
  `productname` varchar(20) DEFAULT NULL,
  `category` varchar(30) NOT NULL,
  `quantity` int(100) DEFAULT NULL,
  `size` varchar(10) DEFAULT NULL,
  `price` int(5) DEFAULT NULL,
  `totalprice` int(7) NOT NULL,
  `card` varchar(20) DEFAULT NULL,
  `cardno` varchar(30) DEFAULT NULL,
  `expirydate` date DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `userid` varchar(50) NOT NULL,
  `ordertime` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `action` varchar(20) NOT NULL,
  `received` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `productid`, `productname`, `category`, `quantity`, `size`, `price`, `totalprice`, `card`, `cardno`, `expirydate`, `status`, `userid`, `ordertime`, `action`, `received`) VALUES
(1, 0, 'None', '', 0, 'None', 0, 0, 'credit or debit card', '23456', '2024-03-29', 'Confirm', '', '2024-03-13 06:54:15.469791', 'Product Delivered', ''),
(2, 0, '103', '', 0, 'm', 800, 0, 'credit or debit card', '3456789', '2024-03-29', 'Cancel', '', '2024-03-13 04:59:07.529946', '', ''),
(3, 0, '109', '', 0, 'm', 600, 0, 'credit or debit card', '234567', '2024-03-29', '', '', '2024-03-13 05:02:12.645169', '', ''),
(4, 0, '103', 'Women', 2, 'None', 0, 0, 'credit or debit card', '2147483647', '2025-02-01', '', '', '2024-03-13 05:02:21.786572', '', ''),
(5, 0, '109', 'men', 3, 'l', 600, 0, 'credit or debit card', '34567890', '2024-03-20', 'Confirm', '', '2024-03-13 06:03:01.600254', '', ''),
(6, 0, '113', 'kids', 0, 'None', 900, 0, 'credit or debit card', '1234567', '2024-03-27', '', '', '2024-03-13 04:59:37.037918', '', ''),
(7, 0, '104', 'Women', 0, 'None', 450, 0, 'credit or debit card', '23456789', '2024-03-13', '', '', '2024-03-13 05:02:49.606695', '', ''),
(8, 103, 'Women', '700', 0, 'None', 0, 0, 'credit or debit card', '234567890', '2024-03-21', '', '', '2024-03-13 04:59:48.290334', '', ''),
(9, 103, 'Women', '700', 0, 'None', 0, 0, 'credit or debit card', '234567890', '2024-03-21', '', '', '2024-03-13 04:59:57.902597', '', ''),
(10, 0, '103', 'Women', 2, 'm', 0, 0, 'credit or debit card', '2147483647', '2024-03-14', '', '', '2024-03-13 04:06:47.640375', '', ''),
(11, 0, '103', 'women kurt', 2, 'None', 1600, 0, 'credit or debit card', '2147483647', '2024-03-15', 'Cancel', '', '2024-03-13 05:00:08.155528', '', ''),
(12, 0, '103', 'women kurt', 0, 'None', 1600, 0, 'credit or debit card', '2147483647', '2024-03-15', 'Confirm', '', '2024-03-13 06:08:45.940507', '', ''),
(13, 0, '103', 'women kurt', 2, 'None', 1600, 0, 'credit or debit card', '2147483647', '2024-03-15', '', '18', '2024-03-13 11:29:54.072280', '', ''),
(14, 0, '123', 'men', 3, 'l', 2400, 0, 'credit or debit card', '2147483647', '2024-03-14', 'Confirm', '18', '2024-03-13 11:37:42.632017', 'Product Delivered', ''),
(25, 0, '103', 'women kurt', 3, 'l', 2400, 0, 'credit or debit card', '7445689', '2024-03-09', 'Received', '17', '2024-03-14 17:20:02.037969', 'Product Delivered', ''),
(26, 0, '103', 'women kurt', 3, 'l', 2400, 0, 'credit or debit card', '3456782', '2024-03-16', '', '', '2024-03-13 09:59:10.473008', '', ''),
(27, 0, '103', 'women kurt', 1, 'm', 800, 0, 'credit or debit card', '87654567', '2024-03-16', '', '', '2024-03-13 10:00:37.278544', '', ''),
(28, 0, '103', 'women kurt', 2, 'l', 1600, 0, 'credit or debit card', '456784321', '2024-03-15', '', 'None', '2024-03-13 10:07:45.896707', '', ''),
(29, 0, '103', 'women kurt', 2, 'm', 1600, 0, 'credit or debit card', '354678902', '2024-03-15', 'Confirm', '17', '2024-03-14 17:23:06.545973', 'Product Delivered', 'Product Received'),
(30, 0, '122', 'women bott', 3, 'None', 4800, 0, 'credit or debit card', '456789', '2024-03-30', '', 'None', '2024-03-14 10:30:58.577594', '', ''),
(31, 0, '107', 'women part', 3, 'xl', 4500, 0, 'credit or debit card', '234567897', '2024-03-30', '', '', '2024-03-14 10:41:30.242783', '', ''),
(32, 0, '107', 'women part', 3, 'xl', 4500, 0, 'credit or debit card', '234567897', '2024-03-30', '', 'None', '2024-03-14 10:44:27.629895', '', ''),
(33, 0, '122', 'women bott', 2, 'xl', 3200, 0, 'credit or debit card', '2147483647', '2024-03-29', '', '17', '2024-03-14 10:47:53.103241', '', ''),
(34, 0, '107', 'women part', 2, 'xxl', 3000, 0, 'credit or debit card', '3456789', '2024-03-30', '', '17', '2024-03-14 10:48:28.421750', '', ''),
(35, 122, 'kurta', 'women bott', 3, 'xl', 4800, 0, 'credit or debit card', '456789', '2024-03-29', '', '18', '2024-03-14 10:55:36.931952', '', ''),
(36, 122, 'kurta', 'women bott', 3, 'l', 1600, 4800, 'credit or debit card', '6789', '2024-03-23', '', '18', '2024-03-14 10:58:13.761668', '', ''),
(37, 122, 'kurta', 'women bott', 2, 'xl', 1600, 3200, 'credit or debit card', '456789', '2024-03-30', '', '18', '2024-03-14 10:58:56.109849', '', ''),
(38, 122, 'kurta', 'women bott', 3, 'xxl', 1600, 4800, 'credit or debit card', '2345667', '2024-03-22', '', '17', '2024-03-14 11:00:24.007714', '', ''),
(39, 122, 'kurta', 'women bott', 3, 'xl', 1600, 4800, 'credit or debit card', '56789', '2024-03-29', '', '18', '2024-03-14 11:01:49.320784', '', ''),
(40, 0, '103', 'women kurt', 3, 'xl', 800, 2400, 'credit or debit card', '3456789', '2024-04-01', '', '18', '2024-03-14 11:06:45.795812', '', ''),
(41, 0, '107', 'women part', 3, 'xl', 4500, 0, 'credit or debit card', '3456789', '2024-03-29', '', 'None', '2024-03-14 11:07:56.396963', '', ''),
(42, 0, '103', 'women kurt', 4, 'xxl', 800, 3200, 'credit or debit card', '3456789', '2024-03-27', '', '18', '2024-03-14 11:10:06.492404', '', ''),
(43, 126, 'shirt', 'women spor', 4, 'None', 400, 1600, 'credit or debit card', '345678', '2024-03-22', '', '18', '2024-03-14 11:15:03.788464', '', ''),
(44, 126, 'shirt', 'women spor', 4, 'None', 400, 1600, 'credit or debit card', '345678', '2024-03-22', '', '18', '2024-03-14 11:23:30.473841', '', ''),
(45, 126, 'shirt', 'women spor', 4, 'None', 400, 1600, 'credit or debit card', '345678', '2024-03-22', '', '18', '2024-03-14 11:25:59.824745', '', ''),
(46, 104, 'tops', 'women wint', 1, 'xxl', 800, 800, 'credit or debit card', '34567890', '2024-03-28', '', '17', '2024-03-14 11:27:28.765389', '', ''),
(47, 134, 'men topwear', 'men topwea', 2, 'xl', 800, 1600, 'credit or debit card', '23456789', '2024-03-23', '', '17', '2024-03-14 11:29:03.494541', '', ''),
(48, 109, 'Shirt', 'men bottom', 3, 'xl', 800, 2400, 'credit or debit card', '23456789', '2024-03-30', '', 'None', '2024-03-14 11:32:14.865731', '', ''),
(49, 109, 'shirt', 'men sports', 3, 'xxl', 600, 1800, 'credit or debit card', '234567', '2024-03-28', '', '18', '2024-03-14 11:34:58.808464', '', ''),
(50, 123, 'shirt', 'men winter', 3, 'xl', 800, 2400, 'credit or debit card', '34567890', '2024-03-21', '', '17', '2024-03-14 11:37:21.295228', '', ''),
(51, 113, 'Lipsy', 'boys cloth', 3, 'xl', 900, 2700, 'credit or debit card', '23456789', '2024-04-06', '', '17', '2024-03-14 11:39:54.254220', '', ''),
(52, 121, 'suit', 'girls clothing', 2, 'xxl', 1000, 2000, 'credit or debit card', '34567890', '2024-03-27', '', '17', '2024-03-14 11:41:56.053060', '', ''),
(53, 115, 'suit', 'baby boy', 3, 'xl', 2500, 7500, 'credit or debit card', '34567890', '2024-03-23', '', '17', '2024-03-14 11:47:36.426996', '', ''),
(54, 115, 'suit', 'baby girl', 3, 'xl', 2500, 7500, 'credit or debit card', '2147483647', '2024-03-13', '', '17', '2024-03-14 11:52:20.193036', '', ''),
(55, 103, 'tops', 'women kurta', 3, 'xxl', 800, 2400, 'credit or debit card', '3456789', '2024-03-21', 'Confirm', '17', '2024-03-17 02:56:59.356687', 'Product Delivered', ''),
(56, 0, '134', 'men topwear', 2, 'xxl', 1600, 0, 'credit or debit card', '456789964', '2024-03-30', '', '', '2024-03-14 17:36:28.147878', '', ''),
(57, 122, 'kurta', 'women bottom wear', 3, 'xl', 1600, 4800, 'credit or debit card', '2147483647', '2024-04-02', '', 'None', '2024-03-14 17:37:02.501116', '', ''),
(58, 122, 'kurta', 'women bottom wear', 2, 'l', 1600, 3200, 'credit or debit card', '4567890', '2024-03-27', 'Confirm', '19', '2024-03-14 17:45:21.535095', 'Product Delivered', 'Product Received'),
(59, 111, 'asdd', 'ssd', 6, 'x', 234, 345, 'dxx', '3345', '1000-05-24', 'Cancel', '17', '2024-03-16 15:55:09.614729', '', ''),
(60, 103, 'tops', 'women kurta', 3, 'xl', 800, 2400, 'credit or debit card', '23456789', '2024-03-23', 'Confirm', '20', '2024-03-15 07:05:14.614105', 'Product Delivered', 'Product Received'),
(61, 103, 'tops', 'women kurta', 3, 'l', 800, 2400, 'credit or debit card', '2147483647', '2024-03-30', '', 'None', '2024-03-16 13:48:31.263553', '', ''),
(62, 103, 'tops', 'women kurta', 2, 'xl', 800, 1600, 'credit or debit card', '23456', '2024-03-21', '', 'None', '2024-03-16 13:58:39.171104', '', ''),
(63, 17, 'kurta', 'kurta', 2, 'l', 100, 200, 'credit or debit card', '2345678902345678', '2024-03-01', '', '17', '2024-03-17 07:23:18.008188', '', ''),
(64, 17, 'kurta', 'kurta', 2, 'l', 100, 200, 'credit or debit card', '2345678902345678', '2024-03-09', '', '17', '2024-03-17 07:36:51.452145', '', ''),
(65, 17, 'kurta', 'kurta', 2, 'l', 100, 200, 'credit or debit card', '2345678902345678', '2024-03-01', '', '17', '2024-03-17 07:50:57.618549', '', ''),
(66, 18, 'kurta', 'kurta', 2, 'xl', 700, 1400, 'credit or debit card', '2345678902345678', '2024-03-01', '', '19', '2024-03-17 07:52:28.765406', '', ''),
(67, 20, 'kurta', 'kurta', 1, 'l', 1000, 1000, 'credit or debit card', '2345678902345678', '2024-03-09', '', '20', '2024-03-17 08:04:00.426548', '', ''),
(68, 20, 'kurta', 'kurta', 1, 'l', 1000, 1000, 'credit or debit card', '2345678902345678', '2024-03-15', 'Confirm', '20', '2024-03-17 08:09:46.515371', 'Product Delivered', 'Product Received');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(200) NOT NULL,
  `productid` int(5) DEFAULT NULL,
  `productname` varchar(20) DEFAULT NULL,
  `productimage` varchar(10) DEFAULT NULL,
  `description` varchar(200) NOT NULL,
  `quantity` int(3) DEFAULT NULL,
  `size` varchar(5) DEFAULT NULL,
  `category` varchar(30) DEFAULT NULL,
  `userprice` int(8) DEFAULT NULL,
  `wholesalerprice` int(8) NOT NULL,
  `useroffer` int(8) NOT NULL,
  `wholesaleroffer` int(6) NOT NULL,
  `status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `productid`, `productname`, `productimage`, `description`, `quantity`, `size`, `category`, `userprice`, `wholesalerprice`, `useroffer`, `wholesaleroffer`, `status`) VALUES
(5, 103, 'tops', 'women1.jpg', 'Women Cotton Blend Kurta ', 96, 'm', 'women kurta', 800, 700, 500, 0, 'Approved'),
(6, 104, 'tops', 'w7.jpg', 'Womens Floral Print Rayon A-line Kurta', 50, 'xl', 'women winter', 800, 750, 450, 0, 'Approved'),
(7, 107, 'tops', 'w5.jpg', 'Womens Printed kurta', 96, 'l', 'women party dress', 1500, 1400, 900, 0, 'Approved'),
(8, 109, 'shirt', 'm3.jpg', 'Cotton Dobby shirt', 52, 'xl', 'men sports', 600, 550, 0, 0, 'Approved'),
(9, 109, 'Shirt', 'm2.jpg', 'Men Checkered Stylish Casual Shirts', 23, 'l', 'men bottomwear', 800, 710, 0, 0, 'Approved'),
(10, 110, 'Bullmer', 'm4.jpg', 'Athleisure Activewear Sportswear Track Pants ', 36, 'l', 'men', 1500, 1450, 0, 0, 'Discard'),
(12, 113, 'Lipsy', 'k2.jpg', 'White Cut Out Floral Scuba Dress', 40, 's', 'boys clothing', 900, 820, 700, 500, 'Approved'),
(13, 115, 'suit', 'images.jpg', 'Cotton Checks Printed Shawl Lapel Suit ', 41, 's', 'baby girl', 2500, 2350, 0, 0, 'Approved'),
(14, 120, 'kurta', 'w7.jpg', 'women cotton kurta', 56, 'xl', 'Women', 1000, 910, 0, 0, 'Discard'),
(15, 121, 'suit', 'images.jpg', 'Cotton Checks Printed Shawl Lapel Suit', 10, 'l', 'girls clothing', 1000, 910, 0, 0, 'Approved'),
(16, 122, 'kurta', 'w6.jpg', 'Women Printed, Embroidered Viscose Rayon Flared Kurta', 85, 's', 'women bottom wear', 1600, 1500, 0, 0, 'Approved'),
(17, 123, 'shirt', 'm1.jpg', 'Men Regular Fit Checkered Spread Collar Casual Shirt', 67, 'm', 'men winter', 800, 720, 0, 0, 'Approved'),
(18, 126, 'shirt', 'm3.jpg', 'cotton shirt', 96, 'm', 'women sports', 400, 300, 0, 0, 'Approved'),
(20, 134, 'Kurta and Kurti', 'kurta9.jpe', 'wertysdrfgh', 82, 'm', 'women kurta', 700, 640, 0, 0, ''),
(21, 137, 'Kurta and Kurti', 'kurta10.jp', 'sdfghbnj', 82, 'l', 'women kurta', 500, 450, 0, 0, ''),
(22, 134, 'men topwear', 'm3.jpg', 'cotton shirt', 85, 'm', 'men topwear', 800, 700, 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(100) NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `gender` varchar(7) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  `phno` bigint(10) DEFAULT NULL,
  `door` varchar(100) DEFAULT NULL,
  `street` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `reg_date` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `gender`, `email`, `dob`, `password`, `phno`, `door`, `street`, `city`, `district`, `state`, `pincode`, `reg_date`, `status`) VALUES
(17, 'siva', 'female', 'ramyabharathi.242002@gmail.com', '2024-03-02', 'asdf', 9876548123, '23', 'asasf', 'erode', 'erode', 'tamilnadu', '123456', '2024-03-05 05:11:31.880636', 'Approved'),
(18, 'siva', 'male', 'ramyabharathi.242002@gmail.com', '2024-03-07', 'fghj', 9876548123, '23', 'asasf', 'erode', 'erode', 'tamilnadu', '123456', '2024-03-13 07:38:41.848722', 'Approved'),
(19, 'nandhini', 'female', 'nandhinidevi.0610@gmail.com', '2024-03-05', 'qwer', 9876543456, '23', 'sg street', 'erode', 'erode', 'tamilnadu', '638004', '2024-03-14 17:35:18.705702', 'Approved'),
(20, 'sutha', 'female', 'murugasutha18@gmail.com', '2024-03-07', 'poiu', 9876543456, '27', 'sg street', 'erode', 'erode', 'tamilnadu', '638004', '2024-03-17 06:07:54.457231', 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `userdesign`
--

CREATE TABLE `userdesign` (
  `id` int(200) NOT NULL,
  `userid` int(5) NOT NULL,
  `designfor` varchar(15) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dresstype` varchar(30) DEFAULT NULL,
  `fabric` varchar(20) DEFAULT NULL,
  `color` varchar(15) DEFAULT NULL,
  `size` varchar(7) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `referenceimage` varchar(20) DEFAULT NULL,
  `quantity` int(5) DEFAULT NULL,
  `additionalrequest` varchar(200) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `price` int(8) NOT NULL,
  `totalprice` int(7) NOT NULL,
  `card` varchar(17) NOT NULL,
  `cardno` int(17) NOT NULL,
  `expirydate` date DEFAULT NULL,
  `ordertime` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `accept` varchar(20) NOT NULL,
  `action` varchar(20) NOT NULL,
  `receive` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userdesign`
--

INSERT INTO `userdesign` (`id`, `userid`, `designfor`, `gender`, `dresstype`, `fabric`, `color`, `size`, `age`, `referenceimage`, `quantity`, `additionalrequest`, `status`, `price`, `totalprice`, `card`, `cardno`, `expirydate`, `ordertime`, `accept`, `action`, `receive`) VALUES
(1, 0, 'women', 'female', 'kurta', 'cotton', 'blue', 'xl', 20, 'w7.jpg', 2, 'None', 'Discard', 0, 0, '', 0, NULL, '2024-03-14 15:50:44.816432', '', '', ''),
(3, 2, 'men', 'male', 'kurta', 'cotton', 'blue', 'xxl', 20, 'm1.jpg', 2, 'None', 'Approved', 500, 1000, '', 0, NULL, '2024-03-17 07:00:28.246911', '', '', ''),
(4, 0, 'men', 'male', 'kurta', 'cotton', 'blue', 'm', 20, 'm3.jpg', 2, 'sdfghjkl', 'Approved', 0, 0, '', 0, NULL, '2024-03-14 15:50:44.816432', '', '', ''),
(5, 17, 'women', 'female', 'kurta', 'cotton', 'blue', 'xl', 20, 'm1.jpg', 2, 'SDFGHJKL', '', 200, 400, '', 0, NULL, '2024-03-17 06:59:43.282630', '', '', ''),
(6, 17, 'men', 'male', 'kurta', 'cotton', 'blue', 'xl', 20, 'm1.jpg', 2, 'sdfghjkl', '', 0, 0, '', 0, NULL, '2024-03-14 15:50:44.816432', '', '', ''),
(17, 17, 'women', 'female', 'kurta', 'cotton', 'blue', 'l', 20, 'kurta9.jpeg', 2, 'None', 'Approved', 100, 200, '', 0, NULL, '2024-03-15 05:34:51.366524', 'confirm Order', 'Product Delivered', 'Product Re'),
(18, 19, 'women', 'female', 'kurta', 'cotton', 'blue', 'xl', 20, 'women1.jpg', 2, 'i want a perfect fit', 'Approved', 700, 1400, '', 0, NULL, '2024-03-17 07:52:28.755824', 'None', '', ''),
(19, 17, 'women', 'female', 'kurta', 'cotton', 'blue', 'l', 20, 'kurta9.jpeg', 2, 'None', 'Approved', 100, 200, '', 0, NULL, '2024-03-15 05:34:51.366524', 'confirm Order', 'Product Delivered', ''),
(20, 20, 'women', 'female', 'kurta', 'cotton', 'blue', 'l', 20, 'kurta10.jpeg', 1, 'perfect fit', 'Approved', 1000, 1000, '', 0, NULL, '2024-03-17 08:05:47.681845', 'Place Order', '', ''),
(21, 20, 'men', 'male', 'kurta', 'cotton', 'blue', 'l', 20, 'm3.jpg', 1, 'asdfghjk', 'Discard', 0, 0, '', 0, NULL, '2024-03-17 08:15:48.555697', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `wholedesign`
--

CREATE TABLE `wholedesign` (
  `userid` int(4) DEFAULT NULL,
  `designfor` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dresstype` varchar(20) DEFAULT NULL,
  `fabric` varchar(20) DEFAULT NULL,
  `color` varchar(10) DEFAULT NULL,
  `size` varchar(5) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `referenceimage` varchar(20) DEFAULT NULL,
  `quantity` int(5) DEFAULT NULL,
  `additionalrequest` varchar(200) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `price` int(5) DEFAULT NULL,
  `totalprice` int(8) DEFAULT NULL,
  `card` varchar(30) DEFAULT NULL,
  `cardno` int(17) DEFAULT NULL,
  `expirydate` date DEFAULT NULL,
  `ordertime` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `accept` varchar(20) NOT NULL,
  `action` varchar(20) NOT NULL,
  `receive` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `wholeorders`
--

CREATE TABLE `wholeorders` (
  `id` int(200) NOT NULL,
  `productid` int(10) DEFAULT NULL,
  `productname` varchar(20) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `quantity` int(5) DEFAULT NULL,
  `size` varchar(5) DEFAULT NULL,
  `price` int(5) DEFAULT NULL,
  `totalprice` int(10) DEFAULT NULL,
  `card` varchar(30) DEFAULT NULL,
  `cardno` int(18) DEFAULT NULL,
  `expirydate` date DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  `userid` int(5) DEFAULT NULL,
  `ordertime` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `action` varchar(20) DEFAULT NULL,
  `receive` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wholeorders`
--

INSERT INTO `wholeorders` (`id`, `productid`, `productname`, `category`, `quantity`, `size`, `price`, `totalprice`, `card`, `cardno`, `expirydate`, `status`, `userid`, `ordertime`, `action`, `receive`) VALUES
(1, 0, '103', 'women kurta', 12, 'None', 800, 9600, 'credit or debit card', 2147483647, '2024-03-22', NULL, NULL, '2024-03-13 07:20:21.546402', NULL, ''),
(2, 0, '103', 'women kurta', 12, 'None', 800, 9600, 'credit or debit card', 2147483647, '2024-03-22', NULL, NULL, '2024-03-13 07:24:51.283141', NULL, ''),
(3, 0, '134', 'men topwear', 24, 'l', 19200, NULL, 'credit or debit card', 34567890, '2024-03-21', NULL, NULL, '2024-03-13 07:27:45.458212', NULL, ''),
(4, 0, '134', 'men topwear', 24, 'l', 19200, NULL, 'credit or debit card', 34567890, '2024-03-21', NULL, NULL, '2024-03-13 07:27:49.001728', NULL, ''),
(5, 0, '103', 'women kurta', 12, 'm', 800, 9600, 'credit or debit card', 2147483647, '2024-03-29', 'Confirm', 33, '2024-03-17 02:53:50.199424', 'Product Delivered', ''),
(6, 103, 'tops', 'women kurta', 24, 'l', 800, 19200, 'credit or debit card', 234567, '2024-03-22', 'Confirm', 33, '2024-03-17 02:56:26.865729', 'Product Delivered', ''),
(7, 103, 'tops', 'women kurta', 24, 'l', 800, 19200, 'credit or debit card', 234567, '2024-03-22', 'Cancel', 33, '2024-03-16 16:03:31.457881', NULL, ''),
(8, 103, 'tops', 'women kurta', 24, 'm', 800, 19200, 'credit or debit card', 2147483647, '2024-03-21', 'Confirm', 33, '2024-03-17 02:56:21.145535', 'Product Delivered', '');

-- --------------------------------------------------------

--
-- Table structure for table `wholesaler`
--

CREATE TABLE `wholesaler` (
  `id` int(100) NOT NULL,
  `ownername` varchar(15) DEFAULT NULL,
  `gender` varchar(7) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `phno` bigint(10) DEFAULT NULL,
  `photo` varchar(25) DEFAULT NULL,
  `shopname` varchar(15) DEFAULT NULL,
  `shoplicence` varchar(20) DEFAULT NULL,
  `shopimage` varchar(20) DEFAULT NULL,
  `aadhaarcard` varchar(20) DEFAULT NULL,
  `door` int(5) DEFAULT NULL,
  `street` varchar(20) NOT NULL,
  `city` varchar(10) NOT NULL,
  `district` varchar(10) NOT NULL,
  `state` varchar(10) NOT NULL,
  `pincode` int(6) NOT NULL,
  `reg_time` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `status` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wholesaler`
--

INSERT INTO `wholesaler` (`id`, `ownername`, `gender`, `email`, `dob`, `phno`, `photo`, `shopname`, `shoplicence`, `shopimage`, `aadhaarcard`, `door`, `street`, `city`, `district`, `state`, `pincode`, `reg_time`, `status`, `password`) VALUES
(1, 'Ramya', 'Female', 'ramyabharathi.242002@gmail.com', '2024-03-07', 99765455676678, 'women2.jpg', 'ramya silks', 'women2.jpg', 'women2.jpg', 'women2.jpg', 23, '123,street,erode', 'erode', 'erode', 'tamilnadu', 638004, '2024-03-13 10:50:48.828161', 'Approved', ''),
(2, 'Ramya', 'Female', 'ramyabharathi.2002@gmail.com', '2024-03-01', 9976545678, 'women2.jpg', 'ramya silks', 'women2.jpg', 'women2.jpg', 'women2.jpg', 23, '123,street,erode', 'erode', 'erode', 'tamilnadu', 638004, '2024-03-05 11:38:11.632675', 'Approved', ''),
(33, 'sutha', 'Female', 'murugasutha18@gmail.com', '2024-03-16', 9976545678, 'w7.jpg', 'ramya silks', 'w7.jpg', 'w7.jpg', 'women1.jpg', 23, '123,street,erode', 'erode', 'erode', 'tamilnadu', 638004, '2024-03-15 07:16:26.708807', 'Approved', 'style00S35'),
(34, 'sutha', 'Female', 'murugasutha18@gmail.com', '2024-03-27', 9876543456, 'women2.jpg', 'sutha silks', 'women2.jpg', 'women2.jpg', 'women2.jpg', 30, 'sg street', 'erode', 'erode', 'tamilnadu', 638004, '2024-03-17 05:50:42.035979', 'Approved', 'style00S35'),
(35, 'sutha', 'Female', 'murugasutha18@gmail.com', '2024-03-09', 9876, 'm2.jpg', 'sutha silks', 'k3.jpg', 'm1.jpg', 'm5.jpg', 23, 'sg street', 'erode', 'erode', 'tamilnadu', 638004, '2024-03-17 03:25:14.065399', '', ''),
(36, 'Ramya', 'Female', 'ramyabharathi.242002@gmail.com', '2024-03-01', 3456789876, 'm1.jpg', 'sdfg', 'kurta10.jpeg', 'm1.jpg', 'kurta10.jpeg', 12, '123,street,erode', 'erode', 'sdd', 'tamilnadu', 6380, '2024-03-17 03:29:47.667423', '', ''),
(37, 'Ramya', 'Female', 'ramyabharathi.242002@gmail.com', '2024-03-02', 0, 'women2.jpg', 'sdf', 'women2.jpg', 'women2.jpg', 'women2.jpg', 25, 'asdf', 'sdfgh', 'sdf', 'bcvb', 234567, '2024-03-17 05:46:19.054468', '', ''),
(38, 'Kala', 'Female', 'ramyabharathi.200224@gmail.com', '1999-07-09', 1234567890, 'kurta7.jpeg', 'Kala Silks', 'w4.jpg', 'kurta5.jpeg', 'kurta5.jpeg', 23, '123,street,erode', 'erode', 'erode', 'tamilnadu', 638004, '2025-03-19 06:56:48.242185', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userdesign`
--
ALTER TABLE `userdesign`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wholeorders`
--
ALTER TABLE `wholeorders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wholesaler`
--
ALTER TABLE `wholesaler`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `userdesign`
--
ALTER TABLE `userdesign`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `wholeorders`
--
ALTER TABLE `wholeorders`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `wholesaler`
--
ALTER TABLE `wholesaler`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
