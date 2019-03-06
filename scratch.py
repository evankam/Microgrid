def solar(time):
    y = (-1/144)*(time**3)*(1/3)+ (65/12)*(time**2)*(0.5)
    y = y/15210
    return(y)

main_generator_price = 3
