import matplotlib.pyplot as plt
import numpy as np

print("جاري توليد ومعالجة بيانات حقل الرياح والسرعة...")

# 1. إعداد الشبكة المكانية (Grid Setup)
nx, ny = 80, 80
x = np.linspace(0, 1000, nx)
y = np.linspace(0, 1000, ny)
X, Y = np.meshgrid(x, y)

# 2. محاكاة مركبات الرياح الأفقية الواقعية (u و v) بناءً على ديناميكا الضغط
u = -5.0 * np.sin(Y / 200.0)
v = 5.0 * np.cos(X / 200.0)

# 3. حساب السرعة الفعلية للرياح (Wind Speed) باستخدام فيثاغورس
wind_speed = np.sqrt(u**2 + v**2)

# 4. حساب اتجاه الرياح بالدرجات (Wind Direction)
wind_dir = (270 - np.rad2deg(np.arctan2(v, u))) % 360

# 5. الرسم والتصوير البصري الاحترافي
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)

# رسم خريطة الألوان لسرعة الرياح
contour = ax.contourf(X, Y, wind_speed, levels=15, cmap='viridis', extend='max')
cbar = plt.colorbar(contour, ax=ax)
cbar.set_label('Wind Speed (m/s)', fontsize=12)

# تراكب متجهات الرياح (Wind Quivers) لبيان الاتجاهات بوضوح
skip = 4
ax.quiver(X[::skip, ::skip], Y[::skip, ::skip], u[::skip, ::skip], v[::skip, ::skip], 
          color='white', scale=40, width=0.003, alpha=0.8)

# تنسيق الخريطة الإحترافية
ax.set_title('Advanced NWP: Wind Speed & Vector Direction Processor', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('X Distance (km)', fontsize=11)
ax.set_ylabel('Y Distance (km)', fontsize=11)

plt.tight_layout()

# حفظ الكود الناتج كإنجاز نظيف ومستقر
plt.savefig('wind_vector_analysis.png', dpi=300)
plt.show()

print("تم معالجة وحساب سرعة واتجاه الرياح بنجاح وتم توليد الخريطة المتقدمة!")
