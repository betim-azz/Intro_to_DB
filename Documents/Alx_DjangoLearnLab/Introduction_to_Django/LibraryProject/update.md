t = Book.objects.get(title="1984")
t.title = "Nineteen Eighty-Four"
t.save()
