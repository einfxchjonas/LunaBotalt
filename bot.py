from pydoc import describe
import discord
from discord import app_commands
from discord import Message, Guild, TextChannel, Permissions, Intents
from discord.ext import tasks, commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ui import Button, View
import time
import datetime
import random
from discord import ui
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def setup_hook(self) -> None:
        # Register the persistent view for listening here.
        # Note that this does not send the view to any message.
        # In order to do this you need to first send a message with the View, which is shown below.
        # If you have the message_id you can also pass it as a keyword argument, but for this example
        # we don't have one.
        self.add_view(VerifyButton1())
        self.add_view(VerifyButton2())
        self.add_view(TicketChannelButtons())
        self.add_view(TicketMenuButtons())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, user: discord.Member):
        print("Mitglied beigetreten!")
        creation_time = user.created_at
        formatted_creation_time = datetime.datetime.strftime(creation_time, '%d/%m/%Y %H:%M')

        join_date = user.joined_at
        formatted_join_time = datetime.datetime.strftime(join_date, "%d/%m/%Y %H:%M")
        channel = bot.get_channel(int(974676722987442241))
        embed = discord.Embed(title="Willkommen", description=f"Wir wünschen {user.mention} hier herzlich willkommen!\nWir hoffen das du hier viel spaß haben wirst!\n\n"
        f"<:emoji_75:1003343610273595463>** | Nutzer Daten**\n"
        f"> Account erstelt am `{formatted_creation_time}`\n\n"
        f"<:emoji_154:1059080593293455380>** | Server Daten**\n"
        f"> **Member:** *{user.guild.member_count}*\n"
        f"> Beigetreten am `{formatted_join_time}`", color=embedColor)

        await channel.send(embed=embed)





intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents, help_command=None, debug_guilds=None)
bot = PersistentViewBot()
bot.baned_Users=[]

botadmin = [686634546577670400, 868727185974890586, 651790916595613696, 830778367367708753, 690543740468723762]

#Normal embed Color: (115, 44, 255)

embedColor = discord.Color.from_rgb(44, 143, 255)
SysEmoji = ""

