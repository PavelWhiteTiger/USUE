str = input("Введите предложение на английском")
letters = {"a", "e", "i", "o", "u", "y"};
print("Длинна предложения =", len(str));
count = 0;
for letter in str:
    if letter.lower() in letters:
        count += 1;
print("Количество глассных букв =", count);
newStr = str.lower().replace("ugly", "beauty");
print(newStr);
if (str.lower().startswith("the")):
    print("Строка начинается с the");
if (str.lower().endswith("end")):
    print("Строка заканчивается на end");
