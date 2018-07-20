import datetime

default_names = ["Akash", "Sagar", "John", "Jim"]
default_amounts = [100, 200, 300, 400]

unf_message = """
  Hi {name},
  This is messsage with {date} & {amount}
  Thank You!
"""

def make_messages(names, amounts):
  if len(names) == len(amounts):
    i = 0
    today = datetime.date.today()
    for name in names:
      new_msg = unf_message.format(
        name= name,
        date=today,
        amount=amounts[i]
      )
      i+=1
      print(new_msg)


make_messages(default_names, default_amounts)