function tech() {
    var container = document.getElementById("tech_content")
    container.innerHTML = '{% for post in tech %}<a href="{% url "postview" post.pk %}"><h5>{{ post.title }}</h5></a><p>Author: {{ post.author }}<br>Publication date: {{ post.pub_date }}</p><hr>{% endfor %}'
}