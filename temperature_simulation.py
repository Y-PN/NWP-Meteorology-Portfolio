import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

# 1. إنشاء شبكة جغرافية حرارية لمتابعة درجات الحرارة
lats = np.linspace(60, 15, 50)
lons = np.linspace(10, 50, 50)
lon_2d, lat_2d = np.meshgrid(lons, lats)

# محاكاة حقل درجات الحرارة السطحية (Surface Temperature Simulation)
temperature = 35 - 0.5 * (lat_2d - 15) + 5 * np.sin(np.radians(lon_2d))

# 2. رسم خريطة درجات الحرارة الأساسية
plt.figure(figsize=(10, 6))

# تلوين الخلفية لتمثيل التدرج الحراري
cf = plt.contourf(
    lon_2d, lat_2d, temperature, levels=15, cmap="Spectral_r", alpha=0.8
)
cbar = plt.colorbar(cf, orientation="vertical", pad=0.03)
cbar.set_label("Surface Temperature (°C)", fontsize=10)

# رسم خطوط التساوي الحراري (Isotherms)
cs = plt.contour(
    lon_2d, lat_2d, temperature, levels=10, colors="black", linewidths=1
)
plt.clabel(cs, inline=True, fontsize=8, fmt="%.1f °C")

# تنسيق العناوين الأساسية
plt.title(
    "NWP Foundation: Thermal Field & Isotherms Simulation",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Longitude (°E)", fontsize=10)
plt.ylabel("Latitude (°N)", fontsize=10)

# حفظ الصورة للملف الشخصي
plt.savefig("temperature_thermal_chart.png", dpi=300, bbox_inches="tight")
print("تم توليد وتخزين خريطة درجات الحرارة بنجاح تام! 🌡️")

plt.show()
