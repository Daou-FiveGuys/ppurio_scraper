from JsonChanger import JsonChanger
from PurrioScraper import PurrioScraper
from JsonlFileHandler import JsonlFileHandler
from FAQDataClass import DataClass

if __name__ == "__main__":
    purrio_scraper = PurrioScraper()
    json_changer = JsonChanger()
    jsonl_file_handler = JsonlFileHandler('./faq.txt')

    try : 
        faq_dict_list : list[DataClass] = purrio_scraper.get_faq()

        #faq_dict_list를 Json으로 변환
        faq_dict_json_list = json_changer.to_json(faq_dict_list)

        #TODO 반환 받은 list[DataClass] jsonl 형식으로 저장
        jsonl_file_handler.write_data(faq_dict_json_list)
    except Exception as e :
        print(f'❌ 실패 {e}')
    finally:
        purrio_scraper.quit()
