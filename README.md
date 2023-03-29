# Mapping Plastic Waste with Earth Remote Sensing Data
 HSE Project Seminar 
 
 This project is aimed to detect marine debris using sattelite imagery. A marine debris oriented dataset called Marine Debris Archive (MARIDA) is chosen as the main dataset. Dataset can be downloaded here: https://zenodo.org/record/5151941#.ZB1cMOxBy3I 
 
 Hosting of the basic tools for the extraction of spectral signatures as well as the code for the reproduction of the baseline models is cited from paper by Kikaki et al. \
 Reference: Kikaki K, Kakogeorgiou I, Mikeli P, Raitsos DE, Karantzalos K (2022) MARIDA: A benchmark for Marine Debris detection from Sentinel-2 remote sensing data. PLoS ONE 17(1): e0262247. https://doi.org/10.1371/journal.pone.0262247 
 
 # Weakly Supervised Pixel-Level Semantic Segmentation
 ## Gradient Boosting 
 A gradient boosting classifier was trained on Spectral Signatures, produced Spectral Indices (SI). Thus, this process requires the Spectral Signatures Extraction i.e., the data/dataset.h5 file. These extraction processes can be seen of opensource code of the paper https://github.com/marine-debris/marine-debris.github.io 

Data preparation, processing and training processes can be seen from this table: 

<img width="982" alt="Screen Shot 2023-03-30 at 00 22 58" src="https://user-images.githubusercontent.com/43060102/228632471-59ede486-025c-41e5-92c8-09db364955e7.png">
