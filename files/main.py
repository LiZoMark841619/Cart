from store_purchase import Purchase

def main():
    purchase = Purchase()
    actions = purchase.actions_()
    while True:
        choice = purchase.menu_()
        if choice == 5: purchase.exit(); break
        actions[choice]()
        
if __name__ == '__main__':  main()