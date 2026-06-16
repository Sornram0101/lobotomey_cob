# main.py
import sys
from entities import Employee
from data_loader import load_monsters
from game_manager import GameManager

def main():
    print("====================================")
    print("WELCOME TO LOBOTOMY SCRIPT CORP")
    print("====================================")
    
    # เจนข้อมูลเริ่มต้น
    manager = GameManager()
    monsters = load_monsters()
    
    # สร้างพนักงานเริ่มต้น 1 คน (ชื่อ John, HP 50, SP 50, โอกาสสำเร็จ 70%)
    player_employee = Employee("John", 50, 50, 0.7)
    
    # เลือกมอนสเตอร์ตัวแรกในลิสต์มาเล่นก่อน
    current_monster = monsters[0]
    
    # ลูปหลักของเกม (Game Loop)
    while not manager.game_over:
        print(f"\n--- วันที่ {manager.day} ---")
        print(f"เป้าหมายพลังงาน: {manager.current_energy} / {manager.target_energy}")
        print(f"พนักงานประจำการ: {player_employee.name} (HP: {player_employee.hp}, SP: {player_employee.sp})")
        print(f"ห้องกักกันมอนสเตอร์: {current_monster.name} [{current_monster.risk_level}] (Counter: {current_monster.qliphoth_counter})")
        
        print("\n[1] ส่งพนักงานเข้าไปทำงาน")
        print("[2] ตรวจสอบสถานะหน่วยงาน")
        print("[3] ปิดบริษัท (ออกจากเกม)")
        
        choice = input("\nเลือกคำสั่ง (1-3): ")
        
        if choice == "1":
            manager.execute_work(player_employee, current_monster)
            
            # เช็คเงื่อนไขชนะผ่านวัน
            if manager.current_energy >= manager.target_energy:
                print(f"\n✨ ยินดีด้วย! คุณเก็บพลังงานครบตามเป้าหมายของวันที่ {manager.day} แล้ว! ✨")
                print("กำลังเข้าสู่ขั้นตอนการบันทึกงาน...")
                sys.exit()
                
        elif choice == "2":
            print(f"\n--- ข้อมูลพนักงาน ---")
            print(f"ชื่อ: {player_employee.name} | โอกาสงานสำเร็จ: {player_employee.work_speed * 100}%")
            print(f"ความทนทานร่าง: {player_employee.hp} | ความทนทานจิต: {player_employee.sp}")
        elif choice == "3":
            print("\nปิดระบบ... ลาซ่อนก่อนผู้จัดการ")
            break
        else:
            print("\n[!] คำสั่งไม่ถูกต้อง กรุณาเลือกใหม่")
            
    if manager.game_over:
        print("\n====================================")
        print("          !!! GAME OVER !!!         ")
        print("    บริษัทล่มสลายเนื่องจากควบคุมภัยพิบัติไม่ได้  ")
        print("====================================")

if __name__ == "__main__":
    main()