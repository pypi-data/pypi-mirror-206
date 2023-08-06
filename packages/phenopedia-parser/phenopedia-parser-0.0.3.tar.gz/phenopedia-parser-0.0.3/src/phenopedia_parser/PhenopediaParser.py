import urllib

import pandas as pd
import requests
from bs4 import BeautifulSoup

cdc_url = 'https://phgkb.cdc.gov'
search_term = 'lung'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 '
                  '(KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def parse(search_term: str, dataframe=True):
    search_term = search_term.strip().replace(" ", "+")
    url = f'{cdc_url}/PHGKB/phenoPedia.action?firstQuery={search_term}' \
          f'&typeSubmit=Go&typeOption=disease&check=n&which=1'
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, features="lxml")
    links = soup.find_all('a')
    diseases = {}
    for link in links:
        href = str(link.get('href'))
        if href.startswith('/PHGKB/phenoPedia.action?firstQuery='):
            diseases[link.getText()] = cdc_url + href

    genes = []
    for disease in diseases.keys():
        html_text = requests.get(diseases[disease]).text
        soup = BeautifulSoup(html_text, features="lxml")
        gene_entries = soup.find_all('tr')
        for gene_entry in gene_entries:
            td_elements = gene_entry.find_all('td')
            if len(td_elements) == 3 and td_elements[0].text.strip() != 'Associated Gene':
                genes.append([td_elements[0].text.strip(), disease, td_elements[1].text.strip(), td_elements[2].text.strip()])

    if dataframe:
        df = pd.DataFrame(genes, columns=['gene', 'disease', 'n_publications', 'n_meta_analyses'])
        return df

    return genes
