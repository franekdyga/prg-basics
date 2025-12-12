import tv

def main():
    telewizor = tv.TV()

    print(telewizor.show_status())
    telewizor.turn_on()
    print(telewizor.show_status())
    telewizor.set_channel(5)
    print(telewizor.show_status())
    telewizor.turn_off()
    print(telewizor.show_status())

if __name__  == "__main__":
    main()