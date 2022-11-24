from selenium.webdriver.common.by import By


class SideBarLocators:
   # Локаторы для меню с классом "menu_1", который на топе сайд бара
   MENU_1_FIRST = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[3]/li[1]/a")
   MENU_1_SECOND = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[3]/li[2]/a")

   # Локаторы для 1го элемента main menu сайд бара, класс которого "menu_2"
   MAIN_MENU_FIRST = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[1]")
   MAIN_MENU_FIRST_SUBMENU = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li/a[@class='left_link']")

   # Локаторы для 2го элемента main menu сайд бара
   MAIN_MENU_SECOND = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[2]")
   MAIN_MENU_SECOND_SUBMENU = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li/a[@class='left_link']")

   # Локаторы для 3го элемента main menu сайд бара
   MAIN_MENU_THIRD = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[3]")
   MAIN_MENU_THIRD_SUBMENU = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li/a[@class='left_link']")

   # Локаторы для 4го элемента main menu сайд бара
   MAIN_MENU_FOURTH = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[4]")
   MAIN_MENU_FOURTH_SUBMENU = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[4]/div/ul/li/a[@class='left_link']")

   # Локаторы для 5го элемента main menu сайд бара
   MAIN_MENU_FIFTH = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[5]")
   MAIN_MENU_FIFTH_SUBMENU = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li/a[@class='left_link']")

   # Локаторы для 6го элемента main menu сайд бара
   MAIN_MENU_SIXTH = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[6]")

   # Локаторы для 7го элемента main menu сайд бара
   MAIN_MENU_SEVENTH = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[7]")

   # Локаторы контакт инфо div
   SHORT_NUMBER = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/a[1]")

   # Локатор для элемента отображающий 2 полных номеров связи
   FULL_NUMBERS_ELEMS = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/a")

   # Локатор для элемента отображающий обратный связь с параллелограммом
   FEEDBACK_ELEMENT = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/a")

   # Локатор для li элементов с иконками социальных сетей
   SOCIAL_MEDIA_ICONS_LI_EL = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/ul/li")