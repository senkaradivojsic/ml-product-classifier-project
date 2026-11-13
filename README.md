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

Celokupan proces analize i treniranja modela nalazi se u Jupyter Notebook svesci u folderu notebooks/.

- Proces obuhvata:
  - Učitavanje i analizu podataka
  - Čišćenje i pripremu podataka
  - TF-IDF vektorizaciju tekstualnih podataka
  - Treniranje više klasifikacionih modela
  - Evaluaciju i poređenje rezultata modela
  - Čuvanje finalnog istreniranog modela pomoću Joblib biblioteke

- Korišćenje modela

Finalni istrenirani model sačuvan je u folderu model/ pod nazivom product_classifier_final_model.pkl
Za korišćenje modela i klasifikaciju novih tekstualnih podataka koristi se Python skripta predict.py, koja učitava prethodno sačuvani model.

- Dalji razvoj projekta i moguća unapređenja

  - Testiranje dodatnih algoritama mašinskog učenja
  - Poboljšanje performansi klasifikacionog modela
  - Testiranje modela na novim, prethodno neviđenim podacima
