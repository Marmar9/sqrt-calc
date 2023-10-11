
def truncate_float(original_float: float, quality: int) -> float:
    quality = 2

    float_str = str(original_float)

    integer_part, decimal_part = float_str.split(".")

    if len(decimal_part) > quality:
        decimal_part = decimal_part[:quality]
    else:
        decimal_part = decimal_part.ljust(quality, "0")

    truncated_float_str = f"{integer_part}.{decimal_part}"

    return float(truncated_float_str)


def sqrt_calc():
    number = int(input())
    quality = int(input())
    # "round" for Round up or "trun" for truncate
    option = input()

    if option != "round" and option != "trun":
        raise ValueError("option must be 'round' or 'trun'")

    # Compute the first side of the square
    bottom_side = number * 1 / 2

    while True:
        new_sqrt = number / bottom_side

        bottom_side = (bottom_side + new_sqrt) / 2

        if option == "round":
            diff = round(new_sqrt, quality) - round(bottom_side, quality)
        elif option == "trun":
            diff = truncate_float(new_sqrt, quality) - truncate_float(
                bottom_side, quality
            )
        if diff == 0:
            break

    print(truncate_float(new_sqrt, quality))


sqrt_calc()
