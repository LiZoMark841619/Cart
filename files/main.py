from store_purchase import Purchase

def main():
    purchase = Purchase()
    actions = purchase.actions_()
    while True:
        choice = purchase.menu_()
        actions[choice]()
if __name__ == '__main__':  main()