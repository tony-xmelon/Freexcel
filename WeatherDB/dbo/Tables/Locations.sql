CREATE TABLE [dbo].[Locations] (
    [LocationId] INT            IDENTITY (1, 1) NOT NULL,
    [Name]       NVARCHAR (100) NOT NULL,
    [Country]    NVARCHAR (100) NULL,
    [Latitude]   DECIMAL (9, 6) NOT NULL,
    [Longitude]  DECIMAL (9, 6) NOT NULL,
    [Timezone]   NVARCHAR (60)  NOT NULL,
    [CreatedAt]  DATETIME2 (7)  DEFAULT (sysutcdatetime()) NOT NULL,
    PRIMARY KEY CLUSTERED ([LocationId] ASC)
);
GO

ALTER TABLE [dbo].[Locations]
    ADD CONSTRAINT [UQ_Locations_Name] UNIQUE NONCLUSTERED ([Name] ASC);
GO

