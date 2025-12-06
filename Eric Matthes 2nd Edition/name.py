'''
name = "welcome home"
print(name.title())
print(name.upper())
print(name.lower())


first_name = "Lloyd"
last_name = "Agyapong"
fullname = f'{first_name} {last_name}'
print(fullname)

print("\tPython")
print("Languages: \nPyhton\nC++\nJava")




simplest_language = "Python "
simplest_language = simplest_language.rstrip()
print(simplest_language)

simplest_language_1 = " Python "
print(f'\n{simplest_language_1}')

simplest_language_1 = simplest_language_1.lstrip()
print(simplest_language_1)

simplest_language_1 = simplest_language_1.strip()
print(simplest_language_1)

'''
google_url = "https://www.google.com"
google_url = google_url.removeprefix('https://')
print(google_url)