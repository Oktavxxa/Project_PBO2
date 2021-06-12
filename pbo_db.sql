-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 12, 2021 at 04:43 PM
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
  `id` int(11) NOT NULL,
  `hari` varchar(10) NOT NULL,
  `matkul` varchar(25) NOT NULL,
  `kelas` varchar(5) NOT NULL,
  `jamMulai` varchar(6) NOT NULL,
  `jamSelesai` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jadwal`
--

INSERT INTO `jadwal` (`id`, `hari`, `matkul`, `kelas`, `jamMulai`, `jamSelesai`) VALUES
(1, 'a', 'aa', 'aaa', '00:00:', '00:00:'),
(2, 'q', 'qqq', 'qqqq', '00:00:', '00:00:'),
(3, '', '', '', '00:00:', '00:00:'),
(4, '', '', '', '07:00:', '08:40:'),
(5, 'a', 'aaaaa', 'aa', '07:00:', '08:00:'),
(6, 'Jumat', 'RPB', 'A', '10:00:', '12:20:'),
(7, 'Rabu', 'RPB PR', 'D', '08:40:', '10:00:'),
(8, 'Selasa', 'RPB', 'A', '19.00', '20.30'),
(9, 'Selasa', 'TKTI', 'A', '09.00', '09.30');

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
(2, '', '', ''),
(5, 'RPB', 'Jumat, 20 Oktober 2021, jam 07', 'Tugas Individu'),
(6, 'Matdis', '10 Januari 2021 jam 9 malem', 'Tugas Kelompok, Semangat'),
(7, 'MKWU', '9 Januari 2021, 19.00', 'Semangat tugas akhir'),
(8, 'A', 'B', 'C'),
(9, 'PBO', 'Besok ', 'Yukkk'),
(10, 'A', 'B', 'V'),
(11, 'a', 'a', 'a'),
(12, 'A', 'C', 'D'),
(13, 'Statistika', 'Selasa, 20 Januari 2021', 'Tugas individu '),
(14, 'Statistika', 'Jumat', 'Semangat');

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
-- Indexes for table `jadwal`
--
ALTER TABLE `jadwal`
  ADD PRIMARY KEY (`id`);

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
-- AUTO_INCREMENT for table `jadwal`
--
ALTER TABLE `jadwal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tugas`
--
ALTER TABLE `tugas`
  MODIFY `idTugas` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
