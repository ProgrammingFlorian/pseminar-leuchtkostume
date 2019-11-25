# P-Seminar Informatik: Leuchtkostüme für das Tanzprojekt
Der Source für die Leuchtgadgets für das Tanzprojekt.
Thema: "Timm Thaler"
## Hinweise zur Ausführung
* Wir verwenden Python 3.
### Leuchtband
Die Programme, die die Neopixels-Bibliothek verwenden, können nur mit `sudo` aufgerufen werden (jedenfalls auf Raspberry Pi № 3). Also z. B. `sudo python3 band-testen.py`.

Bei einem kleinem Leuchtband reicht es, das Leuchtband an die Pins 5V, Ground und Pin 18 anzuschließen. Bei einer größeren Anzahl an LEDs müssten wir eine externe Stromversorgung verwenden.
### RGB-LED
Hier brauchen wir uns keine Sorgen um die Stromversorgung zu machen — wir werden ja nur eine solche LED im Gehstock haben. Dieses Programm kann ohne `sudo` aufgerufen werden.

Das Kabel für rotes Licht soll an Pin 25 angeschlossen werden, für grünes Licht an Pin 24, für blaues Licht an Pin 23. Diese Werte lassen sich ändern, falls es notwendig ist, aber dann muss man ein paar Zahlen im Code verändern und nicht einfach umstecken. Ein weiteres Kabel geht immer zu Ground.
