def generate_deep_research_prompt():
    print("🔧 Генератор промптов для Deep Research в ChatGPT")
    
    topic = input("1. Введите тему исследования: ").strip()
    report_lang = input("2. На каком языке должен быть отчет? (русский / английский / другой): ").strip()
    search_lang = input("3. На каком языке искать материалы? (английский / русский / оба): ").strip()
    depth = input("4. Какой уровень глубины? (введение / продвинутый / экспертный): ").strip()
    source_type = input("5. Какие источники использовать? (научные / любые / только peer-reviewed): ").strip()
    year_cutoff = input("6. С какого года использовать источники? (например, 2017): ").strip()
    keywords = input("7. Укажите ключевые слова (через запятую) или оставьте пустым: ").strip()
    files_included = input("8. Использовать прикрепленные файлы? (да / нет): ").strip().lower() == "да"
    banality = input("9. Что в теме считается банальностью и не должно включаться? (например: 'ИИ — это искусственный интеллект'): ").strip()

    # 🧩 Сборка финального промпта
    prompt = generate_deep_research_prompt_web(
        topic, report_lang, search_lang, depth, source_type, 
        year_cutoff, keywords, files_included, banality
    )
    
    print("\n✅ Твой готовый промпт:\n")
    print(prompt)

def generate_deep_research_prompt_web(
    topic, report_lang, search_lang, depth, source_type,
    year_cutoff, keywords, files_included, banality
):
    """Web-friendly version that accepts parameters and returns the prompt"""
    prompt = f"""
Проанализируй тему: **"{topic}"**.

🔹 Язык отчета: {report_lang}
🔹 Язык поиска источников: {search_lang}
🔹 Уровень глубины: {depth}
🔹 Тип источников: {source_type}
🔹 Учитывай источники только после: {year_cutoff}
🔹 Добавь графики, таблицы и при необходимости напиши код для визуализации
"""
    if keywords:
        prompt += f"🔹 Используй ключевые термины: {keywords}\n"

    if files_included:
        prompt += "🔹 Учитывай прикрепленные в чате файлы и включи их анализ в отчет\n"

    prompt += f"""🔹 НЕ повторяй одни и те же идеи или абзацы в разных формулировках — это ВАЖНО
🔹 Исключи банальные, очевидные утверждения, например: "{banality}"
🔹 Сначала дай краткое резюме отчета (TL;DR), затем полный текст
🔹 Используй форматированную структуру (заголовки, подзаголовки, списки)
🔹 Если информации не хватает — прямо напиши об этом, не выдумывай
🔹 Пиши без воды, но с логическими связками

Форма вывода:
- Структурированный отчет
- Отдели теоретическую часть от прикладной
- Где возможно — ссылки на источники (необязательно полные DOI, хотя бы названия)

Если готов — начинай.
"""
    return prompt

# Запуск генератора
if __name__ == "__main__":
    generate_deep_research_prompt()
