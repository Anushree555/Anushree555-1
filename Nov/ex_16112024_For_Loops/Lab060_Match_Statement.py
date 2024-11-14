#match variable:
#case pattern1:
#code block
#case pattern2:
#code block


#write a pgn asking cx which browser he want to run automation
browser_name=input("Enter the browser name")
match browser_name:
    case "firefox":
        print("Starting Firefox")
    case "chrome":
        print("Starting chrome")
    case "edge":
        print("Starting edge")
    case "safari":
        print("Starting safari")
    case _:
        print("Browser not found")

