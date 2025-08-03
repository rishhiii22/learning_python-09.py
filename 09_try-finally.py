# Finally block chalts hi chalta hai chahe try block me jao ya except block mai...


def main():
    try:
       a = int(input("Hey, Enter a number: "))
       print(a)
       return

    except Exception as e:
       print(e)
       return

    finally:
         print("Heyy i am inside of finally")

main()