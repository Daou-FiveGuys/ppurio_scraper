from PurrioScraper import PurrioScraper
from JsonlFileHandler import JsonlFileHandler
from FAQDataClass import DataClass

if __name__ == "__main__":
    purrio_scraper = PurrioScraper()
    jsonl_file_handler = JsonlFileHandler('./')

    try : 
        faq_dict_list : list[DataClass] = purrio_scraper.get_faq()
        
        #TODO 반환 받은 list[DataClass] jsonl 형식으로 저장
        # jsonl_file_handler.
    except Exception as e :
        print(f'❌ 실패 {e}')
    finally:
        purrio_scraper.quit()
