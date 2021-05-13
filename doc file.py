import json
import student
import os

def openFile():
    f = input('Nhap ten file: ')
    if f in os.listdir():
        a = f.split('.') 
        if a[1] == 'txt':
            return docFileTxt(f)
        elif a[1] == 'json':
            return docFileJson(f)
    else:
        return False

# ham doc file json
def docFileJson(f): 
    print(f'Da mo file {f}')
    with open('sinhvien.json') as wr:
        listStudents = json.load(wr)
    return listStudents


# ham doc file text
def docFileTxt(f):
    print(f'Da mo file {f}')
    lis=[]
    with open(f, encoding='utf-8') as wr:
        text = wr.readline()
        while text:
            lis.append(text)
            text = wr.readline()
    listStudents = []
    for i in lis:
        a = i.split()
        infor = {
            'id' : '',
            'name' : '',
            'Diem toan': '',
            'Diem ly': '',
            'Diem hoa': '',
            'Diem TB': '',
            'Phan loai': ''
        }
        infor['id'] = str(a[0])
        infor['name'] = a[1]
        infor['Diem toan'] = float(a[2])
        infor['Diem ly'] = float(a[3])
        infor['Diem hoa'] = float(a[4])
        infor['Diem TB'] = float(a[5])
        infor['Phan loai'] = a[6]
        listStudents.append(infor)
    return listStudents

def runProgram(a):    
    s = student.Student()
    s.listStudents = a
    action = 0
    while action >= 0:
        if action == 1:
            s.addStudent()
        elif action == 2:
            s.deleteStudent()
        elif action == 3:
            s.editStudent()
        elif action == 4:
            s.showStudents()
        elif action == 5:
            s.ghiFile()
        print("-"*60)
        print("Chọn chức năng muốn thực hiện:")
        print("Nhập 1: Thêm sinh viên")
        print("Nhập 2: Xóa sinh viên")
        print("Nhập 3: Sửa sinh viên")
        print("Nhập 4: Xem danh sách sinh viên")
        print("Nhập 5: Ghi danh sach sinh vien ra file")
        print("Nhập 0: Thoát khỏi chương trình")
        print("-"*60)
        action = int(input())
        if action == 0:
            break

if __name__ == '__main__':
    li = openFile()
    if li != False:
        s = student.Student()
        s.listStudents = li
        action = 0
        while action >= 0:
            if action == 1:
                s.addStudent()
            elif action == 2:
                s.deleteStudent()
            elif action == 3:
                s.editStudent()
            elif action == 4:
                s.showStudents()
            elif action == 5:
                s.ghiFile()
            print("-"*60)
            print("Chọn chức năng muốn thực hiện:")
            print("Nhập 1: Thêm sinh viên")
            print("Nhập 2: Xóa sinh viên")
            print("Nhập 3: Sửa sinh viên")
            print("Nhập 4: Xem danh sách sinh viên")
            print("Nhập 5: Ghi danh sach sinh vien ra file")
            print("Nhập 0: Thoát khỏi chương trình")
            print("-"*60)
            action = int(input())
            if action == 0:
                break
    else:
        print('File khong ton tai')
