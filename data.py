class Data:

    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru"

    USER = {
        "email": "VasyaPetrov@yandex.ru",
        "password": "PetyaVasechkin",
    }

    RECIPE = {
        "title": "Бургер с бифштексом",
        "tags": ("Завтрак", "Ужин"),
        "ingredients": {
            ("булочки с кунжутом", 1),
            ("бифштекс", 2),
            ("помидоры бурые", 50),
            ("огурцы соленые", 50),
            ("сыр голландский", 20),
            ("лук красный", 10),
            ("зелень рубленая", 10),
            ("соус барбекю", 100)
        },
        "cook_time": 10,
        "description": "Оригинальный авторский рецепт",
        "image": "burger.jpg"
    }
