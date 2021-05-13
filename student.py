import json

class Student:
 
    # Chứa dữ liệu sinh viên
    listStudents= []
 
    def addStudent(self):
        """Hàm thêm một sinh viên"""
        print("*** THÊM SINH VIÊN ***")
 
        # Cấu trúc lưu trữ một sinh viên
        infor = {
            'id' : '',
            'name' : '',
            'Diem toan': '',
            'Diem ly': '',
            'Diem hoa': '',
            'Diem TB': '',
            'Phan loai': ''
        }
 
        # Nhập ID, có kiểm tra trùng ID thì nhập lại
        print("Nhập ID sinh viên:")
        id = input()
 
        while True:
            student = self.findStudent(id)
            if student != False:
                print("ID này đã tồn tại, vui lòng nhập lại:")
                id = input()
            else:
                break
 
        infor['id'] = str(id)
 
        # Nhập thong tin sinh vien
        infor['name'] = input("Nhập tên sinh viên: ")
        infor['Diem toan'] = float(input("Nhập diem toan: "))
        infor['Diem ly'] = float(input("Nhập diem ly: "))
        infor['Diem hoa'] = float(input("Nhập diem hoa: "))
        infor['Diem TB'] = self.averagePoint(infor['Diem toan'], infor['Diem ly'], infor['Diem hoa'])
        infor['Phan loai'] = self.rank(infor['Diem TB'])
        # Lưu vào danh sách sv
        self.listStudents.append(infor)
    
    # Ham tinh diem trung binh
    def averagePoint(self, toan, ly, hoa):
        return round((toan + ly + hoa)/3, 2)

    # Ham tinh phan loai
    def rank(self, tb):
        if tb >= 8:
            return "Gioi"
        elif tb >= 7:
            return "Kha"
        elif tb >= 6:
            return "Trung binh"
        else:
            return "Yeu"
   
    # Hàm tìm một sinh viên
    def findStudent(self, id):
        for i in range(0, len(self.listStudents)):
            if self.listStudents[i]['id'] == str(id):
                # Trả về mảng gồm 2 phần tử,
                # 0 là vị trí tìm thấy và 1 là dữ liệu
                return [i, self.listStudents[i]]
        return False
        
    # Hàm sửa sinh viên 
    def editStudent(self):
        print("*** SỬA THÔNG TIN SINH VIÊN ***")
        print("Nhập ID sinh viên cần sửa:")
        id = input()

        student = self.findStudent(id)
        if student != False:
            self.listStudents[student[0]]['name'] = input("Nhập tên sinh viên: ")
            self.listStudents[student[0]]['Diem toan'] = float(input("Nhập diem toan: "))
            self.listStudents[student[0]]['Diem ly'] = float(input("Nhập diem ly: "))
            self.listStudents[student[0]]['Diem hoa'] = float(input("Nhập diem hoa: "))
            self.listStudents[student[0]]['Diem TB'] = self.averagePoint(self.listStudents[student[0]]['Diem toan'], self.listStudents[student[0]]['Diem ly'], self.listStudents[student[0]]['Diem hoa'])
            self.listStudents[student[0]]['Phan loai'] = self.rank(self.listStudents[student[0]]['Diem TB'])
            print("Sửa thông tin sinh viên thành công")
        else:
            print("Không tìm thấy sinh viên cần sửa")

    # Hàm xóa sih viên
    def deleteStudent(self):
        print("*** XÓA SINH VIÊN ***")
        print("Nhập ID sinh viên cần xóa:")
        id = input()
 
        student = self.findStudent(id)
 
        if student != False:
            self.listStudents.remove(student[1])
            print("Xóa sinh viên thành công")
        else:
            print("Không tìm thấy sinh viên cần xóa")

    # Hàm hiển thị danh sách sv
    def showStudents(self): 
        print('-'*40)
        print("*** DANH SÁCH SINH VIÊN HIỆN TẠI ***")
        if len(self.listStudents) == 0:
            print('Không có dữ liệu về sinh viên')
        else:
            print("STT".center(5), 'ID'.center(5), 'Ten sinh vien'.center(25),
                'Diem toan'.center(12), 'Diem ly'.center(12), 'Diem hoa'.center(12),
                'Diem TB'.center(12), 'Phan loai'.center(12)
                )
            for i in range(0, len(self.listStudents)):
                print(str(i+1).center(5), str( self.listStudents[i]['id']).center(5),
                    str(self.listStudents[i]['name']).center(25),
                    str( self.listStudents[i]['Diem toan']).center(12),
                    str( self.listStudents[i]['Diem ly']).center(12),
                    str( self.listStudents[i]['Diem hoa']).center(12), 
                    str( self.listStudents[i]['Diem TB']).center(12),
                    str( self.listStudents[i]['Phan loai']).center(12)
                )
        print('-'*40)

    def ghiFile(self):
        print('*'*40)
        print('Lua chon dinh dang file muon luu:')
        print('Nhap 1 de luu file txt')
        print('Nhap 2 de luu file json')
        save = int(input())

        # Ghi du lieu vao file text
        if save == 1:
            a = input('Nhap ten file: ')
            with open(f'{a}.txt', 'w', encoding='utf-8') as wf:
                for i in self.listStudents:
                    wf.write(str(i['id']) +' '+ str(i['name']) +' '+ str(i['Diem toan']) +' '
                            + str(i['Diem ly']) +' '+ str(i['Diem hoa']) +' '+ str(i['Diem TB']) +' '
                            + str(i['Phan loai']) +' '+'\n')
            print(f'Da ghi du lieu vao file {a}.txt')

        # Ghi du lieu vao file json
        elif save == 2:
            a = input('Nhap ten file: ')
            with open(f'{a}.json', 'w') as wf:
                json.dump(self.listStudents, wf, ensure_ascii=False, indent=2)
            print(f'Da ghi du lieu vao file {a}.json')
        else:
            print('khong hop le')
         
if __name__ == '__main__':
    s = Student()
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

