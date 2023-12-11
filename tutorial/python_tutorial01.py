### print() ใช้สำหรับแสดงผลลัพธ์บนหน้าจอ ไวยากรณ์ของคำสั่ง print()
print("Hello World")
print("Hello, world!")

### input() ใช้สำหรับรับข้อมูลจากผู้ใช้
name = input("ชื่อของคุณคืออะไร: ")
print("สวัสดี", name)

### type() ใช้สำหรับตรวจสอบชนิดข้อมูลของตัวแปร
name = "Bard"
TypeName = type(name)
print(TypeName)








### ภาษา Python มีตัวเลขอยู่ 2 ชนิด คือ
    #  ตัวเลขจำนวนเต็ม (Integer)    เช่น 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    #  ตัวเลขทศนิยม (Float)        เช่น 1.0, 2.5, 3.14, 4.2, 5.3, 6.4, 7.5, 8.6, 9.7








### ภาษา Python มีคำสั่งคณิตศาสตร์พื้นฐานอยู่หลายคำสั่ง ดังนี้
    # การบวก (+)
    # การลบ (-)
    # การคูณ (*)
    # การหาร (/)
    # การยกกำลัง (**)
    # การหารแบบเศษส่วน (//)
    # การเหลือจากการหาร (%)
# a = 1
# b = 2
# c = a + b       # d = a - b       # e = a * b         # f = a / b         # g = a ** b           # h = a // b         # i = a % b
# print(c)        # print(d)        # print(e)          # print(f)          # print(g)             # print(h)           # print(i)
# 3               # -1              # 2                 # 0.5               # 1                    # 0                  # 1








### ภาษา Python มีคำสั่งตรรกะพื้นฐานอยู่หลายคำสั่ง ดังนี้
    # เท่ากับ (==)
    # ไม่เท่ากับ (!=)
    # มากกว่า (>)
    # น้อยกว่า (<)
    # มากกว่าหรือเท่ากับ (>=)
    # น้อยกว่าหรือเท่ากับ (<=)
# a = 1
# b = 2
# c = a == b        # d = a != b        # e = a > b         # f = a < b         # g = a >= b        # h = a <= b
# print(c)          # print(d)          # print(e)          # print(f)          # print(g)          # print(h)
# False             # True              # False             # True              # False             # True








### คำสั่งเงื่อนไขในภาษา Python มี 2 คำสั่งหลัก คือ
    # if...else
    # elif

##  if...else ใช้สำหรับตรวจสอบเงื่อนไขและดำเนินการตามเงื่อนไขที่กำหนด
age = 20
if age >= 18:
  print("คุณอายุเกิน 18 ปี")
else:
  print("คุณอายุไม่ถึง 18 ปี")
# = คุณอายุเกิน 18 ปี

## elif เป็นคำสั่งเงื่อนไขเพิ่มเติมที่สามารถใช้ร่วมกับคำสั่ง if...else ได้ คำสั่ง elif ใช้สำหรับตรวจสอบเงื่อนไขเพิ่มเติมในกรณีที่เงื่อนไขในคำสั่ง if ไม่เป็นจริง
# if     
    #เงื่อนไข1                        # ดำเนินการหากเงื่อนไข1 เป็นจริง
# elif
    #เงื่อนไข2                        # ดำเนินการหากเงื่อนไข1 เป็นเท็จและเงื่อนไข2 เป็นจริง
# else              
    #ดำเนินการหากเงื่อนไขเป็นเท็จ        # ดำเนินการหากเงื่อนไข1 และเงื่อนไข2 เป็นเท็จ
number = 80
if number >= 90:
  print("คะแนน A")
elif number >= 80:
  print("คะแนน B")
else:
  print("คะแนน C")
# = คะแนน B








### คำสั่งวนซ้ำในภาษา Python มี 2 คำสั่งหลัก คือ
    # for
    # while

## for ใช้สำหรับวนซ้ำตามลำดับของข้อมูลในลำดับข้อมูล
# ตัวเลขจาก 1 ถึง 10 ตัวแปร ตัวเลข จะเก็บค่าตัวเลขในแต่ละรอบของการวนซ้ำ โปรแกรมจะแสดงค่าของตัวแปร ตัวเลข ในแต่ละรอบของการวนซ้ำ
# for ตัวแปร in ลำดับข้อมูล:
  # ดำเนินการซ้ำๆ
# number 1 ถึง 10:
#   print(number)

## while ใช้สำหรับวนซ้ำจนกว่าเงื่อนไขจะไม่เป็นจริง
# while เงื่อนไข:
  # ดำเนินการซ้ำๆ
#   ตัวเลข = 1
# while ตัวเลข <= 10:
#   print(ตัวเลข)
#   ตัวเลข += 1








