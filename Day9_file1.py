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