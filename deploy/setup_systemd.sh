

set -e  

echo " Настройка SmartEducation сервера..."
echo "----------------------------------------"

if [ "$EUID" -ne 0 ]; then 
    echo "Запустите скрипт с sudo:"
    echo "   sudo bash setup_systemd.sh"
    exit 1
fi

echo "Права администратора подтверждены"

# Устанавливаем Gunicorn если нет
echo " Проверяем Gunicorn..."
if ! /home/ubuntu/venv/bin/pip show gunicorn > /dev/null 2>&1; then
    echo "Устанавливаем Gunicorn..."
    /home/ubuntu/venv/bin/pip install gunicorn
else
    echo " Gunicorn уже установлен"
fi

# Копируем файл сервиса
echo " Настраиваем systemd сервис..."
cp /home/ubuntu/SmartEducation/deploy/smarteducation.service /etc/systemd/system/
systemctl daemon-reload

# Останавливаем старые процессы
echo " Останавливаем старые процессы..."
pkill -f "python manage.py runserver" || true
pkill -f "gunicorn.*SmartEducation" || true

echo " Запускаем SmartEducation сервис..."
systemctl enable smarteducation.service
systemctl start smarteducation.service

# Проверяем статус
echo " Проверяем запуск..."
sleep 3
if systemctl is-active --quiet smarteducation.service; then
    echo " Сервис запущен успешно!"
else
    echo "Ошибка запуска сервиса"
    systemctl status smarteducation.service --no-pager
    exit 1
fi

# Настраиваем Nginx
echo " Настраиваем Nginx..."
cp /home/ubuntu/SmartEducation/deploy/nginx.conf /etc/nginx/sites-available/smarteducation
ln -sf /etc/nginx/sites-available/smarteducation /etc/nginx/sites-enabled/smarteducation
rm -f /etc/nginx/sites-enabled/default

# Тестируем конфигурацию Nginx
echo "🧪 Тестируем конфигурацию Nginx..."
if nginx -t; then
    echo " Конфигурация Nginx корректна"
    systemctl restart nginx
    systemctl enable nginx
else
    echo "Ошибка в конфигурации Nginx"
    exit 1
fi

# Создаем папки и собираем статику
echo "Создаем папки и собираем статику..."
mkdir -p /home/ubuntu/SmartEducation/staticfiles
mkdir -p /home/ubuntu/SmartEducation/media
chown -R ubuntu:ubuntu /home/ubuntu/SmartEducation/

cd /home/ubuntu/SmartEducation/SmartEducation
sudo -u ubuntu /home/ubuntu/venv/bin/python manage.py collectstatic --noinput

echo ""
echo " Настройка завершена успешно!"
echo "----------------------------------------"
echo "Полезные команды:"
echo "   sudo systemctl status smarteducation  # Статус"
echo "   sudo systemctl restart smarteducation # Перезапуск"
echo "   sudo systemctl stop smarteducation    # Остановка"
echo "   sudo journalctl -u smarteducation -f  # Логи"
echo ""
echo " Сайт доступен по адресу: http://ваш-ip-сервера"