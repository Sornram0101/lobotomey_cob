# game_manager.py
import random

class GameManager:
    def __init__(self):
        self.day = 1
        self.current_energy = 0
        self.target_energy = 30  # เป้าหมายพลังงานเพื่อผ่านวัน
        self.game_over = False

    def execute_work(self, employee, abnormality):
        print(f"\n[!] {employee.name} กำลังเริ่มทำงานกับ {abnormality.name}...")
        
        # คำนวณผลสำเร็จด้วยระบบสุ่ม (RNG)
        success = random.random() < employee.work_speed
        
        if success:
            self.current_energy += 10
            employee.sp -= 2  # ทำงานสำเร็จแต่เสียสุขภาพจิตเล็กน้อย
            print(f"🎉 สำเร็จ! ได้รับพลังงาน (+10 Energy)")
            print(f"📊 พลังงานปัจจุบัน: {self.current_energy}/{self.target_energy}")
            print(f"🧠 {employee.name} เสียสติเล็กน้อย SP คงเหลือ: {employee.sp}/{employee.max_sp}")
        else:
            employee.hp -= 15  # ทำงานพลาด โดนโจมตี
            abnormality.qliphoth_counter -= 1
            print(f"💥 ล้มเหลว! มอนสเตอร์เกิดคุ้มคลั่ง โจมตีพนักงาน!")
            print(f"🩸 {employee.name} HP ลดลงเหลือ: {employee.hp}/{employee.max_hp}")
            print(f"🚨 {abnormality.name} เกจ Qliphoth Counter ลดลงเหลือ: {abnormality.qliphoth_counter}")
            
            if abnormality.qliphoth_counter <= 0:
                print(f"\n🚨🚨🚨 [วิกฤต] {abnormality.name} หลุดออกจากห้องกักกันแล้ว!! 🚨🚨🚨")
                self.game_over = True

        # เช็คสถานะพนักงานตาย
        if employee.hp <= 0 or employee.sp <= 0:
            print(f"💀 พนักงาน {employee.name} เสียชีวิตในหน้าที่...")
            self.game_over = True