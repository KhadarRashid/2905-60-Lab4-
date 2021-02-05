
def main():
    # Breaking down each step into its own function
    txt = get_input()
    txtList = make_list(txt)
    joined_to_string = join_list(txtList)
    camelCae = camel_case(joined_to_string)
    print(camelCae)


def get_input():
    #turning the input into a capitlazied sentence right off the bat
    txt = input("please enter something to be turned into camelCase: ").title() 
    return txt

def camel_case(joined_to_string):
    # Turning the first letter into lower case and adding the rest
    result = joined_to_string[0:1].lower() + joined_to_string[1:]

    return result

def join_list(txtList):
    # Joining the list
    joined_to_string = ("".join(txtList)) 
    return joined_to_string


def make_list(txt):
    # Turning the text into a list
    txtList = txt.split( )
    return txtList


if __name__ == '__main__':
    main()
