# Пояснительная записка:

- Заставка
    * Название
    * Разработчики

![hippo](../TZ/data/1.png)

- Меню
    * Настройки
        * Размеры экрана
        * Громкость музыки и эффектов
        * Кнопка "Применить"
    * Лого
    * Начать
    * Продолжить

![hippo](1.gif)

-Игра

* Жизни
* Блоки
* Таймер
* Инвентарь
* Бонусы
* Оружие

![hippo](2.gif)

- Инвентарь
    * Блок
    * Бонус к прыжку
    * Бонус к скорости
    * Доп. жизнь
    * Оружие

![hippo](3.gif)

## Файлы

* [main.py](https://github.com/renat2006/lego_master_and_student/blob/Renat/main.py) <br>  
  ___Это основной файл, в нём происходит запуск игры и функций___
* [constants.py](https://github.com/renat2006/lego_master_and_student/blob/Renat/logic/constants.py) <br>  
  ___Здесь хранятся основные переменные и константы, для удобного доступа из других файлов___
* [in_game_menu.py](https://github.com/renat2006/lego_master_and_student/blob/Renat/logic/in_game_menu.py) <br>  
  ___Инвентарь___
* [load_image.py](https://github.com/renat2006/lego_master_and_student/blob/Renat/logic/load_image.py)  <br>  
  ___Загрузка изображений___
* [menu.py](https://github.com/renat2006/lego_master_and_student/blob/Renat/logic/menu.py) <br>  
  ___Меню и настройки___
* [start_screen.py](https://github.com/renat2006/lego_master_and_student/blob/Renat/logic/start_screen.py) <br>  
  ___Стартовый экран___
* [load_design.py](https://github.com/renat2006/lego_master_and_student/blob/Renat/load_design_level1.py) <br>  
  ___Загрузка уровня___

## Классы

`File_viewer` - Класс для работы с файлами и конвертации **pptx** в **png** <br>  
`Main_window` - Окно ввода темы<br>  
`Window2` - Окно выбора шаблона <br>  
`Window3` - Окно предпросмотра презентации <br>  
`Generator` - Класс генерирования презентаций и записи информации в txt<br>  
`CustomDialog`  - Класс c моделью диалогового окна<br>

## Библиотеки

___Все используемые библиотеки находятся в
файле [requirements.txt](https://github.com/renat2006/projet_ya_lc/blob/master/requirements/requirements.txt)___

* [PyQt5](https://pypi.org/project/PyQt5/)
  Используется для вывода графического интерфейса
* [wikipedia](https://pypi.org/project/wikipedia/)
  Википедия - это библиотека Python, которая упрощает доступ и анализ данных из Википедии
* [python-pptx](https://pypi.org/project/python-pptx/)
  python-pptx - это библиотека Python для создания и обновления файлов PowerPoint (.pptx).
