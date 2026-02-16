<h1 align="center">🧠 Pipeline ETL Temps Réel<br>Redpanda • PySpark • MySQL • Docker</h1>

---

## 📌 Objectif du projet <br>
Ce projet met en place un pipeline ETL temps réel permettant de :
 * Générer des tickets clients via un producteur Python
 * Les envoyer dans un broker Kafka-compatible (Redpanda)
 * Les traiter en continu avec PySpark Structured Streaming
 * Stocker les résultats dans MySQL
 * Exporter les données transformées en JSON et Parquet

💡 Ce POC démontre une architecture moderne de streaming temps réel, entièrement conteneurisée avec Docker.

 ----

## ⚙️ Architecture du pipeline <br>
Voici une vue d’ensemble du flux de données :
      
```mermaid
flowchart LR

A[Generator Tickets Python] --> B[Redpanda Kafka]
B --> C[PySpark Streaming]
C --> D[MySQL]
C --> E[Export JSON/Parquet]

D --> F[Dashboard / Analyse]
E --> F
```


------

## 🧩 Technologies utilisées <br>
             +----------------------+------------------------------+
             |  Composant	        |  Technologie                 |
             +----------------------+------------------------------+
             | Broker de messages	| Redpanda (Kafka API)         |
             | Traitement temps réel| PySpark (Spark 3.5)          |
             |  Base de données	    |  MySQL 8                     |
             | Langage	            |  Python 3                    |
             | Conteneurisation	    |  Docker & Docker Compose     |
             |  Export	            |  JSON & Parquet              |
             +----------------------+------------------------------+

## 🚀 Lancer le projet <br>    
   1. Cloner le projet
                   git clone <repo>
                   cd projet         
   2. Lancer l’infrastructure
                   docker-compose up --build                


Les services suivants démarrent :redpanda,mysql,cheik-producer,cheik-spark

## 🔄 Pipeline ETL : fonctionnement <br>
      1. Extraction

         *  Le script Python produce_tickets.py génère des tickets clients 
         *  Les messages sont envoyés dans le topic Kafka : client_tickets

      2. Transformation (PySpark): PySpark Structured Streaming :

        - lit les messages depuis Redpanda
        - parse le JSON
        - ajoute des colonnes (ex : équipe de support)
        - calcule des agrégations :nombre de tickets par type, nombre de tickets par équipe, statistiques temporelles

      3. Chargement:Les résultats sont :

          - stockés dans MySQL (tickets, ticket_stats)
          - exportés en fichiers :(/output/json/),(/output/parquet/ )

------
## 📦 Export des données <br>
- Les données transformées sont disponibles dans :(/output/json/),(/output/parquet/)
- Elles peuvent être utilisées dans :Power BI,Tableau,Pandas,Spark SQL,Jupyter Notebook

-----
## 🗄️ Vérifier les données dans MySQL <br>

          docker exec -it mysql mysql -u root -p
          USE ticketsdb;
          SELECT * FROM tickets LIMIT 10;
          SELECT * FROM ticket_stats LIMIT 10;
-----
## 🎥 Démonstration vidéo <br>  


-----
## 📁 Structure du projet <br>
                
                ├── producer/
                │   ├── Dockerfile
                │   └── produce_tickets.py
                ├── spark/
                │   ├── Dockerfile
                │   └── stream_tickets.py
                ├── output/
                │   ├── json/
                │   └── parquet/
                ├── docker-compose.yml
                └── README.md

