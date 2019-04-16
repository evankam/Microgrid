def solar(time, season):
    if season ==1:
        y = (-1/144)*(time**3)*(1/3)+ (65/12)*(time**2)*(0.5)
        y = y/15210
        return(y)
    if season ==2:
        y = (-1/144)*(time**3)*(1/3)+ (65/12)*(time**2)*(0.5)
        y = (2/3)*y/15210
        return(y)
    if season ==3:
        y = (-1/144)*(time**3)*(1/3)+ (65/12)*(time**2)*(0.5)
        y = 0.5*y/15210
        return(y)
    if season ==4:
        y = (-1/144)*(time**3)*(1/3)+ (65/12)*(time**2)*(0.5)
        y = (2/3)*y/15210
        return(y)


main_generator_price = 3
