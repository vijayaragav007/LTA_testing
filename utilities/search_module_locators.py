from selenium.webdriver.common.by import By


class SearchLocators:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    all_cookies =(By.XPATH,"//button[@id='lta-cookies-button']")
    search_option = (By.XPATH,"//button[@class='lta-btn lta-btn--lg lta-btn--link lta-btn--icon lta-btn--icon-before lta-mega-nav__btn--search']//*[name()='svg']")
    title_of_compete = (By.XPATH,"//button[contains(text(), 'COMPETE')]")
    junior_option = (By.XPATH,"//a[contains(text(),'Juniors')]")
    click_all_youth_option =(By.XPATH,"//body/main[@id='main-content']/div[1]/div[1]/div[4]/div[1]/div[4]/a[1]/div[1]/p[1]/span[1]/*[1]")
    # local_tour =(By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]/p[1]/span[1]/*[1]")