def to_camel_case(text):
    i = 0
    text = text.replace("-", " ").replace("_", " ")
    text = text.title()
    text = text.replace(" ", "")
            
    return text

def main():
    print(to_camel_case(input("")))
  
main()