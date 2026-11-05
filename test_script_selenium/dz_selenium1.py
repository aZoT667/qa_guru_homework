import time
from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver.common.by import By

max_name = "Й" * 5000
name = ["!@#$%^&*()_+|!№;%:?*())_+", max_name, "{name:false , test:1}", "' OR '1'='1'; DROP TABLE users;--"]

# Первый шаг - выделение каждого теста в отдельную функцию и ее последующий вызов

def test01():
    print("Рефакторинг - итерация 1! Позитивный со всеми заполненными полями")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Афанасьев Максим")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("m.afanasev@example.com")

        # Находим поле Current Address по его ID и вводим текст
        current_address_field = driver.find_element(By.ID, "currentAddress")
        current_address_field.send_keys("Москва и Московская область")

        # Находим поле Permanent Address по его ID и вводим текст
        permanent_address_field = driver.find_element(By.ID, "permanentAddress")
        permanent_address_field.send_keys("Забайкалье")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        result_name = result_box.find_element(By.ID, "name")
        result_email = result_box.find_element(By.ID, "email")
        result_current_address = result_box.find_element(By.ID, "currentAddress")
        result_permanent_address = result_box.find_element(By.ID, "permanentAddress")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Афанасьев Максим" in result_name.text, "Не найдено имя"
        assert "m.afanasev@example.com" in result_email.text, "Не найден email"
        assert "Москва и Московская область" in result_current_address.text, \
            f"Не найден currentAddress - {result_current_address.text}"
        assert result_permanent_address.text is not None \
            and result_permanent_address.text != "", \
            f"permanentAddress не должен быть пустым - {result_permanent_address.text}"
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test02():
    print("Рефакторинг - итерация 1! Позитивный с пустыми полями")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        # time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 3. Проверка результата
        # time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        result_name = result_box.find_element(By.ID, "name")
        result_email = result_box.find_element(By.ID, "email")
        result_current_address = result_box.find_element(By.ID, "currentAddress")
        result_permanent_address = result_box.find_element(By.ID, "permanentAddress")

        # Проверяем, что в блоке результата появился введенный текст
        assert result_name.text == "Name:", \
            f"Name должен быть пустым - {result_name.text}"
        assert result_email.text == "Email:", \
            f"Email должен быть пустым - {result_email.text}"
        assert result_current_address.text == "Current Address :", \
            f"currentAddress должен быть пустым - {result_current_address.text}"
        assert result_permanent_address.text == "Permananet Address :", \
            f"permanentAddress должен быть пустым - {result_permanent_address.text}"
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test03():
    print("Рефакторинг - итерация 1! Негативный сценарий - некорректный email")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("m.afanasev@")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 3. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        if result_box.is_displayed():
            assert "m.afanasev@" in result_box.text
            print("Тест успешно пройден!")
        else:
            print("Некорректный email")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test04(name):
    print("Рефакторинг - итерация 1! Валидация поля name")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        # time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        for i in name:
            # Находим поле Name по его ID и вводим текст
            name_field = driver.find_element(By.ID, "userName")
            name_field.send_keys(i)

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()

            # 3. Проверка результата
            # time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = driver.find_element(By.ID, "output")

            # Проверяем, что в блоке результата появился введенный текст
            if result_box.is_displayed():
                assert i in result_box.text
                print("Тест успешно пройден!")
            else:
                print("Некорректные данные")
            name_field.clear()

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

test01()
test02()
test03()
test04(name)