from selenium.webdriver.common.by import By

# Кнопка «Войти в аккаунт» на главной странице
MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
# Ссылка «Личный Кабинет» в хедере
MAIN_PROFILE_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
# Логотип Stellar Burgers (ссылка на главную страницу)
MAIN_CONSTRUCTOR_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a[@href='/']")

# Поле ввода имени на форме регистрации
REG_NAME_INPUT = (By.XPATH, "//fieldset[1]//input[@name='name']")
# Поле ввода email на форме регистрации
REG_EMAIL_INPUT = (By.XPATH, "//fieldset[2]//input[@name='name']")
# Поле ввода пароля на форме регистрации
REG_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
# Кнопка «Зарегистрироваться» на форме регистрации
REG_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
# Ссылка «Войти» на форме регистрации
REG_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
# Сообщение об ошибке при некорректном пароле
REG_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

# Поле ввода email на форме входа
LOGIN_EMAIL_INPUT = (By.XPATH, "//fieldset[1]//input[@name='name']")
# Поле ввода пароля на форме входа
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
# Кнопка «Войти» на форме входа
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
# Ссылка «Восстановить пароль» на форме входа
LOGIN_RESTORE_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

# Кнопка «Выход» в личном кабинете
PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
# Ссылка «Конструктор» в личном кабинете
PROFILE_CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']//p[text()='Конструктор']")

# Вкладка «Булки» в конструкторе
CONSTRUCTOR_BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
# Вкладка «Соусы» в конструкторе
CONSTRUCTOR_SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
# Вкладка «Начинки» в конструкторе
CONSTRUCTOR_FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")