import yfinance as yf
import discord
import asyncio

client=discord.Client()
@client.event

async def on_message(message):
    stonk = ''
    cur = 0
    comm = ''
    messageContent = message.content
    if messageContent[0] == '$':
        if messageContent == '$love':
            async with message.channel.typing():
                await asyncio.sleep(1)
            await message.channel.send("STONKY LOVES THE STONKS")
        if messageContent == '$help':
            async with message.channel.typing():
                await asyncio.sleep(2)
            await message.channel.send("***Stonky gonna help!***")
            async with message.channel.typing():
                await asyncio.sleep(1)
                await message.channel.send("***$<ticker> gen-*** Gives general info pertaining to stock.")
                await message.channel.send("***$<ticker> hilo-*** Gives the highs and lows of requested stock.")
                await message.channel.send("***$<ticker> volume-*** Gives info on volume of a stock.")
                await message.channel.send("***$love-*** You know what Stonky loves.")
        if 'gen' in messageContent or  'hilo' in messageContent or 'volume' in messageContent and message.author.id != 809709845917335603:
            async with message.channel.typing():
                await asyncio.sleep(2)
            await message.channel.send("**Stonky getting info, please wait!**")
            async with message.channel.typing():
                space = messageContent.find(' ')
                stonk = messageContent[1:space]
                comm = messageContent[space+1:]
                ticker = yf.Ticker(stonk)
                tickerinf = ticker.info
                if comm =='gen':
                    ask = tickerinf['ask']
                    bid = tickerinf['bid']
                    prevClose = tickerinf['previousClose']
                    marketCap = tickerinf['marketCap']
                    name = tickerinf['shortName']
                    regPrice = tickerinf['regularMarketPrice']
                    await message.channel.send('Company Name: ${}'.format(name))
                    await message.channel.send('Previous Close: ${}'.format(prevClose))
                    await message.channel.send('Market Cap: ${}'.format(marketCap))

                    if ask == 0 or ask == 'None':
                        await message.channel.send('No ask retreived.')
                    else:
                        await message.channel.send('Ask: ${}'.format(ask))
                    if bid == 0 or bid == 'None':
                        await message.channel.send('No bid retreived.')
                    else:
                        await message.channel.send('Bid: ${}'.format(bid))
                    await message.channel.send('Regular Market Price: ${}'.format(regPrice))
                if comm == 'hilo':
                    name = tickerinf['shortName']
                    high52 = tickerinf['fiftyTwoWeekHigh']
                    low52 = tickerinf['fiftyTwoWeekLow']
                    dayLow = tickerinf['dayLow']
                    dayHigh = tickerinf['dayHigh']
                    regDayLow = tickerinf['regularMarketDayLow']
                    regDayHigh = tickerinf['regularMarketDayHigh']
                    await message.channel.send('Company Name: ${}'.format(name))
                    await message.channel.send('52 Week High: ${}'.format(high52))
                    await message.channel.send('52 Week Low: ${}'.format(low52))
                    await message.channel.send('Day Low: ${}'.format(dayLow))
                    await message.channel.send('Day High: ${}'.format(dayHigh))
                    await message.channel.send('Regular Day Low: ${}'.format(regDayLow))
                    await message.channel.send('Regular Day High: ${}'.format(regDayHigh))
                
                if comm == 'volume':
                    name = tickerinf['shortName']
                    avgVol10 = tickerinf['averageVolume10days']
                    avgDailyVol10 = tickerinf['averageDailyVolume10Day']
                    avgVol = tickerinf['averageVolume']
                    volume = tickerinf['volume']
                    await message.channel.send('Company Name: ${}'.format(name))
                    await message.channel.send('Average 10 Day Volume: ${}'.format(avgVol10))
                    await message.channel.send('Average Daily 10 Day Volume: ${}'.format(avgDailyVol10))
                    await message.channel.send('Average Volume: ${}'.format(avgVol))




        

client.run('')

