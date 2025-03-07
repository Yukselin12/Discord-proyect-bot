import random
import requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>QWERTYUIOPASDFGHJKLÑZXCVBNMqwertyuiopasdfghjklñzxcvbnm-12345678910,.-'¿hello hello123123"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
    return password
def gen_pass1(pass_length1):
    elements1 = "/*!&$#qwertyuiopasdfghjklñzxcvbnm"
    password_s = ""

    for i in range(pass_length1):
        password_s += random.choice(elements1)
    return password_s
def gen_emodji():
    emodji = [":relaxed:", ":angry:", ":smile:", ":face_holding_back_tears:", ":thinking:", ":hushed:", ":rofl:"]
    return random.choice(emodji)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']