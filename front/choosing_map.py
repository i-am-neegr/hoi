import json

import folium

def create_map(points):
    # Создаем карту с начальной точкой
    first_point = next(iter(points.values()))
    m = folium.Map(location=[float(first_point['lat']), float(first_point['lon'])], zoom_start=14)

    # Добавляем точки на карту
    for key, point in points.items():
        folium.CircleMarker(
            location=[float(point['lat']), float(point['lon'])],
            radius=7,
            color='',
            fill=True,
            fill_color='blue',
            fill_opacity=1,
            popup=f"Location: {point['lat']}, {point['lon']}",
            id=f"point_{key}"
        ).add_to(m)

    # Добавляем JavaScript для изменения цвета точек при клике
    map_html = m.get_root().render()
    custom_js = """
    <script>
        function initialize() {
            var points = document.querySelectorAll('path.leaflet-interactive');
            points.forEach(function(point) {
                point.addEventListener('click', function() {
                    points.forEach(p => p.style.fill = 'blue');
                    this.style.fill = 'red';
                });
            });
        }
        window.onload = initialize;
    </script>
    """
    map_html = map_html.replace('</body>', custom_js + '</body>')

    # Записываем результат в HTML файл
    with open('map.html', 'w') as file:
        file.write(map_html)

with open('..\\data\\points_position.json', 'r') as file:
    points = json.load(file)

create_map(points)
