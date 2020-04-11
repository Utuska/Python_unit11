import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(name, filename, to_lang,  on_lang):
    results = []
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            results.append(line)

    text_de = ''.join(results)

    params = {
        'key': API_KEY,
        'text': text_de,
        'lang': '{}-{}'.format(to_lang, on_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(filename, 'w') as f:
        f.write(''.join(json_['text']))
    return ''.join(json_['text'])

if __name__ == '__main__':

    print(translate_it("DE.txt", "DE_conversion.txt", 'de', 'ru'))

    print(translate_it("ES.txt", "ES_conversion.txt", 'es', 'ru'))

    print(translate_it("FR.txt", "FR_conversion.txt", 'fr', 'ru'))




