import os
import discord
from discord.ext import commands
from discord import app_commands
import datetime

# =========================
# CONFIG
# =========================
TOKEN = os.getenv("MTQ2NDIwNjk0MTYyMTMyNTgzNg.GHHZcM.MJayriQn_CkAM8lNJB6G-2e2yr15B6f4G4TaTE")

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced")

bot = MyBot()

# =========================
# EVENTS
# =========================
@bot.event
async def on_ready():
    print(f"System Ready: {bot.user}")

# =========================
# PING
# =========================
@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(bot.latency*1000)}ms")

@bot.tree.command(name="ping", description="เช็คความหน่วงบอท")
async def ping_slash(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🏓 Pong! {round(bot.latency*1000)}ms",
        ephemeral=True
    )

# =========================
# SAY
# =========================
@bot.command()
async def say(ctx, *, text: str):
    await ctx.send(text)

@bot.tree.command(name="say", description="ให้บอทพูดแทน")
async def say_slash(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text)

# =========================
# HELP
# =========================
@bot.command()
async def help(ctx):
    await ctx.send(
        "📖 คำสั่ง: ping, say, info, server, user, time, avatar, clear, invite, status, echo"
    )

@bot.tree.command(name="help", description="แสดงคำสั่งทั้งหมด")
async def help_slash(interaction: discord.Interaction):
    await interaction.response.send_message(
        "📖 คำสั่ง: ping, say, info, server, user, time, avatar, clear, invite, status, echo",
        ephemeral=True
    )

# =========================
# INFO
# =========================
@bot.command()
async def info(ctx):
    await ctx.send(f"🤖 {bot.user} | Latency {round(bot.latency*1000)}ms")

@bot.tree.command(name="info", description="ข้อมูลบอท")
async def info_slash(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🤖 {bot.user} | Latency {round(bot.latency*1000)}ms",
        ephemeral=True
    )

# =========================
# SERVER
# =========================
@bot.command()
async def server(ctx):
    g = ctx.guild
    await ctx.send(f"🏠 {g.name} | Members {g.member_count}")

@bot.tree.command(name="server", description="ข้อมูลเซิร์ฟเวอร์")
async def server_slash(interaction: discord.Interaction):
    g = interaction.guild
    await interaction.response.send_message(
        f"🏠 {g.name} | Members {g.member_count}",
        ephemeral=True
    )

# =========================
# USER
# =========================
@bot.command()
async def user(ctx, member: discord.Member = None):
    m = member or ctx.author
    await ctx.send(f"👤 {m} | ID {m.id}")

@bot.tree.command(name="user", description="ดูข้อมูลผู้ใช้")
async def user_slash(interaction: discord.Interaction, member: discord.Member = None):
    m = member or interaction.user
    await interaction.response.send_message(
        f"👤 {m} | ID {m.id}",
        ephemeral=True
    )

# =========================
# TIME
# =========================
@bot.command()
async def time(ctx):
    await ctx.send(f"🕒 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

@bot.tree.command(name="time", description="เวลาปัจจุบัน")
async def time_slash(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🕒 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        ephemeral=True
    )

# =========================
# AVATAR
# =========================
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    m = member or ctx.author
    await ctx.send(m.display_avatar.url)

@bot.tree.command(name="avatar", description="ดูรูปโปรไฟล์")
async def avatar_slash(interaction: discord.Interaction, member: discord.Member = None):
    m = member or interaction.user
    await interaction.response.send_message(m.display_avatar.url, ephemeral=True)

# =========================
# CLEAR (ADMIN)
# =========================
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

@bot.tree.command(name="clear", description="ลบข้อความ")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear_slash(interaction: discord.Interaction, amount: int):
    await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(
        f"🧹 ลบ {amount} ข้อความแล้ว",
        ephemeral=True
    )

# =========================
# INVITE
# =========================
@bot.command()
async def invite(ctx):
    await ctx.send("🔗 ใส่ลิงก์เชิญบอทของคุณตรงนี้")

@bot.tree.command(name="invite", description="ลิงก์เชิญบอท")
async def invite_slash(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🔗 ใส่ลิงก์เชิญบอทของคุณตรงนี้",
        ephemeral=True
    )

# =========================
# STATUS
# =========================
@bot.command()
async def status(ctx):
    await ctx.send("✅ Bot is online")

@bot.tree.command(name="status", description="สถานะบอท")
async def status_slash(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Bot is online", ephemeral=True)

# =========================
# ECHO
# =========================
@bot.command()
async def echo(ctx, *, text: str):
    await ctx.send(text)

@bot.tree.command(name="echo", description="พูดซ้ำ")
async def echo_slash(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text)

# =========================
# RUN
# =========================
if __name__ == "__main__":
    bot.run(TOKEN)
