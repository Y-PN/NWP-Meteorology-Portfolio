import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

# 1. إعداد شبكة الإحداثيات الجغرافية
lats = np.linspace(60, 15, 50)
lons = np.linspace(10, 50, 50)
lon_2d, lat_2d = np.meshgrid(lons, lats)

# 2. محاكاة حقل الضغط الجوي (MSLP)
mslp = (
    1013
    + 15 * np.cos(np.radians(lat_2d - 30)) * np.cos(np.radians(lon_2d - 35))
    - 4 * (lat_2d - 30) / 10
)

# 3. محاكاة متجهات الرياح (Wind Vectors)
u_wind = -2.0 * (lat_2d - 30) / 5
v_wind = 2.0 * (lon_2d - 35) / 5

# 4. رسم الخريطة السينوبتيكية المتقدمة
plt.figure(figsize=(10, 6))

# تلوين الخلفية للضغط الجوي
contourf_levels = np.linspace(mslp.min(), mslp.max(), 15)
cf = plt.contourf(
    lon_2d, lat_2d, mslp, levels=contourf_levels, cmap="coolwarm", alpha=0.7
)
cbar = plt.colorbar(cf, orientation="vertical", pad=0.03)
cbar.set_label("Mean Sea Level Pressure (hPa)", fontsize=10)

# رسم خطوط الضغط المتساوي (Isobars)
cs = plt.contour(lon_2d, lat_2d, mslp, levels=10, colors="black", linewidths=1)
plt.clabel(cs, inline=True, fontsize=8, fmt="%d hPa")

# رسم متجهات الرياح (Quiver) مع أخذ عينات لعدم الازدحام
skip = 3
plt.quiver(
    lon_2d[::skip, ::skip],
    lat_2d[::skip, ::skip],
    u_wind[::skip, ::skip],
    v_wind[::skip, ::skip],
    color="navy",
    scale=80,
    width=0.003,
)

# العناوين والتنسيق
plt.title(
    "NWP Synoptic Chart: Pressure Contours & Wind Vectors",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Longitude (°E)", fontsize=10)
plt.ylabel("Latitude (°N)", fontsize=10)

# حفظ الصورة تلقائياً
plt.savefig("synoptic_pressure_wind_chart.png", dpi=300, bbox_inches="tight")
print("تم توليد وتخزين خريطة الضغط والرياح بنجاح تام! 🌪️")

plt.show()
