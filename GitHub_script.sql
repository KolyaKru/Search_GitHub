USE [master]
GO
/****** Object:  Database [GitHub]    Script Date: 02.04.2022 14:42:38 ******/
CREATE DATABASE [GitHub]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'GitHub', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\GitHub.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%)
 LOG ON 
( NAME = N'GitHub_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\GitHub_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [GitHub] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [GitHub].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [GitHub] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [GitHub] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [GitHub] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [GitHub] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [GitHub] SET ARITHABORT OFF 
GO
ALTER DATABASE [GitHub] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [GitHub] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [GitHub] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [GitHub] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [GitHub] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [GitHub] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [GitHub] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [GitHub] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [GitHub] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [GitHub] SET  DISABLE_BROKER 
GO
ALTER DATABASE [GitHub] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [GitHub] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [GitHub] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [GitHub] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [GitHub] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [GitHub] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [GitHub] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [GitHub] SET RECOVERY FULL 
GO
ALTER DATABASE [GitHub] SET  MULTI_USER 
GO
ALTER DATABASE [GitHub] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [GitHub] SET DB_CHAINING OFF 
GO
ALTER DATABASE [GitHub] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [GitHub] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [GitHub] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [GitHub] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'GitHub', N'ON'
GO
ALTER DATABASE [GitHub] SET QUERY_STORE = OFF
GO
USE [GitHub]
GO
/****** Object:  Table [dbo].[Repositories]    Script Date: 02.04.2022 14:42:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Repositories](
	[Name] [nvarchar](max) NULL,
	[Owner] [nvarchar](max) NULL,
	[Description] [nvarchar](max) NULL,
	[Date_created] [smalldatetime] NULL,
	[Date_push] [smalldatetime] NULL,
	[Homepage] [nvarchar](max) NULL,
	[Language] [nvarchar](max) NULL,
	[Url] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
UPDATE STATISTICS [dbo].[Repositories] WITH ROWCOUNT = 0, PAGECOUNT = 0
GO
USE [master]
GO
ALTER DATABASE [GitHub] SET  READ_WRITE 
GO