### คำสั่งฟังก์ชัน ในภาษา Python ใช้สำหรับรวบรวมชุดคำสั่งไว้ด้วยกันเพื่อใช้งานซ้ำๆ
# def ชื่อฟังก์ชัน(อาร์กิวเมนต์):
   # บล็อกคำสั่งของฟังก์ชัน
#   return ค่าส่งคืน
def บวกสองจำนวน(จำนวน1, จำนวน2):
  """
  ฟังก์ชันสำหรับบวกสองจำนวน

  อาร์กิวเมนต์:
    จำนวน1: จำนวนแรก
    จำนวน2: จำนวนที่สอง

  ค่าส่งคืน:
    ผลบวกของจำนวน1 และจำนวน2
  """

  ผลบวก = จำนวน1 + จำนวน2
  return ผลบวก

ผลบวก = บวกสองจำนวน(10, 20)
print(ผลบวก)











### คำสั่งการจัดการไฟล์และไดเรกทอรี
# ใช้สำหรับจัดการไฟล์และไดเรกทอรีในระบบไฟล์ คำสั่งเหล่านี้สามารถช่วยให้เราสร้าง ลบ แก้ไข ย้าย คัดลอก แสดงรายการ และค้นหาไฟล์และไดเรกทอรีได้อย่างสะดวก
# [คำสั่ง]	                    [รายละเอียด]	                             [ตัวอย่างการใช้งาน]
# os.getcwd()             แสดงที่อยู่ของไดเรกทอรีปัจจุบัน	                    print(os.getcwd())
# os.chdir()	          เปลี่ยนไดเรกทอรีปัจจุบัน	                           os.chdir("C:\\Users\\Bard\\Desktop")
# os.listdir()	          แสดงรายการไฟล์และไดเรกทอรีในไดเรกทอรีที่กำหนด	      print(os.listdir("C:\\Users\\Bard\\Desktop"))
# os.path.exists()	      ตรวจสอบว่าไฟล์หรือไดเรกทอรีมีอยู่หรือไม่	              print(os.path.exists("C:\\Users\\Bard\\Desktop\\test.txt"))
# os.path.join()	      รวมเส้นทางของไดเรกทอรีและไฟล์	                    print(os.path.join("C:\\Users\\Bard\\Desktop", "test.txt"))
# os.path.split()	      แยกเส้นทางของไดเรกทอรีและไฟล์ออกจากกัน	        print(os.path.split("C:\\Users\\Bard\\Desktop\\test.txt"))
# os.path.basename()	  แสดงชื่อไฟล์จากเส้นทาง	                        print(os.path.basename("C:\\Users\\Bard\\Desktop\\test.txt"))
# os.path.dirname()	      แสดงไดเรกทอรีจากเส้นทาง	                       print(os.path.dirname("C:\\Users\\Bard\\Desktop\\test.txt"))
# os.path.getsize()	      แสดงขนาดของไฟล์	                             print(os.path.getsize("C:\\Users\\Bard\\Desktop\\test.txt"))
# os.path.isfile()	      ตรวจสอบว่าไฟล์เป็นไฟล์หรือไม่	                      print(os.path.isfile("C:\\Users\\Bard\\Desktop\\test.txt"))
# os.path.isdir()	      ตรวจสอบว่าไดเรกทอรีเป็นไดเรกทอรีหรือไม่	           print(os.path.isdir("C:\\Users\\Bard\\Desktop"))
# os.path.splitext()	  แยกนามสกุลไฟล์ออกจากชื่อไฟล์	                    print(os.path.splitext("C:\\Users\\Bard\\Desktop\\test.txt"))
# os.rename()	          เปลี่ยนชื่อไฟล์หรือไดเรกทอรี                         os.rename("C:\\Users\\Bard\\Desktop\\test.txt", "C:\\Users\\Bard\\Desktop\\new_test.txt")
# os.remove()	          ลบไฟล์                                         os.remove("C:\\Users\\Bard\\Desktop\\new_test.txt")
# os.mkdir()	          สร้างไดเรกทอรี                                   os.mkdir("C:\\Users\\Bard\\Desktop\\new_dir")
# os.rmdir()	          ลบไดเรกทอรี	                                 os.rmdir("C:\\Users\\Bard\\Desktop\\new_dir")
# open()	              เปิดไฟล์	                                      f = open("C:\\Users\\Bard\\Desktop\\test.txt", "r")
# read()	              อ่านข้อมูลจากไฟล์	                               data = f.read()
# write()	              เขียนข้อมูลลงในไฟล์                              f.write("Hello, world!")
# close()	              ปิดไฟล์                                        f.close()