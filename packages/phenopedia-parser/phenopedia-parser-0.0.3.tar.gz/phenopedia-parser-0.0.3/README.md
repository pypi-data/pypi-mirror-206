# PhenopediaParser

A python API for parsing [Phenopedia](https://phgkb.cdc.gov/PHGKB/startPagePhenoPedia.action "Phenopedia's Homepage"). 

"Phenopedia provides a disease-centered view of genetic association studies summarized in the online Human Genome Epidemiology (HuGE) encyclopedia. Users can switch to a gene-centered view (Genopedia) or to other HuGE Tools."


## Getting Started

### Install

```pip install phenopedia_parser```

### Usage

```
from phenopedia_parser import PhenopediaParser

pheno_dataframe = PhenopediaParser.parse(search_term='lung', dataframe=True)
print(pheno_dataframe)
```

### License
MIT License

### Support
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/julianspaeth)
