#### INITIAL DATA
patient_list = [
    {
        'ID': '12345',
        'NAMA': 'MARJONO',
        'DOB': '1975-01-03',
        'ADDRESS' : 'DEPOK'
    },
    {
        'ID': '12346',
        'NAMA': 'PRABOWO',
        'DOB': '1980-03-04',
        'ADDRESS' : 'JAKARTA'
    },
    {
        'ID': '12347',
        'NAMA': 'DEDDY',
        'DOB': '1962-05-08',
        'ADDRESS' : 'BSD'
    }
]

#### READING DATA
def showPatientList() :
    while True:
        print('\n******** menu pencarian Pasien ******** \n'.upper())
        print('1. Data Seluruh Pasien'.upper())
        print('2. Pencarian Data Pasien'.upper())
        print('3. Kembali ke menu utama'.upper())
        read = input('\nSILAHKAN INPUT PILIHAN READ DATA [1-3] : '.upper())
        if (read == '1'):
            if len(patient_list) != 0 :
                print('\n******** DAFTAR NAMA PASIEN ********\n')
                print('NO\t| ID     \t| NAMA   \t| DOB    \t| address'.upper())
                for j,i in enumerate(patient_list) :
                    print(f"{j+1}\t| {i['ID']}   \t| {i['NAMA']}   \t| {i['DOB']}  \t| {i['ADDRESS']}")
            else :
                print('\n******** Data Pasien Tidak Ditemukan ********'.upper())
            continue
        elif (read == '2'):
            if len(patient_list) != 0 :
                pat_id = (input('\nInput ID Pasien : '.upper()))
                print('\nData ID Pasien : {}\n'.format(pat_id).upper())
                for j,i in enumerate(patient_list) :
                    if i['ID'] == pat_id:
                        print('NO\t| ID     \t| NAMA   \t| DOB    \t| address'.upper())
                        print(f"{j+1}\t| {i['ID']}   \t| {i['NAMA']}   \t| {i['DOB']}  \t| {i['ADDRESS']}")
                        break
                else:
                    print('\n******** pasien belum terdaftar ********\n'.upper())
            else:
                print('\n******** data pasien tidak ditemukan ********\n'.upper())                               
        elif (read == '3'):
            break
        else:
            print('\n******** Pilihan Tidak Sesuai ********\n'.upper())
    return

#### ADDING DATA
def addPatient():
    while True:
        print('\n******** menu penambahan data Pasien ********\n'.upper())
        print('1. tambah data Pasien'.upper())
        print('2. Kembali ke menu utama'.upper())
        add = input('\nSILAHKAN INPUT PILIHAN tambah DATA [1-2] : '.upper())
        if add == '1':
            if len(patient_list) >= 0 :
                print('\n******** DAFTAR NAMA PASIEN ********\n')
                print('NO\t| ID     \t| NAMA   \t| DOB    \t| address'.upper())
                for j,i in enumerate(patient_list) :
                    print(f"{j+1}\t| {i['ID']}   \t| {i['NAMA']}   \t| {i['DOB']}  \t| {i['ADDRESS']}")
                patientID = input('\nINPUT ID PASIEN baru : '.upper())
                for j,i in enumerate(patient_list) :
                    if i['ID'] == patientID:
                        print('\n******** ID pasien telah terdaftar ********\n'.upper())
                        break
                    else:
                        patientName = input('INPUT NAMA PASIEN : '.upper())
                        patientDOB = input('INPUT DOB PASIEN : '.upper())
                        patientADD = input('INPUT ADDRESS PASIEN : '.upper())
                        while True:
                            ans1 = input('konfirmasi data akan ditambahkan [Y/N] : '.upper())
                            if ans1 == 'Y' or ans1 == 'y':
                                patient_list.append({
                    'ID' : patientID,
                    'NAMA': patientName.upper(),
                    'DOB': patientDOB.upper(),
                    'ADDRESS': patientADD.upper()
    })
                                print('\n******** data berhasil ditambahkan ********\n'.upper())
                                break
                            elif ans1 == 'N' or ans1 == 'n':
                                print('\n******** data batal ditambahkan ********\n'.upper())
                                break
                            else:
                                print('\n******** Pilihan Tidak Sesuai ********\n'.upper())
                        break    
            else :
                print('\n******** Data Nama Pasien Tidak Ditemukan ********'.upper())
        elif add == '2':
            break
        else:
            print('\n******** Pilihan Tidak Sesuai ********\n'.upper())
    return

