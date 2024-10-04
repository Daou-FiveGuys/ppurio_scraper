from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class ChromeDriver():
    """
        크롬 드라이버 클래스
    """
    def __init__(self) -> None:
        """
            생성자 : 
            1. 크롬 실행
            2. FAQ 페이지 이동
            3. 화면 최대크기로
        """
        self.__faq_link = "https://www.ppurio.com/customer/view/faq"
        self.__driver = webdriver.Chrome()
        self.__driver.get(self.__faq_link)
        self.__driver.maximize_window()

    @property
    def driver(self) -> webdriver:
        return self.__driver
    
    def get_page_buttons(self) -> list[WebElement] :
        """
            페이지 하단의 페이지로 이동 버튼 리턴

            Returns: list[버튼]
        """
        try : 
            page_box = self.__driver.find_element(By.CLASS_NAME, 'page_box')
            return page_box.find_elements(By.TAG_NAME,'button')
        except NoSuchElementException | TimeoutException as e :
            print(f'{e.stacktrace} : {e.msg}')
            exit(-1)

    def to_next_page(self) -> None:
        """
            페이지 이동 (만약 다음 페이지가 없으면 종료)
        """
        page_buttons : list[WebElement] = self.get_page_buttons()
        index : int = 0
        actions = ActionChains(self.__driver)
        actions.move_to_element(page_buttons[0]).perform()
        for page_button in page_buttons :
            if index + 1 >= len(page_buttons) : 
                break
            if page_button.get_attribute('class') == 'paging on' : 
                if page_buttons[index + 1].get_attribute('class') == 'paging ' :
                    print(f'페이지 ({page_button.text}->{page_buttons[index+1].text}) 로 이동합니다.')
                    page_buttons[index + 1].click()
                    time.sleep(0.2)
                    return
                else:
                    break
            index += 1

        print('마지막 페이지 입니다.')
        exit(0)

    def get_faq(self) -> None :
        """
            FAQ 크롤링
        """
        time.sleep(1)
        li_list : list[WebElement] = self.__driver.find_elements(By.CSS_SELECTOR, '#customerFaqList > li')
        dict = {}
        for li in li_list : 
            Q_type = li.find_element(By.CLASS_NAME,'Q_type')
            Q_title = li.find_element(By.CLASS_NAME,'Q_title')
            Q_title.click()
            time.sleep(0.5)

            dict['Q_type'] = Q_type.text
            dict['Q_type'] = Q_title.text
            
            answer : str = ''
            p_list = li.find_element(By.CLASS_NAME,'A_con').find_elements(By.TAG_NAME,'p')
            for p in p_list :
                # TODO 링크 있는 경우
                try : 
                    a = WebDriverWait(p, 0.01).until(EC.element_to_be_clickable((By.TAG_NAME,'a')))
                    a.text
                    a.get_attribute('href')
                    answer += f'{a.text} : {a.get_attribute('href')}\n'
                # TODO 링크 없는 경우
                except :
                    if len(p.text) != 0 :
                        answer += p.text + '\n'
            Q_title.click()
            print(answer)


    def quit(self):
        self.__driver.quit()

if __name__ == "__main__":
    chrome_driver = ChromeDriver()
    chrome_driver.get_faq()
    chrome_driver.quit()
