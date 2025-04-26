def shopping_list_program ():
    Shopping_list= []
    for count in range (1000):
        print ("What option do you want to choose")
        print ("(1) Add item")
        print ("(2) Remove item")
        print ("(3) View cart")
        print ("(4) Exit")
        Choice= input ("Enter you choice (1-4):")
        if Choice=="1":

            item= input("Enter an item you want to add")
            Shopping_list.append(item)
            print ("You have successfully added an item:", item)

        elif Choice=="2": 
            item= input('Enter the item you want to remove')
            Shopping_list.remove(item)
            print ("You have removed the item successfully:", item)
    
        elif Choice=="3":
            print("View you cart:", Shopping_list)
    
        elif Choice=="4":
            print ("Thank you for shopping with Shopping list program")
            break 
        else:
            print ("Choose option between 1 to 4")
    
shopping_list_program ()
      
 
       
       

            


