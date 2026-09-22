"""This is a main entry for the whoele delphi program."""

from dotenv import dotenv_values, load_dotenv

from discord import ApplicationContext, Bot, Intents
import dotenv

intents: Intents = Intents.default()
intents.members = True


bot = Bot(intents=intents)


@bot.slash_command(name="hello")
async def hello(ctx: ApplicationContext) -> None:
    """Basic stuff"""
    await ctx.respond(f"Hello {ctx.author}!!!")


env_variables: dict[str, str | None] = dotenv_values()
bot.run(env_variables.get("DISCORD_TOKEN"))

if __name__ == "__main__":
    pass
