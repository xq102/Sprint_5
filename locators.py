from selenium.webdriver.common.by import By

# Кнопка «Войти в аккаунт» на главной странице
MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
# Ссылка «Личный Кабинет» в хедере
MAIN_PROFILE_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
# Кнопка "Оформить заказ" на главной странице
BASKET_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
# Логотип Stellar Burgers (ссылка на главную страницу)
MAIN_CONSTRUCTOR_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a[@href='/']")

# Поле ввода имени на форме регистрации
REG_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")
# Поле ввода email на форме регистрации
REG_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")
# Поле ввода пароля на форме регистрации
REG_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
# Кнопка «Зарегистрироваться» на форме регистрации
REG_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
# Ссылка «Войти» на форме регистрации
REG_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
# Сообщение об ошибке при некорректном пароле
REG_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

# Поле ввода email на форме входа
LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")
# Поле ввода пароля на форме входа
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
# Кнопка «Войти» на форме входа
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
# Ссылка «Восстановить пароль» на форме входа
LOGIN_RESTORE_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
# Ссылка «Зарегистрироваться» на странице входа
LOGIN_REG_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")

# Кнопка «Выход» в личном кабинете
PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
# Ссылка «Конструктор» в личном кабинете
PROFILE_CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']//p[text()='Конструктор']")

# Заголовок «Булки» в конструкторе
CONSTRUCTOR_BUNS = (By.XPATH, "//h2[text()='Булки']")

# Вкладка «Булки» в конструкторе
CONSTRUCTOR_BUNS_TAB = (By.XPATH, "//span[text()='Булки']")

# Активная вкладка «Булки» в конструкторе
CONSTRUCTOR_BUNS_CURRENT = (By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")

# Вкладка «Соусы» в конструкторе
CONSTRUCTOR_SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")

# Активная вкладка «Соусы» в конструкторе
CONSTRUCTOR_SAUCES_CURRENT= (By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")

# Вкладка «Начинки» в конструкторе
CONSTRUCTOR_FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

# Активная вкладка «Начинки» в конструкторе
CONSTRUCTOR_FILLINGS_CURRENT = (By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab_type_current__2BEPc')]")
