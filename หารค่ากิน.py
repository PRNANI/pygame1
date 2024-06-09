import tkinter as tk

def calculate_bill_split():
    try:
        num_people = int(num_people_entry.get())
        total_bill = float(total_bill_entry.get())

        if num_people <= 0 or total_bill <= 0:
            result_label.config(text="กรุณากรอกจำนวนคนและค่าอาหารที่มากกว่าศูนย์")
            return

        each_person_share = total_bill / num_people
        result_label.config(text=f"ค่าอาหารแต่ละคนคือ: {each_person_share:.2f} บาท")
    except ValueError:
        result_label.config(text="โปรดกรอกจำนวนคนและค่าอาหารที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณค่าอาหาร")

# สร้างแท็บเพื่อเก็บข้อมูล
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# สร้างแท็บเพื่อกรอกจำนวนคน
num_people_label = tk.Label(input_frame, text="จำนวนคน: ")
num_people_label.grid(row=0, column=0)

num_people_entry = tk.Entry(input_frame)
num_people_entry.grid(row=0, column=1)

# สร้างแท็บเพื่อกรอกค่าอาหารทั้งหมด
total_bill_label = tk.Label(input_frame, text="ค่าอาหารทั้งหมด: ")
total_bill_label.grid(row=1, column=0)

total_bill_entry = tk.Entry(input_frame)
total_bill_entry.grid(row=1, column=1)

# สร้างปุ่มเพื่อคำนวณ
calculate_button = tk.Button(root, text="คำนวณ", command=calculate_bill_split)
calculate_button.pack(pady=10)

# สร้างป้ายแสดงผลลัพธ์
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
