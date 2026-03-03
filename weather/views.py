import requests
from django.shortcuts import render
from django.conf import settings
from datetime import datetime, timedelta

# Session funktsiyalari
def get_current_city(request):
    """Session dan shahar nomini olish"""
    return request.session.get('current_city', 'Tashkent')

def set_current_city(request, city):
    """Session ga shahar nomini saqlash"""
    request.session['current_city'] = city

# Vaqt funktsiyalari
def get_local_time(timezone_offset):
    """Timezone offset bo'yicha mahalliy vaqtni hisoblash"""
    try:
        # UTC vaqt
        utc_time = datetime.utcnow()
        # Mahalliy vaqt
        local_time = utc_time + timedelta(seconds=timezone_offset)
        return local_time.strftime("%Y-%m-%d %H:%M")
    except:
        # Agar xatolik bo'lsa, server vaqtini qaytaramiz
        return datetime.now().strftime("%Y-%m-%d %H:%M")

# API funktsiyalari
def get_weather_data(city_name):
    """Joriy ob-havo ma'lumotlari"""
    API_KEY = settings.OPENWEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=uz"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return {'success': True, 'data': response.json()}
        return {'success': False, 'error': 'Shahar topilmadi'}
    except:
        return {'success': False, 'error': 'Xatolik yuz berdi'}

def get_pollution_data(city_name):
    """Havo ifloslanish ma'lumotlari"""
    API_KEY = settings.OPENWEATHER_API_KEY
    
    # Avval koordinatalarni olish
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
    
    try:
        geo_response = requests.get(geo_url)
        if geo_response.status_code == 200 and geo_response.json():
            lat = geo_response.json()[0]['lat']
            lon = geo_response.json()[0]['lon']
            
            pollution_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
            pollution_response = requests.get(pollution_url)
            
            if pollution_response.status_code == 200:
                return {'success': True, 'data': pollution_response.json()}
    except:
        pass
    
    return {'success': False, 'error': 'Ifoloslanish ma\'lumotlari topilmadi'}

def get_forecast_data(city_name):
    """5 kunlik prognoz"""
    API_KEY = settings.OPENWEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric&lang=uz"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return {'success': True, 'data': response.json()}
        return {'success': False, 'error': 'Prognoz topilmadi'}
    except:
        return {'success': False, 'error': 'Xatolik yuz berdi'}

def get_air_quality_info(aqi):
    """Havo sifati haqida ma'lumot"""
    aqi_info = {
        1: {"level": "Yaxshi", "color": "success", "mask": "✅ Niqob shart emas", "health": "👌 Nafas olish uchun xavfsiz"},
        2: {"level": "Maqbul", "color": "info", "mask": "⚠️ Majburiy emas", "health": "😊 Odatiy holat"},
        3: {"level": "O'rtacha", "color": "warning", "mask": "🎭 Sezgir odamlar niqob taqsin", "health": "😐 Sezgir odamlar ehtiyot bo'lsin"},
        4: {"level": "Yomon", "color": "orange", "mask": "😷 NIQOB TAVSIYA ETILADI", "health": "🤧 Nafas olish qiyinlashishi mumkin"},
        5: {"level": "Juda yomon", "color": "danger", "mask": "🚨 NIQOBSIZ CHIQMANG!", "health": "💀 Nafas olish XAVFLI!"}
    }
    return aqi_info.get(aqi, {"level": "Noma'lum", "color": "secondary", "mask": "Ma'lumot yo'q", "health": "Ma'lumot yo'q"})

def kun_nomini_ozbekcha(inglizcha_kun):
    """Kun nomlarini o'zbekchaga o'girish"""
    kun_nomlari = {
        'Monday': 'Dushanba',
        'Tuesday': 'Seshanba', 
        'Wednesday': 'Chorshanba',
        'Thursday': 'Payshanba',
        'Friday': 'Juma',
        'Saturday': 'Shanba',
        'Sunday': 'Yakshanba'
    }
    return kun_nomlari.get(inglizcha_kun, inglizcha_kun)

