  GNU nano 7.2                                                             producer/produce_tickets.py                                                                      from kafka import KafkaProducer
import json
from datetime import datetime
import random
import time

# Connexion au broker Redpanda
producer = KafkaProducer(
    bootstrap_servers="redpanda:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Valeurs aléatoires pour le ticket
types_demande = ["Technique", "Commerciale", "Support"]
priorites = ["Basse", "Moyenne", "Haute"]

# Fonction pour générer un ticket aléatoire
def generate_ticket(ticket_id):
    return {
        "ticket_id": ticket_id,
        "client_id": random.randint(1, 100),
        "created_at": datetime.now().isoformat(),
        "demande": "Problème avec le produit",
        "type_demande": random.choice(types_demande),
        "priorite": random.choice(priorites)
    }

# Envoi continu des tickets
ticket_id = 1
while True:
    ticket = generate_ticket(ticket_id)
    producer.send('client_tickets', ticket)
    print(f"Ticket envoyé: {ticket}")
    ticket_id += 1
    time.sleep(1)  # envoyer un ticket toutes les secondes