"""11) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს და თუ ის დადებითი იქნება, დააბრუნებს "დადებითი", და თუ უარყოფითი იქნება, "უარყოფითი"."""

def posneg():
    num=float(input("enter num: "))
    if num > 0:
        print("possitive")
    else:
        print("negative")