# VIEW LAR
def current_weather(request):
    """Asosiy sahifa - joriy ob-havo"""
    current_city = get_current_city(request)
    
    if request.method == 'POST':
        current_city = request.POST.get('city', 'Tashkent').strip()
        set_current_city(request, current_city)
    
    result = get_weather_data(current_city)
    weather_data = None
    error = None
    
    if result['success']:
        data = result['data']
        
        # Timezone offset ni olish
        timezone_offset = data.get('timezone', 0)
        
        # Mahalliy vaqtni hisoblash
        local_time = get_local_time(timezone_offset)
        
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'icon': data['weather'][0]['icon'],
            'date': local_time,  # Mahalliy vaqt
            'timezone_offset': timezone_offset
        }
    else:
        error = result.get('error', 'Xatolik yuz berdi')
    
    return render(request, 'current_weather.html', {
        'weather_data': weather_data,
        'error': error,
        'current_city': current_city
    })

def air_pollution(request):
    """Havo ifloslanish sahifasi"""
    current_city = get_current_city(request)
    
    if request.method == 'POST':
        current_city = request.POST.get('city', 'Tashkent').strip()
        set_current_city(request, current_city)
    
    pollution_data = None
    error = None
    
    # Ob-havo ma'lumotlari
    weather_result = get_weather_data(current_city)
    pollution_result = get_pollution_data(current_city)
    
    if weather_result['success']:
        w_data = weather_result['data']
        
        # Timezone offset ni olish
        timezone_offset = w_data.get('timezone', 0)
        local_time = get_local_time(timezone_offset)
        
        weather_info = {
            'city': w_data['name'],
            'country': w_data['sys']['country'],
            'temperature': round(w_data['main']['temp']),
            'icon': w_data['weather'][0]['icon'],
            'date': local_time  # Mahalliy vaqt
        }
        
        if pollution_result['success']:
            p_data = pollution_result['data']
            if 'list' in p_data and len(p_data['list']) > 0:
                components = p_data['list'][0]['components']
                aqi = p_data['list'][0]['main']['aqi']
                air_quality = get_air_quality_info(aqi)
                
                pollution_data = {
                    'weather': weather_info,
                    'aqi': aqi,
                    'aqi_info': air_quality,
                    'components': {
                        'pm2_5': components.get('pm2_5', 0),
                        'pm10': components.get('pm10', 0),
                        'co': components.get('co', 0),
                        'no2': components.get('no2', 0),
                        'o3': components.get('o3', 0),
                        'so2': components.get('so2', 0),
                    }
                }
        else:
            error = "Ifoloslanish ma'lumotlari topilmadi"
    else:
        error = "Shahar topilmadi"
    
    return render(request, 'air_pollution.html', {
        'pollution_data': pollution_data,
        'error': error,
        'current_city': current_city
    })

def five_day_forecast(request):
    """5 kunlik prognoz sahifasi"""
    current_city = get_current_city(request)
    
    if request.method == 'POST':
        current_city = request.POST.get('city', 'Tashkent').strip()
        set_current_city(request, current_city)
    
    result = get_forecast_data(current_city)
    forecast_data = None
    error = None
    
    if result['success']:
        data = result['data']
        
        # Shahar timezone ni olish
        timezone_offset = data['city'].get('timezone', 0)
        local_time = get_local_time(timezone_offset)
        
        # Kunlik prognozlarni guruhlash
        daily_forecasts = {}
        for item in data['list']:
            date = item['dt_txt'].split(' ')[0]
            if date not in daily_forecasts:
                daily_forecasts[date] = []
            daily_forecasts[date].append(item)
        
        # Har kunning o'rtacha ma'lumotlari
        processed_forecasts = []
        for date, items in list(daily_forecasts.items())[:5]:
            temps = [item['main']['temp'] for item in items]
            descriptions = [item['weather'][0]['description'] for item in items]
            icons = [item['weather'][0]['icon'] for item in items]
            
            # Kun nomini o'zbekchaga o'girish
            english_day = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
            uzbek_day = kun_nomini_ozbekcha(english_day)
            
            processed_forecasts.append({
                'date': date,
                'day_name': uzbek_day,
                'min_temp': round(min(temps)),
                'max_temp': round(max(temps)),
                'avg_temp': round(sum(temps) / len(temps)),
                'description': max(set(descriptions), key=descriptions.count),
                'icon': max(set(icons), key=icons.count),
                'humidity': round(sum(item['main']['humidity'] for item in items) / len(items))
            })
        
        forecast_data = {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'forecasts': processed_forecasts,
            'current_time': local_time  # Mahalliy vaqt
        }
    else:
        error = result.get('error', 'Prognoz topilmadi')
    
    return render(request, 'five_day_forecast.html', {
        'forecast_data': forecast_data,
        'error': error,
        'current_city': current_city
    })