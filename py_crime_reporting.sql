-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 26, 2019 at 07:41 PM
-- Server version: 5.7.22-0ubuntu0.17.10.1
-- PHP Version: 7.1.19-1+ubuntu17.10.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `py_trafficrule`
--
CREATE DATABASE IF NOT EXISTS `py_trafficrule` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `py_trafficrule`;

-- --------------------------------------------------------

--
-- Table structure for table `application_complaint`
--

CREATE TABLE `application_complaint` (
  `id` int(11) NOT NULL,
  `complaint_type` varchar(50) NOT NULL,
  `complaint` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `resolved_date` datetime(6) DEFAULT NULL,
  `resolved_message` varchar(500) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_updated` datetime(6) NOT NULL,
  `police_station_id` int(11) NOT NULL,
  `resolved_by_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `application_complaint`
--

INSERT INTO `application_complaint` (`id`, `complaint_type`, `complaint`, `status`, `resolved_date`, `resolved_message`, `date_created`, `date_updated`, `police_station_id`, `resolved_by_id`, `user_id`) VALUES
(1, 'FIR', 'Testing complaing.', 'Resolved', '2019-10-06 13:00:30.221418', 'wqerty', '2019-10-06 11:29:26.538783', '2019-10-06 13:00:30.355282', 1, 4, 1),
(2, 'Information', '234567uiopxcvbnm,.\r\nsdfghjk', 'Reject', '2019-10-06 13:00:48.630581', 'wqerty', '2019-10-06 11:58:23.097027', '2019-10-06 13:00:48.687427', 1, 4, 4),
(3, 'Other', '2ertyjkl./vbnm, fghm,.', 'Resolved', '2019-10-06 13:00:41.762914', 'resolved', '2019-10-06 11:58:36.167571', '2019-10-06 13:00:41.861493', 1, 4, 1),
(4, 'Information', 'completing qertyuio;', 'Pending', NULL, NULL, '2019-10-06 12:24:31.970025', '2019-10-06 12:24:32.051408', 2, NULL, 1),
(5, 'Other', 'qertyui', 'Resolved', '2019-10-06 12:27:49.000000', 'Resolved', '2019-10-06 12:25:51.651683', '2019-10-06 12:27:55.310379', 1, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `application_contact`
--

CREATE TABLE `application_contact` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `message` varchar(500) NOT NULL,
  `status` smallint(5) UNSIGNED NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `application_contact`
--

INSERT INTO `application_contact` (`id`, `name`, `email`, `mobile`, `message`, `status`, `date_created`, `date_updated`) VALUES
(1, 'Kamal Kant', 'kamalkant975@gmail.com', 'a56789p89', 'fghjkl;fghjkl;\'', 1, '2019-09-29 19:52:28.369226', '2019-09-29 19:52:28.369706');

-- --------------------------------------------------------

--
-- Table structure for table `application_policestation`
--

CREATE TABLE `application_policestation` (
  `id` int(11) NOT NULL,
  `station_city` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `no_of_employee` int(11) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_updated` datetime(6) NOT NULL,
  `station_incharge_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `application_policestation`
--

INSERT INTO `application_policestation` (`id`, `station_city`, `address`, `no_of_employee`, `date_created`, `date_updated`, `station_incharge_id`) VALUES
(1, 'Vikashpuri', 'B-13, B - Block Vikashpuri', 5, '2019-10-04 15:45:58.332830', '2019-10-06 04:26:58.464348', 4),
(2, 'Tilak Nagar', 'Tilak Nagar', 7, '2019-10-06 04:27:19.166014', '2019-10-06 04:27:19.166064', 3);

-- --------------------------------------------------------

--
-- Table structure for table `application_profile`
--

CREATE TABLE `application_profile` (
  `id` int(11) NOT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `city` varchar(200) DEFAULT NULL,
  `state` varchar(200) DEFAULT NULL,
  `pin` varchar(10) DEFAULT NULL,
  `country` varchar(200) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `police_station_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `application_profile`
--

INSERT INTO `application_profile` (`id`, `mobile`, `gender`, `dob`, `address`, `city`, `state`, `pin`, `country`, `user_id`, `police_station_id`) VALUES
(1, '8989898989', 'Male', '1989-10-10', 'New Delhi', 'Delhi', 'Delhi', '110018', 'India', 1, NULL),
(2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, NULL),
(3, NULL, 'Male', NULL, NULL, NULL, NULL, NULL, 'India', 3, 2),
(4, NULL, 'Male', NULL, NULL, 'New Delhi', 'Delhi', '110018', 'India', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 10),
(2, 1, 11),
(3, 1, 19),
(4, 1, 20),
(5, 1, 22),
(6, 1, 23),
(7, 1, 24);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add contact', 7, 'add_contact'),
(20, 'Can change contact', 7, 'change_contact'),
(21, 'Can delete contact', 7, 'delete_contact'),
(22, 'Can add profile', 8, 'add_profile'),
(23, 'Can change profile', 8, 'change_profile'),
(24, 'Can delete profile', 8, 'delete_profile'),
(25, 'Can add police station', 9, 'add_policestation'),
(26, 'Can change police station', 9, 'change_policestation'),
(27, 'Can delete police station', 9, 'delete_policestation'),
(28, 'Can add complaint', 10, 'add_complaint'),
(29, 'Can change complaint', 10, 'change_complaint'),
(30, 'Can delete complaint', 10, 'delete_complaint');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$hXMHiBSJ7Rc9$1zhiSk7qICEHAK6y7ivMgDlQcbInfZirXDx/51b4Eyg=', '2019-10-06 12:40:28.579573', 0, 'pawan', 'Pawan', 'Kumar', 'pk1@gmail.com', 0, 1, '2019-10-04 13:40:00.000000'),
(2, 'pbkdf2_sha256$100000$58k8NYb3T2bz$qP1YURqHJPtzBM1iv/xREuBpUJ/lKt+0kUwkfUj5xsM=', '2019-10-06 12:26:51.434696', 1, 'admin', '', '', '', 1, 1, '2019-10-04 14:54:22.236294'),
(3, 'pbkdf2_sha256$100000$A3hsYYrVBGP4$n0sO0kLSKU5MgCFB7mUdUDYJ734Yg4vLZPZkLBdTm94=', NULL, 0, 'salini', 'Salini', 'Yadav', 'salini@gmail.com', 0, 1, '2019-10-04 14:56:05.000000'),
(4, 'pbkdf2_sha256$100000$FaEU82YM1282$qMAmnOV2jd2jmHgii0cB4VLjqbpEkojuWRk+/M9z6hs=', '2019-10-06 12:40:48.035213', 0, 'hemant', 'Hemant', 'Kumar', 'hemant@gmail.com', 0, 1, '2019-10-06 04:21:16.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 3, 1),
(2, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-10-04 14:54:57.463595', '1', 'Employee', 1, '[{\"added\": {}}]', 3, 2),
(2, '2019-10-04 14:55:38.619074', '1', 'Employee', 2, '[{\"changed\": {\"fields\": [\"permissions\"]}}]', 3, 2),
(3, '2019-10-04 14:56:05.960328', '3', 'employee', 1, '[{\"added\": {}}]', 4, 2),
(4, '2019-10-04 15:10:45.819543', '3', 'employee', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"email\", \"groups\"]}}]', 4, 2),
(5, '2019-10-04 15:12:32.315426', '3', 'employee', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]', 4, 2),
(6, '2019-10-04 15:45:58.333708', '1', 'Vikashpuri', 1, '[{\"added\": {}}]', 9, 2),
(7, '2019-10-06 04:21:16.857856', '4', 'hemant', 1, '[{\"added\": {}}]', 4, 2),
(8, '2019-10-06 04:23:23.259552', '4', 'hemant', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"groups\"]}}]', 4, 2),
(9, '2019-10-06 04:26:28.422898', '4', 'hemant', 2, '[{\"changed\": {\"name\": \"profile\", \"object\": \"Profile object (4)\", \"fields\": [\"police_station\", \"gender\", \"city\", \"state\", \"pin\", \"country\"]}}]', 4, 2),
(10, '2019-10-06 04:26:58.466260', '1', 'Vikashpuri', 2, '[{\"changed\": {\"fields\": [\"station_incharge\"]}}]', 9, 2),
(11, '2019-10-06 04:27:19.166809', '2', 'Tilak Nagar', 1, '[{\"added\": {}}]', 9, 2),
(12, '2019-10-06 04:27:54.231051', '3', 'employee', 2, '[{\"changed\": {\"name\": \"profile\", \"object\": \"Profile object (3)\", \"fields\": [\"police_station\", \"gender\", \"country\"]}}]', 4, 2),
(13, '2019-10-06 04:28:17.709165', '1', 'pawankumar', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 2),
(14, '2019-10-06 04:28:26.867713', '1', 'pawan', 2, '[{\"changed\": {\"fields\": [\"username\"]}}]', 4, 2),
(15, '2019-10-06 04:28:37.544363', '3', 'pooja', 2, '[{\"changed\": {\"fields\": [\"username\"]}}]', 4, 2),
(16, '2019-10-06 04:28:59.375372', '3', 'salini', 2, '[{\"changed\": {\"fields\": [\"username\", \"email\"]}}]', 4, 2),
(17, '2019-10-06 11:33:26.937015', '1', 'FIR', 2, '[{\"changed\": {\"fields\": [\"user\", \"resolved_message\"]}}]', 10, 2),
(18, '2019-10-06 12:27:27.608649', '3', 'Other', 2, '[{\"changed\": {\"fields\": [\"user\", \"resolved_by\", \"resolved_date\", \"resolved_message\"]}}]', 10, 2),
(19, '2019-10-06 12:27:55.312255', '5', 'Other', 2, '[{\"changed\": {\"fields\": [\"status\", \"resolved_by\", \"resolved_date\", \"resolved_message\"]}}]', 10, 2),
(20, '2019-10-06 12:28:12.557646', '2', 'Information', 2, '[{\"changed\": {\"fields\": [\"user\", \"resolved_by\", \"resolved_date\", \"resolved_message\"]}}]', 10, 2),
(21, '2019-10-06 12:29:01.234782', '4', 'hemant', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(10, 'application', 'complaint'),
(7, 'application', 'contact'),
(9, 'application', 'policestation'),
(8, 'application', 'profile'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-09-15 19:02:59.453985'),
(2, 'auth', '0001_initial', '2019-09-15 19:03:11.158246'),
(3, 'admin', '0001_initial', '2019-09-15 19:03:13.647614'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-09-15 19:03:13.708764'),
(5, 'contenttypes', '0002_remove_content_type_name', '2019-09-15 19:03:15.255372'),
(6, 'auth', '0002_alter_permission_name_max_length', '2019-09-15 19:03:15.468330'),
(7, 'auth', '0003_alter_user_email_max_length', '2019-09-15 19:03:15.624432'),
(8, 'auth', '0004_alter_user_username_opts', '2019-09-15 19:03:15.684674'),
(9, 'auth', '0005_alter_user_last_login_null', '2019-09-15 19:03:16.393989'),
(10, 'auth', '0006_require_contenttypes_0002', '2019-09-15 19:03:16.438844'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2019-09-15 19:03:16.503841'),
(12, 'auth', '0008_alter_user_username_max_length', '2019-09-15 19:03:18.269440'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2019-09-15 19:03:18.414932'),
(14, 'sessions', '0001_initial', '2019-09-15 19:03:19.361558'),
(15, 'application', '0001_initial', '2019-09-29 19:08:02.803517'),
(16, 'application', '0002_auto_20191004_1538', '2019-10-04 15:38:31.161253'),
(17, 'application', '0003_auto_20191004_1544', '2019-10-04 15:44:39.976957'),
(18, 'application', '0004_auto_20191004_1545', '2019-10-04 15:45:04.950620'),
(19, 'application', '0005_auto_20191006_0422', '2019-10-06 04:22:44.649094'),
(20, 'application', '0006_auto_20191006_1105', '2019-10-06 11:05:47.698013'),
(21, 'application', '0007_auto_20191006_1108', '2019-10-06 11:08:14.456171'),
(22, 'application', '0008_auto_20191006_1133', '2019-10-06 11:34:01.555761');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ahbf7tr8aheruoa7izxpak3thi9jcs4k', 'MzQ5MTc3ZjllYjYyOWE5MTEzYTU0YmEzOTg0ZmIzMzQ2NmYwM2ExYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjODZiMGFjMjhhNzI1NzlhYzBkNTgxMDE4YTcxMDE2ZTUwMzg1YmJkIn0=', '2019-10-20 12:29:01.457993'),
('loknry2eu92a98tipurjfej9ytczpmny', 'MzQ5MTc3ZjllYjYyOWE5MTEzYTU0YmEzOTg0ZmIzMzQ2NmYwM2ExYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjODZiMGFjMjhhNzI1NzlhYzBkNTgxMDE4YTcxMDE2ZTUwMzg1YmJkIn0=', '2019-10-20 06:54:33.707696'),
('slg9sp2rasi7s2yk7tnrvqa6rl0nar6t', 'MDE1ODRmMThhZDMwMDY2MTgxZmE0MDcwNmFiYWQ0ZTA3ZmJiMWM1MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1M2I2MTgwMzUwYTk0NWRmNDY3MjA3NzBiODk4Yjg0NzI0N2QwOGE4In0=', '2019-10-18 13:56:35.176254'),
('tljorau14ozc52zjebfw52vc0p8rdkqg', 'ZmZkN2UxZjZhNGQzMzJhOTU4OTM1MjEwYmMwMzU0YjVkNWY5YmMyNTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNjQwOTU2YWVmMDY5MTI5ZDA5NzVkYzllM2Q2YjEyYjM3Mzg5MzliIn0=', '2019-10-18 14:54:32.177242');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `application_complaint`
--
ALTER TABLE `application_complaint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `application_complaint_resolved_by_id_3b4c0b76_fk_auth_user_id` (`resolved_by_id`),
  ADD KEY `application_complaint_user_id_3fc0133e_fk_auth_user_id` (`user_id`),
  ADD KEY `application_complain_police_station_id_a537badd_fk_applicati` (`police_station_id`);

--
-- Indexes for table `application_contact`
--
ALTER TABLE `application_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `application_policestation`
--
ALTER TABLE `application_policestation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `station_incharge_id` (`station_incharge_id`),
  ADD UNIQUE KEY `application_policestation_station_city_96306bc2_uniq` (`station_city`);

--
-- Indexes for table `application_profile`
--
ALTER TABLE `application_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `application_profile_police_station_id_fef70193_fk_applicati` (`police_station_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `application_complaint`
--
ALTER TABLE `application_complaint`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `application_contact`
--
ALTER TABLE `application_contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `application_policestation`
--
ALTER TABLE `application_policestation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `application_profile`
--
ALTER TABLE `application_profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `application_complaint`
--
ALTER TABLE `application_complaint`
  ADD CONSTRAINT `application_complain_police_station_id_a537badd_fk_applicati` FOREIGN KEY (`police_station_id`) REFERENCES `application_policestation` (`id`),
  ADD CONSTRAINT `application_complaint_resolved_by_id_3b4c0b76_fk_auth_user_id` FOREIGN KEY (`resolved_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `application_complaint_user_id_3fc0133e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `application_policestation`
--
ALTER TABLE `application_policestation`
  ADD CONSTRAINT `application_policest_station_incharge_id_5d456b0c_fk_auth_user` FOREIGN KEY (`station_incharge_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `application_profile`
--
ALTER TABLE `application_profile`
  ADD CONSTRAINT `application_profile_police_station_id_fef70193_fk_applicati` FOREIGN KEY (`police_station_id`) REFERENCES `application_policestation` (`id`),
  ADD CONSTRAINT `application_profile_user_id_34c04f69_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
