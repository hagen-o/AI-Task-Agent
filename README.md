# AI Task Agent

Der AI Task Agent ist ein lokaler, deterministischer Lernprototyp in Python. Er zeigt die grundlegende Architektur eines sicheren Agentensystems: Ein einzelner Agent verarbeitet ein Ziel, folgt einer begrenzten Schleife und darf ausschließlich vorher registrierte Werkzeuge ausführen. Werkzeugergebnisse werden als Beobachtungen gespeichert, Agentenläufe können in SQLite gesichert und anschließend ausgewertet werden.

Das Projekt verwendet Pydantic für strukturierte Daten, Typer für die Kommandozeile, SQLite für Persistenz und pytest für Tests. Ein Mock-Modellanbieter erzeugt reproduzierbare Entscheidungen ohne Netzwerkzugriff, API-Schlüssel oder laufende API-Kosten.

Aktuell enthalten sind:

- eine begrenzte Agentenschleife mit den Entscheidungen `tool` und `finish`,
- eine Registry für ausdrücklich erlaubte Werkzeuge,
- ein Beispielwerkzeug zur formatierten Darstellung von Aufgaben,
- deterministische Mock-Modellanbieter,
- ein einfacher Planner,
- Speicherung, Evaluation und Reflexion von Agentenläufen,
- eine Typer-CLI sowie Unit- und End-to-End-Tests.

Das Projekt ist kein Multi-Agenten-System: Es gibt derzeit keinen Router, der selbstständig den besten spezialisierten Agenten auswählt. Neue Fähigkeiten werden als registrierte Werkzeuge ergänzt; Entscheidungen des skriptgesteuerten Mock-Anbieters werden vorher festgelegt.
