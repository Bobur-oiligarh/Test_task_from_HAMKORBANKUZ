from selenium.webdriver.common.by import By


class SideBarLocators:
   # Локаторы для меню, на топе сайд бара
   INTERNET_BANKING_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[3]/li[1]/a")
   FOYDANGIZNI_XISOBLANG_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[3]/li[2]/a")

   # Локаторы для 1го элемента main menu сайд бара, класс которого "menu_2"
   JISMONIY_SHAXSLARGA_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[1]")
   SUBMENU_JISMONIY_SHAXSLARGA = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li/a[@class='left_link']")

   # Локаторы для 2го элемента main menu сайд бара
   BIZNES_UCHUN_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[2]")
   SUBMENU_BIZNES_UCHUN = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li/a[@class='left_link']")

   # Локаторы для 3го элемента main menu сайд бара
   AKSIYADOR_VA_INVESTORLARGA_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[3]")
   SUBMENU_AKSIYADOR_VA_INVESTORLARGA = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li/a[@class='left_link']")

   # Локаторы для 4го элемента main menu сайд бара
   MOLIYAVIY_TASHKILOTLARGA_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[4]")
   SUBMENU_MOLIYAVIY_TASHKILOTLARGA = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[4]/div/ul/li/a[@class='left_link']")

   # Локаторы для 5го элемента main menu сайд бара
   BANK_TOGRISIDA_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[5]")
   SUBMENU_BANK_TOGRISIDA = (By.XPATH, ".//body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li/a[@class='left_link']")

   # Локаторы для 6го элемента main menu сайд бара
   MATBUOT_MARKAZI_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[6]")

   # Локаторы для 7го элемента main menu сайд бара
   ISTEMOLCHI_BURCHAGI_BUTTON = (By.XPATH, "/html/body/div[2]/div[1]/div/ul[5]/li[7]")

   # Локаторы контакт инфо
   SHORT_NUMBER = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/a[1]")

   # Локатор для элемента отображающий 2 полных номеров связи
   FULL_NUMBERS_ELEMS = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/a")

   # Локатор для элемента отображающий обратный связь с параллелограммом
   QAYTA_ALOQA_LINK = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/a")

   # Локатор для li элементов с иконками социальных сетей
   SOCIAL_MEDIA_ICONS_LI_EL = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/ul/li")