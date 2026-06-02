list_employees = []

while True: 
    choice = input("""
                QUAN LY NHÂN SỰ - STAFF MANAGER

                1. Thêm nhân viên mới
                2. Danh sach nhan viên
                3. Tim kiem nhan vien (theo mã)
                4. Xoa nhan vien khoi he thông
                5. Thoat chương trinh

                Nhập lựa chọn của bạn: """)
    if choice.isdigit():
        choice = int(choice)
        match choice:
            case 1:
                if list_employees == []:
                    id_employees = 101
                else:
                    id_employees = list_employees[len(list_employees) - 1]['id'] + 1
                while True:
                    name_input = input("Nhập tên nhân viên: ")
                    if name_input.strip() == "":
                        print("Tên người dùng không được để trống")
                    else: 
                        break
                while True:
                    salary_input = input("Hãy nhập lương: ")
                    try:
                        salary_input = float(salary_input)
                        if salary_input > 0:
                            break
                        else:
                            print("Lương phải lớn hơn 0")
                    except ValueError:
                        print("Lương phải là số thực")
                new_employees = {
                    "id": id_employees,
                    "name": name_input,
                    "salary": salary_input
                }
                list_employees.append(new_employees)
                print(f"Thêm nhân viên thành công! ID: {id_employees}")

            case 2:
                if len(list_employees) == 0:
                    print("Chưa có dữ liệu nhân sự")
                else:
                    print("ID    | TÊN NHÂN VIÊN     | MỨC LƯƠNG")
                    for item in list_employees:
                        print(f"{item['id']}  | {item['name']}   | {item['salary']}")

            case 3:
                flag = None
                search_id = int(input("Hãy nhập ID: "))
                for item in list_employees:
                    if item["id"] == search_id:
                        flag = item
                        print(f"thông tin nhân viên: {item}")
                        break
                if flag is None:
                    print(f"Không tìm thấy nhân viên có ID: {search_id}")

            case 4:
                flag = None
                search_id = int(input("Hãy nhập ID: "))
                for item in list_employees:
                    if item["id"] == search_id:
                        flag = item
                        print(f"Đã xóa nhân viên ID: {item['id']} thành công!")
                        list_employees.remove(item)
                        break
                if flag is None:
                    print(f"Không tìm thấy nhân viên để xóa")

            case 5:
                print("Chương trình kết thúc")
                break
            case _:
                print("Dữ liệu không hợp lệ")
    else:
        print("Dữ liệu không hợp lệ")