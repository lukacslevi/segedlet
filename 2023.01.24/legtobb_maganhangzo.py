napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]

mgh = "aáeéiíoóöőuúüű"

def mghSzama(szo):
    db = 0
    for i in szo:
        if i in mgh:
            db +=1

    return db

maxpoz=0
for i in range(len(napok)):
    if mghSzama(napok[i]) > mghSzama(napok[maxpoz]):
        maxpoz=i

