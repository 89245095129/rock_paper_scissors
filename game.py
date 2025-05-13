# Добавьте в начало файла
import json
import os

class ScoreBoard:
    """Класс для ведения счета игры."""
    
    def __init__(self, filename='scores.json'):
        self.filename = filename
        self.scores = self.load_scores()
    
    def load_scores(self):
        """Загружает сохраненные результаты из файла."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {'user': 0, 'computer': 0, 'draws': 0}
    
    def save_scores(self):
        """Сохраняет текущие результаты в файл."""
        with open(self.filename, 'w') as f:
            json.dump(self.scores, f)
    
    def update_score(self, result):
        """Обновляет счет на основе результата раунда."""
        if result == "победа":
            self.scores['user'] += 1
        elif result == "проигрыш":
            self.scores['computer'] += 1
        else:
            self.scores['draws'] += 1
        self.save_scores()
    
    def display_score(self):
        """Выводит текущий счет на экран."""
        print("\n--- Текущий счет ---")
        print(f"Вы: {self.scores['user']}")
        print(f"Компьютер: {self.scores['computer']}")
        print(f"Ничьи: {self.scores['draws']}")

# Обновите функцию main
def main():
    """Основная функция игры."""
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!")
    print("Введите 'выход' в любой момент для завершения игры.")
    
    score_board = ScoreBoard()
    
    while True:
        print("\n--- Новый раунд ---")
        user_choice = get_user_choice()
        if user_choice == 'выход':
            print("\nИтоговый счет:")
            score_board.display_score()
            print("Спасибо за игру! До свидания!")
            sys.exit()
            
        computer_choice = get_computer_choice()
        print(f"\nВаш выбор: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        score_board.update_score(result)
        
        if result == "ничья":
            print("Ничья! Попробуйте снова.")
        elif result == "победа":
            print("Поздравляем! Вы победили!")
        else:
            print("Увы, вы проиграли. Попробуйте ещё раз!")
        
        score_board.display_score()


import random
import json
from pathlib import Path

class ScoreBoard:
    def __init__(self):
        self.scores = {'player': 0, 'computer': 0, 'draws': 0}
        self.load_scores()
    
    def update_score(self, result):
        if result == "игрок":
            self.scores['player'] += 1
        elif result == "компьютер":
            self.scores['computer'] += 1
        else:
            self.scores['draws'] += 1
        self.save_scores()
    
    def show_score(self):
        print(f"\nТекущий счет: Игрок - {self.scores['player']}, "
              f"Компьютер - {self.scores['computer']}, "
              f"Ничьи - {self.scores['draws']}\n")
    
    def save_scores(self):
        with open('scores.json', 'w') as f:
            json.dump(self.scores, f)
    
    def load_scores(self):
        if Path('scores.json').exists():
            with open('scores.json', 'r') as f:
                self.scores = json.load(f)

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def get_user_choice():
    while True:
        user_input = input("Выберите: камень, ножницы или бумага (или 'выход'): ").lower()
        if user_input in ['камень', 'ножницы', 'бумага', 'выход']:
            return user_input
        print("Некорректный ввод. Попробуйте еще раз.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "ничья"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "игрок"
    return "компьютер"

def main():
    print("Добро пожаловать в игру Камень-Ножницы-Бумага!")
    score_board = ScoreBoard()
    
    while True:
        score_board.show_score()
        user_choice = get_user_choice()
        if user_choice == 'выход':
            break
            
        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        score_board.update_score(result)
        print("Ничья!" if result == "ничья" else f"Победил {result}!")

if __name__ == "__main__":
    main()

# Добавьте в начало файла
import sys

# Обновите функцию determine_winner
def determine_winner(user_choice, computer_choice):
    """Определяет победителя и возвращает результат."""
    if user_choice == computer_choice:
        return "ничья"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "победа"
    else:
        return "проигрыш"

# Обновите функцию main
def main():
    """Основная функция игры."""
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!")
    print("Введите 'выход' в любой момент для завершения игры.")
    
    while True:
        print("\n--- Новый раунд ---")
        user_choice = get_user_choice()
        if user_choice == 'выход':
            print("Спасибо за игру! До свидания!")
            sys.exit()
            
        computer_choice = get_computer_choice()
        print(f"\nВаш выбор: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "ничья":
            print("Ничья! Попробуйте снова.")
        elif result == "победа":
            print("Поздравляем! Вы победили!")
        else:
            print("Увы, вы проиграли. Попробуйте ещё раз!")