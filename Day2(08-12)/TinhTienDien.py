def electric_calculator():
    so_dien = int(input("Nhap so dien: "))

    if so_dien <= 52:
        tien_dien = (so_dien * 1984) * 1.08
    elif 53 <= so_dien <= 104:
        tien_dien = ((52 * 1984) + ((so_dien - 52) * 2050)) * 1.08
    elif 105 <= so_dien <= 207:
        tien_dien = ((52 * 1984) + (52 * 2050) + ((so_dien - 104) * 2380)) * 1.08
    elif 208 <= so_dien <= 310:
        tien_dien = ((52 * 1984) + (52 * 2050) + (103 * 2380) + ((so_dien - 207) * 2998)) * 1.08
    elif 311 <= so_dien <= 413:
        tien_dien = ((52 * 1984) + (52 * 2050) + (103 * 2380) + (103 * 2998) + ((so_dien - 310) * 3350)) * 1.08
    else:
        tien_dien = ((52 * 1984) + (52 * 2050) + (103 * 2380) + (103 * 2998) + (103 * 3350) + ((so_dien - 413) * 3460)) * 1.08

    tien_dien = int(round(tien_dien))
    print(f"Tien dien la: {tien_dien}")

electric_calculator()
