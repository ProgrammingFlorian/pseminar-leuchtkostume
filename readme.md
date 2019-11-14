# P-Seminar Informatik: Leuchtkostüme für das Tanzprojekt
Der Source für die Leuchtgadgets für das Tanzprojekt.
Thema: "Timm Thaler"
## Hinweise zur Ausführung
### Leuchtband
Die Programme, die die Neopixels-Bibliothek verwenden, können nur mit `sudo` aufgerufen werden (jedenfalls auf Raspberry Pi № 3). Also z. B. `sudo python3 band-testen.py`.

Bei einem kleinem Leuchtband reicht es, das Leuchtband an die Pins 5V, Ground und Pin 18 anzuschließen. Bei einer größeren Anzahl an LEDs müssten wir eine externe Stromversorgung verwenden.
