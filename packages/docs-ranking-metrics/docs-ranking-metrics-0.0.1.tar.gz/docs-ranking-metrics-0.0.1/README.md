# Описание
Данный репозиторий содержит реализацию алгоритмов ранжирования Bm25, LaBSE 
с подсчетом метрик: 
* Top@1;
* Top@3;
* Top@5;
* Средняя позиция в выдачах (AverageLoc);
* Оценка как часто фейковый документ выше релевантных (FDARO)

# Пример использования
Пример использования представлен в `examples/using_metrics.py`

```commandline
# Объявление метрик
metrics = [LaBSE(), Bm25()]
# Объявление класса агрегирующего обновление метрик
rank_metrics = RankingMetrics(metrics)

...

'''
Обновление значений метрик, где 
query - запрос по которому сгенерирован документ, 
sentences - массив документов,
labels - метки документов
'''
rank_metrics.update(query, sentences, labels)

...
# Получение значений подсчитанных метрик ввиде словаря
rank_metrics.get()
```

Возможный вывод метода get:
```
{
    'LaBSE_AverageLoc': 10.5, 
    'Bm25_AverageLoc': 1.13513, 
    'LaBSE_Top@1': 0.0, 
    'LaBSE_Top@3': 0.013513, 
    'LaBSE_Top@5': 0.013513, 
    'Bm25_Top@1': 0.91891, 
    'Bm25_Top@3': 1.0, 
    'Bm25_Top@5': 1.0, 
    'LaBSE_FDARO': 0.6216, 
    'Bm25_FDARO': 1.0
}
```

# Загрузка пакета
Необходимо установить все зависимости 

```commandline
pip install twine wheel
```

Для создания пакета необходимо воспользоваться командой:
```commandline
python3 setup.py sdist bdist_wheel
```

Загружаем пакет в PyPI
```commandline
python3 -m twine upload dist/*
```

# Улучшения:

* Исправить подсчет метрик под документы разной релевантности
* Внедрить модель https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2
* Придумать дополнительные метрики
* Завернуть все в пакет
* Написать тесты, workflows