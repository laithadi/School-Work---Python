"""
-----------------------------------------------------
CP104 - Assignment 6
-----------------------------------------------------
Author: Laith Adi
ID: 170265190
Email: adix5190@mylaurier.ca
__updated__ = "2018-11-09"
-----------------------------------------------------
"""
seconds_day = 86400
seconds_hour = 3600
seconds_minutes = 60


def get_brightness(wattage):
    """
    -------------------------------------------------------
    Converts watts to lumens for lightbulbs. Return -1 for an
    invalid wattage.
    Use: brightness = get_brightness(wattage)
    -------------------------------------------------------
    Parameters:
        wattage - wattage in watts (int >= 0)
    Returns:
        brightness - brightness in lumens (int)
    -------------------------------------------------------
    """
    brightness = 0
    if wattage == 15:
        brightness = 125
    elif wattage == 25:
        brightness = 215
    elif wattage == 40:
        brightness = 500
    elif wattage == 60:
        brightness = 880
    elif wattage == 75:
        brightness = 1000
    elif wattage == 100:
        brightness = 1675
    else:
        brightness = -1
    return brightness


def payment(principal, interest, months):
    """
    -------------------------------------------------------
    Calculates a monthly payment on a loan.
    Use: monthly_payment = payment(principal, interest, months)
    -------------------------------------------------------
    Parameters:
        principal - amount borrowed in $ (float > 0)
        interest - yearly interest rate on loan (float > 0)
        months - number of months for the loan (int > 0)
    Returns:
        monthly_payment - monthly payment on loan in $ (float)
    -------------------------------------------------------
    """
    monthly_payment = ((interest / 12) * principal) / \
        (1 - ((1 + (interest / 12)) ** -months))

    return monthly_payment


def get_total_change(n, d, q, l, t):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins. Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: tv = get_total_change(n, d, q, l, t)
    -------------------------------------------------------
    Parameters:
        n - number of nickels (int >= 0)
        d - number of dimes (int >= 0)
        q - number of quarters (int >= 0)
        l - number of loonies (int >= 0)
        t - number of toonies (int >= 0)
    Returns:
        tv - total value of coins
    -------------------------------------------------------
    """
    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.10
    QUARTER_VALUE = 0.25
    LOONIE_VALUE = 1.00
    TOONIE_VALUE = 2.00

    tv = (n * NICKEL_VALUE) + (d * DIME_VALUE) + \
        (q * QUARTER_VALUE) + (l * LOONIE_VALUE) + (t * TOONIE_VALUE)
    return tv


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    num = num1 * num2
    den = den1 * den2
    product = num / den
    return num, den, product


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns total_seconds in different formats. Results are
    rounded down to the nearest day, hour, minute.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """

    days = seconds // seconds_day
    hours = seconds // seconds_hour
    minutes = seconds // seconds_minutes
    return days, hours, minutes


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts initial seconds into days, hours, minutes, and seconds.    
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    days = initial_seconds // seconds_day
    initial_seconds -= (days * seconds_day)
    hours = initial_seconds // seconds_hour
    initial_seconds -= (hours * seconds_hour)
    minutes = initial_seconds // seconds_minutes
    initial_seconds -= (minutes * seconds_minutes)
    seconds = initial_seconds
    return days, hours, minutes, seconds


def wall_area(width, height):
    """
    -------------------------------------------------------
    Calculates rectangular wall area on a painting job.
    Use: area = wall_area(width, height)
    -------------------------------------------------------
    Parameters:
        width - width of wall (ft) (int > 0)
        height - height of wall (ft) (int > 0)
    Returns:
        area - area of wall (sq ft) (int)
    -------------------------------------------------------
    """
    area = height * width
    return area


def paint_required(area, standard_area):
    """
    -------------------------------------------------------
    Calculates paint required on a painting job. Resulting gallons
    are rounded up.
    Use: total = paint_required(area, standard_area)
    -------------------------------------------------------
    Parameters:
        area - area of wall (sq ft) (int > 0)
        standard_area - area covered by 1 gallon of paint (sq ft) (int > 0)
    Returns:
        total - gallons of paint required (int)
    -------------------------------------------------------
    """
    total = area // standard_area + (area % standard_area > 0)
    return total


def hours_required(area, area_per_hour):
    """
    -------------------------------------------------------
    Calculates hours required on a painting job. Resulting hours are
    rounded up.
    Use: hours = hours_required(area, area_per_hour)
    -------------------------------------------------------
    Parameters:
        area - area of wall (sq ft) (int > 0)
        area_per_hour - area painted per hour (int > 0)
    Returns:
        hours - hours required to paint area (int)
    -------------------------------------------------------
    """
    hours = area // area_per_hour + (area % area_per_hour > 0)
    return hours


def paint_cost(total_paint, cost):
    """
    -------------------------------------------------------
    Calculates paint cost on a painting job.
    Use: pc = paint_cost(total_paint, cost)
    -------------------------------------------------------
    Parameters:
        total_paint - paint required (gallons) (int > 0)
        cost - cost of paint ($/gallon) (float > 0)
    Returns:
        pc - total paint cost (float)
    -------------------------------------------------------
    """
    pc = total_paint * cost
    return pc
