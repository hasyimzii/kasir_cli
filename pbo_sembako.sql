-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 01, 2021 at 09:58 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo_sembako`
--

-- --------------------------------------------------------

--
-- Table structure for table `order_transaksi`
--

CREATE TABLE `order_transaksi` (
  `idOrder` int(11) NOT NULL,
  `idTransaksi` int(11) NOT NULL,
  `idSembako` int(11) NOT NULL,
  `jumlahSembako` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `order_transaksi`
--

INSERT INTO `order_transaksi` (`idOrder`, `idTransaksi`, `idSembako`, `jumlahSembako`) VALUES
(4, 6, 1, 6),
(11, 17, 1, 5),
(12, 17, 3, 7),
(14, 19, 1, 5),
(15, 19, 3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `sembako`
--

CREATE TABLE `sembako` (
  `idSembako` int(11) NOT NULL,
  `jenis` varchar(20) NOT NULL,
  `merk` varchar(20) NOT NULL,
  `harga` int(7) NOT NULL,
  `stok` int(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sembako`
--

INSERT INTO `sembako` (`idSembako`, `jenis`, `merk`, `harga`, `stok`) VALUES
(1, 'beras', 'ambon', 11000, 10),
(3, 'minyak', 'bimoli', 7000, 2);

-- --------------------------------------------------------

--
-- Table structure for table `toko`
--

CREATE TABLE `toko` (
  `idToko` int(11) NOT NULL,
  `alamat` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `toko`
--

INSERT INTO `toko` (`idToko`, `alamat`) VALUES
(1, 'jalan mangga 5, kota mojokerto');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `idTransaksi` int(11) NOT NULL,
  `tanggal` datetime NOT NULL,
  `idUser` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`idTransaksi`, `tanggal`, `idUser`) VALUES
(6, '2021-01-02 02:11:51', 8),
(17, '2021-01-02 03:52:21', 8),
(19, '2021-01-02 03:54:37', 8),
(20, '2021-01-02 03:55:17', 8);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `idUser` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `jabatan` enum('manager','petugas kasir') NOT NULL,
  `idToko` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`idUser`, `username`, `password`, `jabatan`, `idToko`) VALUES
(7, 'manager', '123123', 'manager', 1),
(8, 'kasir', '123123', 'petugas kasir', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `order_transaksi`
--
ALTER TABLE `order_transaksi`
  ADD PRIMARY KEY (`idOrder`),
  ADD KEY `order-sembako` (`idSembako`),
  ADD KEY `order-transaksi` (`idTransaksi`);

--
-- Indexes for table `sembako`
--
ALTER TABLE `sembako`
  ADD PRIMARY KEY (`idSembako`);

--
-- Indexes for table `toko`
--
ALTER TABLE `toko`
  ADD PRIMARY KEY (`idToko`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`idTransaksi`),
  ADD KEY `transaksi-user` (`idUser`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`idUser`),
  ADD KEY `user-toko` (`idToko`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `order_transaksi`
--
ALTER TABLE `order_transaksi`
  MODIFY `idOrder` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `sembako`
--
ALTER TABLE `sembako`
  MODIFY `idSembako` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `toko`
--
ALTER TABLE `toko`
  MODIFY `idToko` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `idTransaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `order_transaksi`
--
ALTER TABLE `order_transaksi`
  ADD CONSTRAINT `order-sembako` FOREIGN KEY (`idSembako`) REFERENCES `sembako` (`idSembako`),
  ADD CONSTRAINT `order-transaksi` FOREIGN KEY (`idTransaksi`) REFERENCES `transaksi` (`idTransaksi`);

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi-user` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user-toko` FOREIGN KEY (`idToko`) REFERENCES `toko` (`idToko`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
