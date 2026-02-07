book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
t = Book.objects.get(title="1984")
t.title = "Nineteen Eighty-Four"
t.save()
t.delete()
