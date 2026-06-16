# entities.py
class Employee:
    def __init__(self, name, hp, sp, work_speed):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_sp = sp
        self.sp = sp
        self.work_speed = work_speed  # โอกาสสำเร็จในการทำงาน (0.0 - 1.0)

class Abnormality:
    def __init__(self, id, name, risk_level, max_counter):
        self.id = id
        self.name = name
        self.risk_level = risk_level  # ZAYIN, TETH, HE, WAW, ALEPH
        self.max_counter = max_counter
        self.qliphoth_counter = max_counter  # เกจเตือนภัยก่อนหลุด