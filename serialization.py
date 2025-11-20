import json

class Person:
    def __init__(self, name, age, languages):
        self.name = name
        self.age = age
        self.languages = languages

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "languages": self.languages
        }

    def save_to_json(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        return cls(**data)



person = Person("Alex", 21, ["Python", "C++", "Go"])


person.save_to_json("person.json")
print("Объект сохранён в person.json")


loaded_person = Person.load_from_json("person.json")

print("Загруженный объект:")
print(loaded_person.name, loaded_person.age, loaded_person.languages)
