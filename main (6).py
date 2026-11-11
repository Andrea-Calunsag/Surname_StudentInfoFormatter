first_name = str(input("Enter first name:")).strip()
last_name = str(input("Enter last name:")).strip()
section = str(input("Enter section:")).strip()
fav_subject = str (input("Enter favorite subject:")).strip()

full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = fav_subject.title()
char_count = len(full_name)

print("\nFORMATTED OUTPUT:")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {formatted_subject}")
print(f"Character Count: {char_count}")