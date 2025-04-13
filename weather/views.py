import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    weather_note = ''
    
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '6c4bb55a4a09f501d60f6181222ea2ca'  
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            description = data['weather'][0]['description'].lower()

            # Notes based on weather condition
            if 'rain' in description:
                weather_note = "Make sure you're with an umbrella."
            elif 'clear' in description or 'sunny' in description:
                weather_note = "It’s sunny! Don’t forget your sunscreen and sunglasses."
            elif 'scattered clouds' in description:
                weather_note = "A mix of sun and clouds—keep plans flexible, just in case."
            elif 'broken clouds' in description:
                weather_note = "Some sun, some cloud—ideal for light outdoor activities."
            elif 'overcast' in description:
                weather_note = "Grey skies above—consider indoor plans."
            elif 'clouds' in description:
                weather_note = "Might feel a bit gloomy—perfect weather for a book or a calm walk."
            elif 'mist' in description or 'haze' in description or 'fog' in description:
                weather_note = "Low visibility—be cautious if you're stepping out."
            elif 'thunderstorm' in description:
                weather_note = "Stay indoors if possible—thunderstorms can be risky."
            elif 'drizzle' in description:
                weather_note = "A light drizzle—an umbrella could still come in handy."
            elif 'snow' in description:
                weather_note = "Cold and snowy—dress warm!"
            else:
                weather_note = "Stay safe and dress appropriately."

            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'note': weather_note
            }
        else:
            weather_data = {
                'city': city,
                'temperature': '-',
                'description': 'City not found',
                'note': ''
            }

    return render(request, 'index.html', {'weather': weather_data})
