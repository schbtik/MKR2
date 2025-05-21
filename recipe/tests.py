from django.test import TestCase
from .models import Category, Recipe
from django.utils import timezone

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Супи")  # категорія

    def test_category_str(self):
        self.assertEqual(str(self.category), "Супи")  # рядок категорії

    def test_category_iter(self):
        self.assertEqual(list(iter(self.category)), [])  # ітератор категорії


class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Супи")  # категорія
        self.recipe = Recipe.objects.create(
            title="Борщ",  # назва рецепту
            description="Традиційний український буряковий суп",  # опис
            instructions="1. Варити бульйон...\n2. Додати овочі...",  # інструкції
            ingredients="Буряк, капуста, морква, картопля",  # інгредієнти
            category=self.category  # категорія
        )

    def test_recipe_str(self):
        self.assertEqual(str(self.recipe), "Борщ")  # рядок рецепту

    def test_recipe_fields(self):
        self.assertEqual(self.recipe.title, "Борщ")  # назва рецепту
        self.assertEqual(self.recipe.description, "Традиційний український буряковий суп")  # опис
        self.assertIn("Варити бульйон", self.recipe.instructions)  # перевірка інструкцій
        self.assertIn("Буряк", self.recipe.ingredients)  # перевірка інгредієнтів
        self.assertEqual(self.recipe.category, self.category)  # категорія рецепту

    def test_created_at_and_updated_at(self):
        now = timezone.now()  # теперішній час
        self.assertLessEqual(self.recipe.created_at, now)  # дата створення
        self.assertLessEqual(self.recipe.updated_at, now)  # дата оновлення
