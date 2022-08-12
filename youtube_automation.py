import time
import click

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import pyttsx3
import speech_recognition as speech


def speak(arg):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[10].id)
    engine.say(arg)
    engine.runAndWait()


def main():
    speak("This is the automation of youtube ,which is created ,by Mahir.")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.youtube.com/")
    speak("what you want to search sir?")
    recording = speech.Recognizer()

    with speech.Microphone() as source:
        recording.adjust_for_ambient_noise(source)
        audio = recording.listen(source)
    speak(f"you searched {recording.recognize_google(audio)} sir.")

    searchbox = driver.find_element(
        By.CLASS_NAME, "style-scope ytd-searchbox")
    searchbox.click()

    searchbox.send_keys(recording.recognize_google(audio))
    button = driver.find_element(
        By.ID, "search-icon-legacy")
    button.click()
    time.sleep(6)

    select_video = driver.find_element_by_xpath(
        "(//a[@id='video-title'])")
    select_video.click()

    time.sleep(100)


main()
