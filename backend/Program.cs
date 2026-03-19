using Microsoft.EntityFrameworkCore;
using K53PrepApp.Data;
using K53PrepApp.Models;

var builder = WebApplication.CreateBuilder(args);

// --- Services ---
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();

// --- Database: PostgreSQL in production, SQLite locally ---
var connectionString = Environment.GetEnvironmentVariable("DATABASE_URL");
if (!string.IsNullOrEmpty(connectionString))
{
    // Heroku/Railway-style: postgres://user:pass@host:port/db
    // Convert to Npgsql format if needed
    if (connectionString.StartsWith("postgres://"))
    {
        var uri = new Uri(connectionString);
        connectionString = $"Host={uri.Host};Port={uri.Port};Database={uri.AbsolutePath.TrimStart('/')};Username={uri.UserInfo.Split(':')[0]};Password={uri.UserInfo.Split(':')[1]};SSL Mode=Require;Trust Server Certificate=true";
    }
    builder.Services.AddDbContext<AppDbContext>(opt => opt.UseNpgsql(connectionString));
}
else
{
    // Local development — use SQLite
    builder.Services.AddDbContext<AppDbContext>(opt =>
        opt.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection") ?? "Data Source=k53prep.db"));
}

// --- CORS ---
var frontendUrl = Environment.GetEnvironmentVariable("FRONTEND_URL");
builder.Services.AddCors(options =>
{
    options.AddPolicy("DevPolicy", policy =>
        policy.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader());

    if (!string.IsNullOrEmpty(frontendUrl))
    {
        options.AddPolicy("ProductionPolicy", policy =>
            policy.WithOrigins(frontendUrl).AllowAnyMethod().AllowAnyHeader());
    }
});

var app = builder.Build();

// --- Middleware ---
var isProd = app.Environment.IsProduction();
app.UseCors(isProd && !string.IsNullOrEmpty(frontendUrl) ? "ProductionPolicy" : "DevPolicy");
app.UseStaticFiles();
app.MapControllers();

// --- Auto-migrate and seed on startup ---
using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    db.Database.EnsureCreated();
    SeedData.Seed(db);
}

app.Run();
