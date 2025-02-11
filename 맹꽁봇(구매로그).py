import discord
from discord import app_commands

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# 특정 채널 ID 설정
TARGET_CHANNEL_ID = 1300073798564974632  # 여기에 원하는 채널 ID 입력

# 상품 선택지 목록
상품_선택지 = [
    app_commands.Choice(name="신분증", value="신분증"),
    app_commands.Choice(name="중꽁업자", value="중꽁업자"),
    app_commands.Choice(name="기초컨설팅", value="기초컨설팅"),
    app_commands.Choice(name="고급컨설팅", value="고급컨설팅"),
    app_commands.Choice(name="중복비법", value="중복비법"),
    app_commands.Choice(name="new업자", value="new업자")
]

@bot.event
async def on_ready():
    await tree.sync()  # 슬래시 명령어 동기화
    print(f"✅ {bot.user} 봇이 온라인입니다!")

@tree.command(name="구매완료", description="구매 완료 로그를 남깁니다.")
@app_commands.describe(상품="구매한 상품을 선택하세요.", 사용자="구매한 사용자")
@app_commands.choices(상품=상품_선택지)
async def 구매완료(interaction: discord.Interaction, 상품: str, 사용자: discord.Member):
    채널 = bot.get_channel(TARGET_CHANNEL_ID)
    if 채널:
        embed = discord.Embed(
            description=f"{사용자.mention}님께서 **{상품}**(을)를 구매해주셨습니다.",
            color=0x5865F2
        )
        embed.set_author(name="🛒 구매로그")
        embed.set_footer(text=f"CSO DATA VENDING • {interaction.created_at.strftime('%Y-%m-%d %p %I:%M')}")
        
        await 채널.send(embed=embed)
        await interaction.response.send_message(f"✅ {상품} 구매 메시지를 {채널.mention}에 보냈습니다!", ephemeral=True)
    else:
        await interaction.response.send_message("❌ 채널을 찾을 수 없습니다. 관리자에게 문의하세요.", ephemeral=True)

# 봇 실행 (토큰 입력 필요)
bot.run("MTMzNzY0OTUzOTg4ODE4NTM3NQ.Gs3gZI.H-CdXF2oV_4d6xvUwUvk77r6GSDU62IFPKltAs")
