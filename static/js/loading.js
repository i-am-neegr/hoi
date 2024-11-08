document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('guide-form').addEventListener('submit', function(event) {
        document.getElementById('loading').style.display = 'flex'; // Показываем элемент загрузки
    });
});
