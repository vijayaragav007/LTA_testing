from selenium.webdriver.common.by import By


class LTALocators:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    all_cookies =(By.XPATH,"//button[@id='lta-cookies-button']")
    compete = (By.XPATH,"//button[contains(text(), 'COMPETE')]")
    junior = (By.XPATH,"//a[contains(text(),'Juniors')]")
    youth_Competitions =(By.XPATH,"//div[4]//div[1]//div[4]//a[1]//div[1]//p[1]")
    youth_match_play = (By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]/p[1]/span[1]/*[1]")
    submit_lta =(By.XPATH,"//span[contains(text(),'Enter an LTA Youth Local Tour Competition')]")
    accept =(By.XPATH,"//span[contains(text(),'Accept')]")
    tournaments =(By.XPATH,"//span[contains(text(),'Tournaments')]")
    entry_open =(By.XPATH,"//a[normalize-space()='Entry open']")
    leamington_tennis_club =(By.XPATH,"//span[contains(text(),'Central & East Tour - Dallington Lawn Tennis Club ')]")
    enter_leamington =(By.XPATH,"//span[contains(text(),'Enter')]")

    