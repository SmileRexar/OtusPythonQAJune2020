#Автотесты

## Выполнение ДЗ по Page Object

1. Согласно PageObjection вынесены локаторы и их вызовы
2. Опционально вынесены фикстуры над страницами в отдельный каталог
3. Работа с allure через Windows Subsystem for Linux из под windows


## Предустановленная среда:
1. Windows, 
2. [Установлен wsl](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
3. В wsl любой дистрибутив linux (для запуска bash)
4. Выше на каталог от проекта есть папка allure-2.13.9 с allure


## Виртуализация
1. Тесты запускаются в docker. Подготовлен docker-compose файл.
Сборка проекта
```
docker-compose up --build
```
2. Перед выполнением тестов собирается docker образ используя dockerfile на уровне рабочего каталога