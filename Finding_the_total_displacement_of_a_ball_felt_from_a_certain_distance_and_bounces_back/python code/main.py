while True:
    try:
            x:int = int(input("Enter the distance from which the ball is felt:--->> "))
            a:int = int(input("Enter the percentage the ball bounces back to the privious hight:--->> "))
            if a <= 0 or a >= 100 :
                 print("a ball cant bounce back more than the hight it felt, and if happen and this program will not support that case.")
                 continue
            else:
                  break
    except ValueError:
            print("Please enter a valid integer")
            continue


total_displacement = (100+a)*x/(100-a)
print(f"The total displacement of the ball is:--->> {total_displacement}")