#### DELETING DATA
def delPatient() :
    while True:
        print('\n******** menu penghapusan data Pasien ********\n'.upper())
        print('1. hapus data Pasien'.upper())
        print('2. Kembali ke menu utama'.upper())
        delData = input('\nSILAHKAN INPUT PILIHAN hapus DATA [1-2] : '.upper())
        if delData == '1':
            if len(patient_list) != 0 :
                pat_id = (input('\nInput ID Pasien yang ingin dihapus : '.upper()))
                print('\nData ID Pasien : {}\n'.format(pat_id).upper())
                print('NO\t| ID     \t| NAMA   \t| DOB    \t| address'.upper())
                for j,i in enumerate(patient_list) :
                    if i['ID'] == pat_id:
                        print(f"{j+1}\t| {i['ID']}   \t| {i['NAMA']}   \t| {i['DOB']}  \t| {i['ADDRESS']}")
                        break
                else:
                    print('\n******** pasien belum terdaftar ********'.upper())
                    continue            
            while True:
                ans2 = input('\nkonfirmasi data akan dihapus [Y/N] : '.upper())
                if ans2 == 'Y' or ans2 == 'y':
                    del patient_list[j]
                    print('\n******** data berhasil dihapus ********\n'.upper())
                    break
                elif ans2 == 'N' or ans2 == 'n':
                    print('\n******** data batal dihapus ********\n'.upper())
                    break
                else:
                    print('\n******** Pilihan Tidak Sesuai ********\n'.upper())
                continue
        elif delData == '2':
            break
        else:
            print('\n******** Pilihan Tidak Sesuai ********\n'.upper())
    return 

#### EDITING DATA
def editPatient():
    while True:
        print('\n******** menu perubahan data Pasien ********\n'.upper())
        print('1. ubah data Pasien'.upper())
        print('2. Kembali ke menu utama'.upper())
        editData = input('\nSILAHKAN INPUT PILIHAN ubah DATA [1-2] : '.upper())
        if editData == '1':
            if len(patient_list) != 0 :
                pat_id = (input('\nInput ID Pasien yang ingin diubah : '.upper()))
                print('\nData ID Pasien : {}\n'.format(pat_id).upper())
                print('NO\t| ID     \t| NAMA   \t| DOB    \t| address'.upper())
                for j,i in enumerate(patient_list) :
                    if i['ID'] == pat_id:
                        print(f"{j+1}\t| {i['ID']}   \t| {i['NAMA']}   \t| {i['DOB']}  \t| {i['ADDRESS']}")
                        break
                else:
                    print('\n******** pasien belum terdaftar ********'.upper())
                    break
                while True:
                    ans3 = input('\nkonfirmasi data akan diubah [Y/N] : '.upper())
                    if ans3 == 'Y' or ans3 == 'y':
                        kolEdit = input('\ninput kolom data yang ingin diubah : '.upper())
                        newVal = input('Input data {} baru : '.format(kolEdit).upper())
                        if kolEdit == 'ID' or kolEdit == 'id':
                            i['ID'] = newVal
                        elif kolEdit == 'NAMA' or kolEdit == 'nama':
                            i['NAMA'] = newVal.upper()
                        elif kolEdit == 'DOB' or kolEdit == 'dob':
                            i['DOB'] = newVal
                        elif kolEdit == 'ADDRESS' or kolEdit == 'address':
                            i['ADDRESS'] = newVal.upper()
                        else:
                            print('\n******** kolom tidak tersedia ********'.upper())
                            break
                        print('\n******** data berhasil diubah ********\n'.upper())
                        break
                    elif ans3 == 'N' or ans3 == 'n':
                        print('\n******** data batal diubah ********\n'.upper())
                        break
                    else:
                        print('\n******** Pilihan Tidak Sesuai ********\n'.upper())
                continue
            else :
                print('\n******** Data Nama Pasien Tidak Ditemukan ********'.upper())
        elif editData == '2':
            break
        else:
            print('\n******** Pilihan Tidak Sesuai ********\n'.upper())
    return 
    


while True :
    pilihanMenu = input('''\n
******** Selamat Datang di RS Tidak Sehat ********

Pilihan Menu :
1. Tampilkan Daftar Nama Pasien
2. Tambah Pasien Baru
3. ubah Data Pasien
4. hapus Data Pasien
5. Exit Program

Input Menu yang ingin dijalankan [1-5] : '''.upper())

    if(pilihanMenu == '1') :
        showPatientList()
    elif(pilihanMenu == '2') :
        addPatient()
    elif(pilihanMenu == '3') :
        editPatient()
    elif(pilihanMenu == '4') :
        delPatient()
    elif(pilihanMenu == '5') :
        print('\nexiting program .....'.upper())
        print('\nexiting program ----- done\n'.upper()) 
        break
    else :
        print('\npilihan yang anda masukan salah.\nsilahkan ulangi kembali.'.upper())
