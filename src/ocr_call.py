import requests
import json
import os

# API call to ocr.space with the key
def ocr_space_file(filename, language, overlay=False, api_key='PKMXB4121888A'):
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


# Input directory containing the cropped and enhanced data
input_directory_name = "customers_13"
input_directory = "/home/jay/Desktop/china_sc_tickers/" + input_directory_name + "/"
# Output file for OCR results

output_directory = "/home/jay/Desktop/ocr_output/"
error_directory = "/home/jay/Desktop/ocr_error/"

korean_failed = []
english_failed = []
number_mismatch = []
error_files = []

output_filename = "customers1_correct_available_tickers_17_output_{dir_name}.txt"
error_filename = "customers1_correct_available_tickers_17_error_{dir_name}.txt"

output_log = open(os.path.join(output_directory, output_filename.format(dir_name=input_directory_name)), "w")
error_log = open(os.path.join(error_directory, error_filename.format(dir_name=input_directory_name)), "w")

count = 1

for filename in os.listdir(input_directory):
    if filename.endswith(".png"):
        print "processing file: " + filename
        print count
        count = count + 1
        # Basic logging
        output_log.write(os.path.join(input_directory, filename) + "\n")
        try:
            # Korean language gives the best accuracy, so first I try using that.
            test_file = ocr_space_file(filename=os.path.join(input_directory, filename), language="kor")
        except:
            korean_failed.append(os.path.join(input_directory, filename))
            try:
                # In case, that call fails, I try to extract content using English language.
                test_file = ocr_space_file(filename=os.path.join(input_directory, filename), language="eng")
            except:
                english_failed.append(os.path.join(input_directory, filename))
                test_file = ""
        try:
            # JSON parsing
            json_d = json.loads(test_file)
            # print test_file
            # print json_d
            # Fetching the array of parsed text
            company_str = json_d["ParsedResults"][0]["ParsedText"]
            company_list = company_str.splitlines()
            if len(company_list) < 19:
                number_mismatch.append(os.path.join(input_directory, filename))

            for company in company_list:
                company_f = company.lstrip()
                company_clean = company_f.rstrip()
                # Writing output in output file
                output_log.write(company_clean + "\n")
        except:
            error_files.append(os.path.join(input_directory, filename))
output_log.close()

error_log.write("ocr error" + "\n")
error_log.write(','.join(error_files) + "\n")
error_log.write("korean ocr error" + "\n")
error_log.write(','.join(korean_failed) + "\n")
error_log.write("english ocr error" + "\n")
error_log.write(','.join(english_failed) + "\n")
error_log.write("mismatch" + "\n")
error_log.write(','.join(number_mismatch))

error_log.close()
