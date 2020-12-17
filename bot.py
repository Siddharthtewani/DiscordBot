import discord
from discord.ext import commands

client = commands.Bot(command_prefix="#")

f = open("rules.txt","r")
rules=f.readlines()
filtered_word=["cat","dog","tushar","love","relationship","crush"]

@client.event
async def on_ready():
    print("Bot is ready")
    
@client.event
async def on_message(msg):
    for word in filtered_word:
        if word in msg.content:
            await msg.delete()
    await client.process_commands(msg)

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You cant do that ;-;")
        await ctx.message.delete() 

    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please enter all the req arguments ;-;")
        await ctx.message.delete() 
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("Command Not Found   ; - ;")
        await ctx.message.delete()     
    else :
        raise error


@client.command(aliases=["rules","instn"])
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)+1])



@client.command()
async def tushar_manvi(ctx):
    await ctx.send("Mushu chee cheee")

@client.command()
async def vaibhav_lisha(ctx):
    await ctx.send("Vaishya hmmmmmm")    

##          Deleting Messages

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)



##       Banning a Member

@client.command(aliases=["b"])
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member,*,reason="Reason not given"):
    
    
    await ctx.send("You have been banned becoz "+ reason)
    await member.ban(reason=reason)


##       Kicking a Member

@client.command(aliases=["k"])
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,reason="Reason not given"):
    try:
        await member.send("You have been kicked becoz "+ reason)
    except:
        await ctx.send("Their dms are off")

    await member.kick(reason=reason)



##   Unbanning a Member

@client.command(aliases=["ub"])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_members=await ctx.guild.bans()
    ban_name,ban_desc=member.split("#")

    for banned_user in banned_members:
        user=banned_user

        if((user.name,user.descriminator==(ban_name,ban_desc))):
            await ctx.guild.unban(user)
            await ctx(user.name+" has been unbanned")
            return

        await ctx.send("Member not Found")


##            Muting someone
@client.command(aliases=["m"])
@commands.has_permissions(kick_members=True)
async def mute(ctx,member:discord.Member):
    muted_role = ctx.guild.get_role(788279972660772875)
    await member.add_roles(muted_role)
    await ctx.send(member.mention +"Muted")


##            UnMuting someone
@client.command(aliases=["um"])
@commands.has_permissions(kick_members=True)


async def unmute(ctx,member:discord.Member):
    muted_role = ctx.guild.get_role(788279972660772875)
    await member.remove_roles(muted_role)
    await ctx.send(member.mention +"UnnMuted")


##              Embed


@client.command(aliases=["user","info"])
@commands.has_permissions(kick_members=True)
async def whois(ctx,member:discord.Member):
    members_list=[]
    for i in range(0,len(member.roles)): 
        await ctx.send(member.roles[i])
        # members_list.append(member.roles[0])
    embed=discord.Embed(title=member.name,description=member.mention,color=discord.Color.red())
    embed.add_field(name="Roles",value=member.roles,inline=False)
    embed.set_thumbnail(url=member.avatar_url)

    for i in range(0,len(member.roles)-1):    
        await ctx.send(members_list[i])



@client.command()
async def emoji(ctx):
    await ctx.send("❤️‍🔥")

client.run("Nzg3OTE4ODEzMTg1NzAzOTc2.X9b8kw.0TESoIve4pMu8PPljtffIKcPz9Y")