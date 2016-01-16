import os,sys
from PIL import Image
def printStart():
    print("""
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
    #include <avr/power.h>
#endif

//Adafruit_Neopixel(NumOfLEDs, PIN, pixel type flags (default))
Adafruit_NeoPixel strip1 = Adafruit_NeoPixel(60, 2, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip2 = Adafruit_NeoPixel(60, 3, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip3 = Adafruit_NeoPixel(60, 4, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip4 = Adafruit_NeoPixel(60, 5, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip5 = Adafruit_NeoPixel(60, 6, NEO_GRB + NEO_KHZ800);

void setup() {
    strip1.begin();
    strip1.show();
    strip2.begin();
    strip2.show();
    strip3.begin();
    strip3.show();
    strip4.begin();
    strip4.show();
    strip5.begin();
    strip5.show();
    Serial.begin(9600);
}

void loop() {
    showImageOne();
    delay(1000);
    showImageTwo();
    delay(1000);
}
    """)

def printImage(image):
    for i in range (1, 29):
        print("""    strip1.setPixelColor(""" + str(i) + """, strip1.Color""" + str(image.getpixel((i, 0))) + """);
    strip1.setPixelColor(""" + str(57-i) + """, strip1.Color""" + str(image.getpixel((i, 1))) + """);""")
    print("""    strip1.show();""")

    for i in range (0, 29):
        print("""    strip2.setPixelColor(""" + str(i) + """, strip2.Color""" + str(image.getpixel((i, 2))) + """);
    strip2.setPixelColor(""" + str(57-i) + """, strip2.Color""" + str(image.getpixel((i, 3))) + """);""")
    print("""    strip2.show();""")

    for i in range (0, 29):
        print("""    strip3.setPixelColor(""" + str(i) + """, strip3.Color""" + str(image.getpixel((i, 4))) + """);
    strip3.setPixelColor(""" + str(57-i) + """, strip3.Color""" + str(image.getpixel((i, 5))) + """);""")
    print("""    strip3.show();""")

    for i in range (0, 29):
        print("""    strip4.setPixelColor(""" + str(i) + """, strip4.Color""" + str(image.getpixel((i, 6))) + """);
    strip4.setPixelColor(""" + str(57-i) + """, strip4.Color""" + str(image.getpixel((i, 7))) + """);""")
    print("""    strip4.show();""")

    for i in range (0, 29):
        print("""    strip5.setPixelColor(""" + str(i) + """, strip5.Color""" + str(image.getpixel((i, 8))) + """);
    strip5.setPixelColor(""" + str(57-i) + """, strip5.Color""" + str(image.getpixel((i, 9))) + """);""")
    print("""    strip5.show();""")


printStart()

image = Image.open('one.png')
image = image.convert('RGB')
print("void showImageOne() {")
printImage(image)
print("}")

image = Image.open('two.png')
image = image.convert('RGB')
print("void showImageTwo() {")
printImage(image)
print("}")