@bot.event
async def on_member_join(guild):
    banner_url = guild.banner_url_as(format="png")
    member_count = len(guild.members)
    text = f"{member_count} Mitglieder"

    # Lade das Banner-Bild herunter
    response = requests.get(banner_url)
    banner_image = Image.open(BytesIO(response.content))

    # Erstelle ein ImageDraw-Objekt
    draw = ImageDraw.Draw(banner_image)

    # Wähle eine Schriftart und Schriftgröße
    font = ImageFont.truetype("Arial.ttf", size=50)

    # Wähle eine Textfarbe
    text_color = (255, 255, 255)  # Weiß

    # Berechne die Position des Textes im Bild
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((banner_image.width - text_width) // 2, (banner_image.height - text_height) // 2)

    # Füge den Text zum Bild hinzu
    draw.text(text_position, text, font=font, fill=text_color)

    # Speichere das aktualisierte Banner-Bild temporär
    temp_banner_path = "temp_banner.png"
    banner_image.save(temp_banner_path)

    # Lade das aktualisierte Banner-Bild hoch
    with open(temp_banner_path, "rb") as file:
        await guild.edit(banner=file.read())

    # Lösche das temporäre Bild
    banner_image.close()
    os.remove(temp_banner_path)


@bot.event
async def on_member_remove(guild):
    banner_url = guild.banner_url_as(format="png")
    member_count = len(guild.members)
    text = f"{member_count} Mitglieder"

    # Lade das Banner-Bild herunter
    response = requests.get(banner_url)
    banner_image = Image.open(BytesIO(response.content))

    # Erstelle ein ImageDraw-Objekt
    draw = ImageDraw.Draw(banner_image)

    # Wähle eine Schriftart und Schriftgröße
    font = ImageFont.truetype("Arial.ttf", size=50)

    # Wähle eine Textfarbe
    text_color = (255, 255, 255)  # Weiß

    # Berechne die Position des Textes im Bild
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((banner_image.width - text_width) // 2, (banner_image.height - text_height) // 2)

    # Füge den Text zum Bild hinzu
    draw.text(text_position, text, font=font, fill=text_color)

    # Speichere das aktualisierte Banner-Bild temporär
    temp_banner_path = "temp_banner.png"
    banner_image.save(temp_banner_path)

    # Lade das aktualisierte Banner-Bild hoch
    with open(temp_banner_path, "rb") as file:
        await guild.edit(banner=file.read())

    # Lösche das temporäre Bild
    banner_image.close()
    os.remove(temp_banner_path)


async def update_banner(guild):
    banner_url = guild.banner_url_as(format="png")
    member_count = len(guild.members)
    text = f"{member_count} Mitglieder"

    # Lade das Banner-Bild herunter
    response = requests.get(banner_url)
    banner_image = Image.open(BytesIO(response.content))

    # Erstelle ein ImageDraw-Objekt
    draw = ImageDraw.Draw(banner_image)

    # Wähle eine Schriftart und Schriftgröße
    font = ImageFont.truetype("Arial.ttf", size=50)

    # Wähle eine Textfarbe
    text_color = (255, 255, 255)  # Weiß

    # Berechne die Position des Textes im Bild
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((banner_image.width - text_width) // 2, (banner_image.height - text_height) // 2)

    # Füge den Text zum Bild hinzu
    draw.text(text_position, text, font=font, fill=text_color)

    # Speichere das aktualisierte Banner-Bild temporär
    temp_banner_path = "temp_banner.png"
    banner_image.save(temp_banner_path)

    # Lade das aktualisierte Banner-Bild hoch
    with open(temp_banner_path, "rb") as file:
        await guild.edit(banner=file.read())

    # Lösche das temporäre Bild
    banner_image.close()
    os.remove(temp_banner_path)

@bot.event
async def on_ready():

    print("Bot is Up and Ready!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"euch beim chatten zu!"))
    try:
        synced = await bot.tree.sync()
        print("Synced with the Server")
    except:
        print("Could not sync with Server!")




class VerifyButton2(discord.ui.View):
    def __init__(self):
         super().__init__(timeout=None)
    @discord.ui.button(label="Verify", custom_id="verify2", style=discord.ButtonStyle.green, emoji="✅")
    async def verify_button2(self, interation: discord.Interaction, Button: discord.ui.Button):
        channel = bot.get_channel(974676722727403667)
        embedV = discord.Embed(title="Nur noch ein schritt!", description=f"Bevor du dich verifizierst, möchten wir das du dir die Regeln in <#974676722727403667> durchlißt und dich an diese hätst.\nIn <#974676722727403667> kannst du dich verifizieren.")
        embedV2 = discord.Embed(title="Nur noch ein schritt!", description="Nachdem du dir die regeln hier durchgelesen hast, kannst du dich hier Verifizieren.")
        role = discord.utils.get(interation.guild.roles, name="『💎』 Verified")
        role2 = discord.utils.get(interation.guild.roles, name="『👤』 Mitglieder")
        await interation.user.add_roles(role2)
        await interation.user.add_roles(role)
        await interation.response.send_message("**ERFOLG**\nDu wurdest Verifiziert!", ephemeral=True)
        await interation.user.send("**ERFOLG**\nDu wurdest Verifiziert!")
        creation_time = interation.user.created_at
        formatted_creation_time = datetime.datetime.strftime(creation_time, '%d/%m/%Y %H:%M')

        join_date = interation.user.joined_at
        formatted_join_time = datetime.datetime.strftime(join_date, "%d/%m/%Y %H:%M")
        channel = bot.get_channel(974676722987442241)
        embed = discord.Embed(title="Willkommen", description=f"Wir wünschen {interation.user.mention} hier herzlich willkommen!\nWir hoffen das du hier viel spaß haben wirst!\n\n"
        f"<:emoji_75:1003343610273595463>** | Nutzer Daten**\n"
        f"> Account erstelt am `{formatted_creation_time}`\n\n"
        f"<:emoji_154:1059080593293455380>** | Server Daten**\n"
        f"> **Member:** *{interation.guild.member_count}*\n"
        f"> Beigetreten am `{formatted_join_time}`", color=embedColor)
        embed.set_footer(text="Gemacht mit ❤️", icon_url=interation.guild.icon.url)
        embed.set_thumbnail(url=interation.user.avatar.url)
        await channel.send(embed=embed)


class VerifyButton1(discord.ui.View):
    def __init__(self):
         super().__init__(timeout=None)
    @discord.ui.button(label="Verify", custom_id="verify1", style=discord.ButtonStyle.green, emoji="✅")
    async def verify_button1(self, interation: discord.Interaction, Button: discord.ui.Button):
        embedV2 = discord.Embed(title="Nur noch ein schritt!", description="Nachdem du dir die regeln hier durchgelesen hast, kannst du dich hier Verifizieren.\n\n**Regeln**\n"
        "§1.1 Namensgebung\nNicknames dürfen keine beleidigenden oder anderen verbotenen oder geschützen Namen oder Namensteile enthalten.\n\n"
        "§1.2 Avatar\nAvatare dürfen keine pornographischen, rassistischen oder beleidigenden Inhalte beinhalten.\n\n"
        "§2.1 Umgangston\nDer Umgang mit anderen Discord Benutzern sollte stets freundlich sein. Verbale Angriffe gegen andere User sind strengstens untersagt.\n\n"
        "§2.2 Gespräche aufnehmen\nDurch Das betreten eines Textkanales erklärst du dich damit einverstanden, dass du eventuell Aufgezeichnet und veröffentlich wirst\n\n"
        "§2.3 Abwesenheit\nBei längerer Abwesenheit wird der Benutzer gebeten in den entsprechnden AFK-Channel zu gehen.\n\n"
        "§3.1 Kicken/Bannen\nEin Kick oder Bann ist zu keinem Zeitpunkt unbegründet, sondern soll zum Nachdenken der eigenen Verhaltensweise anregen. Unangebrachte Kicks/Banns müssen den zuständigen Admins gemeldet werden.\n\n"
        "§3.2 Discord Rechte\nDiscord Rechte werden nicht wahllos vergeben, sondern dienen immer einem bestimmten Grund. Bei Bedarf von Rechten kann sich an den zuständigen Admin gewandt werden.\n\n"
        "§3.3 Weisungsrecht\nServer Admins, Moderatoren oder anderweitig befugte Admins haben volles Weisungsrecht. Das Verweigern einer bestimmten Anweisung kann zu einem Kick oder Bann führen.\n\n"
        "§4.1 Werbung\nJegliche Art von Werbung ist auf diesem Server untersagt. Ggf. kann sich an einen zuständigen Admin gewandt werden, um über eine Möglichkeit zur Werbung zu verhandeln.\n\n"
        "§4.2 Datenschutz\nPrivate Daten wie Telefonnummern, Adressen, Passwörter und ähnlichem dürfen nicht öffentlich ausgetauscht werden.\n\n"
        "§5.1 Bots (insb. Musik-Bots)\nEs dürfen keine eigenen Bots mit dem Discord Server verbunden werden.\n\n"
        "§6.1 Meldepflicht\nEs sind alle Benutzer angehalten, die Discord-Server Regeln zu beachten. Sollte ein Regelverstoß von einem Benutzer erkannt werden, ist dieser umgehend einem Admin zu melden.", color=embedColor)
        role = discord.utils.get(interation.guild.roles, name="『💎』 Verified")
        role2 = discord.utils.get(interation.guild.roles, name="『👤』 Mitglieder")

        #await interation.user.add_roles(role2)
        await interation.response.send_message(embed=embedV2, view=VerifyButton2(), ephemeral=True)

@bot.command()
async def rulesA(ctx):
    embedV2 = discord.Embed(title="Regelwerk", description=
        "§1.1 Namensgebung\nNicknames dürfen keine beleidigenden oder anderen verbotenen oder geschützen Namen oder Namensteile enthalten.\n\n"
        "§1.2 Avatar\nAvatare dürfen keine pornographischen, rassistischen oder beleidigenden Inhalte beinhalten.\n\n"
        "§2.1 Umgangston\nDer Umgang mit anderen Discord Benutzern sollte stets freundlich sein. Verbale Angriffe gegen andere User sind strengstens untersagt.\n\n"
        "§2.2 Gespräche aufnehmen\nDurch Das betreten eines Textkanales erklärst du dich damit einverstanden, dass du eventuell Aufgezeichnet und veröffentlich wirst\n\n"
        "§2.3 Abwesenheit\nBei längerer Abwesenheit wird der Benutzer gebeten in den entsprechnden AFK-Channel zu gehen.\n\n"
        "§3.1 Kicken/Bannen\nEin Kick oder Bann ist zu keinem Zeitpunkt unbegründet, sondern soll zum Nachdenken der eigenen Verhaltensweise anregen. Unangebrachte Kicks/Banns müssen den zuständigen Admins gemeldet werden.\n\n"
        "§3.2 Discord Rechte\nDiscord Rechte werden nicht wahllos vergeben, sondern dienen immer einem bestimmten Grund. Bei Bedarf von Rechten kann sich an den zuständigen Admin gewandt werden.\n\n"
        "§3.3 Weisungsrecht\nServer Admins, Moderatoren oder anderweitig befugte Admins haben volles Weisungsrecht. Das Verweigern einer bestimmten Anweisung kann zu einem Kick oder Bann führen.\n\n"
        "§4.1 Werbung\nJegliche Art von Werbung ist auf diesem Server untersagt. Ggf. kann sich an einen zuständigen Admin gewandt werden, um über eine Möglichkeit zur Werbung zu verhandeln.\n\n"
        "§4.2 Datenschutz\nPrivate Daten wie Telefonnummern, Adressen, Passwörter und ähnlichem dürfen nicht öffentlich ausgetauscht werden.\n\n"
        "§5.1 Bots (insb. Musik-Bots)\nEs dürfen keine eigenen Bots mit dem Discord Server verbunden werden.\n\n"
        "§6.1 Meldepflicht\nEs sind alle Benutzer angehalten, die Discord-Server Regeln zu beachten. Sollte ein Regelverstoß von einem Benutzer erkannt werden, ist dieser umgehend einem Admin zu melden.",
        color=embedColor, timestamp=datetime.datetime.now())
    await ctx.send(embed=embedV2)
@bot.tree.command(name="setup_verify", description="Setze das verify system auf.")
async def setup_verify(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("Erfolg! Verify system aktiv!", ephemeral=True)
        embed= discord.Embed(title="Verify", description=f"Willkommen auf {interaction.guild.name}!\nUm Dich auf diesem Server zu verifizieren, musst du untern mit dem Button interagieren.\nWir wünschen dir viel spaß!", color=embedColor)
        embed.set_footer(text="Gemacht mit ❤️ von @einfxch_jonas")
        await interaction.channel.send(embed=embed, view=VerifyButton1())
    else:
        await interaction.response.send_message("Du bist kein administrator!", ephemeral=True)

class TicketChannelDeleteButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Delete", custom_id="yes_ticket", style=discord.ButtonStyle.danger,
                       emoji="<:emoji_71:1002849943519776810>")
    async def yes_buton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        embed = discord.Embed(title="In the process of deletion", description="The ticket will be deleted shortly...", color=embedColor)
        await interaction.response.send_message(embed=embed)
        await time.sleep(5)
        await interaction.channel.delete()
        TicketChannelDeleteButtons().disabled = True

    @discord.ui.button(label="No", custom_id="no_ticket", style=discord.ButtonStyle.gray,
                       emoji="<:emoji_59:1002849625562173510>")
    async def no_buton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        embed = discord.Embed(title="Operation aborted",
                              description="The process has been canceled! The ticket will not be deleted.",
                              color=embedColor)
        await interaction.response.send_message(embed=embed)
        return

class TicketChannelButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Close", custom_id="close", style=discord.ButtonStyle.danger,
                       emoji="<:emoji_71:1002849943519776810> ")
    async def close_button(self, interaction: discord.Interaction, Button: discord.ui.Button):
        embed = discord.Embed(title="Ticket System", description="Are you sure you want to close the ticket?",
                              color=embedColor)
        role = discord.utils.get(interaction.guild.roles, name="ticket_admin")
        if role in interaction.user.roles:
            await interaction.response.send_message(embed=embed, view=TicketChannelDeleteButtons())
        else:
            # Nachricht senden, wenn der Nutzer nicht über die Rolle "ticket_admin" verfügt
            await interaction.response.send_message("You don't have permission to use this command!",
                                                    ephemeral=True)

    @discord.ui.button(label="Claim", custom_id="claim", style=discord.ButtonStyle.blurple,
                       emoji="<:team:1021134957621563453>")
    async def claim_button(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="ticket_admin")
        if role in interaction.user.roles:
            # Code ausführen, wenn der Nutzer über die Rolle "ticket_admin" verfügt
            embed2 = discord.Embed(title="Claimed",
                                   description=f"The user {interaction.user.mention} is now taking care of you.",
                                   color=embedColor, timestamp=datetime.datetime.now())
            await interaction.response.send_message(embed=embed2)
        else:
            # Nachricht senden, wenn der Nutzer nicht über die Rolle "ticket_admin" verfügt
            await interaction.response.send_message("You don't have permission to use this command!",
                                                    ephemeral=True)


class TicketMenuButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Frage", custom_id="question", style=discord.ButtonStyle.green,
                       emoji="<:icon_chat:1108822865865867374>")
    async def question_button(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="ticket_admin")
        # await interaction.guild.create_role(name="ticketacces")
        channel = await interaction.guild.create_text_channel(name=f"🎫{interaction.user.name}-Frage")
        await channel.set_permissions(interaction.guild.default_role, view_channel=False)
        await channel.set_permissions(interaction.user, view_channel=True, send_messages=True,
                                      read_message_history=True)
        try:
            await channel.set_permissions(role, view_channel=True, send_messages=True, read_message_history=True)
        except:
            await channel.send("Die Rolle 'ticket_admin' wurde nicht gefunden! Daher konnten die Rechte für den Kanal nicht vollständig verarbeitet werden. ")

        embedticketchannl = discord.Embed(title="Support Ticket",
                                          description=f"Willkommen bei Support! Das Team wird sich in Kürze um dich kümmern.\n**Benutzer:**{interaction.user.mention}\n**Betreff:** *Frage*",
                                          color=embedColor, timestamp=datetime.datetime.now())
        await channel.send("@here", embed=embedticketchannl, view=TicketChannelButtons())
        embedticketcreated = discord.Embed(title="Ticket erstellt",
                                           description=f"Dein Ticket wurde erstellt! {channel.mention}")
        await interaction.response.send_message(embed=embedticketcreated, ephemeral=True)
        category = discord.utils.get(interaction.guild.categories, name="🎫〢Tickets")
        try: 
            await channel.edit(category=category)
        except:
            await channel.send("Die Kategorie '🎫〢Tickets' wurde nicht gefunden! Daher konnte der Kanal nicht verschoben werden.")
            pass

    @discord.ui.button(label="Melden", custom_id="report_button", style=discord.ButtonStyle.red,
                       emoji="<:Ban:1102992708743729294>")
    async def report_button(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="ticket_admin")
        channel = await interaction.guild.create_text_channel(name=f"🎫{interaction.user.name}-report")
        await channel.set_permissions(interaction.guild.default_role, view_channel=False)
        await channel.set_permissions(interaction.user, view_channel=True, send_messages=True,
                                      read_message_history=True)
        try:
            await channel.set_permissions(role, view_channel=True, send_messages=True, read_message_history=True)
        except:
            await channel.send("Die Rolle 'ticket_admin' wurde nicht gefunden! Daher konnten die Rechte für den Kanal nicht vollständig verarbeitet werden. ")
        embedticketchannl = discord.Embed(title="Support Ticket",
                                          description=f"Willkommen bei Support! Das Team wird sich in Kürze um dich kümmern. \n**Benutzer:**{interaction.user.mention}\n **Betreff:** *Meldung*",
                                          color=embedColor, timestamp=datetime.datetime.now())
        embedticketcreated = discord.Embed(title="Ticket erstellt",
                                           description=f"Dein Ticket wurde erstellt! {channel.mention}")
        await channel.send("@here", embed=embedticketchannl, view=TicketChannelButtons())
        await interaction.response.send_message(embed=embedticketcreated, ephemeral=True)
        category = discord.utils.get(interaction.guild.categories, name="🎫〢Tickets")
        try: 
            await channel.edit(category=category)
        except:
            await channel.send("Die Kategorie '🎫〢Tickets' wurde nicht gefunden! Daher konnte der Kanal nicht verschoben werden.")
            pass

    @discord.ui.button(label="Team Bewerbung", custom_id="apply", style=discord.ButtonStyle.gray,
                       emoji="<:Team:1099009792942559282>")
    async def apply_button(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="ticket_admin")
        channel = await interaction.guild.create_text_channel(name=f"🎫{interaction.user.name}-t-bewerbung")
        await channel.set_permissions(interaction.guild.default_role, view_channel=False)
        await channel.set_permissions(interaction.user, view_channel=True, send_messages=True,
                                      read_message_history=True)
        try:
            await channel.set_permissions(role, view_channel=True, send_messages=True, read_message_history=True)
        except:
            await channel.send("Die Rolle 'ticket_admin' wurde nicht gefunden! Daher konnten die Rechte für den Kanal nicht vollständig verarbeitet werden. ")
        embedticketchannl = discord.Embed(title="Support Ticket",
                                          description=f"Willkommen bei Support! Das Team wird sich in Kürze um dich kümmern. \n**Benutzer:**{interaction.user.mention}\n **Betreff:** *Bewerbung*",
                                          color=embedColor, timestamp=datetime.datetime.now())
        embedticketcreated = discord.Embed(title="Ticket erstellt",
                                           description=f"Dein Ticket wurde erstellt! {channel.mention}")
        await channel.send("@here", embed=embedticketchannl, view=TicketChannelButtons())
        await interaction.response.send_message(embed=embedticketcreated, ephemeral=True)
        category = discord.utils.get(interaction.guild.categories, name="🎫〢Tickets")
        
        try: 
            await channel.edit(category=category)
        except:
            await channel.send("Die Kategorie '🎫〢Tickets' wurde nicht gefunden! Daher konnte der Kanal nicht verschoben werden.")
            pass

    @discord.ui.button(label="Partner Bewerbung", custom_id="papply", style=discord.ButtonStyle.gray,
                       emoji="<:icon_partner:1108822857372418148>")
    async def papply(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="ticket_admin")
        channel = await interaction.guild.create_text_channel(name=f"🎫{interaction.user.name}-p-bewerbung")
        await channel.set_permissions(interaction.guild.default_role, view_channel=False)
        await channel.set_permissions(interaction.user, view_channel=True, send_messages=True,
                                      read_message_history=True)
        try:
            await channel.set_permissions(role, view_channel=True, send_messages=True, read_message_history=True)
        except:
            await channel.send("Die Rolle 'ticket_admin' wurde nicht gefunden! Daher konnten die Rechte für den Kanal nicht vollständig verarbeitet werden. ")
        embedticketchannl = discord.Embed(title="Support Ticket",
                                          description=f"Willkommen bei Support! Das Team wird sich in Kürze um dich kümmern. \n**Benutzer:**{interaction.user.mention}\n **Betreff:** *Bewerbung*",
                                          color=embedColor, timestamp=datetime.datetime.now())
        embedticketcreated = discord.Embed(title="Ticket erstellt",
                                           description=f"Dein Ticket wurde erstellt! {channel.mention}")
        await channel.send("@here", embed=embedticketchannl, view=TicketChannelButtons())
        await interaction.response.send_message(embed=embedticketcreated, ephemeral=True)
        category = discord.utils.get(interaction.guild.categories, name="🎫〢Tickets")
        
        try: 
            await channel.edit(category=category)
        except:
            await channel.send("Die Kategorie '🎫〢Tickets' wurde nicht gefunden! Daher konnte der Kanal nicht verschoben werden.")
            pass

    @discord.ui.button(label="Entbannungs Antrag", custom_id="unban", style=discord.ButtonStyle.gray,
                       emoji="<:unban:1109061987197005864>")
    async def unban(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="ticket_admin")
        channel = await interaction.guild.create_text_channel(name=f"🎫{interaction.user.name}-unban")
        await channel.set_permissions(interaction.guild.default_role, view_channel=False)
        await channel.set_permissions(interaction.user, view_channel=True, send_messages=True,
                                      read_message_history=True)
        try:
            await channel.set_permissions(role, view_channel=True, send_messages=True, read_message_history=True)
        except:
            await channel.send("Die Rolle 'ticket_admin' wurde nicht gefunden! Daher konnten die Rechte für den Kanal nicht vollständig verarbeitet werden. ")
        embedticketchannl = discord.Embed(title="Support Ticket",
                                          description=f"Willkommen bei Support! Das Team wird sich in Kürze um dich kümmern. \n**Benutzer:**{interaction.user.mention}\n **Betreff:** *Unban*",
                                          color=embedColor, timestamp=datetime.datetime.now())
        embedticketcreated = discord.Embed(title="Ticket erstellt",
                                           description=f"Dein Ticket wurde erstellt! {channel.mention}")
        await channel.send("@here", embed=embedticketchannl, view=TicketChannelButtons())
        await interaction.response.send_message(embed=embedticketcreated, ephemeral=True)
        category = discord.utils.get(interaction.guild.categories, name="🎫〢Tickets")
        
        try: 
            await channel.edit(category=category)
        except:
            await channel.send("Die Kategorie '🎫〢Tickets' wurde nicht gefunden! Daher konnte der Kanal nicht verschoben werden.")
            pass

    @discord.ui.button(label="Bug Report", custom_id="breport", style=discord.ButtonStyle.gray,
                       emoji="<:unban:1109061987197005864>")
    async def breport(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="ticket_admin")
        channel = await interaction.guild.create_text_channel(name=f"🎫{interaction.user.name}-bug-report")
        await channel.set_permissions(interaction.guild.default_role, view_channel=False)
        await channel.set_permissions(interaction.user, view_channel=True, send_messages=True,
                                      read_message_history=True)
        try:
            await channel.set_permissions(role, view_channel=True, send_messages=True, read_message_history=True)
        except:
            await channel.send("Die Rolle 'ticket_admin' wurde nicht gefunden! Daher konnten die Rechte für den Kanal nicht vollständig verarbeitet werden. ")
        embedticketchannl = discord.Embed(title="Support Ticket",
                                          description=f"Willkommen bei Support! Das Team wird sich in Kürze um dich kümmern. \n**Benutzer:**{interaction.user.mention}\n **Betreff:** *Bug Report*",
                                          color=embedColor, timestamp=datetime.datetime.now())
        embedticketcreated = discord.Embed(title="Ticket erstellt",
                                           description=f"Dein Ticket wurde erstellt! {channel.mention}")
        await channel.send("@here", embed=embedticketchannl, view=TicketChannelButtons())
        await interaction.response.send_message(embed=embedticketcreated, ephemeral=True)
        category = discord.utils.get(interaction.guild.categories, name="🎫〢Tickets")
        
        try: 
            await channel.edit(category=category)
        except:
            await channel.send("Die Kategorie '🎫〢Tickets' wurde nicht gefunden! Daher konnte der Kanal nicht verschoben werden.")
            pass



@bot.tree.command(name="ticket_setup", description="Activate the ticket system.")
async def ticket_setup(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
            guild = interaction.guild
            role = discord.utils.get(guild.roles, name='ticket_admin')
            if role is None:
                role = await guild.create_role(name='ticket_admin')
                print("erstellt!")
            category = discord.utils.get(guild.categories, name='🎫〢Tickets')
            if category is None:
                category = await guild.create_category('🎫〢Tickets')
                print("erstellt!")
            embed_image = discord.Embed(title="", description="", color=embedColor)
            embed = discord.Embed(title="Ticket Support",
                                  description="Der Ticket Support ist die erste Anlaufstelle, wenn du Hilfe benötigst oder das Serverteam kontaktieren möchtest!",
                                  color=embedColor, timestamp=datetime.datetime.now())
            # Füge Felder hinzu
            embed.add_field(
                name="<:icon_chat:1108822865865867374> Support",
                value="Für einfache Fragen/Anliegen.",
                inline=False
            )

            embed.add_field(
                name="<:Ban:1102992708743729294> Meldung",
                value="Zum Melden von Nutzern/Bots.",
                inline=False
            )

            embed.add_field(
                name="<:Team:1099009792942559282> Bewerben",
                value="Für Teambewerbungen.",
                inline=False
            )

            embed.add_field(
                name="<:icon_partner:1108822857372418148>  Partner bewerben",
                value="Für Partner-Bewerbungen.",
                inline=False
            )

            embed.add_field(
                name="<:unban:1109061987197005864>: Entbannungs Antrag",
                value="Hier kannst du einen Entbannungsantrag stellen.",
                inline=False
            )

            embed.add_field(
                name="<a:robot_st:1114322038291714068> Bug Report",
                value="Hier kannst du einen Bug melden.",
                inline=False
            )
            embed.set_footer(text="Ticket System v2.3")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1118638876936900608/1119712415483953263/icon.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1118638876936900608/1119714475650584657/auto_faqw.png")
            embed_image.set_image(url="https://cdn.discordapp.com/attachments/1118638876936900608/1119712415832084611/banner_support.png") #ticket_icon

            embed2 = discord.Embed(title="Success", description="The ticket system has been set up successfully! \n"
                                                                f"The role {role.mention} has been created. All people who have this role will be able to see and respond to the tickets. It is recommended that all team members have this role! **The role must NOT be unnamed!**\n"
                                                                f"The category '{category.mention}' has been created! All open tickets will be created in this category. You can move the category at any time, but you cannot rename it. \n"
                                                                f"If you encounter any problems or something is not working, please contact support.",
                                   color=embedColor)
            embed2.set_author(name="Ticket Setup Assistant - Midnight Studio")
            await interaction.response.send_message(embed=embed2, ephemeral=True)
            await interaction.channel.send(embed=embed_image)
            await interaction.channel.send(embed=embed, view=TicketMenuButtons())
            await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False,
                                                      use_application_commands=False, read_message_history=True)

    else:
        await interaction.response.send_message("Du hast keine Erlaubnis, diesen Befehl zu nutzen!",
                                                ephemeral=True)
from discord.utils import format_dt

@bot.tree.command(name="timestamp_test")
@app_commands.describe(tfu = "Time in future")
async def timestamp(interaction: discord.Interaction, tfu: str):
    tfu = int(tfu)
    timestamp = datetime.datetime.utcnow() + datetime.timedelta(hours=tfu+2)# Example: 2 hours ago

    # Format the datetime object as a relative timestamp
    relative_time = format_dt(timestamp, style="R")
    await interaction.response.send_message(relative_time)



class ReportModal(ui.Modal, title="Report Menu"):
    user = ui.TextInput(label="Nutzer", placeholder="Wähle den Nutzer den du reporten möchtest.", style=discord.TextStyle.short)
    grund = ui.TextInput(label="Grund", placeholder="Gib den Grund deines Reports an.", style=discord.TextStyle.long)

    async def on_submit(self, interaction: discord.Interaction):
         role = discord.utils.get(interaction.guild.roles, name="『❓』 Supporter")
         role2 = discord.utils.get(interaction.guild.roles, name="『🔨』 Moderator")
         role4 = discord.utils.get(interaction.guild.roles, name="『🔨』 Moderator+")
         role3 = discord.utils.get(interaction.guild.roles, name="『🚨』 Admin")
         report_channel = bot.get_channel(974676724526743570)
         ebmed = discord.Embed(title=self.title, description=f"**{self.user.label}:** *{self.user}*\n**{self.grund.label}:** {self.grund}", timestamp=datetime.datetime.now(), color=embedColor)
         ebmed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
         ebmed.set_footer(text="Gemacht mit ❤️ von @einfxch_jonas")
         await interaction.response.send_message(embed=ebmed, ephemeral=True)
         await report_channel.send(f"{role.mention} {role2.mention} {role3.mention} {role4.mention}", embed=ebmed)

@bot.tree.command(name="report", description="Reporte Nutzer, Bots und bugs")
async def bugreport(interaction: discord.Interaction):

    await interaction.response.send_modal(ReportModal())


class feedbackModal(ui.Modal, title="Entbannungsantrag"):
	grund  = ui.TextInput(label="Grund", placeholder="Warumm wurdest du gebannt?", style=discord.TextStyle.short, max_length=30)
	lektion = ui.TextInput(label="Lektion", placeholder="Hast du eine Lektion gelernt? Wenn ja, welche?", style=discord.TextStyle.long, min_length=60)
	async def on_submit(self, interaction: discord.Interaction):
         report_channel = bot.get_channel(1059141981911134339)
         ebmed = discord.Embed(title=self.title, description=f"**Nutzer:** *{interaction.user.mention}*\n**{self.grund.label}:** *{self.grund}*\n**{self.lektion.label}:** *{self.lektion}*", timestamp=datetime.datetime.now(), color=embedColor)
         ebmed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
         await interaction.response.send_message(embed=ebmed, ephemeral=True)
         await report_channel.send(embed=ebmed)

@bot.tree.command(name="entbannungsantrag", description="Sende einen Entbannungs Antrag an das Team.")
async def entbannungsantrag(interaction: discord.Interaction):
    await interaction.response.send_modal(feedbackModal())



bot.run("MTExMjEzMjIyNDUyMzk2MDMyMA.GCbAjV.O-IJfKst4cLxWCh8sUzj37iR6ULUVxI1ekInEI")
