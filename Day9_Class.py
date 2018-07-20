class MessageUser():
  users = []
  messages = []
  base_message = """ Hi!  {name} - amount {amount} """
  
  def add_user(self, name, amount):
    detail = {
      "name": name,
      "amount": amount,
    }
    self.users.append(detail)
  
  def get_users(self):
    return self.users

  def make_messages(self):
    if len(self.users) > 0:
      for detail in self.get_users():
        name = detail["name"]
        amount = detail["amount"]
        new_msg = base_message.format(
          name=name,
          amount=amount
        )
        self.messages.append(new_msg)
      return self.messages
    return []

obj = MessageUser()
obj.add_user("Akash", 112)
obj.get_users()
obj.make_messages()