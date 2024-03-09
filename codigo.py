import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("Microfsoft Edge")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=446, y=358)
pyautogui.write("contato@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    pyautogui.click(x=443, y=243)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)