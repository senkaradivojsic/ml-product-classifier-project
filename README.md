# Product Classifier – Klasifikacija proizvoda

- O projektu

Ovaj projekat predstavlja primenu mašinskog učenja za automatsku klasifikaciju proizvoda na osnovu tekstualnih podataka.
Cilj projekta je obrada i priprema tekstualnih podataka, treniranje i evaluacija različitih klasifikacionih modela, kao i čuvanje najboljeg modela za buduće predikcije.

- Dataset

Originalni skup podataka nalazi se u folderu data/. Dataset sadrži tekstualne podatke o proizvodima koji se koriste za analizu, pripremu podataka i treniranje klasifikacionih modela.

- Korišćene tehnologije i biblioteke:
  - Python – programski jezik
  - Pandas – obrada i analiza podataka
  - Scikit-learn – priprema podataka, TF-IDF vektorizacija i treniranje modela
  - Joblib – čuvanje i učitavanje istreniranog modela
  - Jupyter Notebook / Google Colab – razvoj i analiza projekta

- Analiza i treniranje modela

Celokupan proces analize i treniranja modela nalazi se u Jupyter Notebook sveskama u folderu notebooks/.

    - product_classifier_training_analysis.ipynb – analiza podataka, priprema i treniranje modela, evaluacija i poređenje rezultata.
    - product_classifier_predict_analysis.ipynb – analiza i testiranje predikcija.

- Proces treniranja obuhvata:
    - Učitavanje i analizu podataka
    - Čišćenje i pripremu podataka
    - TF-IDF vektorizaciju tekstualnih podataka
    - Treniranje više klasifikacionih modela
    - Evaluaciju i poređenje rezultata modela
    - Čuvanje finalnog istreniranog modela pomoću Joblib biblioteke

- Korišćenje modela

Finalni istrenirani model sačuvan je u folderu model/ pod nazivom product_classifier_final_model.pkl
Za treniranje modela i klasifikaciju novih tekstualnih podataka koriste se Python skripte iz foldera src/:

     - product_classifier_training.py – skripta za treniranje modela.
     - product_classifier_predict.py – skripta za učitavanje sačuvanog modela i predikciju kategorije novih proizvoda.

- Pokretanje projekta

Sve komande pokreću se iz glavnog foldera repozitorijuma.

Treniranje modela:
  
    - python src/product_classifier_training.py
  
Predikcija kategorije proizvoda:
  
    - python src/product_classifier_predict.py

- Dalji razvoj projekta i moguća unapređenja

  - Testiranje dodatnih algoritama mašinskog učenja
  - Poboljšanje performansi klasifikacionog modela
  - Testiranje modela na novim, prethodno neviđenim podacima
