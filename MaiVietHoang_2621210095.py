#bai3
import math
def tinh_tien_dien(kwh):
    if kwh <= 50:
        tong_tien = kwh * 1678
    elif kwh <= 100:
        tong_tien = (50 * 1678)+((kwh - 50) * 1734)
    else:
        tong_tien = (50 * 1678)+(50 * 1734)+ ((kwh-100) * 2000)
    return tong_tien


#%%bai4
def tinh_tong_a(n):
    tong = 2022
    for i in range(2, n + 1, 2):
        tong += i
    return tong
def tinh_tong_b(n):
    tong = 1
    for i in range(1, n+1):
        tong += 1/ math.factorial(i)
    return tong


#%Bai6
def dem_so_ngay_virus_tang(lenh_khoi_dau):
    so_ngay = 0
    muc_tieu = 1_000_000_000
    
    while lenh_khoi_dau < muc_tieu:
        lenh_khoi_dau *= 2
        so_ngay += 1
    return so_ngay

#%%Bai7
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i ==0:
            return False
    return True


#%%Bai8
def la_nam_nhuan(nam):
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        return True
    return False
def tinh_so_ngay(nam):
    if la_nam_nhuan(nam):
        return 366
    return 365


#%Menu'
def main():
    while True:
        print("\n---MENU---")
        print("1. Bai3: tinh tien dien")
        print("2. Bai4: tinh tong")
        print("3. Bai6: virus")
        print("4. Bai7: kiem tra so nguyen so")
        print("5. Bai8: tinh so ngay cua nam")
        print("0. Thoat")
        choice = int(input("chon chuc nang: "))
        
        if choice == 1:
            kwh = int(input("nhap so dien tieu thu: "))
            tong_tien = tinh_tien_dien(kwh)
            print(f"so tien phai tra la: {tong_tien} VND")
        elif choice == 2:
            n= int(input("nhap so nguyen duong n: "))
            tong_a = tinh_tong_a(n)
            tong_b = tinh_tong_b(n)
            print(f"tong cho bai toan a(2022 + 2 + 4 + 6 +...+2n):{tong_a}")
            print(f"tong cho bai toan b(1 + 1/1 + 1/2! +...+1/n):{tong_b}")
        elif choice == 3:
            so_virus = int(input("nhap so luong virus ban dau: "))
            so_ngay = dem_so_ngay_virus_tang(so_virus)
            print(f"sau {so_ngay} ngay, so luong virus vuot 1 ty.")
        elif choice == 4:
            n = int(input("nhap so nguyen to duong n: "))
            if kiem_tra_nguyen_to(n):
                print("YES")
            else:
                print("NO")
        elif choice == 5:
            nam = int(input("nhap nam can kiem tra: "))
            so_ngay = tinh_so_ngay(nam)
            print(f"so ngay cua nam {nam} la: {so_ngay}")
        elif choice == 0:
            print("Thoat chuong trinh.")
            break
        else:
            print("lua chon khong hop le. Vui long chon lai!")


#%% goi ham main
if __name__ == "__main__":
    main()







            
            
            
    
    
    
    
    
    
    
    