CREATE TABLE [dbo].[TemperatureReadings] (
    [ReadingId]          BIGINT         IDENTITY (1, 1) NOT NULL,
    [LocationId]         INT            NOT NULL,
    [TemperatureCelsius] DECIMAL (5, 2) NOT NULL,
    [RecordedAt]         DATETIME2 (7)  DEFAULT (sysutcdatetime()) NOT NULL,
    [Source]             NVARCHAR (50)  NULL,
    PRIMARY KEY CLUSTERED ([ReadingId] ASC),
    FOREIGN KEY ([LocationId]) REFERENCES [dbo].[Locations] ([LocationId]) ON DELETE CASCADE
);
GO

CREATE NONCLUSTERED INDEX [IX_TemperatureReadings_LocationId_RecordedAt]
    ON [dbo].[TemperatureReadings]([LocationId] ASC, [RecordedAt] DESC);
GO

