class Car:
    def get_gen_info(self):
        return "This is Car Class"

    def get_obj_info(self):
        return str(self.id) + " - " + str(self.color) + " - " + str(self.style)

    def prepare_txt(self, x, y):
        res = str(x).upper() + " - " + str(y).upper()
        return res


c1 = Car()
c1.id = 1
c1.color = "Πράσινο"
c1.style = "Οικογενειακό"
print(c1.get_gen_info())

print(c1.get_obj_info())

print(c1.prepare_txt(c1.id, c1.color))
