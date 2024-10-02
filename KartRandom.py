import discord
import random
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

# Discord 봇 설정
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
slash = SlashCommand(bot, sync_commands=True)

# 35개의 요소가 있는 리스트
text_list = [
    "빌리지 고가의 질주", "포레스트 지그재그", "차이나 서안 병마용", "해적 해적들의 수로", "공동묘지 해골손가락",
    "아이스 갈라진 빙산", "사막 피라미드 탐험", "포레스트 지그재그", "빌리지 수로", "사막 모래구덩이",
    "아이스 하프파이프", "차이나 북경 스포츠공원", "[리버스] 차이나 북경 자금성", "공동묘지 비밀의 수도원", "포레스트 버섯동굴",
    "빌리지 시계탑", "사막 스핑크스 수수께끼", "사막 오아시스"
]

# 슬래시 명령어 등록
@slash.slash(name="Club_Random", description="클럽 대항전 랜덤")
async def show_random_list(ctx: SlashContext):
    # 리스트에서 중복되지 않게 8개의 요소를 랜덤으로 선택
    random_sample = random.sample(text_list, 8)
    
    # 선택된 요소를 하나의 문자열로 병합
    output = "\n".join(random_sample)
    
    # 임베드 객체 생성
    embed = discord.Embed(
        description=output,  # 선택된 텍스트를 설명에 넣음
        color=discord.Color.blue()  # 임베드 색상 설정
    )
    
    # 이미지 추가 (원하는 이미지 URL로 변경 가능)
    embed.set_image(url="https://raw.githubusercontent.com/Hyun-Manda/KartRandom/refs/heads/main/TestIMG.png")
    
    # 바닥글 추가
    embed.set_footer(text="K A R T R I D E R - S U P E R R U S H")
    
    # 메시지 응답
    await ctx.send(embed=embed)

# 봇 실행
bot.run("YOUR_BOT_TOKEN")
