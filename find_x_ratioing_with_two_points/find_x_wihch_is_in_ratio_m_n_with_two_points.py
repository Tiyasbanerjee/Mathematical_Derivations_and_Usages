
def find(x1 , x2 , m , n): #type: ignore

    x1 = int(x1)  #type: ignore
    x2 = int(x2)  #type: ignore
    m = int(m)    #type: ignore
    n = int(n)    #type: ignore

    return (m*x2 + n*x1)/(m + n)   #type: ignore


x1 = input("\nenter x1:").strip()
y1 = input("enter y1:").strip()

x2 = input("\nenter x2:").strip()
y2 = input("enter y2:").strip()

m=input("\nenter m:").strip()
n=input("enter n:").strip()



ox = find(x1, x2 , m, n)  #type: ignore
oy = find(y1, y2 , m, n)  #type: ignore

print("\n\nthe point which divides the line in ratio m:n is: (",ox,",",oy,")\n\n")  #type: ignore

