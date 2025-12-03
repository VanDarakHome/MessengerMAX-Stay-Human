import random

class bosses1:
    def boss1():
        questions = [
            {
                "question": "Блогер говорит: 'МАКС медленный!' Ваш ответ:",
                "answers": [
                    "1. Это неправда, у него быстрые серверы!",
                    "2. Да, но он безопасный",
                    "3. Зато он патриотичный"
                ],
                "correct": 0
            },
            {
                "question": "Блогер: 'У МАКС мало функций!' Ваш ответ:",
                "answers": [
                    "1. Зато он постоянно обновляется",
                    "2. Это временно, скоро добавят",
                    "3. Главное - безопасность"
                ],
                "correct": 1
            }
        ]
        
        print("=== ВИКТОРИНА ===")
        count = 0
        for i, q in enumerate(questions, 1):
            print(f"\nВопрос {i}: {q['question']}")
            for j in q['answers']:
                print(j)
            while True:
                try:
                    user_answer = int(input("Введите номер ответа (1, 2 или 3): ")) - 1
                    if 0 <= user_answer <= 2:
                        break
                    else:
                        print("Пожалуйста, введите число от 1 до 3")
                except ValueError:
                    print("Пожалуйста, введите число от 1 до 3")
            if user_answer == q['correct']:
                print("✓ Правильно!")
                count += 1
            else:
                print(f"✗ Неправильно. Правильный ответ: {q['correct'] + 1}")
        print(f"\n=== РЕЗУЛЬТАТ ===")
        print(f"Правильных ответов: {count} из {len(questions)}")
        result = count > 1
        return result

    def boss2():
        print("\n=== БОСС: СОЗДАНИЕ ПАРОЛЯ ДЛЯ МАКС ===")
        print("-" * 50)
        print("Для регистрации в МАКС нужен надежный пароль!")
        print("Вам будут показываться правила. Создайте пароль,")
        print("который соответствует ВСЕМ открытым правилам.\n")
        
        rules = [
            {
                "text": "Пароль должен содержать хотя бы 5 символов",
                "check": lambda p: len(p) >= 5,
                "revealed": True
            },
            {
                "text": "Пароль должен содержать цифру",
                "check": lambda p: any(c.isdigit() for c in p),
                "revealed": False
            },
            {
                "text": "Пароль должен содержать заглавную букву",
                "check": lambda p: any(c.isupper() for c in p),
                "revealed": False
            },
            {
                "text": "Сумма цифр в пароле должна равняться 25",
                "check": lambda p: sum(int(c) for c in p if c.isdigit()) == 25,
                "revealed": False
            },
            {
                "text": "Пароль должен содержать название месяца (например: январь, february, март)",
                "check": lambda p: any(month in p.lower() for month in 
                                    ['январь', 'january', 'февраль', 'february', 'март', 'march',
                                     'апрель', 'april', 'май', 'may', 'июнь', 'june',
                                     'июль', 'july', 'август', 'august', 'сентябрь', 'september',
                                     'октябрь', 'october', 'ноябрь', 'november', 'декабрь', 'december']),
                "revealed": False
            },
            {
                "text": "Пароль должен содержать римскую цифру (I, V, X, L, C, D, M)",
                "check": lambda p: any(r in p.upper() for r in ['I', 'V', 'X', 'L', 'C', 'D', 'M']),
                "revealed": False
            }
        ]
        
        attempts = 0
        max_attempts = 6
        passed_rules = 0
        
        print("ПРАВИЛА:")
        print("1. ✓ Пароль должен содержать хотя бы 5 символов")
        while attempts < max_attempts:
            print(f"\n{'='*40}")
            print(f"Попытка {attempts + 1} из {max_attempts}")
            print(f"Открыто правил: {passed_rules + 1}")
            print("\nТекущие требования к паролю:")
            for i, rule in enumerate(rules[:passed_rules + 1], 1):
                status = "✓" if rule["revealed"] else "-"
                print(f"{status} Правило {i}: {rule['text']}")
            password = input(f"\nВведите пароль: ")
            all_passed = True
            for i, rule in enumerate(rules[:passed_rules + 1]):
                if not rule["check"](password):
                    print(f"\n❌ Нарушено правило {i + 1}: {rule['text']}")
                    all_passed = False
                    break
            if all_passed:
                passed_rules += 1
                if passed_rules < len(rules):
                    rules[passed_rules]["revealed"] = True
                    print(f"\n✅ Все правила соблюдены!")
                    print(f"🎉 Открыто новое правило: {rules[passed_rules]['text']}")
                    if passed_rules == 3:
                        print("💡 Подсказка: цифры 9+9+7=25, или 8+8+9=25 и т.д.")
                    elif passed_rules == 4:
                        print("💡 Примеры месяцев: январь, February, март, april, ИЮЛЬ")
                    elif passed_rules == 5:
                        print("💡 Римские цифры: I=1, V=5, X=10, L=50, C=100, D=500, M=1000")
                    
                    input("Нажмите Enter чтобы продолжить...")
                else:
                    print("\n" + "="*50)
                    print("🎉 ПОБЕДА! Вы создали идеальный пароль для МАКС!")
                    print(f"Ваш пароль: '{password}'")
                    print("МАКС теперь под надежной защитой!")
                    print("="*50)
                    return True
            else:
                print("Попробуйте еще раз!")
            
            attempts += 1
        
        print("\n" + "="*50)
        print("❌ ПОРАЖЕНИЕ! Вы исчерпали все попытки.")
        print("Пароль для МАКС не создан. Попробуйте позже.")
        print("="*50)
        return False
    def test():
        original_lines = [
            "И хочется просто любить и дышать",
            "И мне другого не нужно",
            "Такой, какой есть, и меня не сломать",
            "И всё потому что…",
            "Я русский, я иду до конца!",
            "Я русский, моя кровь от отца, хе-хей",
            "Я русский, и мне повезло",
            "Я русский всему миру назло!"
        ]
        
        lines_words = [line.split() for line in original_lines]
        
        print("\n" + "="*50)
        print("ТЕСТ: ЗАПОЛНИ ПРОПУЩЕННЫЕ СЛОВА")
        print("="*50)
        print("\nПеред вами текст песни, но в каждой строке пропущено одно слово.")
        print("Введите пропущенное слово для каждой строки.\n")
        
        score = 0
        total_lines = len(original_lines)
        
        for i in range(total_lines):
            words = lines_words[i]
            if len(words) == 0:
                continue
                
            word_to_remove_idx = random.randint(0, len(words) - 1)
            word_to_remove = words[word_to_remove_idx]
            
            line_with_gap = words.copy()
            line_with_gap[word_to_remove_idx] = "______"
            line_with_gap_text = " ".join(line_with_gap)
            
            print(f"\nСтрока {i+1}: {line_with_gap_text}")
            
            user_answer = input("Введите пропущенное слово: ").strip()
            
            if (user_answer.lower() == word_to_remove.lower() or 
                user_answer.lower() == word_to_remove.rstrip(".,!…").lower()):
                print(f"✅ Правильно! Это слово: '{word_to_remove}'")
                score += 1
            else:
                print(f"❌ Неправильно. Правильный ответ: '{word_to_remove}'")
        if score <= 2:
            result = 0
        elif 3 <= score <= 5:
            result = 1
        else:
            result = 2
        
        print("="*50)
        print("\nПолный текст песни:")
        print("-" * 30)
        for line in original_lines:
            print(line)
        return result
