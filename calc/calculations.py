from functions import relative


def calc_perimetr(CH):
    per = 0
    for i in range(len(CH)-1):
        per += relative.length(CH[i].get_coords(), CH[i+1].get_coords())
    return per
