# def main(car):
#     return car in ["a", "b", "c", "d"]
    
# print(main("t"))
status_code_message ={
    200: "Sucessfull",
    201: "Created",
    404: "Page not found",
    500: "Internal Server Error"
}
# def status_code_handler(status_code):
#     if status_code == 200:
#         return "Sucessfull"
#     elif status_code == 201:
#         return "Created"
#     elif status_code == 404:
#         return "Page not found"
#     elif status_code == 500:
#         return "Internal Server Error"
#     else:
#         return "Default message"

def status_code_handler(status_code):
    return status_code_message.get(status_code, "Default message")
print(status_code_handler(600))