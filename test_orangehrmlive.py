from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_orangehrmlive():
  options = Options()
  options.add_argument("--start-maximized")

  driver = webdriver.Chrome(options=options)
  driver.delete_all_cookies()
  wait = WebDriverWait(driver, 20)

  driver.get("https://opensource-demo.orangehrmlive.com/")

  username_el = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[1]')))
  password_el = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[2]')))

  username = username_el.text.replace(' ', '').split(':')[1]
  password = password_el.text.replace(' ', '').split(':')[1]

  input_username = wait.until(
    EC.presence_of_element_located((By.NAME, 'username')))
  input_password = wait.until(
    EC.presence_of_element_located((By.NAME, 'password')))

  input_username.send_keys(username)
  input_password.send_keys(password)

  button_login = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
  button_login.click()

  button_admin = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')))
  button_admin.click()

  button_job = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')))
  button_job.click()

  button_workshifts = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]/a')))
  button_workshifts.click()

  button_add = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button')))
  button_add.click()

  input_shiftname = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input')))
  input_shiftname.send_keys('Oleksii Nakhod Shift')

  input_from = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input')))
  input_from.click()
  input_from.clear()
  input_from.send_keys('06:00 AM')

  input_to = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input')))
  input_to.click()
  input_to.clear()
  input_to.send_keys('06:00 PM')

  input_assignedemployees = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[1]/input')))
  input_assignedemployees.send_keys('Odis Adalwin')

  input_odis = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[2]/div/span')))
  input_odis.click()

  button_save = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]')))
  button_save.click()

  text_shiftname = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[text() = "Oleksii Nakhod Shift"]')))
  text_from = text_shiftname.find_element(
      By.XPATH, '../../div[3]/div')
  text_to = text_shiftname.find_element(
      By.XPATH, '../../div[4]/div')
  text_hoursperday = text_shiftname.find_element(
      By.XPATH, '../../div[5]/div')
  assert (text_from.text == '06:00') and (text_to.text == '18:00') and (text_hoursperday.text == '12.00')

  button_checkbox = text_shiftname.find_element(By.XPATH, '../../div[1]/div/div/label/span/i')
  button_checkbox.click()

  button_deleteselected = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/button')))
  button_deleteselected.click()

  button_confirm = wait.until(EC.presence_of_element_located(
      (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')))
  button_confirm.click()
  
  try:
    text_shiftname = driver.find_element(By.XPATH, '//*[text() = "Oleksii Nakhod Shift"]')
    assert False
  except:
    assert True

  driver.quit()