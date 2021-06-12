-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2021 at 03:25 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `jadwal`
--

CREATE TABLE `jadwal` (
  `idJadwal` int(3) NOT NULL,
  `Hari` date NOT NULL,
  `Matkul` varchar(50) NOT NULL,
  `Kelas` varchar(2) NOT NULL,
  `jamMulai` time NOT NULL,
  `jamSelesai` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jadwal`
--

INSERT INTO `jadwal` (`idJadwal`, `Hari`, `Matkul`, `Kelas`, `jamMulai`, `jamSelesai`) VALUES
(0, '0000-00-00', 'MKWU', 'E', '00:00:12', '00:00:13'),
(0, '0000-00-00', 'MKWU', 'E', '00:00:09', '00:00:10'),
(0, '0000-00-00', 'PBO', 'C', '00:00:09', '00:00:10'),
(0, '0000-00-00', 'RPB', 'A', '00:00:09', '00:00:10'),
(0, '0000-00-00', 'MKWU', 'A', '00:00:09', '00:00:10');

-- --------------------------------------------------------

--
-- Table structure for table `tugas`
--

CREATE TABLE `tugas` (
  `idTugas` int(5) NOT NULL,
  `matkul` varchar(25) NOT NULL,
  `deadline` varchar(30) NOT NULL,
  `ket` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tugas`
--

INSERT INTO `tugas` (`idTugas`, `matkul`, `deadline`, `ket`) VALUES
(2, 'MKWU', 'Senin, 12 Januari, jam 8', 'Tugas Individu'),
(3, 'RPB', 'Sabtu, 20 Agustus 2020', 'Tugas Individu'),
(4, 'MKWU', 'Selasa', 'Tugas Akhir'),
(5, 'RPB', 'Jumat, 20 Oktober 2021, jam 07', 'Tugas Individu');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `Nama` varchar(200) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `Nama`, `Username`, `Password`) VALUES
(4, 'Icha', 'icha123', '123'),
(5, 'Vivi', 'vivi456', '456'),
(11, 'Dito', 'dito12', 'dit123'),
(12, 'ahmad', 'a456', '456'),
(13, 'awan', 'a1', '11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tugas`
--
ALTER TABLE `tugas`
  ADD PRIMARY KEY (`idTugas`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tugas`
--
ALTER TABLE `tugas`
  MODIFY `idTugas` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
