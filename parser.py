from bs4 import BeautifulSoup
import requests
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt',"w", encoding='utf-8')
film_info = {}
for href in soup_list_href:
    f.write(f"{href['href']}\n")

f.close()
links_list = []
with open('link.txt', 'r') as file:
    links_list = file.readlines()

print(links_list)
f = open('info.txt', 'w', encoding='utf-8')

for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text,features="html.parser" )
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    soup_list_ul = soup1.find_all('ul',{"class":"short-list fx-1"})
    name = ""
    desc = ""
    if len(soup_list_name_film)> 0:
        name = soup_list_name_film[0].text.strip()
        f.write(f'{name}\n')
    if len(soup_list_ul) > 0:
        desc_parts = [item.text.strip() for item in soup_list_ul]
        desc = "\n".join(desc_parts)
        f.write(f"{desc}\n")
    if name and desc:
        film_info[name] = desc

f.close()
command = """/help - список всіх команд бота
/hello - привітання.
/film - список найновіших фільмів
/namefilm - список назв фільмів
/random - випадковий фільм
/strashno - фільми жахів та трилери
/drama - фільми драми
/bambum - фільми бойовики"""

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = "Список найновіших фільмів:\n"
    for name, link in zip(film_info.keys(), links_list):
        response += f"- {name} ({link.strip()})\n"
    await update.message.reply_text(response)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)

async def namefilm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if film_info:
        names = "\n".join(film_info.keys())
        await update.message.reply_text(names)
    else:
        await update.message.reply_text("Наразі список назв фільмів порожній.")

async def random_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if film_info:
        random_name = random.choice(list(film_info.keys()))
        random_link = links_list[list(film_info.keys()).index(random_name)].strip()
        await update.message.reply_text(f"Випадковий фільм: {random_name}\nПосилання: {random_link}")
    else:
        await update.message.reply_text("Наразі список фільмів порожній.")

async def strashno(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    scary_films = []
    for name, desc in film_info.items():
        if "жахи" in desc.lower() or "трилер" in desc.lower():
            link_index = list(film_info.keys()).index(name)
            scary_films.append(f"- {name} ({links_list[link_index].strip()})")
    if scary_films:
        response = "Фільми жахів та трилери:\n" + "\n".join(scary_films)
        await update.message.reply_text(response)

async def drama(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    drama_films = []
    for name, desc in film_info.items():
        if "драма" in desc.lower():
            link_index = list(film_info.keys()).index(name)
            drama_films.append(f"- {name} ({links_list[link_index].strip()})")
    if drama_films:
        response = "Фільми драми:\n" + "\n".join(drama_films)
        await update.message.reply_text(response)

async def bambum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    action_films = []
    for name, desc in film_info.items():
        if "бойовик" in desc.lower() or "екшн" in desc.lower():
            link_index = list(film_info.keys()).index(name)
            action_films.append(f"- {name} ({links_list[link_index].strip()})")
    if action_films:
        response = "Фільми бойовики:\n" + "\n".join(action_films)
        await update.message.reply_text(response)

app = ApplicationBuilder().token("8154740969:AAGSK56sxFFWmCeOjgztb64lsfWe0aTFkpM").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))
app.add_handler(CommandHandler("namefilm", namefilm))
app.add_handler(CommandHandler("random", random_film))
app.add_handler(CommandHandler("strashno", strashno))
app.add_handler(CommandHandler("drama", drama))
app.add_handler(CommandHandler("bambum", bambum))
app.run_polling()
