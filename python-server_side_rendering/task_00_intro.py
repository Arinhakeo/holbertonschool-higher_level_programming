#!/usr/bin/env python3

import os

def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Vérification des entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traitement de chaque participant
    for index, attendee in enumerate(attendees, start=1):
        # Remplacement des placeholders
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A") if attendee.get("event_date") is not None else "N/A"
        event_location = attendee.get("event_location", "N/A")

        # Création du contenu final
        invitation = template.format(name=name, event_title=event_title, event_date=event_date, event_location=event_location)

        # Écriture dans le fichier de sortie
        with open(f'output_{index}.txt', 'w') as file:
            file.write(invitation)