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
                await reply.edit(f'`ā­āāāš„ šš„š”š¤šššš£š ššššš¤šØāāāā®\nāšš§š¤šš§ššØšØ š -ć {perc} ć\nāšš„ššš š¦¾ -ć {sp} ć\nāšš¤šššš āļø -ć {cur} ć\nāšššÆš š -ć {tot} ć\n----ššššš ššš š½šš š¤----`')
               
            except FloodWait as e:
                time.sleep(e.x)
