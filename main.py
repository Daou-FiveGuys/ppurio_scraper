from PurrioScraper import PurrioScraper
from JsonlFileHandler import JsonlFileHandler
from FAQDataClass import DataClass

if __name__ == "__main__":
    purrio_scraper = PurrioScraper()
    jsonl_file_handler = JsonlFileHandler('./')

    #TODO while문으로 페이지 넘기는 로직 추가
    faq_dict_list : list[DataClass] = purrio_scraper.get_faq()

    #TODO 반환 받은 list[DataClass] jsonl 형식으로 저장
    # jsonl_file_handler.
    purrio_scraper.quit()
