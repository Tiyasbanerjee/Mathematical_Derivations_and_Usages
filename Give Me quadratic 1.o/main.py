
import random
                        # let , x^2 + xp + q
                        # p = (a) + (b)
                        # q = (a) * (b)


def give_format(a:int = 1 , b:int = 1 ):
              p =  a + b
              q = a * b
              if p > 0:
                      p = "+" + str(p)
              else:
                      p = str(p)
              if q >= 0:
                      q = "+" + str(q)
              else:
                      q = str(q)
           
              str_ = f"x^2 {p}x {q}"

              return str_



def random_num_get():
        a , b = random.randint(-100,100) , random.randint(-100,100)
        return a ,b


def scoore(try_:int = 0 , a:int = 0 , b:int = 0):
        pass


def main():
        print("Heyyyyyyy..... seems like you want to play a match with me , right?")
        again = ""

        while True:
                inp = input(f"press ENTER to play{again} and '0' to exit:---->>>")
                try:
                        if inp == "":
                                guess_1 , guess_2 = random_num_get()

                                print("ok i have gessued a number between -100 to 100 (includeing -100 and 100). \n But dont worry you will find two options by solveing My problem")
                                print(f"-----------[{give_format(guess_1 , guess_2)}]------")
                                print("enter any of the functions solution ( any of its x cordinate when 'y == 0' )")

                                while True:
                                    answer = input("Fast Fast time is running more than useual, LETS DOOOOO ITTTTT!!!------->>>>")
                                    try:
                                            answer = int(answer)
                                            if answer == -guess_1 or answer == -guess_2:
                                                    print("GRESTT!!! YOU DID IT!!!")
                                                    break
                                            else:
                                                    print("OOOHHHH NOOOOOOOO, TRY AGAIN")
                                            
                                    except ValueError:
                                            answer = input("ohhhh, no somthing went wrong")
                                        
                        else:
                                print("Thank youuuuuuuu, May God of math Bless you")
                                exit()
                        again = " again"
                        
                except ValueError:
                        print("ohhhh, no somthing went wrong")
            
                


main()
