import requests
import json
import os

def ocr_space_file(filename, language, overlay=False, api_key='PKMXB3776888A'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://apipro1.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

input_directory = "/home/jay/Desktop/en1/"

korean_failed = []
number_mismatch = []
error_files = []
for filename in os.listdir(input_directory):
    if filename.endswith(".png"):
        print(os.path.join(input_directory, filename))
        try:
            test_file = ocr_space_file(filename=os.path.join(input_directory, filename), language="kor")
        except:
            korean_failed.append(filename)
            test_file = ocr_space_file(filename=os.path.join(input_directory, filename), language="eng")
        try:
            json_d = json.loads(test_file)
            #print test_file
            #print json_d
            company_str = json_d["ParsedResults"][0]["ParsedText"]
            company_list = company_str.splitlines()
            if len(company_list) < 19:
                number_mismatch.append(filename)

            for company in company_list:
                company_f = company.lstrip()
                company_clean = company_f.rstrip()
                print company_clean
        except:
            error_files.append(filename)

print korean_failed
print "mismatch"
print number_mismatch
print "error"
print error_files