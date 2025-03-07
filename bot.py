import discord
import random
from bot_func import gen_pass
from bot_func import gen_pass1
from bot_func import gen_emodji
from discord.ext import commands
from bot_func import get_duck_image_url
from bot_func import get_dog_image_url
from model import prueba
import os


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    """Te saluda"""
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    """Te envia un emoji triste"""
    await ctx.send("😔")

@bot.command()
async def password(ctx):
    """Hard password."""
    await ctx.send(gen_pass(10))
    

@bot.command()
async def simple_password(ctx):
    """Easy password."""
    await ctx.send(gen_pass1(10))
    

@bot.command()
async def emoji(ctx):
    """Gerates a random emoji."""
    await ctx.send(gen_emodji())


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def add1(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def add2(ctx, left: int, right: int):
    """Divides two numbers."""
    await ctx.send(left / right)

@bot.command()
async def add3(ctx, left: int, right: int):
    """Subtracts two numbers."""
    await ctx.send(left - right)

@bot.command()
async def ayuda(ctx):
    """Help in spanish. Ayuda en español"""
    await ctx.send("Ayuda. Para ejecutar comandos siempre utiliza $ al inicio. Ejemplo: $hello, Comandos: add, add1, add2, add3 (suma, multiplica, divide, resta), hello, bye, tambien existen los comandos: emoji password cat dog duck etc.")

@bot.command()
async def Help(ctx):
    """Help inecesario mejor utiliza $help no $Help"""
    await ctx.send("Help. Use $ at startup to execute commands. Example: $hello, Commands: add, add1, add2, add3 (add, multiply, divide, subtract), hello, bye, There are also the commands: emoji password simple_password cat dog duck etc. etc.")
    
@bot.command()
async def meme(ctx):
    """Te envia memes"""
    meme_alet = random.choice(os.listdir("images"))
    with open(f'images/{meme_alet}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def gato(ctx):
    """Te envia videos e imagenes de gatitos"""
    meme_alet = random.choice(os.listdir("images_cat"))
    with open(f'images_cat/{meme_alet}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def dato(ctx):
    """Generates a data (in spanish)."""
    datos_curiosos = [
        "las huellas dactilares de los koalas son muy similares a las de los humanos", "el corazon de los camarones se encuentra en la cabeza", "las medusas de la especie turritopsis dohrnii pueden revertir su ciclo joven, es decir son potencialmente inmortales", "la cocacola inicialmente tenia cocaina", "algunas especies de bambus pueden crecer 30cm x dia", "Los murciélagos son los únicos mamíferos capaces de volar.","Si hueles pescado podrido 9 de cada 10 veces es un incendio electrico"
    ]
    await ctx.send(random.choice(datos_curiosos)) 

@bot.command()
async def cat(ctx):
    """Generates an image of a cat"""
    meme_alet = random.choice(os.listdir("images_gatitos"))
    with open(f'images_gatitos/{meme_alet}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    """Generates an image of a duck."""
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    """Generates an image of a dog."""
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('video')
async def video(ctx):
    """Está funcion no está disponible"""
    await ctx.send("No está disponible por ahora está función")

@bot.command('check')
async def check(ctx):
    """Envia imagenes al administrador/creador y te detecta si la imagen es un lugar seguro o no"""
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            file_name = archivo.filename
            file_url = archivo.url
            await archivo.save(f"images/{file_name}")
            await ctx.send(prueba(model_path="./keras_model.h5", label_path="./labels.txt", image_path=f"images/{file_name}"))
    else:
        await ctx.send("No hemos recibido ningun archivo")


bot.run("MTI4NTcxNTQzNDA1Nzg5MTkwMg.GQ6h_w.J9WcY-D4idwRNwaYW5igL_tEra649ImzsJMfeY")

