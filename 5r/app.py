class MyName:
    """Опис класу / Документація
    """
    total_names = 0  

    def __init__(self, name=None) -> None:
        """Ініціалізація класу (конструктор)
        """

        if name is None:
            anon = self.anonymous_user()   
            name = anon.name               
        
        name = name.capitalize()

        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        self.name = name

        MyName.total_names += 1
        self.my_id = self.total_names 

    @property
    def whoami(self) -> str:
        """Повертає рядок з ім'ям"""
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Повертає e-mail за замовчуванням"""
        return self.create_email()

    @property
    def full_name(self) -> str:
        """Повертає повну інформацію про користувача"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def create_email(self, domain="itcollege.lviv.ua") -> str:
        """Створює e-mail. Домен можна змінювати параметром."""
        return f"{self.name}@{domain}"

    def name_length(self) -> int:
        """Повертає кількість букв в імені"""
        return len(self.name)

    def save_to_file(self, filename="users.txt") -> None:
        """Зберігає інформацію про користувача у файл (додає рядок в кінець файлу)"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")

    @classmethod
    def anonymous_user(cls):
        """Створює та повертає об'єкт з ім'ям 'Anonymous'"""
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Повертає привітальне повідомлення"""
        return f"You say: {message}"
    



print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", None, "sergiy")

all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me}
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email("student.itcollege.lviv.ua")}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()}
This is static with custom msg: {me.say_hello("Привіт з лабораторної роботи!")}
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
Name length: {me.name_length()} letters
FULL: {me.full_name}
{"<*>"*20}""")
    me.save_to_file()

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
