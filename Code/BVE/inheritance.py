class ContactList(list):
	def search(self, name):
		'''Return all contacts that contain the search value in their name.'''
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts


class Contact:
	# Now we create a ContactList instead of a normal list
	all_contacts = ContactList()

	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.all_contacts.append(self)

	def __str__(self):
		return "Name:" + self.name + ", email:" + self.email


class Address:
	def __init__(self, number, street, city, code):
		self.number = number
		self.street = street
		self.city = city
		self.code = code

	def __str__(self):
		return str(self.number) + " " + self.street + " " + self.city +\
			" " + str(self.code)


class Friend(Contact):
	def __init__(self, name, email, phone, number, street, city, code):
		Contact.__init__(self, name, email)
		self.phone = phone
		self.adr = Address(number, street, city, code)

	def __str__(self):
		return super().__str__() + ", phone:" + self.phone +\
			", address: " + str(self.adr)

#######################################

c = Contact('Tom', 'tom@gmail.com')
f = Friend('Kate', 'kate@gmail.com', '+36301112222', 12, 'Main str', 'Miskolc', 3515)
#print("Contact: ", c.name, c.email)
#print("Friend: ", f.name, f.email, f.phone, f.adr)
print("Contact: ", c)
print("Friend: ", f)
print(Contact.all_contacts)