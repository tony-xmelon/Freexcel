using Microsoft.Data.SqlClient;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddHttpClient();
builder.Services.AddCors(o => o.AddDefaultPolicy(p =>
    p.WithOrigins("null", "http://localhost", "http://127.0.0.1",
                  "http://34.147.118.203", "https://34-147-118-203.sslip.io")
     .AllowAnyMethod().AllowAnyHeader()));

var app = builder.Build();
app.UseCors();

string ConnStr() => app.Configuration.GetConnectionString("WeatherHistory")!;

// POST /api/readings?locationId=1
// Fetches current temp from Open-Meteo for the location, saves it, returns reading
app.MapPost("/api/readings", async (int locationId, IHttpClientFactory httpFactory) =>
{
    // Load location
    Location? loc = null;
    using (var conn = new SqlConnection(ConnStr()))
    {
        await conn.OpenAsync();
        using var cmd = new SqlCommand(
            "SELECT LocationId, Name, Latitude, Longitude, Timezone FROM Locations WHERE LocationId = @id", conn);
        cmd.Parameters.AddWithValue("@id", locationId);
        using var reader = await cmd.ExecuteReaderAsync();
        if (await reader.ReadAsync())
            loc = new Location(reader.GetInt32(0), reader.GetString(1),
                               reader.GetDecimal(2), reader.GetDecimal(3), reader.GetString(4));
    }
    if (loc is null) return Results.NotFound("Location not found");

    // Fetch temperature from Open-Meteo
    var http = httpFactory.CreateClient();
    var url = $"https://api.open-meteo.com/v1/forecast?latitude={loc.Latitude}&longitude={loc.Longitude}&current=temperature_2m&temperature_unit=celsius";
    var meteo = await http.GetFromJsonAsync<MeteoResponse>(url);
    if (meteo is null) return Results.Problem("Failed to fetch weather data");

    var temp = meteo.Current.Temperature2m;

    // Save to DB
    long readingId;
    using (var conn = new SqlConnection(ConnStr()))
    {
        await conn.OpenAsync();
        using var cmd = new SqlCommand(
            @"INSERT INTO TemperatureReadings (LocationId, TemperatureCelsius, Source)
              OUTPUT INSERTED.ReadingId
              VALUES (@locId, @temp, 'open-meteo')", conn);
        cmd.Parameters.AddWithValue("@locId", locationId);
        cmd.Parameters.AddWithValue("@temp", temp);
        readingId = (long)(await cmd.ExecuteScalarAsync())!;
    }

    return Results.Ok(new { readingId, locationId, loc.Name, temperatureCelsius = temp, recordedAt = DateTime.UtcNow, source = "open-meteo" });
});

// GET /api/readings?locationId=1&limit=20
// Returns recent readings for a location
app.MapGet("/api/readings", async (int locationId, int limit = 20) =>
{
    var readings = new List<object>();
    using var conn = new SqlConnection(ConnStr());
    await conn.OpenAsync();
    using var cmd = new SqlCommand(
        @"SELECT TOP (@limit) r.ReadingId, r.TemperatureCelsius, r.RecordedAt, r.Source, l.Name
          FROM TemperatureReadings r
          JOIN Locations l ON l.LocationId = r.LocationId
          WHERE r.LocationId = @locId
          ORDER BY r.RecordedAt DESC", conn);
    cmd.Parameters.AddWithValue("@limit", limit);
    cmd.Parameters.AddWithValue("@locId", locationId);
    using var reader = await cmd.ExecuteReaderAsync();
    while (await reader.ReadAsync())
        readings.Add(new
        {
            readingId        = reader.GetInt64(0),
            temperatureCelsius = reader.GetDecimal(1),
            recordedAt       = reader.GetDateTime(2),
            source           = reader.IsDBNull(3) ? null : reader.GetString(3),
            locationName     = reader.GetString(4)
        });

    return Results.Ok(readings);
});

// GET /api/locations
app.MapGet("/api/locations", async () =>
{
    var locations = new List<object>();
    using var conn = new SqlConnection(ConnStr());
    await conn.OpenAsync();
    using var cmd = new SqlCommand(
        "SELECT LocationId, Name, Country, Latitude, Longitude, Timezone FROM Locations ORDER BY Name", conn);
    using var reader = await cmd.ExecuteReaderAsync();
    while (await reader.ReadAsync())
        locations.Add(new
        {
            locationId = reader.GetInt32(0),
            name       = reader.GetString(1),
            country    = reader.IsDBNull(2) ? null : reader.GetString(2),
            latitude   = reader.GetDecimal(3),
            longitude  = reader.GetDecimal(4),
            timezone   = reader.GetString(5)
        });

    return Results.Ok(locations);
});

app.Run();

record Location(int LocationId, string Name, decimal Latitude, decimal Longitude, string Timezone);
record MeteoCurrentData([property: System.Text.Json.Serialization.JsonPropertyName("temperature_2m")] double Temperature2m);
record MeteoResponse(MeteoCurrentData Current);
