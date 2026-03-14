"""
File     : code_set1.py
Tujuan   : menyediakan fungsi sederhana untuk menghitung kuadrat bilangan 
           positif berdasarkan kondisi bolean tertentu.
Fitur utama 
    -mengecek kondisi boolean sebagai pemicu proses perhitungan 
    -menghitung kuadrat bilangan jika nilainya positif
    -mengembalika nilai 0 jika kondisi tidak terpenuhi

Penulis : Ervan Gusti Wanjaya
Tanggal : 14-maret-2026
"""

def calc(a, b):
    """
    Hitung kuadrat dari bilangan jika terpenuhi.

    periksa nilai boolean 'a'. jika 'a' bernilai True dan 'b' lebih besar
    dari 0, kembalikan kuadrat dari 'b'. jika kondisi tersebut tidak 
    terpenuhi, kembalikan nilai 0 

    Parameters
    ----------
    a : bool
        Menentukan apakah proses perhitungan dilakukan 
    b : int     
        Bilangan yang akan diperiksa dan dihitung kuadratnya 
        jika bernilai positif>

    Returns 
    ----------
    int     
       nilai kuadrat dari 'b' jika 'a == True' dan 'b > 0'
       jika tidak maka mengembalikan 0

    contoh 
    ----------
    >>> calc(True, 5)
    25
    >>> calc(True, -3)
    0
    >>> calc(False, 4)
    0
    """

    if a:
        if b > 0:
            return b*b
    return 0


x = [1, 2, -3]
print(calc(True, x[2]))
