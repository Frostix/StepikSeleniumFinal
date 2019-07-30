from .pages.login_page import LoginPage


def test_login_sould_be_in_url(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_url()          # выполняем метод страницы - переходим на страницу логина


def test_should_be_login_form(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_should_be_login_form(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()