import time
import math
import os
from Easy_F import hrb,hrt
from pyrogram.errors import FloodWait

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

timer = Timer()
async def progress_bar(current,total,reply,start):
      if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            sp=str(hrb(speed))+"ps"
            tot=hrb(total)
            cur=hrb(current)
            try:
                await reply.edit(f'`╭──⌈📥 𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙑𝙞𝙙𝙚𝙤𝙨⌋──╮\n├𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨 📈 -【 {perc} 】\n├𝙎𝙥𝙚𝙚𝙙 🦾 -【 {sp} 】\n├𝙇𝙤𝙖𝙙𝙚𝙙 ⚙️ -【 {cur} 】\n├𝙎𝙞𝙯𝙚 📂 -【 {tot} 】\n----𝙍𝙊𝙇𝙀𝙓 𝙎𝙄𝙍 𝘽𝙊𝙏 🤖----`')
               
            except FloodWait as e:
                time.sleep(e.x)
