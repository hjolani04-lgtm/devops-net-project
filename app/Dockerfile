FROM python:3.11-slim

# إنشاء مستخدم محدود الصلاحيات في لينكس لزيادة الأمان
RUN useradd -m appuser

WORKDIR /app

# نسخ وتثبيت المكتبات أولاً للاستفادة من الـ Layer Caching في Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# التحويل للمستخدم غير الجذري
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
