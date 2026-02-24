

# blog\views.py

    from django.shortcuts import render
    from django.utils import timezone
    from .models import Post

    ## Create your views here.
    def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})



# blog\templates\blog\post_list.html

    <!DOCTYPE html>
    <html>
        <head>
            <title>Django Girls blog</title>
        </head>
        <body>
            <header>
                <h1><a href="/">Django Girls Blog</a></h1>
            </header>

            <p>And this is the list of posts from the database:</p>
            {% for post in posts %}
                <article>
                    <list>{{ post }}</list>
                </article>
            {% endfor %}
            <p>this is the number of posts: {{ posts.count }}</p>
            {% for post in posts %}
                <article>
                    <h2><a href="">{{ post.title }}</a></h2>
                    <p>{{ post.text|linebreaks }}</p>
                    <time>published: {{ post.published_date }}</time>
                </article>
            {% endfor %}
        </body>
    </html>






